"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Calculate the normal distribution produces by the mutual information found 
    between two signals that are not recorded at the same time during a recording. 
    This will help to evaluate if the highest MI scores found are caused by 
    randomness or if it shares enough information between the two signals.

    The null hypothesis is 2 signals share an expected (normal) mutual information.
    We want the criteria to reject the null hypothesis.
    We want the criteria to identify when 2 signals share an unexpected high mutual informaiton.
    The confidence level indicates the degree of confidence that the criteria did not occur by sampling error.

    Parameters
    -----------
        signals1: List
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        signals2: List
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        parameters : Dict
            Dictionnary of all the parameters to compute the decision threshold (criteria)
            max_iter: int
                Number of iteration max to evaluate the normal distribution
            confidence_level: float
                The degree of confidence that the criteria did not occur by sampling error.
                (suggested value = 0.9)

        cycle_events : pandas DataFrame
            Events (columns=['group','name','start_sec','duration_sec','channels'])   
            Sleep cycles are defined with the 'group' cycle and the 'name' cycle

    Returns
    -----------    
        mean_ami : array of float
            Mean of the distribution of accidental mutual info for each item of signals1
        std_ami : array of float
            Standard deviation of the distribution of accidental mutual info for each item of signals1
        criteria : array of float
            Threshold of mutual information (MI) for each item of signals1. 
            Below the criteria value : MI is caused by randomness (normal).
            Above the criteria value : MI is higher than expected by randomness.
"""

from commons.NodeInputException import NodeInputException
from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.PSGReader import commons

import numpy as np
import pandas as pd
from random import sample
from sklearn.metrics import mutual_info_score
from tqdm import tqdm

DEBUG = False

class AccidentalMutualInfo(SciNode):
    """
        Calculate the normal distribution produce by the mutual information found 
        between two signals that are not record at the same time during a recording. 
        This will helps to evaluate if the highest MI scores found are caused by 
        randomness or if it shares enough information between the two signals.

        Parameters
        -----------
            signals1: List
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            signals2: List
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            parameters : Dict
                Dictionnary of all the parameters to compute the decision threshold (criteria)
                max_iter: int
                    Number of iteration max to evaluate the normal distribution
                confidence_level: float
                    The degree of confidence that the criteria did not occur by sampling error.
                    (suggested value = 0.9)
                criteria_scope : integer
                    0 to compute a criteria per sleep cycle and channel
                    1 to compute a criteria per channel (through all signals).

            cycle_events : pandas DataFrame
                Events (columns=['group','name','start_sec','duration_sec','channels'])   
                Sleep cycles are defined with the 'group' cycle and the 'name' cycle

        Returns
        -----------    
            mean_ami : array of float
                Mean of the distribution of accidental mutual info for each item of signals1
            std_ami : array of float
                Standard deviation of the distribution of accidental mutual info for each item of signals1
            criteria : array of float
                Threshold of mutual information (MI) for each item of signals1. 
                Below the criteria value : MI is caused by randomness (normal).
                Above the criteria value : MI is higher than expected by randomness.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('AccidentalMutualInfo.__init__')
        self._filename = None
        InputPlug('signals1', self)
        InputPlug('signals2', self)
        InputPlug('parameters', self)
        InputPlug('cycle_events', self)
        InputPlug('artifact_events', self)
        OutputPlug('mean_ami', self)
        OutputPlug('std_ami', self)
        OutputPlug('criteria', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, signals1, signals2, parameters, cycle_events, artifact_events):
        """
            Calculate the normal distribution produce by the mutual information found 
            between two signals that are not record at the same time during a recording. 
            This will helps to evaluate if the highest MI scores found are caused by 
            randomness or if it shares enough information between the two signals.

            Parameters
            -----------
                signals1: List
                    List of signal with dictionary of channels with SignalModel with 
                    properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original
                signals2: List
                    List of signal with dictionary of channels with SignalModel with 
                    properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original
                parameters : Dict
                    Dictionnary of all the parameters to compute the decision threshold (criteria)
                    max_iter: int
                        Number of iteration max to evaluate the normal distribution
                    confidence_level: float
                        The degree of confidence that the criteria did not occur by sampling error.
                        (suggested value = 0.9)
                    criteria_scope : integer
                        0 to compute a criteria per sleep cycle and channel
                        1 to compute a criteria per channel (through all signals).

                cycle_events : pandas DataFrame
                    Events (columns=['group','name','start_sec','duration_sec','channels'])   
                    Sleep cycles are defined with the 'group' cycle and the 'name' cycle

                artifact_events : pandas DataFrame
                    Events (columns=['group','name','start_sec','duration_sec','channels'])   

            Returns
            -----------    
                mean_ami : array of float
                    Mean of the distribution of accidental mutual info for each item of signals1
                std_ami : array of float
                    Standard deviation of the distribution of accidental mutual info for each item of signals1
                criteria : array of float
                    Threshold of mutual information (MI) for each item of signals1. 
                    Below the criteria value : MI is caused by randomness (normal).
                    Above the criteria value : MI is higher than expected by randomness.
        """

        if DEBUG: print('AccidentalMutualInfo.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Verify inputs
        if isinstance(signals1,str) and signals1=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals1", \
                f"AccidentalMutualInfo this input is not connected.")
        if not isinstance(signals1,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals1", \
                f"AccidentalMutualInfo input of wrong type. Expected: <class 'list'> received: {type(signals1)}")
        elif isinstance(signals1, list) and len(signals1)==0:
            return {'mean_ami': '',
                    'std_ami': '',
                    'criteria': ''}

        if isinstance(signals2,str) and signals2=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals2", \
                f"AccidentalMutualInfo this input is not connected.")
        if not isinstance(signals2,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals2", \
                f"AccidentalMutualInfo input of wrong type. Expected: <class 'list'> received: {type(signals2)}")
        elif isinstance(signals2, list) and len(signals2)==0:
            return {'mean_ami': '',
                    'std_ami': '',
                    'criteria': ''}

        if not isinstance(parameters['criteria_scope'], int):
            err_message = "ERROR: criteria_scope of pramaters unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals1", \
                f"AccidentalMutualInfo input of wrong type. Expected: <int> received: {type(parameters['criteria_scope'])}")

        if parameters['criteria_scope']==0:
            if isinstance(cycle_events,str) and cycle_events=='':
                raise NodeInputException(self.identifier, "cycle_events", \
                    f"AccidentalMutualInfo this input is not connected.")
            if not isinstance(cycle_events,pd.DataFrame):
                raise NodeInputException(self.identifier, "cycle_events", \
                    f"AccidentalMutualInfo input of wrong type. Expected: <class pd.DataFrame> received: {type(cycle_events)}")                     
            cycle_df = cycle_events[cycle_events.group==commons.sleep_cycle_group]
            # Format events_df event list
            cycle_df = cycle_df.sort_values(by=['start_sec'])
            cycle_df = cycle_df.reset_index(drop=True)

        # Set progress bar
        total_event = parameters['max_iter']

        # signals1_event is [n_rem_10_s][n_channels][time series]
        signals1_event = SignalModel.get_attribute(signals1, None, 'start_time') # signal that share all the same start time are grouped
        signals2_event = SignalModel.get_attribute(signals2, None, 'start_time')

        signals1_start = SignalModel.get_attribute(signals1, 'start_time', 'start_time') 
        signals1_start = signals1_start[:,0]
        signals1_dur = SignalModel.get_attribute(signals1, 'duration', 'start_time') 
        signals1_dur = signals1_dur[:,0]

        # Remove item of signals when it includes an artifact
        if isinstance(artifact_events, pd.DataFrame) and len(artifact_events)>0:
            art_start = artifact_events['start_sec'].to_numpy().astype(float)
            art_dur = artifact_events['duration_sec'].to_numpy().astype(float)
            # If there is at least one artefact that : 
            #   start before the end of the spindle AND stop after the start of the spindle.
            index_2_drop = []
            cur_index = 0
            for start, dur in zip(signals1_start, signals1_dur):
                if any( (art_start<= (start + dur)) & ((art_start+art_dur)>=start) ):
                    index_2_drop.append(cur_index)
                cur_index +=1
            # Drop index
            if len(index_2_drop)>0:
                signals1_art_free = np.delete(signals1_event, index_2_drop, 0)
                signals2_art_free = np.delete(signals2_event, index_2_drop, 0)
                signals1_start_art_free = np.delete(signals1_start, index_2_drop, 0)
                signals1_dur_art_free = np.delete(signals1_dur, index_2_drop, 0)
        else:
            signals1_art_free = signals1_event
            signals2_art_free = signals2_event
            signals1_start_art_free = signals1_start
            signals1_dur_art_free = signals1_dur

        if parameters['criteria_scope']==0: # Per sleep cycle
            mean_ami_start = []
            std_ami_start = []
            z_score_start = []
            sleep_cycle = 0
            for index, row in cycle_df.iterrows():
                # split the signalsx_event per sleep cycle
                # Find in which sleep cycle the current signal_model is included
                # Original signals
                idx_start = round(row["start_sec"],2)<=np.round(signals1_start,2)
                idx_stop = round(row["start_sec"]+row["duration_sec"],2) > np.round(signals1_start,2) # 3s epoch always aligned with cycle
                selected_signals = idx_start & idx_stop
                n_start_time_ori = sum(selected_signals)
                # Artifact free signal
                idx_start_art_free = round(row["start_sec"],2)<=np.round(signals1_start_art_free,2)
                idx_stop_art_free = round(row["start_sec"]+row["duration_sec"],2) > np.round(signals1_start_art_free,2) # 3s epoch always aligned with cycle
                selected_signals_art_free = idx_start_art_free & idx_stop_art_free
                signals1_event_sel = signals1_art_free[selected_signals_art_free]
                signals2_event_sel = signals2_art_free[selected_signals_art_free]
                # if there is at least one epoch in the current cycle
                if len(signals1_event_sel)>0:
                    desc = f'Calculating Accidental mutual information-cycle{sleep_cycle}'
                    pbar = tqdm(total=total_event, desc=desc)
                    ite = 0
                    ami = []
                    while (ite != parameters['max_iter']):
                        # Gennerate 2 random index to select 1x"10 s epoch" in signals1_event and 1x"10 s epoch" in signals2_event
                        rand_event_index = sample(range(len(signals1_event_sel)),2)
                        # Extract samples, samples1 is [n_channels x time series of 10 s epoch]
                        samples1 = SignalModel.get_attribute(signals1_event_sel[rand_event_index[0]], 'samples', None)
                        samples2 = SignalModel.get_attribute(signals2_event_sel[rand_event_index[1]], 'samples', None)
                        # Make sure signals have the same number of samples
                        if not samples1.shape[1] == samples2.shape[1]:
                            min_len = min(samples1.shape[1], samples2.shape[1])
                            samples1 = samples1[:,0:min_len]
                            samples2 = samples2[:,0:min_len]
                        #  Compute mutual information for each combination, combine_signals is [n_channels][2 x time series of 10 s epoch]
                        combine_signals = [[x,y] for x in samples1 for y in samples2]
                        mutual_info_event = np.hstack([mutual_info_score(combine_signal[0], combine_signal[1], contingency=None) for combine_signal in combine_signals])
                        ami.append(mutual_info_event)
                        ite += 1
                        pbar.update(1)
                    pbar.close
                    ami = np.hstack(ami)
                    # Get stats of the distribution. Will be used to calculate Z value.
                    mean_ami = np.mean(ami, axis=0)
                    std_ami = np.std(ami, axis=0)
                    # Calculate threshold
                    ami_distribution = np.sort(ami, axis=0)
                    area_undercurve = np.cumsum(ami_distribution)/np.sum(ami_distribution)
                    ami_threshold = ami_distribution[len(np.where(area_undercurve < parameters['confidence_level'])[0])]
                    z_score = (ami_threshold - mean_ami)/std_ami
                    if DEBUG:
                        print(f'z_score={z_score}')
                    # one criteria per start time
                    tmp_mean_ami_start = np.repeat(mean_ami, n_start_time_ori)
                    tmp_std_ami_start = np.repeat(std_ami, n_start_time_ori)
                    tmp_z_score_start = np.repeat(z_score, n_start_time_ori)
                    mean_ami_start.append(tmp_mean_ami_start)
                    std_ami_start.append(tmp_std_ami_start)
                    z_score_start.append(tmp_z_score_start)              
                sleep_cycle += 1
            if len(mean_ami_start)>0:
                mean_ami_start = np.hstack(mean_ami_start)
                std_ami_start = np.hstack(std_ami_start)    
                z_score_start = np.hstack(z_score_start)
        else:
            desc = 'Calculating Accidental mutual information'
            pbar = tqdm(total=total_event, desc=desc)
            ite = 0
            ami = []
            while ite != parameters['max_iter']:
                # Gennerate 2 random index to select 1x"10 s epoch" in signals1_art_free and 1x"10 s epoch" in signals2_art_free
                rand_event_index = sample(range(len(signals1_art_free)),2)
                # Extract samples, samples1 is [n_channels x time series of 10 s epoch]
                samples1 = SignalModel.get_attribute(signals1_art_free[rand_event_index[0]], 'samples', None)
                samples2 = SignalModel.get_attribute(signals2_art_free[rand_event_index[1]], 'samples', None)
                # Make sure signals have the same number of samples
                if not samples1.shape[1] == samples2.shape[1]:
                    min_len = min(samples1.shape[1], samples2.shape[1])
                    samples1 = samples1[:,0:min_len]
                    samples2 = samples2[:,0:min_len]

                #  Compute mutual information for each combination, combine_signals is [n_channels][2 x time series of 10 s epoch]
                combine_signals = [[x,y] for x in samples1 for y in samples2]
                mutual_info_event = np.hstack([mutual_info_score(combine_signal[0], combine_signal[1], contingency=None) for combine_signal in combine_signals])
                ami.append(mutual_info_event)
                ite += 1
                pbar.update(1)
            ami = np.hstack(ami)

            # Get stats of the distribution. Will be used to calculate Z value.
            mean_ami = np.mean(ami, axis=0)
            std_ami = np.std(ami, axis=0)
            # Calculate threshold
            ami_distribution = np.sort(ami, axis=0)
            area_undercurve = np.cumsum(ami_distribution)/np.sum(ami_distribution)
            ami_threshold = ami_distribution[len(np.where(area_undercurve < parameters['confidence_level'])[0])]
            z_score = (ami_threshold - mean_ami)/std_ami
            # one criteria per start time
            n_start_time = len(signals1_event)
            mean_ami_start = np.repeat(mean_ami, n_start_time)
            std_ami_start = np.repeat(std_ami, n_start_time)
            z_score_start = np.repeat(z_score, n_start_time)
            pbar.close

        # Write the cache
        cache = {}
        cache['ami_distribution'] = ami_distribution
        cache['ami_threshold'] = ami_threshold
        cache['confidence_level'] = parameters['confidence_level']
        cache['mean'] = mean_ami
        cache['std'] = std_ami
        cache['criteria'] = z_score
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {'mean_ami': mean_ami_start,
                'std_ami': std_ami_start,
                'criteria': z_score_start}
    
    
