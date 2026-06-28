import json
import os
from tui_engine import TuiEngine

# 🌟 SIMULACIÓN DE DATA RAW: El tipo de JSON de prueba que descargarías de internet
DATA_RAW_FARMACIA = """
[
    {"id": 1, "nombre": "Paracetamol 500mg", "stock": 12, "stock_minimo": 20, "costo": 1.50, "precio_venta": 3.00, "categoria": "Analgésico"},
    {"id": 2, "nombre": "Amoxicilina 1g", "stock": 45, "stock_minimo": 15, "costo": 4.20, "precio_venta": 8.50, "categoria": "Antibiótico"},
    {"id": 3, "nombre": "Ibuprofeno 400mg", "stock": 8, "stock_minimo": 25, "costo": 0.80, "precio_venta": 2.20, "categoria": "Analgésico"},
    {"id": 4, "nombre": "Loratadina 10mg", "stock": 80, "stock_minimo": 30, "costo": 1.10, "precio_venta": 4.00, "categoria": "Antihistamínico"},
    {"id": 5, "nombre": "Insulina Glargina", "stock": 4, "stock_minimo": 10, "costo": 25.00, "precio_venta": 48.00, "categoria": "Diabetes"}
]
"""

# ====================================================================
# CLASES DE DOMINIO (Modelando el Negocio con Fórmulas Matemáticas)
# ====================================================================

class Producto:
    """Modela un producto individual de la farmacia."""
    def __init__(self, id_prod, nombre, stock, stock_minimo, costo, precio_venta, categoria):
        self.id = id_prod
        self.nombre = nombre
        self.stock = stock
        self.stock_minimo = stock_minimo
        self.costo = costo
        self.precio = precio_venta
        self.categoria = categoria

    def calcular_margen_ganancia(self):
        """Fórmula matemática: Porcentaje de retorno de inversión."""
        if self.costo == 0:
            return 0
        return ((self.precio - self.costo) / self.costo) * 100

    def requiere_reabastecimiento(self):
        """Lógica condicional de control de stock."""
        return self.stock < self.stock_minimo

    def obtener_valor_inventario(self):
        """Fórmula: Capital neto retenido en este producto."""
        return self.stock * self.costo


class ConvertidorData:
    """Clase encargada de consumir e interpretar la data externa (JSON)."""
    @staticmethod
    def procesar_json(json_string):
        lista_diccionarios = json.loads(json_string)
        # Transformamos diccionarios planos en objetos reales del tipo 'Producto'
        return [
            Producto(p["id"], p["nombre"], p["stock"], p["stock_minimo"], p["costo"], p["precio_venta"], p["categoria"])
            for p in lista_diccionarios
        ]

# ====================================================================
# SISTEMA PRINCIPAL (Controlador y Menú Interactivo)
# ====================================================================

class SistemaFarmacia:
    def __init__(self):
        # Consumimos y parseamos la data de prueba inmediatamente al iniciar
        self.inventario = ConvertidorData.procesar_json(DATA_RAW_FARMACIA)

    def mostrar_dashboard_general(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Fórmulas de agregación global
        total_articulos = sum(p.stock for p in self.inventario)
        capital_invertido = sum(p.obtener_valor_inventario() for p in self.inventario)
        productos_criticos = sum(1 for p in self.inventario if p.requiere_reabastecimiento())

        # Preparamos las líneas para nuestro motor TUI
        contenido = [
            f"📦 Variedad de Productos: {len(self.inventario)} ítems",
            f"📊 Stock Total en Almacén: {total_articulos} unidades",
            f"💰 Capital Invertido     : ${capital_invertido:.2f} USD",
            f"🚨 Alertas de Stock Bajo : \033[31m{productos_criticos} productos\033[0m"
        ]
        
        TuiEngine.crear_tarjeta("🐼 DASHBOARD DE CONTROL GLOBAL", contenido, TuiEngine.MAGENTA)

    def mostrar_detalle_productos(self):
        print("\n=== Catálogo Detallado de Fórmulas por Producto ===")
        for p in self.inventario:
            margen = p.calcular_margen_ganancia()
            estado = "\033[31m[REORDEN]\033[0m" if p.requiere_reabastecimiento() else "\033[32m[OK]\033[0m"
            
            # Construimos una mini tarjeta dinámica para cada medicamento usando el tui_engine
            info_producto = [
                f"Categoría : {p.categoria}",
                f"Existencia: {p.stock} uds (Mínimo requerido: {p.stock_minimo})",
                f"Inversión : ${p.obtener_valor_inventario():.2f} USD",
                f"Margen Ret: {margen:.1f}% de ganancia estimada"
            ]
            TuiEngine.crear_tarjeta(f"{estado} {p.nombre}", info_producto, TuiEngine.CYAN)


if __name__ == "__main__":
    app = SistemaFarmacia()
    app.mostrar_dashboard_general()
    app.mostrar_detalle_productos()
