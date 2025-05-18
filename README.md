# MCP World Time Explorer

Esta aplicación utiliza Streamlit y MCP (Model Context Protocol) para proporcionar información sobre la hora actual en cualquier país o zona horaria del mundo.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Clave API de OpenAI (para GPT-4)

## Configuración

1. Clone este repositorio
2. Cree un archivo `.env` en la raíz del proyecto y agregue su clave API de OpenAI:
   ```
   OPENAI_API_KEY=su_clave_api_aquí
   ```

## Instalación

Ejecute el siguiente comando para instalar las dependencias:

```bash
make install
```

## Uso

Para iniciar la aplicación, ejecute:

```bash
make run
```

La aplicación se abrirá en su navegador predeterminado. Simplemente ingrese el nombre de un país o ciudad y presione "Consultar Hora" para obtener la hora actual en esa ubicación.

## Características

- Interfaz de usuario intuitiva con Streamlit
- Soporte para consultas en múltiples idiomas
- Información precisa de la hora actual en cualquier ubicación
- Integración con GPT-4 para un procesamiento natural del lenguaje

## Licencia

MIT
