# Algoritmo de búsqueda no informada
import queue
from model.Node import Node

def busqueda_por_amplitud(world, initial_state, goal_test):
    cola = queue.Queue()
    nodo_inicial = Node(initial_state)
    cola.put(nodo_inicial)

    while not cola.empty():
        nodo_actual = cola.get()

        if goal_test(nodo_actual.state, world):
            print("Goal reached!")
            return nodo_actual

        if evitarCiclos(nodo_actual.state, nodo_actual.get_path()):
            continue
        
        nodos_hijos = nodo_actual.expand(world, goal_test)
        
        for hijo in nodos_hijos:
            cola.put(hijo)
    return 0

def evitarCiclos(estado, camino):
    for nodo in camino:
        if estado == nodo.state:
            return True
    return False