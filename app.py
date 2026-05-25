import streamlit as st

st.set_page_config(
    page_title="EducaIA",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class='hero'>
    <h1>🎓 EducaIA</h1>
    <h3>Plataforma Inteligente de Gestão Acadêmica</h3>
    <p>
        Monitoramento acadêmico, inteligência analítica,
        produtividade e acompanhamento estudantil em tempo real.
    </p>
</div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👨‍🎓 Estudantes", "12.540", "+14%")

with col2:
    st.metric("📚 Horas Estudadas", "48.920", "+22%")

with col3:
    st.metric("📈 Média Geral", "8.7", "+0.8")

with col4:
    st.metric("🧠 Engajamento", "92%", "+11%")

st.divider()

st.markdown("## 🚀 Sobre a Plataforma")

st.write("""
A EducaIA é uma plataforma educacional inteligente desenvolvida para auxiliar
instituições e estudantes no monitoramento de desempenho acadêmico,
produtividade e análise comportamental.

O sistema utiliza dashboards interativos, inteligência analítica
 e visualização geográfica para gerar insights educacionais.
""")

st.image(
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
    use_container_width=True
)