import streamlit as st
import pandas as pd

st.title("📑 Relatórios")


df = pd.read_csv("data/estudantes.csv")

cidade = st.selectbox(
    'Selecione a cidade',
    df['cidade'].unique()
)

filtrado = df[df['cidade'] == cidade]

st.subheader(f'Relatório — {cidade}')

st.dataframe(filtrado)

csv = filtrado.to_csv(index=False).encode('utf-8')

st.download_button(
    label='⬇️ Baixar relatório CSV',
    data=csv,
    file_name='relatorio.csv',
    mime='text/csv'
)