from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL_BASE = "https://www.bne.gob.cl/ofertas?mostrar=empleo&numPaginaRecuperar=1&numResultadosPorPagina=50&clasificarYPaginar=true"


def obtener_ofertas_bne(termino_busqueda="desarrollador"):
    """Busca ofertas en BNE usando el buscador del sitio, controlado con Playwright."""
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page()
        pagina.goto(URL_BASE, wait_until="networkidle")

        pagina.click("#buscadorOfertas")
        pagina.type("#buscadorOfertas", termino_busqueda, delay=100)
        pagina.wait_for_timeout(1000)
        pagina.click("#botonBuscarOfertas")
        pagina.wait_for_load_state("networkidle")
        pagina.wait_for_timeout(1000)

        html = pagina.content()
        navegador.close()

    # ... el resto de la función queda igual
    soup = BeautifulSoup(html, "html.parser")
    ofertas = []

    tarjetas = soup.select("article.resultadoOfertas")
    for tarjeta in tarjetas:
        titulo_tag = tarjeta.select_one("div.tituloOferta span")
        descripcion_tag = tarjeta.select_one("div.descripcionOferta span")
        link_tag = tarjeta.select_one("div.tituloOferta a")
        fecha_tag = tarjeta.select_one("span.fechaOferta")
        empresa_tag = tarjeta.select_one("div.datosEmpresaOferta div")

        if not titulo_tag or not link_tag:
            continue

        oferta = {
            "titulo": titulo_tag.get_text(strip=True),
            "url": "https://www.bne.gob.cl" + link_tag["href"],
            "descripcion": descripcion_tag.get_text(strip=True) if descripcion_tag else "",
            "fecha": fecha_tag.get_text(strip=True) if fecha_tag else "",
            "fuente": "BNE",
        }
        ofertas.append(oferta)

    return ofertas


if __name__ == "__main__":
    ofertas = obtener_ofertas_bne()
    print(f"Se encontraron {len(ofertas)} ofertas\n")
    for oferta in ofertas[:3]:
        print(oferta["titulo"])
        print(oferta["descripcion"][:100])
        print(f"Fecha: {oferta['fecha']}")
        print(oferta["url"])
        print("-" * 40)