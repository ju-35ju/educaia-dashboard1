import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("🌎 Georreferenciamento Acadêmico")

# Dados fictícios
locais = pd.DataFrame({
    'cidade': ['Teresina', 'Fortaleza', 'Recife', 'Salvador'],
    'lat': [-5.0892, -3.7319, -8.0476, -12.9777],
    'lon': [-42.8019, -38.5267, -34.8770, -38.5016],
    'alunos': [320, 450, 280, 390]
})

# Mapa
m = folium.Map(location=[-8.0, -40.0], zoom_start=5)

for _, row in locais.iterrows():
    folium.Marker(
        [row['lat'], row['lon']],
        popup=f"{row['cidade']} - {row['alunos']} alunos",
        tooltip=row['cidade']
    ).add_to(m)

st_folium(m, width=1200, height=600)