from model.State import State
from model.Action import Action
import queue

# Definición de un nodo en el árbol de búsqueda
class Node:
    # Constructor
    # Recibe:
    # - El estado actual del problema
    # - Una referencia al nodo padre
    # - La acción que se aplicó para generar el nodo
    # - Profundidad en el árbol
    # - El costo del camino desde la raíz hasta el nodo
    def __init__(self, state, parent=None, action=None, depth=0, cost=0):
        self.state = state  
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost

    # Expande el nodo para generar sus hijos
    # recibe el nodo actual y el mundo para verificar movimientos válidos
    # retorna una cola de nodos hijos
    def expand(self, world):
        # Cola para nodos hijos
        children = queue.Queue()

        # Si el movimiento es válido (dentro de los límites y no un obstáculo), crear un nuevo estado y un nuevo nodo
        # Sino, ignorar ese movimiento
        for move in [Action.right, Action.down, Action.left, Action.up]:
            # Calcular la nueva posición del astronauta al moverse en la dirección especificada (Moverse)
            newPosition = (self.state.position[0] + move[0], self.state.position[1] + move[1])

            # Verificar si la nueva posición está dentro de los límites y no es un obstáculo (Verificar si es movimiento válido)
            if not (0 <= newPosition[0] < len(world.matrix) and 
                    0 <= newPosition[1] < len(world.matrix[0])):
                 continue
            
            if world.matrix[newPosition[0]][newPosition[1]] == 1:
                continue

            # Actualizar las muestras recogidas si hay una muestra en la nueva posición (Recolectar muestra)
            samples_collected = self.state.collected.copy()
            if newPosition in world.samples:
                # Verificar si la muestra no ha sido recogida aún
                if newPosition not in self.state.collected:
                    samples_collected.add(newPosition)

            # SOLUTION FIX ----------------------------------------------------------------
            # Actualizar el combustible y estado de la nave

            # Si el astronauta se mueve hacia la posición de la nave
            if newPosition == world.spaceship_position:
                # Caso 1: llega a la nave por primera vez → la toma y recarga combustible
                if not self.state.spaceship_taken:
                    new_spaceshipFuel = 20 # Combustible completo al abordar
                    spaceship_taken = True # Marca que la nave ya fue tomada
                # Caso 2: ya había tomado la nave y vuelve a pasar por ella
                else:
                    # Si aún tiene combustible, sigue consumiendo al moverse
                    if self.state.spaceshipFuel > 0:
                        new_spaceshipFuel = self.state.spaceshipFuel - 1
                     # Si ya no tiene combustible, no puede gastar más
                    else:
                        new_spaceshipFuel = 0
                    spaceship_taken = True # Mantiene el estado de “nave tomada”
                is_spaceship = True # Indica que está dentro de la nave
            
            # Si ya está en la nave y tiene combustible, se mueve consumiéndolo normalmente
            elif self.state.spaceship and self.state.spaceshipFuel > 0:
                new_spaceshipFuel = self.state.spaceshipFuel - 1
                spaceship_taken = self.state.spaceship_taken
                is_spaceship = True

            # En cualquier otro caso (sin nave o sin combustible), se mueve a pie
            else:
                new_spaceshipFuel = 0
                is_spaceship = False
                spaceship_taken = self.state.spaceship_taken

            # Crear el nuevo estado
            new_state = State(newPosition, samples_collected, new_spaceshipFuel, is_spaceship, spaceship_taken)

            # Calcular el costo del movimiento
            move_cost = world.terrain_cost(newPosition, self.state.spaceship, self.state.spaceshipFuel)

            # Crear el nodo hijo
            child_node = Node(new_state, self, move, self.depth + 1, self.cost + move_cost)

            # Agregar el nodo hijo a la lista
            children.put(child_node)
        return children
    
    # Returns the path from the root to this node
    def get_path(self):
        # Define the path
        path = []
        
        # Start from the current node
        node = self

        # If the node has no parent, return an empty path (it is the root)
        if node.parent is None:
            return []
        
        # Walk through the tree from the current node to the root, adding each node to the path
        while node is not None:
            path.append(node)
            node = node.parent

        # Reverse the path to have it from root to current node
        return list(reversed(path))
    
    # String representation 
    def __str__(self):
        return f"Node(state={self.state}, action={self.action}, depth={self.depth}, cost={self.cost})"