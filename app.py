import asyncio
import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient
import pytz

# Configuración de la página
st.set_page_config(page_title="MCP World Time Explorer", page_icon="🕒", layout="wide")

# Cargar variables de entorno
load_dotenv()

# Función para procesar la consulta
async def process_query(location):
    # Crear MCPClient desde el archivo de configuración
    client = MCPClient.from_config_file(
        os.path.join(os.path.dirname(__file__), "time_mcp.json")
    )

    # Crear LLM
    llm = ChatOpenAI(model="gpt-4")

    # Crear agente
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    try:
        prompt = f"Get the current time for {location}"
        result = await agent.run(prompt, max_steps=30)
        return result
    finally:
        if client.sessions:
            await client.close_all_sessions()

# Título y descripción
st.title("🕒 MCP World Time Explorer")
st.markdown(
    """
Esta aplicación te permite consultar la hora actual en cualquier país o zona horaria del mundo
usando el MCP Time Server. Simplemente ingresa el nombre del país o ciudad.
"""
)

# Entrada de ubicación
with st.form("world_time_form"):
    location = st.text_input("País o Ciudad", placeholder="España, Tokyo, New York...")
    submit_button = st.form_submit_button("Consultar Hora")

# Procesar la solicitud cuando se envía el formulario
if submit_button and location:
    with st.spinner("Consultando hora..."):
        try:
            result = asyncio.run(process_query(location))

            # Mostrar resultados
            st.success("¡Consulta completada!")

            with st.expander("Ver resultados", expanded=True):
                st.markdown("### Hora actual")
                st.write(result)

        except Exception as e:
            st.error(f"Error al consultar la hora: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center'>
    <p>Desarrollado por <a href='https://github.com/gildder'>Gildder</a> |
    Usando MCP Time Server y Streamlit</p>
</div>
""",
    unsafe_allow_html=True,
)
