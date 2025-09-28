# Define the World class to represent the environment
class World:
    # Initialize the world with its properties
    def __init__(self, matrix, astronaut_position, spaceship_position, samples, obstacles):
        self.matrix = matrix
        self.astronaut_position = astronaut_position
        self.spaceship_position = spaceship_position
        self.samples = samples
        self.obstacles = obstacles
    
    # Method to get the cost of moving to a new position
    def terrain_cost(self, new_position, spaceship, spaceshipFuel):
        if spaceship and spaceshipFuel > 0:
            return 0.5  # Cost is 0.5 when in spaceship and has fuel
        
        (x, y) = new_position
        newPositionOfAstronaut = self.matrix[x][y]

        if newPositionOfAstronaut in [0, 2, 5, 6]:  # Empty
            return 1
        elif newPositionOfAstronaut == 3:  # Rocky-obstacle
            return 3
        elif newPositionOfAstronaut == 4:  # Volcanic-obstacle
            return 5
        else:
            raise ValueError("Terrain cost not defined for this type of cell.")