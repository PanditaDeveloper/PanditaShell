import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "retos", "retos_01_tienda_ropa", "tienda.db"))

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

# Definimos la query relacional usando alias cortos (p para prendas, c para categorias)
query_relacional = """
SELECT p.id, p.nombre, p.precio, c.nombre_categoria
FROM prendas p
INNER JOIN categorias c ON p.categoria_id = c.id;
"""

cursor.execute(query_relacional)
filas = cursor.fetchall()

print("🧵 REPORTE DE PRENDAS CON SU CATEGORÍA REAL:")
print("-" * 60)
for fila in filas:
    # fila[0] = id, fila[1] = nombre, fila[2] = precio, fila[3] = nombre_categoria
    print(f"🆔 ID: {fila[0]} | 👕 {fila[1]:<30} | Q{fila[2]:<6} | 📁 Cat: {fila[3]}")
print("-" * 60)

conexion.close()
