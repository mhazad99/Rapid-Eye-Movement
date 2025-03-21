"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Find the Z values for a list of scores.
    Parameters
    -----------
        samples: List of SignalModel
            List of scores for each window in each index of the list
        mean: float
            Mean of the distribution
        std: float
            Standard deviation of the distribution
        criteria [optional]: float 
            Threshold to add in result view. Only used to show results. 

    Returns
    -----------    
        z_values : List
            List of Z values for each window in each index of the list
"""


import numpy as np
import pandas as pd

from commons.NodeInputException import NodeInputException
from CEAMSModules.PSGReader.SignalModel import SignalModel
from flowpipe import SciNode, InputPlug, OutputPlug

DEBUG = False

class MutualInfoZScore(SciNode):
    """
        Find the Z values for a list of scores.
        Parameters
        -----------
            samples: List of SignalModel
                List of scores for each window in each index of the list
            mean: float
                Mean of the distribution
            std: float
                Standard deviation of the distribution
            criteria [optional]: float 
                Threshold to add in result view. Only used to show results. 

        Returns
        -----------    
            z_values : List
                List of Z values for each window in each index of the list
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('MutualInfoZScore.__init__')
        self._filename = None
        InputPlug('samples', self)
        InputPlug('mean', self)
        InputPlug('std', self)
        InputPlug('criteria', self)
        OutputPlug('z_values', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, samples, mean, std, criteria):
        """
            Find the Z values for a list of scores.
            Parameters
            -----------
                samples: List of SignalModel
                    List of scores for each window in each index of the list. shape [n,m,o]
                    dimension for REM corrector : [n_start, n_chans, n_time_series_point]
                mean: List (of float)
                    Mean of the distribution, [n_start] items in the list.
                    A list to support different distribution through the night.
                std:  List (of float)
                    Standard deviation of the distribution, [n_start] items in the list.
                    A list to support different distribution through the night.
                criteria [optional]: List (of float) 
                    Threshold to add in result view. Only used to show results. 
                    A list to support different distribution through the night.

            Returns
            -----------    
                z_values : List of SignalModel
                    The Z values (in meta) for each window in each index of the list
        """

        if DEBUG: print('MutualInfoZScore.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        samples = list(samples)
        # Verify inputs
        if isinstance(samples,str) and samples=='':
            err_message = "ERROR: samples not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "samples", \
                f"MutualInfoZScore this input is not connected.")
        if not isinstance(samples,list):
            err_message = "ERROR: samples unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "samples", \
                f"MutualInfoZScore input of wrong type. Expected: <class 'list'> received: {type(samples)}")
        elif isinstance(samples, list) and len(samples)==0:
            return {'z_values': ''}
        if isinstance(mean,str) and mean=='':
            err_message = "ERROR: mean not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "mean", \
                f"MutualInfoZScore this input is not connected.")
        if isinstance(std,str) and std=='':
            err_message = "ERROR: std not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "std", \
                f"MutualInfoZScore this input is not connected.")

        # Compute the zvalue for each item of samples (channels of every 10_s_epoch_R stage)
        # The mean and std can varity for each start time (useful when they vary for each sleep cycle)
        #   samples_meta_per_start is 3 dimensions [n_MOR_3_s][n_channels][meta]
        #   signal that share all the same start time are grouped together
        samples_meta_per_start = SignalModel.get_attribute(samples, 'meta', 'start_time') 
        z_values = []
        for i, start_data in enumerate(samples_meta_per_start):
            z_values_cur = [(sample['mutual_info'] - mean[i])/std[i] for sample in start_data]
            z_values.append(z_values_cur)
        z_values = np.hstack(z_values)

        # Code when only one mean and std are available for the whole recording
        # samples is [n_rem_10_s x n_channels] SignalModel
        # z_values = [(sample.meta['mutual_info'] - mean)/std for sample in samples]

        # Order the samples as the samples_meta_per_start
        samples_ordered = SignalModel.get_attribute(samples, None, 'start_time')
        samples_ordered = np.hstack(samples_ordered).tolist()
        # Init the z_value via samples, add the information into meta field
        for i, sample in enumerate(samples_ordered):
            sample.meta['z_value'] = z_values[i]
        
        # Write the cache
        cache = {}
        cache['z_values'] = samples
        cache['criteria'] =  criteria

        self._cache_manager.write_mem_cache(self.identifier, cache)
        return {'z_values': samples}     
    
    
