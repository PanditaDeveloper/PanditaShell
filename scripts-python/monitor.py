import time

# Lista simulada de logs de telemetría de memoria
# Contiene strings sucios, inputs inválidos y un valor crítico que disparará una alerta
telemetria_ram = ["4GB", "6GB", "ERROR_SENSOR", "8GB", "12GB", "CRITIC_OVERFLOW", "7GB"]

print("==================================================")
print("🤖 SISTEMA DE MONITOREO DE RAM (PANDITA-MONITOR)")
print("==================================================")

suma_ram = 0
muestras_validas = 0

# Iterando sobre la colección (Equivalente a un foreach de C#)
for lectura in telemetria_ram:
    print(f"\n🔄 Procesando muestra: '{lectura}'...")
    
    try:
        # Simulación de interrupción abrupta por error crítico del sistema
        if "CRITIC" in lectura:
            print("🚨 Alerta de hardware detectada. Abortando bucle principal.")
            break
            
        # Intentamos parsear quitando la unidad 'GB'. Puede lanzar ValueError si hay texto sucio.
        valor_numerico = int(lectura.replace("GB", ""))
        
    except ValueError as error:
        # Captura de error de conversión de tipos
        print(f"❌ Error de Parseo: No se pudo convertir '{lectura}' a entero.")
        print(f"   Detalle técnico: {error}")
        
    else:
        # Solo se ejecuta si el try fue exitoso
        suma_ram += valor_numerico
        muestras_validas += 1
        print(f"✅ Muestra integrada con éxito: {valor_numerico} GB")
        
    finally:
        # Se ejecuta en cada iteración pase lo que pase
        time.sleep(0.2)  # Delay para simular procesamiento en tiempo real
        print("🧹 [Telemetry CleanUp]: Liberando buffer de lectura.")

else:
    # Este bloque pertenece al FOR. Solo se ejecuta si el bucle termina SIN tocar el 'break'
    print("\n🎉 Análisis de telemetría completado de punta a punta sin fallos críticos.")

# Cálculo final utilizando operadores lógicos
print("\n==================================================")
if muestras_validas > 0:
    promedio = suma_ram / muestras_validas
    print(f"📊 Reporte Final: Consumo promedio de RAM: {promedio:.2f} GB")
else:
    print("📊 Reporte Final: No se pudieron procesar muestras válidas.")
print("==================================================")
