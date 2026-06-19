def atacar():
    print("🐼 El panda lanza un feroz golpe de bambú y derriba los servidores de producción.")

def defender():
    print("🐼 El panda se esconde detrás de un muro de código espagueti e ignora los ataques.")

def curar():
    print("🐼 El panda se toma un descanso para comer un tazón de ramen y recupera todas sus fuerzas.")


if __name__ == "__main__":

    acciones = {"atacar": atacar, "defender": defender, "curar": curar}
    orden = ["atacar", "defender", "curar", "trabajar"]

    #orden = input("Escoje una accion 'atacar, defender, curar'")

    for accion in orden:
        accion_elegida = acciones.get(accion, None)
        
        if accion_elegida is None:
            print(f"La accion {accion} no es apta para un panda")
        else:
            accion_elegida()

