def registrar_evento(tipo, mensaje):
    if tipo.upper() == "INFO":
        mensaje = f"\033[32m{mensaje}\033[0m"
    elif tipo.upper() == "WARNING":
        mensaje = f"\033[33m{mensaje}\033[0m"
    elif tipo.upper() == "ERROR":
        mensaje = f"\033[31m{mensaje}\033[0m"
    else:
        return False, mensaje
    
    return True, mensaje

if __name__ == "__main__":
    prueva_logs = [("info", "Las credenciales fueron actualizados con exito"), ("warning", "La passwor no puede ser la misma que la anterior"), ("error", "Las credenciales no coinciden"), ("pandita", "un panda desarrollador anda suelto")]

    for tipo, mensaje in prueva_logs:
        estado, msg = registrar_evento(tipo, mensaje)
        if estado:
            print(msg)
        else:
            print(f"el tipo de mensaje: {tipo}, no es valido")
