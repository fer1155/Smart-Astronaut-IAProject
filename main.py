# Imports
from input_output import parser
from model.World import World
from model.State import State
from model.GoalTest import is_goal_state
from model.node import Node
from search.uninformed.amplitud import busqueda_por_amplitud
from search.uninformed.costoUniforme import busqueda_por_costo_uniforme
import time
from input_output.report import generate_report


def main():
    # Load the matrix from a file and create a World instance
    matrix = parser.load_world_from_file('input_output/Prueba1.txt')
    initial_astronaut_position, initial_spaceship_position, sample_positions, obstacles_positions = parser.parse_world(matrix)
    world = World(matrix, initial_astronaut_position, initial_spaceship_position, sample_positions, obstacles_positions)

    # Define the initial state
    initialState = State(initial_astronaut_position)

    # Elegir algoritmo
    print("Seleccione el algoritmo de búsqueda:")
    print("1. Búsqueda por amplitud")
    print("2. Búsqueda por costo uniforme")
    opcion = input("Ingrese 1 o 2: ")

    inicio = time.time()

    if opcion == "1":
        resultado = busqueda_por_amplitud(world, initialState, is_goal_state)
    elif opcion == "2":
        resultado = busqueda_por_costo_uniforme(world, initialState, is_goal_state)
    else:
        print("Opción no válida.")
        return 1

    fin = time.time()
    tiempo_transcurrido = fin - inicio

    # Generate the report with the result and elapsed time
    generate_report(resultado, tiempo_transcurrido)

    return 0

if __name__ == "__main__":
    main()