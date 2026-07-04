import sqlite3
import os

# Apuntamos a la base de datos de tu tienda de ropa
ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "retos", "retos_01_tienda_ropa", "tienda.db"))

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# ====================================================================
# STEP 1: INSERTAR DATOS
# ====================================================================
print("📥 Insertando categorías de prueba...")

# Usamos '?' como marcadores de posición por seguridad (evita SQL Injection)
cursor.execute("INSERT INTO categorias (nombre_categoria) VALUES (?);", ("Sudaderas",))
cursor.execute("INSERT INTO categorias (nombre_categoria) VALUES (?);", ("Jeans",))

# 🚨 IMPORTANTÍSIMO: En SQL, los inserts se quedan en el aire ("limbo") 
# hasta que ejecutas un .commit(). Si no lo pones, los datos se pierden al cerrar.
conexion.commit()

# ====================================================================
# STEP 2: LEER DATOS
# ====================================================================
print("\n📤 Consultando base de datos...")
cursor.execute("SELECT id, nombre_categoria FROM categorias;")

# .fetchall() toma todas las filas que trajo el 'camión' (cursor) y las convierte en una lista de tuplas
filas = cursor.fetchall()

for fila in filas:
    # fila[0] es el id, fila[1] es el nombre
    print(f"🆔 ID: {fila[0]} | 📁 Categoría: {fila[1]}")

conexion.close()
