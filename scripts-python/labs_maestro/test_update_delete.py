import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "retos", "retos_01_tienda_ropa", "tienda.db"))

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# ====================================================================
# STEP 1: MODIFICAR (UPDATE)
# ====================================================================
print("📝 Modificando stock del producto con ID 1...")
# Ponemos el marcador de posición ? para los valores dinámicos
cursor.execute("UPDATE prendas SET stock = ? WHERE id = ?;", (25, 1))

# ====================================================================
# STEP 2: ELIMINAR (DELETE)
# ====================================================================
print("🚨 Eliminando el producto con ID 3...")
cursor.execute("DELETE FROM prendas WHERE id = ?;", (3,))

# Guardamos los cambios de forma permanente en el archivo tienda.db
conexion.commit()
print("💾 Cambios consolidados en el disco duro.")

# Comprobación rápida para ver cómo quedó la base de datos
cursor.execute("SELECT id, nombre, stock FROM prendas;")
for fila in cursor.fetchall():
    print(f"🆔 ID: {fila[0]} | 👕 {fila[1]:<25} | 📦 Stock Actual: {fila[2]} uds")

conexion.close()
