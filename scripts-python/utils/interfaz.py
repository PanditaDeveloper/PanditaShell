import os

class Pantalla:
    """Clase utilitaria para controlar elementos de la terminal."""
    
    @staticmethod
    def limpiar():
        """Limpia la pantalla de la consola de forma multiplataforma."""
        os.system('cls' if os.name == 'nt' else 'clear')
