# Defines a node in the search tree
class Node:
    # Constructor
    def __init__(self, state, parent=None, action=None, depth=0, cost=0):
        self.state = state  # Current state
        self.parent = parent  # Parent node
        self.action = action  # Action taken to reach this state
        self.depth = depth  # Depth of the node in the search tree
        self.cost = cost  # Cost to reach this state

    # String representation 
    def __str__(self):
        return f"Node(state={self.state}, action={self.action}, depth={self.depth}, cost={self.cost})"