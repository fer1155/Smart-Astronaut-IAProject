
# Importa la clase Node y la heuristica Manhattan
import queue
import itertools
from model.node import Node
from search.informed.heuristicas import heuristica_manhattan
from search.informed.heuristicas import heuristica_manhattan_admisible

def busqueda_avara(world, initial_state, goal_test, heuristic=heuristica_manhattan):
    """
    Algoritmo de busqueda avara (Greedy Best-First Search).
    Expande siempre el nodo que parece estar mas cerca del objetivo segun la heuristica.
    """
    cola = queue.PriorityQueue()  # Cola de prioridad para seleccionar el nodo con menor heuristica
    visitados = set()             # Conjunto de estados ya visitados
    counter = itertools.count()   # Contador incremental para desempatar si hay heuristicas iguales

    nodo_inicial = Node(initial_state)  # Nodo raiz
    # Se inserta el nodo inicial en la cola con su valor heuristico
    cola.put((heuristic(nodo_inicial.state, world), next(counter), nodo_inicial))
    visitados.add(nodo_inicial.state)

    nodecont = 0  # Contador de nodos expandidos

    while not cola.empty():
        # Extrae el nodo con menor valor heuristico
        _, _, nodo_actual = cola.get()

        # Si el nodo actual es objetivo, retorna la solución
        if goal_test(nodo_actual.state, world):
            print("Goal reached!")
            return [nodo_actual, nodecont]

        # Expande los hijos del nodo actual
        nodos_hijos = nodo_actual.expand(world)
        nodecont += 1

        # Para cada hijo generado
        while not nodos_hijos.empty():
            hijo = nodos_hijos.get()
            # Si el estado del hijo no ha sido visitado
            if not comprobar_estado_visitado(hijo.state, visitados):
                # Calcula la heuristica y lo agrega a la cola
                cola.put((heuristic(hijo.state, world), next(counter), hijo))
                visitados.add(hijo.state)

    print("No solution found.")
    return None

def comprobar_estado_visitado(estado, visitados):
    """
    Verifica si un estado ya ha sido visitado (comparando con los estados en el conjunto visitados).
    """
    for visitado in visitados:
        if estado.equal(visitado):
            return True
    return False