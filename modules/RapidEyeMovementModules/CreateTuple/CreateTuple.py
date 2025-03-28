"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    CreateTuple
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class CreateTuple(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        Idx0: TODO TYPE
            TODO DESCRIPTION
        Idx1: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        Tuple: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module CreateTuple """
        super().__init__(**kwargs)
        if DEBUG: print('CreateTuple.__init__')

        # Input plugs
        InputPlug('Idx0',self)
        InputPlug('Idx1',self)
        

        # Output plugs
        OutputPlug('Tuple',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, Idx0,Idx1):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            Idx0: TODO TYPE
                TODO DESCRIPTION
            Idx1: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            Tuple: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        First = Idx0
        Second = Idx1
        Tuple = (First, Second)

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module creates a tuple.")

        return {
            'Tuple': Tuple
        }