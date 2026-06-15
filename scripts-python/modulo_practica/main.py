#importamos la funcion de nuestra modulo local
from calculos import analizar_numeros

def ejecutar_aplicacion():
    print("=========================================")
    print("   📊 SISTEMA ESTADÍSTICO PANDITA-DEV   ")
    print("=========================================")
    
    mis_datos = [12, 45, 7, 23, 89, 54, 11]

    #desempaquetado de datos
    bajo, alto, avg = analizar_numeros(mis_datos)

    print(f"📉 Valor más bajo: {bajo}")
    print(f"📈 Valor más alto: {alto}")
    print(f"🧮 Promedio general: {avg:.2f}")
    print("=========================================")


if __name__ == "__main__":
    ejecutar_aplicacion()
