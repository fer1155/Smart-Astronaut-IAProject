 # Lectura y validación de archivos

# Function to load the world from a file
def load_world_from_file(filename):
    matrix = []

    '''
    Read the file and build the matrix

    - 'With' guarantees that the file is automatically closed after use
    - open(filename, 'r') opens the file in read mode
    - line.strip() removes beginning and ending spaces (including new lines \n) (Example: '  1 2 3\n' -> '1 2 3')
    - line.split() splits the string into parts using spaces as separators (Example: '1 2 3' -> ['1', '2', '3'])
    - map(int, ...) converts each string in the list to an integer (Example: ['1', '2', '3'] -> [1, 2, 3])
    - list(...) converts the map object to a list
    '''
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)

    return matrix

'''
semantics = {
    0: 'Empty',
    1: 'Wall',
    2: 'Astronaut',
    3: 'Rocky-obstacle',
    4: 'Volcanic-obstacle',
    5: 'Spaceship',
    6: 'Scientific-sample'
}
'''

# Function to parse the world matrix and extract relevant information
def parse_world(matrix):
    # Initialize variables to store positions and counts
    astronaut_position = None
    spaceship_position = None
    samples = set()
    obstacles = set()

    # Iterate through the matrix to find positions of interest
    # enumerate gives us both the index (i) and the value (row)
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 2:  # Astronaut
                astronaut_position = (i, j)
            elif val == 5:  # Spaceship
                spaceship_position = (i, j)
            elif val == 6:  # Scientific sample
                samples.add((i, j))
            elif val in (3, 4):  # Obstacles (rocky or volcanic)
                obstacles.add((i, j))

    # Check that we found all necessary positions
    if astronaut_position is None:
        raise ValueError("Astronaut position not found in the world.")
    if spaceship_position is None:
        raise ValueError("Spaceship position not found in the world.")

    return astronaut_position, spaceship_position, samples, obstacles