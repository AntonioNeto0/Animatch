import streamlit as st
import pandas as pd

projectName = "Anime Bucket"
ds = pd.read_csv("../resources_dataset/dataset/Anime.csv")




def main():
    st.set_page_config(page_title=projectName,page_icon="🌊")
    st.title(projectName)
    st.dataframe(ds)
    st.write('Média de Rating = ' + str(round(ds['Rating'].mean(),4)))
    st.markdown('**TIPOS DE ANIME**')

    #Substituindo a Release_season FALL por AUTUMN
    ds['Release_season'].replace(['Fall'],'Autumn',inplace=True)

    #Plotandao graficos pela barra lateral
    grafico = st.sidebar.selectbox('Gaficos',['Type','Release_season'])
    ds_type = ds[grafico].value_counts().plot(kind = 'barh')
    st.pyplot(ds_type.figure)

if __name__ == '__main__':
    main()