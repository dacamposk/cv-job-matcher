import time
from cv_parser import extraer_texto_pdf
from connectors.chiletrabajos import obtener_ofertas_chiletrabajos
from connectors.getonbrd import obtener_ofertas_getonbrd
from connectors.bne import obtener_ofertas_bne
from matcher import calcular_compatibilidad
from db import obtener_conexion, ya_fue_vista, marcar_como_vista
from notifier import notificar_oferta

UMBRAL_COMPATIBILIDAD = 10


def obtener_todas_las_ofertas():
    """Junta ofertas de todas las fuentes disponibles en una sola lista."""
    ofertas = []
    ofertas.extend(obtener_ofertas_chiletrabajos()[:100])
    ofertas.extend(obtener_ofertas_getonbrd())
    ofertas.extend(obtener_ofertas_bne())
    return ofertas


def main():
    texto_cv = extraer_texto_pdf("mi_cv.pdf")

    ofertas = obtener_todas_las_ofertas()
    print(f"Total de ofertas recolectadas: {len(ofertas)}")

    resultado = calcular_compatibilidad(texto_cv, ofertas)

    conexion = obtener_conexion()

    ofertas_nuevas = [
        oferta for oferta in resultado
        if not ya_fue_vista(conexion, oferta["url"])
        and oferta["compatibilidad"] >= UMBRAL_COMPATIBILIDAD
    ]

    print(f"Ofertas nuevas relevantes: {len(ofertas_nuevas)}\n")

    for oferta in ofertas_nuevas:
        enviado = notificar_oferta(oferta)
        estado = "✅" if enviado else "❌"
        print(f"{estado} [{oferta['fuente']}] {oferta['compatibilidad']}% — {oferta['titulo']}")

        if enviado:
            marcar_como_vista(conexion, oferta["url"], oferta["titulo"])

        time.sleep(1)

    conexion.close()


if __name__ == "__main__":
    main()