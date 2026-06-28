class Prenda:
    def __init__(self, id_prenda, nombre, talla, precio, stock):
       self.id = id_prenda
       self.nombre = nombre
       self.talla = talla
       self.precio = precio
       self.stock = stock

    def __str__(self):
        return f"[ID:{f'0{self.id}' if self.id < 10 else self.id:<3}] |{self.nombre:<17} {f'Talla {self.talla}':<8} |Q{self.precio:<5} |Stock: {self.stock:<3} uds"

if __name__ == "__main__":
    gorra = Prenda(1, "Gorra", "S", 30.00, 20)
    pantalon = Prenda(15, "pantalon", "L", 25.00, 10)

    print(gorra)
    print(pantalon)
