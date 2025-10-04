"""
Algoritmo de Búsqueda en Profundidad Evitando Ciclos (DFS)
"""


def dfs_avoiding_cycles(initial_state, goal_state, get_successors):
    """
    Búsqueda en profundidad evitando ciclos

    Args:
        initial_state: Estado inicial (posición del astronauta)
        goal_state: Estado objetivo (donde queremos llegar)
        get_successors: Función que retorna lista de sucesores [(accion, estado)]

    Returns:
        tuple: (camino, nodos_expandidos, profundidad) o (None, nodos_expandidos, profundidad)
    """
    stack = [(initial_state, [initial_state])]
    visited = {initial_state}
    nodes_expanded = 0
    max_depth = 0

    while stack:
        current_state, path = stack.pop()
        nodes_expanded += 1
        max_depth = max(max_depth, len(path) - 1)

        if current_state == goal_state:
            return path, nodes_expanded, len(path) - 1

        for action, next_state in get_successors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, path + [next_state]))

    return None, nodes_expanded, max_depth

""" 
Usa una pilla para DFS evitando los ciclos con conjunto de visitados, para implementarlo no olvidar pasar el estado inicial, el objetivo y la función de sucesores
"""