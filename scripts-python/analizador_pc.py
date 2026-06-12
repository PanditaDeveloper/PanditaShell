# --- VARIABLES (guardando los datos de la pc) ---
usuario = "Cristobal (Pandita Developer)"
ram_instalada = 8
procesador = "Intel Core i5-8350U"

print("=========================================")
print(f"  ANALIZADOR DE RENDIMIENTO PARA: {usuario}")
print("=========================================")
print(f"💻 Procesador detectado: {procesador}")
print(f"📊 Memoria RAM: {ram_instalada} GB")
print("-----------------------------------------")

# --- CONDICIONALES (Tomando decisiones en base a la RAM) ---
if ram_instalada < 8:
    print("❌ Alerta: Tu RAM es un poco ajustada para estándares modernos.")
    print("💡 Consejo: Evita usar entornos pesados. ¡Sigue programando en Neovim!")

elif ram_instalada == 8:
    print("🚀 Estado: Rendimiento Equilibrado.")
    print("💡 Consejo: Estás en el punto perfecto. Al usar Windows Terminal y Neovim,")
    print("   estás ahorrando casi 4 GB de RAM en comparación con otros desarrolladores.")

else:
    print("🔥 Estado: Tienes una bestia de máquina. ¡A programar lo que quieras!")

print("=========================================")
