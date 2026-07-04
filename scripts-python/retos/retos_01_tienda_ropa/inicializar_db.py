import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))

conexion = sqlite3.connect(ruta_db)

cursor = conexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

print("💾 Conexión establecida con SQLite exitosamente.")

cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_categoria TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS prendas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    talla TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE RESTRICT
);
""")

conexion.commit()
print("🧱 Tablas 'categorias' y 'prendas' creadas e interconectadas de forma relacional.")

conexion.close()
