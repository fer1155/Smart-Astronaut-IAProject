import tkinter as tk
from ui.tkinterMain import MarsExplorerGUI
from input_output.parser import load_world_from_file, parse_world


def main():
    """Función principal para ejecutar la aplicación"""
    root = tk.Tk()
    
    # Crear la aplicación pasándole las funciones del parser
    app = MarsExplorerGUI(root, load_world_from_file, parse_world)
    
    # Iniciar el loop de la interfaz
    root.mainloop()


if __name__ == "__main__":
    main()