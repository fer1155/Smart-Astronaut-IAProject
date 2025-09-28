# Imports
from input_output import parser
from model.World import World
from model.State import State
from model.GoalTest import is_goal_state
from model.Action import Action
from model.Node import Node
from search.uninformed.amplitud import busqueda_por_amplitud
import queue

def main():
    # Load the matrix from a file and create a World instance
    matrix = parser.load_world_from_file('input_output/Prueba1.txt')
    initial_astronaut_position, initial_spaceship_position, samples, obstacles = parser.parse_world(matrix)
    world = World(matrix, initial_astronaut_position, initial_spaceship_position, samples, obstacles)

    # Define the initial state
    initialState = State(initial_astronaut_position, 0)

    resultado = busqueda_por_amplitud(world, initialState, is_goal_state)
    if resultado:
        print("✅ Solución encontrada:")
        path = resultado.get_path()
        for step in path:
            print(step)
    else:
        print("❌ No se encontró solución")
    
    return 0

if __name__ == "__main__":
    # Run the main program
    main()
