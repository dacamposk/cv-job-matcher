SKILLS_CONOCIDAS = {
    "lenguajes": [
        "python", "javascript", "typescript", "java", "c#", "c++", "php",
        "ruby", "go", "rust", "kotlin", "swift", "sql", "r",
    ],
    "frontend": [
        "react", "vue", "angular", "next.js", "nuxt", "svelte",
        "html", "css", "tailwind", "bootstrap", "sass", "ant design",
    ],
    "backend": [
        "django", "flask", "laravel", "node.js", "express", "spring",
        "django rest framework", "fastapi", ".net", "ruby on rails",
    ],
    "bases_de_datos": [
        "postgresql", "mysql", "mongodb", "oracle", "sqlite",
        "redis", "sql server", "firebase",
    ],
    "herramientas": [
        "git", "github", "gitlab", "docker", "kubernetes", "jenkins",
        "postman", "jira", "figma", "aws", "azure", "gcp",
    ],
    "data_ia": [
        "pandas", "numpy", "tensorflow", "pytorch", "scikit-learn",
        "power bi", "tableau", "excel",
    ],
}


def lista_plana():
    """Convierte el diccionario por categorías en una sola lista de skills."""
    todas = []
    for categoria in SKILLS_CONOCIDAS.values():
        todas.extend(categoria)
    return todas