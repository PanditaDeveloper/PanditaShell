class TuiEngine:
    """Clase de ayuda para renderizar interfaces de caja automáticas en la terminal."""
    # Constantes de dibujo Unicode
    TL, TR = "┌", "┐"
    BL, BR = "└", "┘"
    H, V   = "─", "│"
    ML, MR = "├", "┤"
    
    RESET  = "\033[0m"
    CYAN   = "\033[96m"
    MAGENTA = "\033[95m"

    @classmethod
    def crear_tarjeta(cls, titulo, lineas_contenido, color=None, ancho=52):
        """Genera una tarjeta estilizada ajustando los espacios dinámicamente."""
        col = color if color else cls.CYAN
        
        # 1. Borde Superior
        print(f"{col}{cls.TL}{cls.H * (ancho - 2)}{cls.TR}{cls.RESET}")
        # 2. Título Centrado (`^`)
        print(f"{col}{cls.V}{cls.RESET} {titulo:^{ancho - 4}} {col}{cls.V}{cls.RESET}")
        # 3. Línea Divisoria Intermedia
        print(f"{col}{cls.ML}{cls.H * (ancho - 2)}{cls.MR}{cls.RESET}")
        
        # 4. Contenido Alineado a la Izquierda (`<`)
        for linea in lineas_contenido:
            print(f"{col}{cls.V}{cls.RESET} {linea:<{ancho - 4}} {col}{cls.V}{cls.RESET}")
            
        # 5. Borde Inferior
        print(f"{col}{cls.BL}{cls.H * (ancho - 2)}{cls.BR}{cls.RESET}")
