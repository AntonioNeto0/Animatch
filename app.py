import streamlit as st
import resources_screens.ViewContextModule as viewCM
import resources_plotting.plottingModule as plottingM
import resources_dataset.datasetModule as datasetM

projectName = "Anime Bucket"

def main():
    datasetHandler = datasetM.Handler()
    plottingPHandler = plottingM.Handler(datasetHandler.ds)
    viewHandler = viewCM.ViewHandler(datasetHandler, plottingPHandler)
    st.set_page_config(page_title=projectName,page_icon="🌊")
    viewHandler.exploratoryAScreen.load_screen()

if __name__ == '__main__':
    main()