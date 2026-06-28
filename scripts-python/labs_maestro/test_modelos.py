class ProductoPrueba:
    def __init__(self, nombre_articulo, precio_base):
        # Usamos 'self.' para decirle a Python: "Guarda esto en los atributos de este objeto"
        self.nombre = nombre_articulo
        self.precio = precio_base

    # Método de instancia común (Lleva 'self' porque va a USAR los datos de arriba)
    def obtener_resumen(self):
        return f"🛒 {self.nombre} - Costo: ${self.precio:.2f}"

# Prueba rápida interna
if __name__ == "__main__":
    # Al instanciar, Python pasa automáticamente el objeto como 'self', tú solo pasas el resto
    item1 = ProductoPrueba("Gorra Panda Pro", 15.50)
    print(item1.obtener_resumen())
