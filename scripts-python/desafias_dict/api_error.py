sistema_errores = {
    "db": {
        101: "Conexion rechazada por el host remoto", 
        102: "Query mal formada o error de sintaxis SQL",
        103: "Violacion de restriccion de clave primaria",
        104: "Tiempo de espera de la transaccion agotado",
        105: "Intento de escribir en una base de datos de solo lectura"
    },
    "auth": {
        201: "Token JWT expirado", 
        202: "Password incorrecta o usuario no encontrado",
        203: "Multiples intentos de inicio de sesion bloqueados",
        204: "Firma digital del token no coincide",
        205: "Permisos insuficientes para realizar esta operacion"
    },
    "red": {
        301: "Error de DNS: No se pudo resolver el dominio",
        302: "Puerto de escucha cerrado o inaccesible",
        303: "Paquete de red perdido (Time To Live expirado)",
        304: "Fallo en el protocolo de enlace SSL/TLS",
        305: "Saturacion de peticiones en la interfaz de red"
    }
}

class SubSistemaError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(f"{mensaje}")


try:
    sub_sistema = input("Sub Sistema (db, auth, red): ").strip().lower()
    codigo_numerico = int(input("Código: "))

    mensaje = sistema_errores.get(sub_sistema, {}).get(codigo_numerico, None)

    if mensaje is None:
        raise SubSistemaError("❌ Subsistema o código no catalogado en Pandita-Errors.")

    print(f"✅ [LOG DETECTADO] Error {codigo_numerico}: {mensaje}")

except ValueError:
    print("❌ Error: El código debe ser un número entero.")
except SubSistemaError as error:
    print(error)
