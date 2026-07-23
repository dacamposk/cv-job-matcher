import sqlite3


def obtener_conexion():
    """Abre (o crea si no existe) la base de datos y asegura que la tabla exista."""
    conexion = sqlite3.connect("ofertas.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ofertas_vistas (
            url TEXT PRIMARY KEY,
            titulo TEXT,
            fecha_vista TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexion.commit()

    return conexion


def ya_fue_vista(conexion, url):
    """Revisa si una oferta (por su URL) ya fue notificada antes."""
    cursor = conexion.cursor()
    cursor.execute("SELECT 1 FROM ofertas_vistas WHERE url = ?", (url,))
    return cursor.fetchone() is not None


def marcar_como_vista(conexion, url, titulo):
    """Guarda una oferta como ya vista, para no repetirla."""
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO ofertas_vistas (url, titulo) VALUES (?, ?)",
        (url, titulo)
    )
    conexion.commit()


if __name__ == "__main__":
    conexion = obtener_conexion()

    url_prueba = "https://ejemplo.com/oferta-de-prueba"
    print("¿Ya vista antes?", ya_fue_vista(conexion, url_prueba))

    marcar_como_vista(conexion, url_prueba, "Oferta de prueba")
    print("¿Ya vista ahora?", ya_fue_vista(conexion, url_prueba))

    conexion.close()