# Definition of the World class representing the Mars environment
class World:
    # Constructor
    # receives:
    # - The matrix representing the world
    # - The position of the spaceship
    # - The set of scientific sample positions
    def __init__(self, matrix, spaceship_position, samples):
        self.matrix = matrix
        self.spaceship_position = spaceship_position
        self.samples = samples
    
    # Calculate the cost of moving to a position
    # receives:
    # - The position to move to (row, col)
    # - Whether the astronaut is in the spaceship
    # - The fuel available
    # returns the cost of the movement
    def terrain_cost(self, position, has_spaceship, fuel):
        # Get the terrain type at the position
        terrain = self.matrix[position[0]][position[1]]
        
        # If the astronaut is in the spaceship and has fuel, cost is always 0.5
        # regardless of terrain type (the spaceship protects from terrain difficulties)
        if has_spaceship and fuel > 0:
            return 0.5
        
        # Otherwise, cost depends on terrain type
        if terrain == 0:  # Free cell
            return 1
        elif terrain == 3:  # Rocky terrain
            return 3
        elif terrain == 4:  # Volcanic terrain
            return 5
        elif terrain == 5:  # Spaceship position
            return 1
        elif terrain == 6:  # Sample position
            return 1
        else:
            # Obstacle or invalid
            return float('inf')
    
    # Check if a position is valid (within bounds and not an obstacle)
    def is_valid_position(self, position):
        row, col = position
        # Check bounds
        if not (0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0])):
            return False
        # Check if it's not an obstacle
        if self.matrix[row][col] == 1:
            return False
        return True
    
    # String representation
    def __str__(self):
        result = "World:\n"
        for row in self.matrix:
            result += " ".join(str(cell) for cell in row) + "\n"
        return result