from playwright.sync_api import sync_playwright

URL = "https://www.bne.gob.cl/ofertas?mostrar=empleo&numPaginaRecuperar=1&numResultadosPorPagina=10&clasificarYPaginar=true"

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    pagina = navegador.new_page()
    pagina.goto(URL, wait_until="networkidle")

    html = pagina.content()
    navegador.close()

with open("pagina_bne.html", "w", encoding="utf-8") as archivo:
    archivo.write(html)

print("HTML guardado en pagina_bne.html")
print(f"Largo del HTML: {len(html)} caracteres")