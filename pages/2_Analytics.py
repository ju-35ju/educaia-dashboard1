import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("📈 Analytics Avançado")


df = pd.read_csv("data/estudantes.csv")

# Heatmap
pivot = df.pivot_table(
    values='nota',
    index='cidade',
    columns='disciplina',
    aggfunc='mean'
)

fig_heat = px.imshow(
    pivot,
    text_auto=True,
    aspect='auto',
    title='Mapa de Calor de Notas'
)

st.plotly_chart(fig_heat, use_container_width=True)

# Scatter
fig_scatter = px.scatter(
    df,
    x='horas_estudo',
    y='nota',
    color='disciplina',
    size='engajamento',
    hover_name='nome',
    title='Correlação entre Horas de Estudo e Nota'
)

st.plotly_chart(fig_scatter, use_container_width=True)

# Waterfall
fig_water = go.Figure(go.Waterfall(
    name='Performance',
    orientation='v',
    measure=['relative', 'relative', 'relative', 'total'],
    x=['Estudos', 'Engajamento', 'Projetos', 'Resultado Final'],
    textposition='outside',
    y=[20, 15, 10, 0]
))

fig_water.update_layout(title='Análise de Crescimento Acadêmico')

st.plotly_chart(fig_water, use_container_width=True)