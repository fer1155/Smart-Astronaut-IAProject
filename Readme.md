# Algoritmos de Búsqueda Implementados

Este proyecto implementa dos algoritmos de búsqueda principales para encontrar soluciones en el entorno del astronauta:

## 1. Búsqueda por Amplitud (Breadth-First Search, BFS)

- Expande los nodos por niveles, es decir, primero explora todos los nodos a una cierta profundidad antes de pasar a la siguiente.
- Utiliza una cola FIFO (primero en entrar, primero en salir) para almacenar los nodos por expandir.
- Garantiza encontrar la solución con el menor número de pasos (si todos los movimientos tienen el mismo costo).
- No considera el costo de los movimientos, solo la cantidad de pasos.

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola.
2. Mientras la cola no esté vacía:
	- Se saca el primer nodo de la cola.
	- Si es objetivo, termina.
	- Si no, se expanden sus hijos y se agregan al final de la cola si no han sido visitados.

## 2. Búsqueda por Costo Uniforme (Uniform Cost Search, UCS)

- Expande siempre el nodo con el menor costo acumulado desde el inicio.
- Utiliza una cola de prioridad, donde la prioridad es el costo total del camino recorrido hasta el nodo.
- Garantiza encontrar la solución óptima (de menor costo), incluso si los movimientos tienen costos diferentes.
- Es una generalización del algoritmo de Dijkstra.

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola de prioridad con costo 0.
2. Mientras la cola no esté vacía:
	- Se saca el nodo con menor costo acumulado.
	- Si es objetivo, termina.
	- Si no, se expanden sus hijos y se agregan a la cola de prioridad si no han sido visitados.

Ambos algoritmos permiten explorar el entorno y encontrar caminos, pero UCS es preferible cuando los movimientos tienen diferentes costos y se busca la solución más económica.
