sensores = ["Core 0", "Core 1", "Core 2", "Core 3", "GPU Diode", "Auxiliar"]
temperaturas = [45, 82, 48, 51, 91]

try:
    # strict=True obliga a que ambas listas tengan el mismo tamaño
    for sensor, temperatura in zip(sensores, temperaturas, strict=True):
        if temperatura > 80:
            print(f"🔥 \033[31m[ALERTA CRÍTICA] El componente {sensor} está hirviendo a {temperatura}°C\033[0m")
        else:
            print(f"\033[32m[ESTABLE] El componente {sensor} está a {temperatura}°C\033[0m")

except ValueError:
    # Aquí controlamos los elementos que quedaron fuera
    # Tomamos desde el índice equivalente al largo de las temperaturas en adelante
    sensores_sin_datos = sensores[len(temperaturas):]
    print(f"\n⚠️  [AUDITORÍA] Error de corrupción detectado.")
    print(f"Los siguientes sensores no recibieron telemetría: {sensores_sin_datos}")

