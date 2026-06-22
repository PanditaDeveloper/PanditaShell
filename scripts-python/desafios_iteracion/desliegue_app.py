pasos_despliegue = [
    "Clonando repositorio de GitHub",
    "Instalando dependencias con pip",
    "Corriendo pruebas unitarias en Neovim",
    "Compilando binarios de optimización",
    "Subiendo contenedores a producción"
]

for progreso,paso in enumerate(pasos_despliegue, start=1):
    print(f"\033[32m[paso {progreso}/{len(pasos_despliegue)}] Corriendo: {paso} ({(progreso / len(pasos_despliegue))*100})%\033[0m")
