def analizar_numeros(lista_numeros):
    """
    Recive una lista de numeros y retorna el menor, mayor y el promedio.
    en python no se necesita un objeto contenenedor, retornamos una tupla directamente.
    """

    if not lista_numeros:
        return 0, 0, 0

    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    promedio = sum(lista_numeros) / len(lista_numeros)

    #retorno de multiples valores al estilo de python
    return minimo, maximo, promedio

if __name__ == "__main__":
    print("🧪 Ejecutando pruebas unitarias internas de calculos.py...")
    prueba = [10, 20, 30]
    print(f"Resultado de prueba: {analizar_numeros(prueba)}")
