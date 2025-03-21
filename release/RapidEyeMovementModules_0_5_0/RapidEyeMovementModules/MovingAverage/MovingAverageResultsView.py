"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the MovingAverage plugin
"""
from CEAMSModules.SignalsFromEvents.SignalsFromEventsResultsView import SignalsFromEventsResultsView


class MovingAverageResultsView(SignalsFromEventsResultsView):
    """
        MovingAverageResultsView show the signals averaged through a moving window
    """
