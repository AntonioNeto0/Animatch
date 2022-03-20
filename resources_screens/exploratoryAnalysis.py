import streamlit as st
class Screen:
    def __init__ (self, plottingPackageHandler):
        self.plottingPackageHandler = plottingPackageHandler
    
    def load_screen(self):
        st.title("Análise Exploratória")
        currentPackage = self.plottingPackageHandler.packageList[self.plottingPackageHandler.packageNameList.index(st.selectbox("Análises",self.plottingPackageHandler.packageNameList))]
        st.text(currentPackage.name)
        st.pyplot(currentPackage.build_figure())
        with st.expander("Descrição"):
            st.write(currentPackage.description)
