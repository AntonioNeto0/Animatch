import streamlit as st
import pandas as pd

ds = pd.read_csv("../resources_dataset/dataset/Anime.csv")
projectName = "Anime Bucket"

def main():
    st.set_page_config(layout="wide",page_title=projectName,page_icon="🌊")
    st.title(projectName)
    st.dataframe(ds)

if __name__ == '__main__':
    main()

st.write('Média de Rating = ' + str(round(ds['Rating'].mean(),4)))
st.markdown('**TIPOS DE ANIME**')
ds_type = ds['Type'].value_counts().plot(kind = 'barh')
st.pyplot(ds_type.figure)