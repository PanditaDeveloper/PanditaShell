import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

print("📥 Insertando datos en la tabla prendas...")

nuevas_prendas = [
    ("Sueter Panda dev", "S", 65.0, 5, 1),
    ("Pantalon de bambu", "S", 105.0, 5, 2),
    ("Sueter para dormir", "S", 150.0, 10, 1),
    ("Pantalon para tomar la siesta", "S", 50.0, 5, 2)
]

cursor.executemany(
    "INSERT INTO prendas (nombre, talla, precio, stock, categoria_id) VALUES (?, ?, ?, ?, ?);",
    nuevas_prendas
)

conexion.commit()

print("\n📤 Consultando base de datos...")
cursor.execute("SELECT * FROM prendas;")

filas = cursor.fetchall()

print(f"{'='*70}")
print(f"\033[32m|{'ID':^3}|{'Nombre':^30}|{'Talla':^6}|{'Precio':^8}|{'Stock':^6}|{'Categoria':^8}|\033[0m")
print(f"{'='*70}")
for fila in filas:
    f = f"|{fila[0]:<3}|{fila[1]:<30}|{fila[2]:^6}|Q{fila[3]:>7.2f}|{fila[4]:^6}|{fila[5]:^9}|"
    if int(fila[0]) % 2 == 0:
        print(f"\033[34m{f}\033[0m")
    else:
        print(f"\033[33m{f}\033[0m")
print(f"{'='*70}")

conexion.close()

