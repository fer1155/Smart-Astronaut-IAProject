# Algoritmo de búsqueda por costo uniforme
import queue
import itertools
from model.node import Node

def busqueda_por_costo_uniforme(world, initial_state, goal_test):
    frontera = queue.PriorityQueue()
    visitados = set()
    counter = itertools.count()  # Contador incremental

    nodo_inicial = Node(initial_state)
    frontera.put((0, next(counter), nodo_inicial))
    visitados.add(nodo_inicial.state)

    nodecont = 0

    while not frontera.empty():
        costo_actual, _, nodo_actual = frontera.get()

        if goal_test(nodo_actual.state, world):
            print("Goal reached!")
            return [nodo_actual, nodecont]

        nodos_hijos = nodo_actual.expand(world)
        nodecont += 1

        while not nodos_hijos.empty():
            hijo = nodos_hijos.get()
            if not comprobar_estado_visitado(hijo.state, visitados):
                frontera.put((hijo.cost, next(counter), hijo))
                visitados.add(hijo.state)

    print("No solution found.")
    return None

def comprobar_estado_visitado(estado, visitados):
    for visitado in visitados:
        if estado.equal(visitado):
            return True
    return False

