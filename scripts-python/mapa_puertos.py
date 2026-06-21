puertos_servidor = [22, 80, 443, 3306, 8080]

estado_puertos = {
        puerto: "Puerto protegido por el panda"
        if puerto in {22, 443, 3306} else "El panda no confia en este puerto"
        for puerto in puertos_servidor
}

print(estado_puertos)

