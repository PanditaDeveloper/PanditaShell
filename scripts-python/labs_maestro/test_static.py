
class CalculadoraHerramientas:
    def __init__(self, marca):
        self.marca = marca  # Esto es un dato del objeto

    # Método de instancia normal (usa self)
    def describir_calculadora(self):
        print(f"Esta es una calculadora marca: {self.marca}")

    # Método Estático (NO usa self, es solo una función utilitaria agrupada aquí)
    @staticmethod
    def sumar_impuesto(precio):
        return precio * 1.15
