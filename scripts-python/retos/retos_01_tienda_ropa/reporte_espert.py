import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()


query_relacion = """
SELECT p.id, p.nombre, p.precio, p.stock, c.nombre_categoria
FROM prendas p
INNER JOIN categorias c ON p.categoria_id = c.id;
"""

cursor.execute(query_relacion)
filas = cursor.fetchall()

print(f"\033[31m{'🧵 REPORTE DE PRENDAS CON SU CATEGORÍA':^62}\033[0m")
print(f"{'='*62}")
print(f"\033[32m|{'ID':^3}|{'Nombre':^30}|{'Precio':^8}|{'Stock':^6}|{'Categoria':^8}|\033[0m")
print(f"{'='*62}")
for fila in filas:
    f = f"|{fila[0]:<3}|{fila[1]:<30}|Q{fila[2]:>7.2f}|{fila[3]:^6}|{fila[4]:^9}|"
    if int(fila[0]) % 2 == 0:
        print(f"\033[34m{f}\033[0m")
    else:
        print(f"\033[33m{f}\033[0m")
print(f"{'='*62}")

conexion.close()


