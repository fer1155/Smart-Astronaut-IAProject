# Define the World class to represent the environment
class World:
    # Constructor
    # matrix is a (list of lists)
    # the initial position of the astronaut is a tuple (x, y)
    # the position of the spaceship is a tuple (x, y)
    # samples is a list of tuples [(x1, y1), (x2, y2), ...] to the positions of the samples
    # obstacles is a list of tuples [(x1, y1), (x2, y2), ...] to the positions of the obstacles
    def __init__(self, matrix, astronaut_position, spaceship_position, samples, obstacles):
        self.matrix = matrix
        self.astronaut_position = astronaut_position
        self.spaceship_position = spaceship_position
        self.samples = set(samples)
        self.obstacles = set(obstacles)
    
    # Method to get the cost of moving to a new position
    def terrain_cost(self, new_position, spaceship, spaceshipFuel):
        # If the astronaut is in the spaceship and has fuel, the cost is 0.5
        if spaceship and spaceshipFuel > 0:
            return 0.5  # Cost is 0.5 when in spaceship and has fuel
        
        # Take the position of the astronaut moved to
        (x, y) = new_position

        # Get the type of terrain at the new position
        newPositionOfAstronaut = self.matrix[x][y]

        # Define the cost based on the terrain type
        if newPositionOfAstronaut in [0, 2, 5, 6]:  # Empty
            return 1
        elif newPositionOfAstronaut == 3:  # Rocky-obstacle
            return 3
        elif newPositionOfAstronaut == 4:  # Volcanic-obstacle
            return 5
        else:
            raise ValueError("Terrain cost not defined for this type of cell.")