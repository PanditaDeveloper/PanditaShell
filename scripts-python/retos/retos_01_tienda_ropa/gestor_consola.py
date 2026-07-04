import sqlite3
import os
import sys

ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), "tienda.db"))

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(ruta_raiz)

from utils.interfaz import Pantalla

class InterfazTienda:
        
    @staticmethod
    def ejecutar_sistema():
        while True:
            Pantalla.limpiar()
            
            print(f"\033[36m{'='*40}\033[0m")
            print(f"\033[36m{'🐼 PANDA STYLE': ^40}\033[0m")
            print(f"\033[36m{'='*40}\033[0m\n")

            print("1. Modificar Stock de un Producto en Base de Datos")
            print("2. Eliminar Producto de la Base de Datos")
            print("0. Salir del Sistema")

            opcion = input("\nSelecciona una opción: ")

            if opcion == "1":
                print(f"\033[34m{'='*40}\033[0m")
                print(f"{'📝 Sistema de actualizacion de inventario':^40}")
                print(f"\033[34m{'='*40}\033[0m\n\n")

                prenda_id = int(input("ID: "))
                nueo_stock = input("Nuevo Stock: ")
                cursor.execute("UPDATE prendas SET stock = ? WHERE id = ?;", (nueo_stock, prenda_id))
            elif opcion == "2":
                print(f"\033[31m{'='*40}\033[0m")
                print(f"{'🚨 Sistema de eliminacion de inventario':^40}")
                print(f"\033[31m{'='*40}\033[0m\n\n")

                prenda_id = int(input("ID: "))
                cursor.execute("DELETE FROM prendas WHERE id = ?;", (prenda_id,))
            else:
                break

            
            conexion.commit()
            print(f"\033[32m💾 Cambios consolidados en el disco duro.\033[0m")

        cursor.execute("SELECT id, nombre, stock FROM prendas;")
        for fila in cursor.fetchall():
            print(f"🆔 ID: {fila[0]} | 👕 {fila[1]:<25} | 📦 Stock Actual: {fila[2]} uds")

        conexion.close()

if __name__ == "__main__":   
    InterfazTienda.ejecutar_sistema()
