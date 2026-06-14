print("==================================================")
print("=             Calculadora Professional           =")
print("==================================================")

while True:
    entrada = input("\nOperacion (ej. suma 10 5) o 'exit': ").strip().split()
    
    # Evitar crash si presionan Enter vacío
    if not entrada:
        continue
        
    operacion = entrada[0].lower()
    if operacion == "exit":
        print("¡Adiós, Pandita!")
        break

    try:
        # Validación de estructura: Intentamos desempaquetar exactamente 3 elementos
        if len(entrada) != 3:
            raise ValueError("Debes ingresar exactamente la operación y 2 números.")
            
        # Desempaquetado directo (Súper limpio, estilo Python)
        _, num1_str, num2_str = entrada
        num1 = int(num1_str)
        num2 = int(num2_str)
        
        # Operaciones usando listas de coincidencia exacta
        if operacion in ["suma", "sum", "+"]:
            resultado = num1 + num2
        elif operacion in ["resta", "res", "-"]:
            resultado = num1 - num2
        elif operacion in ["multiplicacion", "multi", "*"]:
            resultado = num1 * num2
        elif operacion in ["divicion", "div", "/"]:
            resultado = num1 / num2  # Python maneja flotantes automáticamente
        else:
            # Lanzamos nuestra excepción personalizada si la operación no existe
            raise Exception(f"La operación '{operacion}' no está soportada.")

    except ValueError as e:
        print(f"❌ Error de Formato: {e}")
    except ZeroDivisionError:
        print("❌ Error Matemático: No se puede dividir entre cero.")
    except Exception as e:
        print(f"❌ Error de Operación: {e}")
    else:
        # Solo se muestra si todo el bloque TRY fue exitoso
        print(f"🔮 El resultado es: {resultado}")
