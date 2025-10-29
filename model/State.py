# Definition of the State class representing the state of the astronaut (el estado del problema)
class State:
    # Constructor
    # receives:
    # - The current position of the astronaut (x, y)
    # - The set of collected scientific samples (positions)
    # - The fuel available for the spaceship
    # - If the spaceship has been reached
    def __init__(self, position, collected = set(), spaceshipFuel = 20, spaceship = False, spaceship_taken=False):
        self.position = position 
        self.collected = set(collected)  
        self.spaceshipFuel = spaceshipFuel  
        self.spaceship = spaceship
        # SOLUTION FIX ----------------------------------------------------------------  
        self.spaceship_taken = spaceship_taken
        # -----------------------------------------------------------------------------

    # Method to compare two states, for checking if they are the same to avoid cycles, 
    # Two states are equal if they have the same position, collected samples, spaceship status, and fuel
    def equal(self, other):
        return self.position == other.position and self.collected == other.collected and self.spaceship == other.spaceship and self.spaceshipFuel == other.spaceshipFuel
