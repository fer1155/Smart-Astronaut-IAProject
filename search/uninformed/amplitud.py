# Algoritmo de búsqueda no informada
import queue
from model.node import Node

# Búsqueda por amplitud
# recibe el mundo, el estado inicial y la función de test de meta
# retorna el nodo objetivo y el número de nodos expandidos
def busqueda_por_amplitud(world, initial_state, goal_test):
    # Cola para guardar los nodos por explorar
    cola = queue.Queue()

    # Conjunto para los nodos ya visitados
    visited = set()

    # Nodo inicial
    nodo_inicial = Node(initial_state)

    # Añadir el nodo inicial a la cola
    cola.put(nodo_inicial)

    # Marcar el nodo inicial como visitado
    visited.add(nodo_inicial.state)

    # Contador de nodos expandidos
    nodecont = 0

    # Bucle principal de la búsqueda
    while not cola.empty():

        # Obtener el nodo para tratar
        nodo_actual = cola.get()

        # Verificar si el nodo actual es el estado objetivo (meta)
        if goal_test(nodo_actual.state, world):
            print("Goal reached!")
            return [nodo_actual, nodecont]

        # Expandir el nodo actual
        nodos_hijos = nodo_actual.expand(world) 

        # Incrementar el contador de nodos expandidos
        nodecont += 1
  
        # Iterar sobre la cola de nodos hijos vaciándola
        while not nodos_hijos.empty():
            # Obtener el siguiente nodo hijo
            hijo = nodos_hijos.get()

            # Si el estado del hijo no ha sido visitado
            # Se añade a la cola y se marca como visitado
            if not comprobar_estado_visitado(hijo.state, visited):
                cola.put(hijo)
                visited.add(hijo.state)

    # Si agotamos la cola y no hay solución
    print("No solution found.")
    return None

# Función para comprobar si un estado ha sido visitado
# Recibe el estado a comprobar y el conjunto de estados visitados
# Retorna True si el estado ha sido visitado, False en caso contrario
def comprobar_estado_visitado(estado, visitados):
    # Itera sobre los estados visitados y compara con el estado actual
    for visitado in visitados:
        if estado.equal(visitado):
            return True
    return False