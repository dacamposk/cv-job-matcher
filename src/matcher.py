from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from stop_words import get_stop_words

def calcular_compatibilidad(texto_cv, ofertas):
    """Compara el texto del CV contra una lista de ofertas y devuelve un score por cada una."""

    textos_ofertas = [oferta["titulo"] + " " + oferta["descripcion"] for oferta in ofertas]

    todos_los_textos = [texto_cv] + textos_ofertas

    stopwords_es = get_stop_words("spanish")
    vectorizador = TfidfVectorizer(stop_words=stopwords_es)
    matriz_tfidf = vectorizador.fit_transform(todos_los_textos)

    vector_cv = matriz_tfidf[0:1]
    vectores_ofertas = matriz_tfidf[1:]
    similitudes = cosine_similarity(vector_cv, vectores_ofertas)[0]

    for oferta, score in zip(ofertas, similitudes):
        oferta["compatibilidad"] = round(float(score) * 100, 1)

    
    ofertas_ordenadas = sorted(ofertas, key=lambda o: o["compatibilidad"], reverse=True)

    return ofertas_ordenadas


if __name__ == "__main__":
    from cv_parser import extraer_texto_pdf
    from connectors.chiletrabajos import obtener_ofertas_chiletrabajos

    texto_cv = extraer_texto_pdf("mi_cv.pdf")
    ofertas = obtener_ofertas_chiletrabajos()[:100]  

    resultado = calcular_compatibilidad(texto_cv, ofertas)

    print("Top 5 ofertas más compatibles:\n")
    for oferta in resultado[:5]:
        print(f"{oferta['compatibilidad']}% — {oferta['titulo']}")
        print(oferta["url"])
        print("-" * 40)