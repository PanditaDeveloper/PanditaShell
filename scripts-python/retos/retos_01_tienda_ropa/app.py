import os
import sys

ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(ruta_raiz)

from utils.interfaz import Pantalla
from retos.retos_01_tienda_ropa.modelos import Prenda

class InterfazTienda:
        
    @staticmethod
    def ejecutar_sistema(inventario_servicio):
        while True:
            Pantalla.limpiar()
            
            print(f"\033[36m{'='*40}\033[0m")
            print(f"\033[36m{'🐼 PANDA STYLE': ^40}\033[0m")
            print(f"\033[36m{'='*40}\033[0m\n")

            print("1. Ver todas las prendas en Inventario")
            print("2. Registrar una nueva Prenda")
            print("3. Modificar Stock de una Prenda")
            print("4. Eliminar una prenda de el inventario")
            print("0. Salir del Sistema")

            opcion = input("\nSelecciona una opción: ")
            
            if opcion == "1":
                Pantalla.limpiar()
                print(f"\033[32m{'='*60}\033[0m")
                print(f"\033[32m{'👕 PIEZAS EN INVENTARIO REGISTRADAS': ^60}\033[0m")
                print(f"\033[32m{'='*60}\033[0m\n")
                
                prendas = inventario_servicio.obtener_prendas()
                if not prendas:
                    print(" No hay prendas registradas en el sistema.")
                else:
                    for p in prendas:
                        print(p)
                        
                print(f"\n\033[32m{'-'*60}\033[0m")
                valor_total = inventario_servicio.calcular_valor_total()
                texto_total = f"\033[34mTotal Monetario: {valor_total:.2f}\033[0m"
                print(f"{texto_total:^69}")

                input("\nPresiona Enter para continuar...")

            elif opcion == "2":
                Pantalla.limpiar()
                print(f"\033[33m{'='*40}\033[0m")
                print(f"\033[33m{'📝 REGISTRO DE NUEVA PRENDA': ^40}\033[0m")
                print(f"\033[33m{'='*40}\033[0m\n")
                
                try:
                    nombre = input("Nombre de la prenda: ")
                    talla = input("Talla (S, M, L, XL): ")
                    precio = float(input("Precio: Q")) 
                    stock = int(input("Cantidad en Stock: "))
                    
                    nuevo_id = inventario_servicio.obtener_id()
                    
                    nueva_prenda = Prenda(nuevo_id, nombre, talla, precio, stock)
                    inventario_servicio.agregar_prendas(nueva_prenda)

                    print("\n\033[32m✅ Prenda agregada con éxito.\033[0m")
                    input("\nPresiona Enter para continuar...")
                    
                except ValueError:
                    print("\n\033[31m❌ [ERROR] Precio o Stock inválidos. Digita solo números.\033[0m")
                    input("\nPresiona Enter para volver a intentar...")
            elif opcion == "3":
                Pantalla.limpiar()
                print(f"\033[91m{'='*40}\033[0m")
                print(f"\033[91m{'📝 MODIFICACIÓN DE STOCK':^40}\033[0m")
                print(f"\033[91m{'='*40}\033[0m\n")

                try:
                    id_prenda = int(input("Ingresa el ID de la prenda: "))

                    prenda = inventario_servicio.buscar_por_id(id_prenda)
                    
                    if prenda is None:
                        print(f"\n⚠️ \033[33m[AVISO] La prenda con ID {id_prenda} no existe.\033[0m")
                        input("\nPresiona Enter para continuar...")
                    else:
                        print(f"\n👕 Prenda Seleccionada: \033[36m{prenda.nombre}\033[0m")
                        nuevo_stock = int(input("Ingresa la nueva cantidad en almacén: "))
                        
                        # Mutación de la entidad
                        prenda.stock = nuevo_stock

                        print(f"\n✅ \033[32mStock actualizado correctamente.\033[0m")
                        input("\nPresiona Enter para continuar...")
                        
                except ValueError:
                    print("\n❌ \033[31m[ERROR] El ID o el Stock deben ser números enteros.\033[0m")
                    input("\nPresiona Enter para volver a intentar...")
            elif opcion == "4":
                
                Pantalla.limpiar()
                print(f"\033[35m{'='*40}\033[0m")
                print("\033[35m🚨 ELIMINACIÓN DE PRODUCTO\033[0m")
                print(f"\033[35m{'='*40}\033[0m\n")
                
                try:
                    id = int(input("ID: "))
                    exito = inventario_servicio.eliminar_por_id(id)
                    if exito:
                        print("\033[32m✅ Prenda eliminada del almacén correctamente\033[0m")
                    else:
                        print("\033[33m⚠️ [AVISO] El ID ingresado no coincide con ningún producto\033[0m")
                    input("presiona enter para continuar...")
                except ValueError:
                    print("\n❌ \033[31m[ERROR] El ID debe ser un número entero.\033[0m")
                    input("\npresiona Enter para volver a intentar...")


            elif opcion == "0":
                Pantalla.limpiar()
                print(f"\033[35m{'='*40}\033[0m")
                print(f"\033[35m{'👋 ¡Gracias por usar PANDA STYLE!': ^40}\033[0m")
                print(f"\033[35m{'='*40}\033[0m\n")
                break
                
            else:
                print("\n\033[31m⚠️ Opción no válida. Elige 1, 2 o 3.\033[0m")
                input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    from retos.retos_01_tienda_ropa.logica import InventarioTienda

    controlador_inventario = InventarioTienda()
    
    InterfazTienda.ejecutar_sistema(controlador_inventario)

