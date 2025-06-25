import streamlit as st
from openai import OpenAI
import traceback

# Usa tu clave desde Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Traductor GPT de Olivia", layout="centered")
st.title("🌍 Traductor GPT de Olivia: Hola mundo")

# Lista de idiomas disponibles
idiomas = [
    "Español", "Inglés", "Francés", "Alemán", "Italiano", "Portugués",
    "Chino", "Japonés", "Árabe", "Ruso", "Hindi", "Coreano", "Neerlandés", 
    "Sueco", "Griego", "Turco", "Polaco", "Hebreo", "Vietnamita", "Catalán"
]

# Selector de idioma
idioma_seleccionado = st.selectbox("Selecciona un idioma", idiomas)

# Botón para lanzar la traducción
if st.button("Traducir 'Hola mundo' (by Olivia)"):

    prompt = f"Traduce 'Hola mundo' al idioma {idioma_seleccionado}. Devuélveme solo la traducción, sin explicaciones."

    with st.spinner("Traduciendo con GPT..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Puedes cambiar por "gpt-4" si tienes acceso
                messages=[
                    {"role": "system", "content": "Eres un traductor profesional."},
                    {"role": "user", "content": prompt}
                ]
            )

            traduccion = response.choices[0].message.content.strip()
            st.success(f"Traducción en {idioma_seleccionado}:")
            st.markdown(f"### {traduccion}")

        except Exception as e:
            st.error("❌ Ocurrió un error con la API de OpenAI:")
            st.code(str(e))
            st.text("Detalles técnicos:")
            st.text(traceback.format_exc())
