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


if __name__ == "__main__":
    texto = extraer_texto_pdf("mi_cv.pdf")
    print(texto)


    SKILLS_CONOCIDAS = [
    "python", "javascript", "typescript", "java", "sql",
    "react", "next.js", "html5", "html", "css3", "css", "tailwind",
    "django", "laravel", "node.js", "django rest framework",
    "postgresql", "mysql", "oracle", "sqlite",
    "git", "github", "postman",
]


def extraer_skills(texto):
    """Busca qué skills conocidas aparecen en el texto del CV."""
    texto_normalizado = texto.lower()
    skills_encontradas = []

    for skill in SKILLS_CONOCIDAS:
        if skill in texto_normalizado:
            skills_encontradas.append(skill)

    return skills_encontradas


if __name__ == "__main__":
    texto = extraer_texto_pdf("mi_cv.pdf")
    skills = extraer_skills(texto)
    print("Skills encontradas:", skills)