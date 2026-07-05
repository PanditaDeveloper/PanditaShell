import sqlite3
import os

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))
conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

try:
    print("📥 Insertando datos en la tabla categorias...")
    nuevas_categorias = [
        ("Sudaderas",),
        ("Pantalones",),
        ("Camisas",),
        ("Gorras",)
    ]

    cursor.executemany(
        "INSERT INTO categorias (nombre_categoria) VALUES (?);",
        nuevas_categorias
    )

    print("📥 Insertando datos en la tabla prendas...")
    nuevas_prendas =[
        ("Sueter Panda dev", "S", 65.0, 5, 1),
        ("Pantalon de bambu", "S", 105.0, 5, 2),
        ("Sueter para dormir", "S", 150.0, 10, 1),
        ("Pantalon para tomar la siesta", "S", 50.0, 5, 2)
    ]

    cursor.executemany(
        "INSERT INTO prendas (nombre, talla, precio, stock, categoria_id) VALUES (?, ?, ?, ?, ?);",
        nuevas_prendas
    )


    # ----------------------------------------------------------------
    # PASO 1: Crear la cabecera de la factura
    # ----------------------------------------------------------------
    print("📥 Generando cabecera de la venta...")
    cursor.execute("INSERT INTO ventas (fecha, total) VALUES (?, ?);", ("2026-07-04", 180.00))
    
    # 🌟 EL TRUCO SENIOR: Capturamos el ID que la base de datos acaba de generar
    venta_id = cursor.lastrowid
    print(f"🆔 Factura registrada en disco duro con el ID: {venta_id}")

    # ----------------------------------------------------------------
    # PASO 2: Registrar los productos dentro de esa factura
    # ----------------------------------------------------------------
    print("📥 Insertando artículos en el detalle de la factura...")
    # NOTA: Asegúrate de haber corrido antes tu archivo 'llenar_inventario.py'
    # para que existan productos con ID 1 y ID 2 en tu almacén.
    detalles = [
        (venta_id, 1, 2, 65.00),  # (venta_id, prenda_id, cantidad, precio_unitario)
        (venta_id, 2, 1, 50.00)
    ]
    
    cursor.executemany("""
        INSERT INTO detalles_ventas (venta_id, prenda_id, cantidad, precio_unitario)
        VALUES (?, ?, ?, ?);
    """, detalles)

    conexion.commit()
    print("✅ Transacción completada con éxito en el disco.")

    # ----------------------------------------------------------------
    # PASO 3: El Súper JOIN de Tres Tablas (Sin nombres ambiguos)
    # ----------------------------------------------------------------
    print("\n🧾 RENDERIZANDO FACTURA PANDA STYLE:")
    print("=" * 90)
    
    query_triple = """
    SELECT v.id, v.fecha, p.nombre, d.cantidad, (d.cantidad * d.precio_unitario) AS subtotal
    FROM detalles_ventas d
    INNER JOIN ventas v ON d.venta_id = v.id
    INNER JOIN prendas p ON d.prenda_id = p.id
    WHERE v.id = ?;
    """
    
    cursor.execute(query_triple, (venta_id,))
    filas = cursor.fetchall()

    for fila in filas:
        print(f"📄 Fac #{fila[0]} | 📅 {fila[1]} | 👕 Prenda: {fila[2]:<25} | 📦 Cant: {fila[3]} | 💰 Subtotal: Q{fila[4]:.2f}")
    print("=" * 90)

except sqlite3.IntegrityError as e:
    print(f"\n❌ \033[31m[ERROR DE INTEGRIDAD]: {e}\033[0m")
    print("⚠️  Asegúrate de que los IDs de las prendas (1 y 2) existan en tu tabla 'prendas'.")
except sqlite3.OperationalError as e:
    print(f"\n❌ \033[31m[ERROR OPERACIONAL]: {e}\033[0m")
    print("⚠️  Revisa que no se te haya escapado una letra en los nombres de las columnas.")
finally:
    conexion.close()
