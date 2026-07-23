import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def notificar_oferta(oferta):
    """Envía un mensaje a Discord con los datos de una oferta compatible."""
    mensaje = (
        f"**{oferta['compatibilidad']}% de compatibilidad**\n"
        f"**{oferta['titulo']}**\n"
        f"{oferta['url']}"
    )

    respuesta = requests.post(WEBHOOK_URL, json={"content": mensaje})
    return respuesta.status_code == 204


if __name__ == "__main__":
    oferta_prueba = {
        "titulo": "Desarrollador de Prueba",
        "url": "https://ejemplo.com/oferta-prueba",
        "compatibilidad": 42.0,
    }

    enviado = notificar_oferta(oferta_prueba)
    print("¿Se envió correctamente?", enviado)