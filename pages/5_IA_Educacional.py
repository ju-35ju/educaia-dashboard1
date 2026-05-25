import streamlit as st
import random

st.title("🧠 IA Educacional")

st.write("Sistema inteligente de recomendação de estudos")

nota = st.slider('Informe sua média atual', 0.0, 10.0, 7.0)

if st.button('Gerar recomendação'):

    recomendacoes = [
        'Aumentar carga horária em matemática.',
        'Melhorar rotina de revisão semanal.',
        'Utilizar técnicas de Pomodoro.',
        'Priorizar exercícios práticos.',
        'Fazer simulados semanais.'
    ]

    st.success(random.choice(recomendacoes))

    if nota < 6:
        st.warning('⚠️ Risco de baixo desempenho acadêmico.')
    else:
        st.success('✅ Desempenho acadêmico satisfatório.')