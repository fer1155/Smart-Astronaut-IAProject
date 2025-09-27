# Imports
from input_output import parser
from model.World import World
from model.State import State
from model.GoalTest import is_goal_state
from model.Action import Action

def main():
    # Load the matrix from a file and create a World instance
    matrix = parser.load_world_from_file('input_output/Prueba1.txt')
    astronaut_position, spaceship_position, samples, obstacles = parser.parse_world(matrix)
    world = World(matrix, astronaut_position, spaceship_position, samples, obstacles)

    return 0

if __name__ == "__main__":
    # Run the main program
    main()
