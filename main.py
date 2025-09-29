# Imports
from input_output import parser
from model.World import World
from model.State import State
from model.GoalTest import is_goal_state
from model.Node import Node
from search.uninformed.amplitud import busqueda_por_amplitud
import time
from input_output.report import generate_report


def main():
    # Load the matrix from a file and create a World instance
    matrix = parser.load_world_from_file('input_output/Prueba1.txt')
    initial_astronaut_position, initial_spaceship_position, sample_positions, obstacles_positions = parser.parse_world(matrix)
    world = World(matrix, initial_astronaut_position, initial_spaceship_position, sample_positions, obstacles_positions)

    # Define the initial state
    initialState = State(initial_astronaut_position)

    # Execute the 'busqueda_por_amplitud' algorithm and time it
    inicio = time.time()

    # Call the search algorithm with the world, initial state, and the goaltest
    resultado = busqueda_por_amplitud(world, initialState, is_goal_state)
    fin = time.time()
    tiempo_transcurrido = fin - inicio

    # Generate the report with the result and elapsed time
    generate_report(resultado, tiempo_transcurrido)

    return 0

if __name__ == "__main__":
    # Run the main program
    main()