import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))
conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

# 🚨 El activador maestro de seguridad
cursor.execute("PRAGMA foreign_keys = ON;")

# Tabla 1: Categorías
cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_categoria TEXT NOT NULL
);
""")

# Tabla 2: Prendas (Inventario)
cursor.execute("""
CREATE TABLE IF NOT EXISTS prendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    talla TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE RESTRICT
);
""")

# Tabla 3: Ventas (La cabecera de la factura)
cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    total REAL NOT NULL
);
""")

# Tabla 4: Detalles Ventas (La hermosa tabla de ruptura N:M)
cursor.execute("""
CREATE TABLE IF NOT EXISTS detalles_ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venta_id INTEGER,
    prenda_id INTEGER,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    FOREIGN KEY (venta_id) REFERENCES ventas(id) ON DELETE CASCADE,
    FOREIGN KEY (prenda_id) REFERENCES prendas(id) ON DELETE RESTRICT
);
""")

conexion.commit()
print("🧱 Arquitectura relacional de Facturación (N:M) inicializada sin errores.")
conexion.close()
