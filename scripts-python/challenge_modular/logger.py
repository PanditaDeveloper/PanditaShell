def registrar_evento(tipo, mensaje):
    """
    Formatea un mensaje con colores ANSI usando el patrón de despacho por diccionario.
    """
    # 1. Definimos nuestro "mapa de despacho" (La base de datos de formatos)
    formatos_ansi = {
        "INFO": f"\033[32m[INFO] {mensaje}\033[0m",
        "WARNING": f"\033[33m[WARN] {mensaje}\033[0m",
        "ERROR": f"\033[31m[ERR ] {mensaje}\033[0m"
    }
    
    # 2. Buscamos el formato en el diccionario de manera segura (.get)
    # Si existe, nos da el texto coloreado. Si no existe, nos da None (el else)
    mensaje_formateado = formatos_ansi.get(tipo.upper(), None)
    
    if mensaje_formateado is None:
        return False, mensaje  # Retornamos el mensaje original intacto si no es válido
        
    return True, mensaje_formateado

if __name__ == "__main__":
    prueva_logs = [("info", "Las credenciales fueron actualizados con exito"), ("warning", "La passwor no puede ser la misma que la anterior"), ("error", "Las credenciales no coinciden"), ("pandita", "un panda desarrollador anda suelto")]

    for tipo, mensaje in prueva_logs:
        estado, msg = registrar_evento(tipo, mensaje)
        if estado:
            print(msg)
        else:
            print(f"el tipo de mensaje: {tipo}, no es valido")
