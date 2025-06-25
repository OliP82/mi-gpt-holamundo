import streamlit as st
from openai import OpenAI

# API Key (recomiendo usar st.secrets en producción)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Traductor GPT", layout="centered")
st.title("🌍 Traductor GPT: Hola mundo")

# Lista de idiomas comunes
idiomas = [
    "Español", "Inglés", "Francés", "Alemán", "Italiano", "Portugués",
    "Chino", "Japonés", "Árabe", "Ruso", "Hindi", "Coreano", "Neerlandés", 
    "Sueco", "Griego", "Turco", "Polaco", "Hebreo", "Vietnamita", "Catalán"
]

# Desplegable para seleccionar idioma
idioma_seleccionado = st.selectbox("Selecciona un idioma", idiomas)

if st.button("Traducir 'Hola mundo'"):
    prompt = f"Traduce 'Hola mundo' al idioma {idioma_seleccionado}. Solo devuelve la traducción, sin explicaciones."

    with st.spinner("Traduciendo con GPT..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un traductor profesional."},
                {"role": "user", "content": prompt}
            ]
        )
        traduccion = response.choices[0].message.content.strip()
        st.success(f"Traducción en {idioma_seleccionado}:")
        st.markdown(f"### {traduccion}")
