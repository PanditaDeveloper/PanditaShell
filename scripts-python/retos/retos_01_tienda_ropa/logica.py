class InventarioTienda():
    def __init__(self):
        self.prendas = []
        self.id = 0

    def agregar_prendas(self, prenda):
        self.prendas.append(prenda)
        self.id += 1

    def obtener_prendas(self):
        return self.prendas

    def calcular_valor_total(self):
        return sum(prenda.precio * prenda.stock for prenda in self.prendas)

    def obtener_id(self):
        return self.id

    def buscar_por_id(self, id_prenda):
        for prenda in self.prendas:
            if prenda.id == id_prenda:
                return prenda
        return None
