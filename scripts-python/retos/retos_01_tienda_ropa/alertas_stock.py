import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")


query = """
SELECT p.id, p.nombre, p.stock, c.nombre_categoria
FROM prendas p
INNER JOIN categorias c ON p.categoria_id = c.id
WHERE p.stock < 6;
"""

cursor.execute(query)
filas = cursor.fetchall()

print(f"\033[31m{'🧵 REPORTE DE PRENDAS CON STOCK BAJO':^52}\033[0m")
print(f"{'='*52}")
print(f"\033[32m|{'ID':^3}|{'Nombre':^30}|{'Stock':^6}|{'Categoria':^8}|\033[0m")
print(f"{'='*52}")
for fila in filas:
    f = f"|{fila[0]:<3}|{fila[1]:<30}|{fila[2]:^6}|{fila[3]:^9}|"
    print(f"\033[33m{f}\033[0m")
print(f"{'='*52}")

conexion.close()

