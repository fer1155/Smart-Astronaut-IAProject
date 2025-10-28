import queue
import itertools
from model.node import Node
from search.informed.heuristicas import heuristica_manhattan_admisible

def busqueda_a_estrella(world, initial_state, goal_test, heuristic=heuristica_manhattan_admisible):
    """
    Algoritmo A* (A estrella).
    Expande el nodo con el menor valor f(n) = g(n) + h(n).
    """
    cola = queue.PriorityQueue()
    counter = itertools.count()
    visitados = set()

    nodo_inicial = Node(initial_state)  
    cola.put((heuristic(nodo_inicial.state, world), next(counter), nodo_inicial))
    visitados.add(nodo_inicial.state)

    nodecont = 0

    while not cola.empty():
        _, _, nodo_actual = cola.get()

        if goal_test(nodo_actual.state, world):
            print("Goal reached!")
            #for step in nodo_actual.get_path():
            #    print(step.state.spaceshipFuel)
            return [nodo_actual, nodecont]

        nodos_hijos = nodo_actual.expand(world)
        nodecont += 1

        while not nodos_hijos.empty():
            hijo = nodos_hijos.get()
            g = hijo.cost  # costo acumulado hasta el hijo
            h = heuristic(hijo.state, world)
            f = g + h

            # Si el estado no fue visitado o encontramos un camino más barato
            if not comprobar_estado_visitado(hijo.state, visitados):
                hijo.cost = g
                cola.put((f, next(counter), hijo))
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