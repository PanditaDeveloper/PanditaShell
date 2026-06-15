from logger import registrar_evento

class MensajeErroneo(Exception):
    def __init__(self, codigo, mensaje):
        self.codigo = codigo
        super().__init__(f"Error: {codigo}, {mensaje}")


def run(tipo, mensaje):
    try:
        estado, msg = registrar_evento(tipo, mensaje)
        if estado:
            print(msg)
        else:
            raise MensajeErroneo(3012, f"El tipo: {tipo} no es valido. Contenido: {msg}")
    except MensajeErroneo as error:
        print(f"{error}")

if __name__ == "__main__":
    prueva_logs = [
        ("info", "Las credenciales fueron actualizados con exito"), 
        ("warning", "La passwor no puede ser la misma que la anterior"), 
        ("error", "Las credenciales no coinciden"), 
        ("pandita", "un panda desarrollador anda suelto"),
        ("info", "Conexion establecida con el servidor principal"),
        ("info", "Inicio de sesion exitoso del usuario admin"),
        ("warning", "El token de sesion expirara en 5 minutos"),
        ("error", "Error 404: No se encontro la ruta solicitada"),
        ("pandita", "Alguien se comio todo el bambu de la oficina"),
        ("info", "Copia de seguridad completada en la nube"),
        ("warning", "Uso de memoria RAM superior al 85%"),
        ("error", "Fallo de conexion con la base de datos"),
        ("info", "Consulta SQL ejecutada en 0.02 segundos"),
        ("warning", "Intento de acceso desde una IP no registrada"),
        ("error", "Permiso denegado para modificar el archivo index.html"),
        ("pandita", "El panda olvido hacer commit antes de ir a dormir"),
        ("info", "Archivo de configuracion cargado correctamente"),
        ("warning", "Espacio en disco bajo (menos del 10% disponible)"),
        ("error", "Desbordamiento de bufer detectado en el puerto 80"),
        ("info", "Peticion GET /api/v1/users procesada"),
        ("warning", "Tiempo de respuesta del servidor lento (1500ms)"),
        ("error", "Fallo al enviar el correo electronico de activacion"),
        ("pandita", "Codigo espagueti detectado por el panda detector"),
        ("info", "Descarga de actualizacion de software iniciada"),
        ("warning", "La API externa esta devolviendo respuestas vacias"),
        ("error", "Token JWT invalido o mal formado"),
        ("info", "Limpieza de cache del sistema finalizada"),
        ("warning", "Multiples peticiones fallidas desde la misma sesion"),
        ("error", "No se pudo escribir en el directorio de logs"),
        ("pandita", "Un panda derramo cafe sobre el teclado mecanico"),
        ("info", "Nuevo dispositivo vinculado a la cuenta"),
        ("warning", "Version de Python desactualizada en el entorno"),
        ("error", "Inyeccion de codigo detectada y bloqueada"),
        ("info", "Cerrando sockets de forma segura"),
        ("warning", "El certificado SSL expirara pronto"),
        ("error", "Falta un parametro requerido en el cuerpo de la peticion"),
        ("pandita", "El panda soluciono el bug borrando todo el codigo"),
        ("info", "Servicio reiniciado con éxito")
    ]
    
    for tipo, mensaje in prueva_logs:
        run(tipo, mensaje)
