import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

class MarsExplorerGUI:
    def __init__(self, root, load_world_func, parse_world_func):
        self.root = root
        self.root.title("Mars Explorer - NASA 2030")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a2e")
        
        # Guardar las funciones del parser
        self.load_world_from_file = load_world_func
        self.parse_world = parse_world_func
        
        # Variables
        self.world_matrix = None
        self.selected_file = None
        self.selected_algorithm = None
        self.search_type = tk.StringVar(value="")
        
        # Estado actual: 'initial' o 'map_loaded'
        self.current_state = 'initial'
        
        self.create_initial_screen()
    
    def create_initial_screen(self):
        """Pantalla inicial para cargar archivo y seleccionar algoritmo"""
        # Frame principal con bordes redondeados simulados
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(expand=True, fill='both', padx=40, pady=40)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="MARS EXPLORER",
            font=("Helvetica", 36, "bold"),
            bg="#1a1a2e",
            fg="#e94560"
        )
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(
            main_frame,
            text="NASA Mission 2030",
            font=("Helvetica", 14),
            bg="#1a1a2e",
            fg="#a8a8a8"
        )
        subtitle_label.pack(pady=(0, 50))
        
        # Frame para la carga de archivo
        file_frame = tk.Frame(main_frame, bg="#16213e", relief="flat")
        file_frame.pack(pady=20, padx=100, fill='x')
        
        file_label = tk.Label(
            file_frame,
            text="📁 Cargar Mapa Marciano",
            font=("Helvetica", 16, "bold"),
            bg="#16213e",
            fg="#ffffff"
        )
        file_label.pack(pady=(20, 10))
        
        self.file_path_label = tk.Label(
            file_frame,
            text="No se ha seleccionado ningún archivo",
            font=("Helvetica", 10),
            bg="#16213e",
            fg="#a8a8a8"
        )
        self.file_path_label.pack(pady=10)
        
        load_btn = tk.Button(
            file_frame,
            text="SELECCIONAR ARCHIVO",
            font=("Helvetica", 12, "bold"),
            bg="#e94560",
            fg="white",
            activebackground="#d63447",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.load_file
        )
        load_btn.pack(pady=(10, 20), ipadx=20, ipady=10)
        
        # Frame para selección de algoritmo
        algo_frame = tk.Frame(main_frame, bg="#16213e", relief="flat")
        algo_frame.pack(pady=20, padx=100, fill='x')
        
        algo_label = tk.Label(
            algo_frame,
            text="🧠 Seleccionar Algoritmo de Búsqueda",
            font=("Helvetica", 16, "bold"),
            bg="#16213e",
            fg="#ffffff"
        )
        algo_label.pack(pady=(20, 20))
        
        # Radio buttons para tipo de búsqueda
        search_type_frame = tk.Frame(algo_frame, bg="#16213e")
        search_type_frame.pack(pady=10)
        
        rb_no_informada = tk.Radiobutton(
            search_type_frame,
            text="No Informada",
            variable=self.search_type,
            value="no_informada",
            font=("Helvetica", 12),
            bg="#16213e",
            fg="#ffffff",
            selectcolor="#1a1a2e",
            activebackground="#16213e",
            activeforeground="#ffffff",
            command=self.update_algorithm_options
        )
        rb_no_informada.pack(side='left', padx=20)
        
        rb_informada = tk.Radiobutton(
            search_type_frame,
            text="Informada",
            variable=self.search_type,
            value="informada",
            font=("Helvetica", 12),
            bg="#16213e",
            fg="#ffffff",
            selectcolor="#1a1a2e",
            activebackground="#16213e",
            activeforeground="#ffffff",
            command=self.update_algorithm_options
        )
        rb_informada.pack(side='left', padx=20)
        
        # Frame para opciones de algoritmo específico
        self.specific_algo_frame = tk.Frame(algo_frame, bg="#16213e")
        self.specific_algo_frame.pack(pady=20)
        
        # Botón para iniciar
        self.start_btn = tk.Button(
            main_frame,
            text="INICIAR EXPLORACIÓN",
            font=("Helvetica", 14, "bold"),
            bg="#0f3460",
            fg="white",
            activebackground="#16213e",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            state='disabled',
            command=self.start_exploration
        )
        self.start_btn.pack(pady=40, ipadx=30, ipady=15)
    
    def update_algorithm_options(self):
        """Actualizar las opciones de algoritmo según el tipo seleccionado"""
        # Limpiar frame
        for widget in self.specific_algo_frame.winfo_children():
            widget.destroy()
        
        search_type = self.search_type.get()
        
        if search_type == "no_informada":
            algorithms = ["Amplitud", "Costo Uniforme", "Profundidad (evitando ciclos)"]
        elif search_type == "informada":
            algorithms = ["Avara", "A*"]
        else:
            return
        
        self.algo_var = tk.StringVar(value="")
        
        for algo in algorithms:
            rb = tk.Radiobutton(
                self.specific_algo_frame,
                text=algo,
                variable=self.algo_var,
                value=algo,
                font=("Helvetica", 11),
                bg="#16213e",
                fg="#ffffff",
                selectcolor="#1a1a2e",
                activebackground="#16213e",
                activeforeground="#ffffff",
                command=self.check_ready_to_start
            )
            rb.pack(anchor='w', padx=40, pady=5)
    
    def load_file(self):
        """Cargar archivo de texto con el mapa"""
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo de mapa",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        
        if filename:
            try:
                # Usar las funciones del parser que fueron pasadas en el constructor
                self.world_matrix = self.load_world_from_file(filename)
                self.selected_file = filename
                
                # Validar que el archivo sea correcto
                self.parse_world(self.world_matrix)
                
                # Actualizar label
                self.file_path_label.config(
                    text=f"✓ {os.path.basename(filename)}",
                    fg="#4ecca3"
                )
                
                self.check_ready_to_start()
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el archivo:\n{str(e)}")
                self.file_path_label.config(
                    text="✗ Error al cargar el archivo",
                    fg="#e94560"
                )
    
    def check_ready_to_start(self):
        """Verificar si se puede habilitar el botón de inicio"""
        if (self.selected_file and 
            self.search_type.get() and 
            hasattr(self, 'algo_var') and 
            self.algo_var.get()):
            self.start_btn.config(state='normal', bg="#4ecca3")
        else:
            self.start_btn.config(state='disabled', bg="#0f3460")
    
    def start_exploration(self):
        """Iniciar la exploración - cambiar a la vista del mapa"""
        self.selected_algorithm = self.algo_var.get()
        self.current_state = 'map_loaded'
        
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Crear la vista del mapa
        self.create_map_view()
    
    def create_map_view(self):
        """Crear la vista del mapa con el grid"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(expand=True, fill='both')
        
        # Header con información
        header_frame = tk.Frame(main_frame, bg="#16213e", height=80)
        header_frame.pack(fill='x', padx=20, pady=(20, 10))
        header_frame.pack_propagate(False)
        
        title = tk.Label(
            header_frame,
            text="MARS EXPLORER - Simulación en Progreso",
            font=("Helvetica", 20, "bold"),
            bg="#16213e",
            fg="#e94560"
        )
        title.pack(side='left', padx=20, pady=20)
        
        algo_info = tk.Label(
            header_frame,
            text=f"Algoritmo: {self.selected_algorithm}",
            font=("Helvetica", 12),
            bg="#16213e",
            fg="#4ecca3"
        )
        algo_info.pack(side='right', padx=20, pady=20)
        
        # Frame para el grid del mapa
        grid_container = tk.Frame(main_frame, bg="#1a1a2e")
        grid_container.pack(expand=True, pady=20)
        
        # Dibujar el grid
        self.draw_grid(grid_container)
    
    def draw_grid(self, parent):
        """Dibujar el grid del mapa 10x10"""
        cell_size = 60
        
        # Frame para el grid
        grid_frame = tk.Frame(parent, bg="#0f3460", relief="flat", bd=2)
        grid_frame.pack()
        
        # Diccionario de colores para cada tipo de celda
        colors = {
            0: "#2d2d44",      # Libre - gris oscuro
            1: "#1a1a1a",      # Obstáculo - negro
            2: "#4ecca3",      # Astronauta - verde
            3: "#8b4513",      # Rocoso - marrón
            4: "#ff6b35",      # Volcánico - naranja/rojo
            5: "#00d4ff",      # Nave - azul cyan
            6: "#e94560"       # Muestra - rojo/rosa
        }
        
        # Emojis para cada tipo
        symbols = {
            0: "",
            1: "🪨",
            2: "👨‍🚀",
            3: "🪨",
            4: "🌋",
            5: "🚀",
            6: "🧪"
        }
        
        # Crear las celdas
        for i in range(10):
            for j in range(10):
                val = self.world_matrix[i][j]
                
                cell_frame = tk.Frame(
                    grid_frame,
                    bg=colors[val],
                    width=cell_size,
                    height=cell_size,
                    relief="solid",
                    bd=1
                )
                cell_frame.grid(row=i, column=j, padx=1, pady=1)
                cell_frame.pack_propagate(False)
                
                # Añadir símbolo
                if symbols[val]:
                    label = tk.Label(
                        cell_frame,
                        text=symbols[val],
                        font=("Helvetica", 24),
                        bg=colors[val],
                        fg="white"
                    )
                    label.pack(expand=True)
        
        # Leyenda
        self.create_legend(parent)
    
    def create_legend(self, parent):
        """Crear leyenda del mapa"""
        legend_frame = tk.Frame(parent, bg="#16213e", relief="flat")
        legend_frame.pack(pady=20)
        
        title = tk.Label(
            legend_frame,
            text="LEYENDA",
            font=("Helvetica", 12, "bold"),
            bg="#16213e",
            fg="#ffffff"
        )
        title.pack(pady=(10, 5))
        
        items = [
            ("👨‍🚀", "Astronauta", "#4ecca3"),
            ("🚀", "Nave", "#00d4ff"),
            ("🧪", "Muestra Científica", "#e94560"),
            ("🪨", "Obstáculo", "#1a1a1a"),
            ("🪨", "Terreno Rocoso (costo 3)", "#8b4513"),
            ("🌋", "Terreno Volcánico (costo 5)", "#ff6b35"),
        ]
        
        for symbol, text, color in items:
            item_frame = tk.Frame(legend_frame, bg="#16213e")
            item_frame.pack(anchor='w', padx=20, pady=2)
            
            symbol_label = tk.Label(
                item_frame,
                text=symbol,
                font=("Helvetica", 12),
                bg="#16213e",
                fg="white"
            )
            symbol_label.pack(side='left', padx=(0, 10))
            
            text_label = tk.Label(
                item_frame,
                text=text,
                font=("Helvetica", 10),
                bg="#16213e",
                fg=color
            )
            text_label.pack(side='left')


def main():
    root = tk.Tk()
    # Necesitas pasar las funciones aquí también si ejecutas desde este archivo
    from input_output.parser import load_world_from_file, parse_world
    app = MarsExplorerGUI(root, load_world_from_file, parse_world)
    root.mainloop()


if __name__ == "__main__":
    main()