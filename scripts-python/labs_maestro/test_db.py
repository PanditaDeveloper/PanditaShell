import sqlite3
import os

# Determinamos la ruta donde se guardará el archivo físico de la base de datos
ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))

# 1. Nos conectamos. Si el archivo 'tienda.db' no existe, SQLite lo creará al instante.
conexion = sqlite3.connect(ruta_db)

# 2. El cursor es el 'camión' encargado de llevar y traer los comandos SQL
cursor = conexion.cursor()

# 3. 🚨 REGLA DE ORO: Activamos el soporte de llaves foráneas obligatoriamente
cursor.execute("PRAGMA foreign_keys = ON;")

print("💾 Conexión establecida con SQLite exitosamente.")

# 4. Creamos la tabla PADRE (Clientes)
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nit TEXT DEFAULT 'C/F'
);
""")

# 5. Creamos la tabla HIJO (Ventas) con su FOREIGN KEY
cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    total REAL NOT NULL,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT
);
""")

# Guardamos los cambios estructurales en el disco
conexion.commit()
print("🧱 Tablas 'clientes' y 'ventas' creadas e interconectadas de forma relacional.")

# Cerramos la conexión para liberar la memoria
conexion.close()

