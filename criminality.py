# importar pacotes
import streamlist as st
import pandas as pd
import pydeck as pdk

# carregar os dados de entrada
df = pd.read.csv("criminalidade_sp_2.csv")

# dashboard
st.title("Criminalidade em São Paulo") # Título do dashboard
st.markdown(
    """
A **criminalidade** é um *problema* recorrente no Brasil. Buscamos sempre formas de diminuir esses índices e usando técnicas de Ciências de Dados conseguimos entender melhor o que está acontecendo e gerar insights que direcionem ações capazes de diminuir os índices de criminalidade.
"""
)

st.sidebar.info("Foram carregadas {} linhas.".format(df.shape[0]))

if st.sidebar.checkbox("Mostrar tabelas de dados"):
    st.subhearder("Tabela de dados") # Cabeçalho
    st.write(df) # tabela do dataframe

# Mapa
st.subhearder("")
st.map(df)
