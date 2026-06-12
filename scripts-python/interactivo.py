print("=========================================")
print("   🤖 BIENVENIDO AL ASISTENTE PANDITA   ")
print("=========================================")

# 1. Capturamos texto normal
nombre_usuario = input("Como te llamas: ")

print(f"\n¡Un placer saludarte, {nombre_usuario}! Vamos a calcular tu entorno")

# 2. capturamos un numero (la ram) y lo convertimos a entero
ram_usuario = int(input("Cuanta memoria ram tiene el pc que estas usando hoy?? (escrive solo el numero): "))

print("\n-----------------------------------------")
print("📊 PROCESANDO DIAGNÓSTICO...")
print("-----------------------------------------")

if ram_usuario < 8:
    print(f"⚠️ {nombre_usuario}, tienes {ram_usuario}GB de RAM. Tu sistema está muy ajustado.")
    print("🛠️ Recomendación: Cierra el navegador y quédate programando solo en Neovim.")

elif ram_usuario == 8:
    print(f"🚀 ¡Punto de equilibrio perfecto, {nombre_usuario}!")
    print(f"Estás exprimiendo al máximo tus {ram_usuario}GB de RAM gracias a esta consola ligera.")
else:
    sobran = ram_usuario - 8
    print(f"🔥 ¡Tienes una máquina potente, {nombre_usuario}! Tienes {ram_usuario}GB.")
    print(f"Te sobran {sobran}GB de RAM respecto a la configuración base de PanditaShell.")

print("=========================================")

