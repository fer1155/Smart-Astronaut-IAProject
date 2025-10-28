from model.State import State
from model.Action import Action
import queue

# Definition of a node in the search tree
class Node:
    # Constructor
    # receives: 
    # - The current state of the problem
    # - A reference to the parent node
    # - The action that was applied to generate the node
    # - Depth in the tree
    # - The cost of the path from the root to the node
    def __init__(self, state, parent=None, action=None, depth=0, cost=0):
        self.state = state  
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost

    # Expands the node to generate its children
    # receives the current node and the world to check for valid moves
    # returns a list of child nodes
    def expand(self, world):
        # queue (cola) for child nodes
        children = queue.Queue()

        # Possible movements in reverse order for DFS (down, right, left, up)
        # So when popped from stack in DFS, they are processed as: up, left, right, down
        # if the move is valid (within bounds and not an obstacle), create a new state and a new node
        for move in [Action.right, Action.down, Action.left, Action.up]:
            # Calculate the new position to the astronaut moving in the specified direction (Moverse)
            newPosition = (self.state.position[0] + move[0], self.state.position[1] + move[1])

            # Check if new position is within bounds and not an obstacle (Verificar si es movimiento válido)
            if not (0 <= newPosition[0] < len(world.matrix) and 
                    0 <= newPosition[1] < len(world.matrix[0])):
                 continue
            
            if world.matrix[newPosition[0]][newPosition[1]] == 1:
                continue

            # Update collected samples if a sample is at the new position (Recolectar muestra)
            samples_collected = self.state.collected.copy()
            if newPosition in world.samples:
                # Verify if the sample has not been collected yet
                if newPosition not in self.state.collected:
                    samples_collected.add(newPosition)
            
            # # Update spaceship fuel and status
            # # Si el astronauta llega a la posición de la nave, "sube" a ella
            # if newPosition == world.spaceship_position:
            #     # Al llegar a la nave, la toma con combustible completo
            #     new_spaceshipFuel = 20
            #     is_spaceship = True
            # elif self.state.spaceship and self.state.spaceshipFuel > 0:
            #     # Si ya está en la nave, consume combustible
            #     new_spaceshipFuel = self.state.spaceshipFuel - 1
            #     is_spaceship = True
            # else:
            #     # No tiene nave o se quedó sin combustible
            #     new_spaceshipFuel = 0
            #     is_spaceship = False
             
            # SOLUTION FIX ----------------------------------------------------------------            
            # Update spaceship fuel and status
            # Si el astronauta llega a la posición de la nave, "sube" a ella
            if newPosition == world.spaceship_position:
                if not self.state.spaceship_taken:
                    new_spaceshipFuel = 20
                    spaceship_taken = True
                else:
                    new_spaceshipFuel = self.state.spaceshipFuel
                    spaceship_taken = self.state.spaceship_taken
                is_spaceship = True
             # -----------------------------------------------------------------------------
            elif self.state.spaceship and self.state.spaceshipFuel > 0:
                # Si ya está en la nave, consume combustible
                new_spaceshipFuel = self.state.spaceshipFuel - 1
                spaceship_taken = self.state.spaceship_taken
                is_spaceship = True
            else:
                # No tiene nave o se quedó sin combustible
                new_spaceshipFuel = 0
                is_spaceship = False
                spaceship_taken = self.state.spaceship_taken

            # Create the new state
            new_state = State(newPosition, samples_collected, new_spaceshipFuel, is_spaceship, spaceship_taken)

            # Calculate the cost of the move (Calcular el costo del movimiento)
            move_cost = world.terrain_cost(newPosition, self.state.spaceship, self.state.spaceshipFuel)

            # Create child node
            child_node = Node(new_state, self, move, self.depth + 1, self.cost + move_cost)

            # Add child node to the list
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