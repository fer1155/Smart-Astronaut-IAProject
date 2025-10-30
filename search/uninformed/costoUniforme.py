# Algoritmo de búsqueda por costo uniforme
import queue
import itertools
from model.node import Node

def busqueda_por_costo_uniforme(world, initial_state, goal_test):
    """
    Búsqueda por costo uniforme que garantiza encontrar la solucion optima.
    Expande siempre el nodo con menor costo acumulado.
    """
    cola = queue.PriorityQueue()
    visitados = set()
    counter = itertools.count()  # Contador incremental para desempatar

    nodo_inicial = Node(initial_state)
    cola.put((0, next(counter), nodo_inicial))

    nodecont = 0

    while not cola.empty():
        costo_actual, _, nodo_actual = cola.get()

        # Marcar como visitado CUANDO SE EXPANDE, no cuando se agrega
        if comprobar_estado_visitado(nodo_actual.state, visitados):
            continue
        
        visitados.add(nodo_actual.state)

        # Verificar si alcanzo el objetivo
        if goal_test(nodo_actual.state, world):
            print("Goal reached!")
            return [nodo_actual, nodecont]

        # Expandir nodos hijos
        nodos_hijos = nodo_actual.expand(world)
        nodecont += 1

        while not nodos_hijos.empty():
            hijo = nodos_hijos.get()
            # Agregar a la cola si no ha sido expandido aun
            if not comprobar_estado_visitado(hijo.state, visitados):
                cola.put((hijo.cost, next(counter), hijo))

    print("No solution found.")
    return None

def comprobar_estado_visitado(estado, visitados):
    for visitado in visitados:
        if estado.equal(visitado):
            return True
    return False

