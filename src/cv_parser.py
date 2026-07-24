import re
import pdfplumber
from skills_data import lista_plana


def extraer_texto_pdf(ruta_archivo):
    """Abre un PDF y devuelve todo su texto como un solo string."""
    texto_completo = ""

    with pdfplumber.open(ruta_archivo) as pdf:
        for pagina in pdf.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_completo += texto_pagina + "\n"

    return texto_completo


def extraer_skills(texto):
    """Busca qué skills conocidas aparecen en el texto, evitando falsos positivos."""
    texto_normalizado = texto.lower()
    skills_encontradas = []

    for skill in lista_plana():
        patron = r"\b" + re.escape(skill) + r"\b"
        if re.search(patron, texto_normalizado):
            skills_encontradas.append(skill)

    return skills_encontradas