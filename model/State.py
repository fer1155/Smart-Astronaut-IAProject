# Model for the state of the astronaut
class State:
    # Constructor
    def __init__(self, position, collected, spaceshipFuel = 20, spaceship = False):
        self.position = position  # (x, y) coordinates of the astronaut
        self.collected = collected  # Number of scientific samples collected
        self.spaceshipFuel = spaceshipFuel  # Fuel available for the spaceship
        self.spaceship = spaceship  # If the spaceship has been reached.

    # Special method to compare two states (to avoid loops)
    def __eq__(self, other):
        return self.position == other.position and self.collected == other.collected and self.spaceship == other.spaceship and self.spaceshipFuel == other.spaceshipFuel
    