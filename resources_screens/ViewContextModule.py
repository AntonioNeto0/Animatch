#import main as main
import resources_screens.exploratoryAnalysis as exploratoryAnalysis

class ViewHandler:
    def __init__(self, datasetHandler, plottingPHandler):


        # self.mainScreen = main.Screen()
        self.exploratoryAScreen =  exploratoryAnalysis.Screen(plottingPHandler)