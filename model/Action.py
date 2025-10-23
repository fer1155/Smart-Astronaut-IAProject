# Model to represent the actions the astronaut can take
class Action:
    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)

    # List of all possible actions (orden estándar para DFS: up, left, down, right)
    all_actions = [up, left, down, right]
    
    # Dictionary to convert action tuples to names
    action_names = {
        (-1, 0): "UP",
        (1, 0): "DOWN",
        (0, -1): "LEFT",
        (0, 1): "RIGHT"
    }
    
    @staticmethod
    def get_action_name(action):
        """Get the name of an action from its tuple representation"""
        return Action.action_names.get(action, "UNKNOWN")