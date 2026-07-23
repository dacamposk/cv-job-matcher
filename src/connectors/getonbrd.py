import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "cv-job-matcher-bot (proyecto de portafolio)"}


def obtener_ofertas_getonbrd():
    """Scrapea la página de empleos de programación de GetOnBrd."""
    respuesta = requests.get("https://www.getonbrd.com/jobs/programming", headers=HEADERS)
    soup = BeautifulSoup(respuesta.text, "html.parser")

    ofertas = []
    tarjetas = soup.select("a.results-item")

    for tarjeta in tarjetas:
        strongs = tarjeta.select("div.results-list-info strong")
        if len(strongs) < 2:
            continue

        titulo = strongs[0].get_text(strip=True)
        empresa = strongs[1].get_text(strip=True)
        descripcion = tarjeta.get("title", "")
        url = tarjeta.get("href")

        fecha_tag = tarjeta.select_one("div.opacity-half.size0")
        fecha = fecha_tag.get_text(strip=True) if fecha_tag else ""

        oferta = {
            "titulo": f"{titulo} en {empresa}",
            "url": url,
            "descripcion": descripcion,
            "fecha": fecha,
            "fuente": "GetOnBrd",
        }
        ofertas.append(oferta)

    return ofertas

if __name__ == "__main__":
    ofertas = obtener_ofertas_getonbrd()
    print(f"Se encontraron {len(ofertas)} ofertas\n")
    for oferta in ofertas[:3]:
        print(oferta["titulo"])
        print(oferta["descripcion"][:100])
        print(f"Fecha: {oferta['fecha']}")
        print(oferta["url"])
        print("-" * 40)