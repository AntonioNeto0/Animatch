import streamlit as st
import pandas as pd

ds = pd.read_csv("../resources_dataset/dataset/Anime.csv")
projectName = "Anime Bucket"

def main():
    st.set_page_config(page_title=projectName,page_icon="🌊")
    st.title(projectName)
    st.dataframe(ds)

if __name__ == '__main__':
    main()

st.write('Média de Rating = ' + str(round(ds['Rating'].mean(),4)))
st.markdown('**TIPOS DE ANIME**')

grafico = st.sidebar.selectbox('Gaficos',['Type','Release_season'])
ds_type = ds[grafico].value_counts().plot(kind = 'bar')
st.pyplot(ds_type.figure)