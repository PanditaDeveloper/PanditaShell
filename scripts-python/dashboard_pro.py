import os
import time

# ====================================================================
# CAPA DE COMPONENTES (OOP con Interfaces Implícitas / Duck Typing)
# ====================================================================

class Procesador:
    def __init__(self, modelo, nucleos):
        self.modelo = modelo
        self.nucleos = nucleos
        
    def obtener_telemetria(self):
        # Retorna una tupla con los datos actuales a renderizar
        return "CPU", self.modelo, f"{self.nucleos} Cores", "🟢 OPTIMAL"


class DiscoDuro:
    def __init__(self, marca, capacidad_gb):
        self.marca = marca
        self.capacidad = capacidad_gb
        
    def obtener_telemetria(self):
        # Cumple con la misma interfaz implícita: da tipo, nombre, info y estado
        return "STORAGE", self.marca, f"{self.capacidad} GB", "🟡 WARNING"

# ====================================================================
# CAPA VISUAL (Diseño TUI Profesional con Box-Drawing)
# ====================================================================

class TarjetaVisual:
    """Clase encargada de dibujar componentes en la terminal."""
    @staticmethod
    def renderizar(componente):
        # 🌟 DUCK TYPING EN ACCIÓN:
        # No nos importa si es un Procesador o un Disco, solo llamamos a su método común.
        tipo, nombre, detalle, estado = componente.obtener_telemetria()
        
        # Colores dinámicos basados en tus códigos ANSI
        color_borde = "\033[95m"  # Magenta brillante
        reset = "\033[0m"
        
        # Construcción de la caja con alineación perfecta usando F-Strings
        print(f"{color_borde}┌──────────────────────────────────────────────┐{reset}")
        print(f"{color_borde}│{reset} {f'📊 COMPONENTE: {tipo}':<28} {estado:>13} {color_borde}│{reset}")
        print(f"{color_borde}├──────────────────────────────────────────────┤{reset}")
        print(f"{color_borde}│{reset} Modelo: {nombre:<36} {color_borde}│{reset}")
        print(f"{color_borde}│{reset} Espec : {detalle:<36} {color_borde}│{reset}")
        print(f"{color_borde}└──────────────────────────────────────────────┘{reset}")


# ====================================================================
# ORQUESTADOR (Punto de Entrada)
# ====================================================================

if __name__ == "__main__":
    # Instanciamos los objetos de la OOP
    hardware_list = [
        Procesador("Intel Core i5-8350U", 4),
        DiscoDuro("NVMe Samsung Evo", 500),
        Procesador("AMD Ryzen 9 (Server Sim)", 16)
    ]
    
    # Limpiamos la pantalla de la terminal antes de dibujar
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\033[1;36m================================================")
    print("      🐼 PANDA SYSTEM ARCHITECTURE MONITOR     ")
    print("================================================\033[0m\n")
    
    # El bucle itera y renderiza de forma polimórfica dinámica
    for item in hardware_list:
        TarjetaVisual.renderizar(item)
        time.sleep(0.3)  # Simula carga secuencial
        
    print("\n\033[32m[Sistema]: Telemetría renderizada con éxito.\033[0m")
