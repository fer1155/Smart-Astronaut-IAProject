# Algoritmos de Búsqueda Implementados

Este proyecto implementa varios algoritmos de búsqueda para encontrar soluciones en el entorno del astronauta:

## 1. Búsqueda por Amplitud (Breadth-First Search, BFS)


**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola.
2. Mientras la cola no esté vacía:
	- Se saca el primer nodo de la cola.
	- Si es objetivo, termina.
	- Si no, se expanden sus hijos y se agregan al final de la cola si no han sido visitados.

## 2. Búsqueda por Costo Uniforme (Uniform Cost Search, UCS)


**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola de prioridad con costo 0.
2. Mientras la cola no esté vacía:
	- Se saca el nodo con menor costo acumulado.
	- Si es objetivo, termina.
	- Si no, se expanden sus hijos y se agregan a la cola de prioridad si no han sido visitados.

## 3. Búsqueda Avara (Greedy Best-First Search)

- Utiliza una función heurística para estimar qué nodo está más cerca del objetivo.
- Expande siempre el nodo con el menor valor heurístico.
- Utiliza una cola de prioridad, donde la prioridad es el valor de la heurística.
- Es más rápida que las búsquedas no informadas, pero no garantiza la solución óptima.

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola de prioridad con su valor heurístico.
2. Mientras la cola no esté vacía:
   - Se saca el nodo con menor heurística.
   - Si es objetivo, termina.
   - Si no, se expanden sus hijos y se agregan a la cola de prioridad si no han sido visitados.

## Heurística Manhattan

La heurística Manhattan estima la distancia mínima desde el astronauta a la muestra más cercana, sumando las diferencias absolutas de filas y columnas. Se utiliza en la búsqueda avara para guiar la exploración.

**Ejemplo de función heurística:**
```python
def heuristica_manhattan(state, world):
	astronauta = state.position
	muestras_restantes = [pos for pos in world.samples if pos not in state.collected]
	if not muestras_restantes:
		return 0
	return min(abs(astronauta[0] - m[0]) + abs(astronauta[1] - m[1]) for m in muestras_restantes)
```

## Estructura del Proyecto

- `main.py`: Punto de entrada. Permite seleccionar el algoritmo de búsqueda.
- `input_output/`: Lectura y parseo de archivos de entrada.
- `model/`: Definición de estados, nodos y lógica del mundo.
- `search/uninformed/`: Algoritmos de búsqueda no informada (amplitud, costo uniforme).
- `search/informed/`: Algoritmos de búsqueda informada (avara) y funciones heurísticas.
- `ui/`: Interfaz gráfica con Tkinter.

Puedes elegir el algoritmo a ejecutar al iniciar el programa y comparar sus resultados en el entorno del astronauta.
Ambos algoritmos permiten explorar el entorno y encontrar caminos, pero UCS es preferible cuando los movimientos tienen diferentes costos y se busca la solución más económica.
