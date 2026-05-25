import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("📊 Dashboard Acadêmico")

# Carregando dados

df = pd.read_csv("data/estudantes.csv")

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Estudantes", len(df))

with col2:
    st.metric("Nota Média", round(df['nota'].mean(), 2))

with col3:
    st.metric("Engajamento Médio", f"{round(df['engajamento'].mean(), 1)}%")

st.divider()

# Pizza
fig_pizza = px.pie(
    df,
    names='disciplina',
    title='Distribuição por Disciplina',
    hole=0.4
)

# Barras
fig_bar = px.bar(
    df.groupby('cidade')['nota'].mean().reset_index(),
    x='cidade',
    y='nota',
    title='Média de Notas por Cidade',
    text_auto=True
)

# Linha
fig_line = px.line(
    df.groupby('idade')['horas_estudo'].mean().reset_index(),
    x='idade',
    y='horas_estudo',
    title='Horas de Estudo por Idade'
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.plotly_chart(fig_bar, use_container_width=True)

st.plotly_chart(fig_line, use_container_width=True)

# Tabela dinâmica
st.subheader("📋 Base de Dados")

st.dataframe(df)