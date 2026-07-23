import feedparser


def obtener_ofertas_chiletrabajos():
    """Lee el feed RSS de ofertas de Informatica/Telecomunicaciones de ChileTrabajos."""
    feed = feedparser.parse("https://www.chiletrabajos.cl/rss/informatica")

    ofertas = []
    for entrada in feed.entries:
        oferta = {
            "titulo": entrada.title,
            "url": entrada.link,
            "descripcion": entrada.get("summary", ""),
            "fecha": entrada.get("published", ""),
            "fuente": "ChileTrabajos",
        }
        ofertas.append(oferta)

    return ofertas


if __name__ == "__main__":
    ofertas = obtener_ofertas_chiletrabajos()
    print(f"Se encontraron {len(ofertas)} ofertas\n")
    for oferta in ofertas[:3]:
        print(oferta["titulo"])
        print(oferta["url"])
        print("-" * 40)