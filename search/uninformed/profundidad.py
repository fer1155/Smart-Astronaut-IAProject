# Algoritmo de busqueda no informada - Profundidad evitando ciclos
from model.node import Node


# Busqueda por profundidad evitando ciclos
# recibe el mundo, el estado inicial y la funcion de test de meta
# retorna el nodo objetivo y el numero de nodos expandidos
def busqueda_profundidad(world, initial_state, goal_test):
    # Pila para guardar los nodos por explorar (LIFO)
    stack = []

    # Conjunto para los nodos ya visitados
    visited = set()

    # Nodo inicial
    nodo_inicial = Node(initial_state)

    # Verificar si el estado inicial es la meta
    if goal_test(nodo_inicial.state, world):
        print("Meta alcanzada!")
        return [nodo_inicial, 0]

    # Añadir el nodo inicial a la pila
    stack.append(nodo_inicial)

    # Contador de nodos expandidos
    nodecont = 0

    # Bucle principal de la busqueda
    while stack:

        # Obtener el ultimo nodo de la pila (LIFO - profundidad)
        nodo_actual = stack.pop()

        # Verificar si ya fue visitado (evitar ciclos)
        if comprobar_estado_visitado(nodo_actual.state, visited):
            continue

        # Marcar el nodo actual como visitado DESPUES de extraerlo y verificar que no es visitado
        visited.add(nodo_actual.state)

        # Verificar si el nodo actual es la meta
        if goal_test(nodo_actual.state, world):
            print("Meta alcanzada!")
            return [nodo_actual, nodecont]

        # Expandir el nodo actual
        nodos_hijos = nodo_actual.expand(world)

        # Incrementar el contador de nodos expandidos
        nodecont += 1

        # Iterar sobre la cola de nodos hijos vaciandola
        while not nodos_hijos.empty():
            # Obtener el siguiente nodo hijo
            hijo = nodos_hijos.get()

            # Agregar a la pila solo si no ha sido visitado
            # La verificacion de visitados se hara al extraerlo de la pila
            if not comprobar_estado_visitado(hijo.state, visited):
                stack.append(hijo)

    # Si agotamos la pila y no hay solucion
    print("No solution found.")
    return None


# Funcion para comprobar si un estado ha sido visitado
# Recibe el estado a comprobar y el conjunto de estados visitados
# Retorna True si el estado ha sido visitado, False en caso contrario
# Para evitar ciclos en DFS, comparamos posicion, nave y muestras, pero NO el combustible
def comprobar_estado_visitado(estado, visitados):
    # Itera sobre los estados visitados y compara con el estado actual
    for visitado in visitados:
        # Comparar sin considerar el combustible exacto para evitar ciclos
        if (
            estado.position == visitado.position
            and estado.collected == visitado.collected
            and estado.spaceship == visitado.spaceship
        ):
            return True
    return False
