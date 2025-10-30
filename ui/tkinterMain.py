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
        self.world_data = None

        # Variables para la animacion
        self.cell_labels = {}
        self.animation_running = False
        self.current_path = []
        self.animation_speed = 500
        self.collected_samples = set()

        # Estadisticas del algoritmo
        self.nodes_expanded = 0
        self.tree_depth = 0
        self.solution_cost = 0
        self.execution_time = 0

        # Estado actual
        self.current_state = "initial"

        self.create_initial_screen()

    def create_initial_screen(self):
        """Pantalla inicial para cargar archivo y seleccionar algoritmo"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(expand=True, fill="both", padx=40, pady=40)

        # Titulo
        title_label = tk.Label(
            main_frame,
            text="MARS EXPLORER",
            font=("Helvetica", 24, "bold"),
            bg="#1a1a2e",
            fg="#e94560",
        )
        title_label.pack(pady=(0, 3))

        subtitle_label = tk.Label(
            main_frame,
            text="NASA Mission 2030",
            font=("Helvetica", 11),
            bg="#1a1a2e",
            fg="#a8a8a8",
        )
        subtitle_label.pack(pady=(0, 15))

        # Frame contenedor para archivo y algoritmo (lado a lado)
        content_frame = tk.Frame(main_frame, bg="#1a1a2e")
        content_frame.pack(pady=8, fill="both", expand=True)

        # Frame para la carga de archivo (IZQUIERDA)
        file_frame = tk.Frame(content_frame, bg="#16213e", relief="flat")
        file_frame.pack(side="left", padx=6, fill="both", expand=True)

        file_label = tk.Label(
            file_frame,
            text="📁 Cargar Mapa",
            font=("Helvetica", 12, "bold"),
            bg="#16213e",
            fg="#ffffff",
        )
        file_label.pack(pady=(12, 6))

        self.file_path_label = tk.Label(
            file_frame,
            text="No se ha seleccionado ningún archivo",
            font=("Helvetica", 8),
            bg="#16213e",
            fg="#a8a8a8",
            wraplength=200,
        )
        self.file_path_label.pack(pady=6, padx=8)

        load_btn = tk.Button(
            file_frame,
            text="SELECCIONAR ARCHIVO",
            font=("Helvetica", 9, "bold"),
            bg="#e94560",
            fg="white",
            activebackground="#d63447",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.load_file,
        )
        load_btn.pack(pady=(6, 12), ipadx=12, ipady=6)

        # Frame para seleccion de algoritmo (DERECHA)
        algo_frame = tk.Frame(content_frame, bg="#16213e", relief="flat")
        algo_frame.pack(side="right", padx=6, fill="both", expand=True)

        algo_label = tk.Label(
            algo_frame,
            text="🧠 Algoritmo de Búsqueda",
            font=("Helvetica", 12, "bold"),
            bg="#16213e",
            fg="#ffffff",
        )
        algo_label.pack(pady=(12, 12))

        # Radio buttons para tipo de busqueda
        search_type_frame = tk.Frame(algo_frame, bg="#16213e")
        search_type_frame.pack(pady=6)

        rb_no_informada = tk.Radiobutton(
            search_type_frame,
            text="No Informada",
            variable=self.search_type,
            value="no_informada",
            font=("Helvetica", 9),
            bg="#16213e",
            fg="#ffffff",
            selectcolor="#1a1a2e",
            activebackground="#16213e",
            activeforeground="#ffffff",
            command=self.update_algorithm_options,
        )
        rb_no_informada.pack(side="left", padx=6)

        rb_informada = tk.Radiobutton(
            search_type_frame,
            text="Informada",
            variable=self.search_type,
            value="informada",
            font=("Helvetica", 9),
            bg="#16213e",
            fg="#ffffff",
            selectcolor="#1a1a2e",
            activebackground="#16213e",
            activeforeground="#ffffff",
            command=self.update_algorithm_options,
        )
        rb_informada.pack(side="left", padx=6)

        # Frame para opciones de algoritmo especifico
        self.specific_algo_frame = tk.Frame(algo_frame, bg="#16213e")
        self.specific_algo_frame.pack(pady=12, fill="x")

        # Boton para iniciar (ABAJO, centrado)
        button_container = tk.Frame(main_frame, bg="#1a1a2e")
        button_container.pack(pady=15, fill="x")

        self.start_btn = tk.Button(
            button_container,
            text="INICIAR EXPLORACIÓN",
            font=("Helvetica", 11, "bold"),
            bg="#0f3460",
            fg="white",
            activebackground="#16213e",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            state="disabled",
            command=self.start_exploration,
        )
        self.start_btn.pack(ipadx=20, ipady=10)

        # Forzar actualizacion de la ventana
        main_frame.update_idletasks()

    def update_algorithm_options(self):
        """Actualizar las opciones de algoritmo segun el tipo seleccionado"""
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
                font=("Helvetica", 8),
                bg="#16213e",
                fg="#ffffff",
                selectcolor="#1a1a2e",
                activebackground="#16213e",
                activeforeground="#ffffff",
                command=self.check_ready_to_start,
            )
            rb.pack(anchor="w", padx=25, pady=2)

        # Forzar actualizacion despues de crear los radiobuttons
        self.specific_algo_frame.update_idletasks()
        self.root.update_idletasks()

    def load_file(self):
        """Cargar archivo de texto con el mapa"""
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo de mapa",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
        )

        if filename:
            try:
                self.world_matrix = self.load_world_from_file(filename)
                self.selected_file = filename
                self.world_data = self.parse_world(self.world_matrix)

                # Mostrar informacion del mapa cargado
                rows = len(self.world_matrix)
                cols = len(self.world_matrix[0]) if rows > 0 else 0

                self.file_path_label.config(
                    text=f"✓ {os.path.basename(filename)}\nTamaño: {rows}x{cols}",
                    fg="#4ecca3",
                )

                self.check_ready_to_start()

            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el archivo:\n{str(e)}")
                self.file_path_label.config(
                    text="✗ Error al cargar el archivo", fg="#e94560"
                )

    def check_ready_to_start(self):
        """Verificar si se puede habilitar el boton de inicio"""
        if (
            self.selected_file
            and self.search_type.get()
            and hasattr(self, "algo_var")
            and self.algo_var.get()
        ):
            self.start_btn.config(state="normal", bg="#4ecca3")
        else:
            self.start_btn.config(state="disabled", bg="#0f3460")

        # Forzar redibujado del boton
        self.start_btn.update_idletasks()

    def start_exploration(self):
        """Iniciar la exploracion - cambiar a la vista del mapa"""
        self.selected_algorithm = self.algo_var.get()
        self.current_state = "map_loaded"

        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_map_view()
        self.root.after(100, self.run_search_algorithm)

    def run_search_algorithm(self):
        """Ejecutar el algoritmo de busqueda seleccionado"""
        import time
        
        try:
            from model.World import World
            from model.State import State
            from model.GoalTest import is_goal_state

            astronaut_pos, spaceship_pos, samples, obstacles = self.world_data
            world = World(self.world_matrix, spaceship_pos, samples)

            initial_state = State(
                position=astronaut_pos,
                collected=set(),
                spaceshipFuel=20,
                spaceship=False,
            )

            result = None
            algorithm_name = self.selected_algorithm

            # Iniciar medicion del tiempo
            start_time = time.time()

            if algorithm_name == "Amplitud":
                from search.uninformed.amplitud import busqueda_por_amplitud

                result = busqueda_por_amplitud(world, initial_state, is_goal_state)
            elif algorithm_name == "Costo Uniforme":
                from search.uninformed.costoUniforme import busqueda_por_costo_uniforme

                result = busqueda_por_costo_uniforme(
                    world, initial_state, is_goal_state
                )
            elif algorithm_name == "Profundidad (evitando ciclos)":
                from search.uninformed.profundidad import busqueda_profundidad

                result = busqueda_profundidad(world, initial_state, is_goal_state)
            elif algorithm_name == "Avara":
                from search.informed.avara import busqueda_avara

                result = busqueda_avara(world, initial_state, is_goal_state)
            elif algorithm_name == "A*":
                from search.informed.AEstrella import busqueda_a_estrella

                result = busqueda_a_estrella(world, initial_state, is_goal_state)

            # Finalizar medicion del tiempo
            end_time = time.time()
            self.execution_time = end_time - start_time

            if result and result[0]:
                goal_node, nodes_expanded = result
                path_nodes = goal_node.get_path()
                path = [node.state.position for node in path_nodes]
                if goal_node.state.position not in path:
                    path.append(goal_node.state.position)

                self.nodes_expanded = nodes_expanded
                self.tree_depth = goal_node.depth
                self.solution_cost = (
                    goal_node.cost if hasattr(goal_node, "cost") else None
                )

                self.animate_path(path)
            else:
                messagebox.showwarning(
                    "Sin solución", "No se encontró una solución al problema."
                )

        except Exception as e:
            import traceback

            error_msg = (
                f"Error al ejecutar el algoritmo:\n{str(e)}\n\n{traceback.format_exc()}"
            )
            messagebox.showerror("Error", error_msg)

    def extract_path_from_node(self, goal_node):
        """Extraer el camino completo desde el nodo inicial hasta el objetivo"""
        path_nodes = goal_node.get_path()
        path = [node.state.position for node in path_nodes]
        if goal_node.state.position not in path:
            path.append(goal_node.state.position)
        return path

    def animate_path(self, path):
        """Animar el movimiento del astronauta a lo largo del camino"""
        if not path or len(path) < 1:
            messagebox.showinfo("Resultado", "No hay camino para animar")
            return

        self.current_path = path
        self.path_index = 0
        self.animation_running = True
        self.collected_samples = set()

        initial_pos = path[0]
        if initial_pos in self.cell_labels:
            original_val = self.world_matrix[initial_pos[0]][initial_pos[1]]
            if original_val == 2:
                self.world_matrix[initial_pos[0]][initial_pos[1]] = 0

        self.animate_next_step()

    def animate_next_step(self):
        """Animar el siguiente paso del camino"""
        if not self.animation_running or self.path_index >= len(self.current_path):
            self.animation_running = False
            # Mostrar estadisticas finales con boton para volver
            self.show_completion_dialog()
            return

        current_pos = self.current_path[self.path_index]

        if (
            current_pos in self.world_data[2]
            and current_pos not in self.collected_samples
        ):
            self.collected_samples.add(current_pos)
            self.world_matrix[current_pos[0]][current_pos[1]] = 0

        if self.path_index > 0:
            prev_pos = self.current_path[self.path_index - 1]
            if prev_pos in self.cell_labels:
                prev_val = self.world_matrix[prev_pos[0]][prev_pos[1]]
                self.update_cell_appearance(prev_pos, prev_val, is_astronaut=False)

        current_val = self.world_matrix[current_pos[0]][current_pos[1]]
        self.update_cell_appearance(current_pos, current_val, is_astronaut=True)

        self.path_index += 1
        self.root.after(self.animation_speed, self.animate_next_step)

    def show_completion_dialog(self):
        """Mostrar dialogo de completado con opcion de volver"""
        # Crear ventana de dialogo personalizada
        dialog = tk.Toplevel(self.root)
        dialog.title("Misión Completada")
        dialog.geometry("400x300")
        dialog.configure(bg="#1a1a2e")
        dialog.resizable(False, False)

        # Centrar la ventana
        dialog.transient(self.root)
        dialog.grab_set()

        # Contenido
        content_frame = tk.Frame(dialog, bg="#16213e")
        content_frame.pack(expand=True, fill="both", padx=20, pady=20)

        title_label = tk.Label(
            content_frame,
            text="🎉 ¡Misión Completada!",
            font=("Helvetica", 16, "bold"),
            bg="#16213e",
            fg="#4ecca3",
        )
        title_label.pack(pady=(10, 20))

        stats_text = f"Nodos expandidos: {self.nodes_expanded}\n"
        stats_text += f"Profundidad del rbol: {self.tree_depth}\n"
        if self.solution_cost is not None:
            stats_text += f"Costo de la solución: {self.solution_cost}\n"
        stats_text += f"Tiempo de ejecución: {self.execution_time:.4f} segundos"

        stats_label = tk.Label(
            content_frame,
            text=stats_text,
            font=("Helvetica", 11),
            bg="#16213e",
            fg="#ffffff",
            justify="left",
        )
        stats_label.pack(pady=10)

        # Botones
        button_frame = tk.Frame(content_frame, bg="#16213e")
        button_frame.pack(pady=20)

        back_btn = tk.Button(
            button_frame,
            text="VOLVER AL INICIO",
            font=("Helvetica", 10, "bold"),
            bg="#e94560",
            fg="white",
            activebackground="#d63447",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=lambda: self.return_to_start(dialog),
        )
        back_btn.pack(side="left", padx=5, ipadx=15, ipady=8)

        close_btn = tk.Button(
            button_frame,
            text="CERRAR",
            font=("Helvetica", 10, "bold"),
            bg="#0f3460",
            fg="white",
            activebackground="#16213e",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=dialog.destroy,
        )
        close_btn.pack(side="left", padx=5, ipadx=15, ipady=8)

    def return_to_start(self, dialog=None):
        """Volver a la pantalla inicial"""
        if dialog:
            dialog.destroy()

        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Resetear variables
        self.world_matrix = None
        self.selected_file = None
        self.selected_algorithm = None
        self.search_type.set("")
        self.world_data = None
        self.cell_labels = {}
        self.animation_running = False
        self.current_path = []
        self.collected_samples = set()
        self.nodes_expanded = 0
        self.tree_depth = 0
        self.solution_cost = 0
        self.current_state = "initial"

        # Recrear pantalla inicial
        self.create_initial_screen()

    def update_cell_appearance(self, pos, original_val, is_astronaut=False):
        """Actualizar la apariencia visual de una celda"""
        cell_frame, cell_label = self.cell_labels.get(pos, (None, None))

        if not cell_frame or not cell_label:
            return

        colors = {
            0: "#2d2d44",
            1: "#1a1a1a",
            2: "#4ecca3",
            3: "#8b4513",
            4: "#ff6b35",
            5: "#00d4ff",
            6: "#e94560",
        }

        symbols = {0: "", 1: "🪨", 2: "👨‍🚀", 3: "🪨", 4: "🌋", 5: "🚀", 6: "🧪"}

        if is_astronaut:
            cell_label.config(text="👨‍🚀", bg=colors.get(original_val, "#2d2d44"))
        else:
            cell_label.config(
                text=symbols.get(original_val, ""),
                bg=colors.get(original_val, "#2d2d44"),
            )

    def create_map_view(self):
        """Crear la vista del mapa con el grid"""
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(expand=True, fill="both")

        header_frame = tk.Frame(main_frame, bg="#16213e", height=80)
        header_frame.pack(fill="x", padx=20, pady=(20, 10))
        header_frame.pack_propagate(False)

        title = tk.Label(
            header_frame,
            text="MARS EXPLORER - Simulación en Progreso",
            font=("Helvetica", 20, "bold"),
            bg="#16213e",
            fg="#e94560",
        )
        title.pack(side="left", padx=20, pady=20)

        algo_info = tk.Label(
            header_frame,
            text=f"Algoritmo: {self.selected_algorithm}",
            font=("Helvetica", 12),
            bg="#16213e",
            fg="#4ecca3",
        )
        algo_info.pack(side="right", padx=(10, 20), pady=20)

        # Boton para volver al inicio
        back_btn = tk.Button(
            header_frame,
            text="← VOLVER",
            font=("Helvetica", 10, "bold"),
            bg="#e94560",
            fg="white",
            activebackground="#d63447",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.return_to_start,
        )
        back_btn.pack(side="right", padx=(10, 10), pady=20, ipadx=10, ipady=5)

        grid_container = tk.Frame(main_frame, bg="#1a1a2e")
        grid_container.pack(expand=True, pady=20)

        self.draw_grid(grid_container)

    def draw_grid(self, parent):
        """Dibujar el grid del mapa con tamaño dinamico"""
        # Obtener dimensiones reales de la matriz
        rows = len(self.world_matrix)
        cols = len(self.world_matrix[0]) if rows > 0 else 0

        # Calcular tamaño de celda dinamicamente
        # Ajustar segun el tamaño del mapa para que quepa en pantalla
        max_cell_size = 60
        min_cell_size = 30

        # Tamaño disponible aproximado (considerando margenes)
        available_width = 1100
        available_height = 600

        cell_size_by_width = available_width // cols
        cell_size_by_height = available_height // rows

        cell_size = min(
            max_cell_size,
            max(min_cell_size, min(cell_size_by_width, cell_size_by_height)),
        )

        grid_frame = tk.Frame(parent, bg="#0f3460", relief="flat", bd=2)
        grid_frame.pack()

        colors = {
            0: "#2d2d44",
            1: "#1a1a1a",
            2: "#4ecca3",
            3: "#8b4513",
            4: "#ff6b35",
            5: "#00d4ff",
            6: "#e94560",
        }

        symbols = {0: "", 1: "🪨", 2: "👨‍🚀", 3: "🪨", 4: "🌋", 5: "🚀", 6: "🧪"}

        # Ajustar tamaño de fuente segun el tamaño de celda
        font_size = max(12, min(24, int(cell_size * 0.4)))

        for i in range(rows):
            for j in range(cols):
                val = self.world_matrix[i][j]

                cell_frame = tk.Frame(
                    grid_frame,
                    bg=colors.get(val, "#2d2d44"),
                    width=cell_size,
                    height=cell_size,
                    relief="solid",
                    bd=1,
                )
                cell_frame.grid(row=i, column=j, padx=1, pady=1)
                cell_frame.pack_propagate(False)

                label = tk.Label(
                    cell_frame,
                    text=symbols.get(val, ""),
                    font=("Helvetica", font_size),
                    bg=colors.get(val, "#2d2d44"),
                    fg="white",
                )
                label.pack(expand=True)

                self.cell_labels[(i, j)] = (cell_frame, label)

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
            fg="#ffffff",
        )
        title.pack(pady=(10, 5))

        items = [
            ("👨‍🚀", "Astronauta", "#4ecca3"),
            ("🚀", "Nave", "#00d4ff"),
            ("🧪", "Muestra Científica", "#e94560"),
            ("🪨", "Obstaculo", "#1a1a1a"),
            ("🪨", "Terreno Rocoso (costo 3)", "#8b4513"),
            ("🌋", "Terreno Volcanico (costo 5)", "#ff6b35"),
        ]

        for symbol, text, color in items:
            item_frame = tk.Frame(legend_frame, bg="#16213e")
            item_frame.pack(anchor="w", padx=20, pady=2)

            symbol_label = tk.Label(
                item_frame,
                text=symbol,
                font=("Helvetica", 12),
                bg="#16213e",
                fg="white",
            )
            symbol_label.pack(side="left", padx=(0, 10))

            text_label = tk.Label(
                item_frame, text=text, font=("Helvetica", 10), bg="#16213e", fg=color
            )
            text_label.pack(side="left")


# Funcion principal
if __name__ == "__main__":
    # Importar las funciones del parser
    from input_output.parser import load_world_from_file, parse_world

    # Crear la ventana principal
    root = tk.Tk()

    # Crear la aplicación
    app = MarsExplorerGUI(root, load_world_from_file, parse_world)

    # Iniciar el loop de eventos
    root.mainloop()
