from model.State import State
from model.Action import Action

# Defines a node in the search tree
class Node:
    # Constructor
    def __init__(self, state, parent=None, action=None, depth=0, cost=0):
        self.state = state  # Current state
        self.parent = parent  # Parent node
        self.action = action  # Action taken to reach this state
        self.depth = depth  # Depth of the node in the search tree
        self.cost = cost  # Cost to reach this state
    
    def expand(self, world, goal):
        is_goal = goal(self.state, world)
        if not(is_goal):
            children = []
            for move in [Action.up, Action.down, Action.left, Action.right]:
                newPosition = (self.state.position[0] + move[0], self.state.position[1] + move[1])

                if not (0 <= newPosition[0] < len(world.matrix) and 
                        0 <= newPosition[1] < len(world.matrix[0])):
                    continue
                
                if world.matrix[newPosition[0]][newPosition[1]] == 1:
                    continue

                samples_collected = self.state.collected
                if newPosition == world.spaceship_position:
                    samples_collected += 1

                move_cost = world.terrain_cost(newPosition, self.state.spaceship, self.state.spaceshipFuel)
                new_spaceshipFuel = max(0, self.state.spaceshipFuel - 1) if self.state.spaceship else self.state.spaceshipFuel
                is_spaceship = (newPosition == world.spaceship_position) or (self.state.spaceship and new_spaceshipFuel > 0)
                new_state = State(newPosition, samples_collected, new_spaceshipFuel, is_spaceship)

                child_node = Node(new_state, self, move, self.depth + 1, self.cost + move_cost)
                children.append(child_node)

            return children
        return []

    # String representation 
    def __str__(self):
        return f"Node(state={self.state}, action={self.action}, depth={self.depth}, cost={self.cost})"
    
    def get_path(self):
        path = []
        node = self
        
        while node is not None:
            path.append(node)
            node = node.parent

        return list(reversed(path))