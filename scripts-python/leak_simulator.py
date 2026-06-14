class InsufficientMemoryError(Exception):
    """Excepción personalizada para el control de hardware."""
    def __init__(self, mensaje, codigo):
        self.codigo = codigo
        super().__init__(f"Error [{codigo}]: {mensaje}")


print("==================================================")
print("   SIMULADOR DE FUGA DE MEMORIA (Pandita-Leak)    ")
print("==================================================")

memoria_disponible = 8  # RAM inicial

for i in range(1, 6):
    if memoria_disponible <= 0:
        break

    print(f"\n[Solicitud #{i}] RAM Disponible Actual: {memoria_disponible} GB")
    
    try:
        proceso = int(input("¿Cuánta memoria requiere este proceso (GB)?: "))
        
        if proceso > memoria_disponible:
            raise InsufficientMemoryError("No hay suficiente bloques de RAM libres para esta petición.", 300)
            
    except ValueError:
        print("❌ Error: Por favor, introduce un número entero válido.")
    except InsufficientMemoryError as error:
        print(f"❌ {error}")
    else:
        # Este bloque SOLO se ejecuta si el proceso fue exitoso y no hubo excepciones
        memoria_disponible -= proceso
        print(f"✅ Proceso asignado con éxito. Consumo: {proceso} GB")
    finally:
        # El finally se usa para auditoría o limpieza, no para cálculos condicionales
        print(f"🧹 [Auditoría del Sistema]: Registro de ciclo {i} completado.")

print("\n==================================================")
print(f"🚨 Estado Final de la RAM de Pandita: {memoria_disponible} GB")
print("==================================================")
