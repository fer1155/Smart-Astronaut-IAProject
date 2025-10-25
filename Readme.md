# Algoritmos de Búsqueda Implementados

Este proyecto implementa varios algoritmos de búsqueda para encontrar soluciones en el entorno del astronauta.

## Cómo ejecutar

1. Clonar o descargar el repositorio
2. Ejecutar el archivo principal:
```bash
   python main.py
```
3. Seleccionar el algoritmo de búsqueda deseado desde la interfaz

## Algoritmos Implementados

### 1. Búsqueda por Amplitud 

- Explora todos los nodos a una profundidad antes de avanzar al siguiente nivel.
- Utiliza una cola FIFO (First In, First Out).
- Garantiza encontrar la solución con menor número de pasos si existe.

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola y se marca como visitado.
2. Mientras la cola no esté vacía:
   - Se saca el primer nodo de la cola.
   - Si es objetivo, termina.
   - Si no, se expanden sus hijos y se agregan al final de la cola si no han sido visitados.

### 2. Búsqueda por Profundidad 

- Explora tan profundo como sea posible antes de retroceder.
- Utiliza una pila LIFO (Last In, First Out).
- No garantiza encontrar la solución óptima, pero puede ser más eficiente en memoria.

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la pila.
2. Mientras la pila no esté vacía:
   - Se saca el último nodo de la pila.
   - Si ya fue visitado, se salta (para evitar ciclos).
   - Se marca como visitado.
   - Si es objetivo, termina.
   - Si no, se expanden sus hijos y se agregan a la pila si no han sido visitados.

**Nota:** La implementación evita ciclos comparando posición, nave y muestras recolectadas.

### 3. Búsqueda por Costo Uniforme 

- Expande siempre el nodo con el menor costo acumulado.
- Utiliza una cola de prioridad ordenada por el costo.
- Garantiza encontrar la solución con menor costo total.

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola de prioridad con costo 0.
2. Mientras la cola no esté vacía:
   - Se saca el nodo con menor costo acumulado.
   - Si ya fue visitado, se salta.
   - Se marca como visitado.
   - Si es objetivo, termina.
   - Si no, se expanden sus hijos y se agregan a la cola de prioridad si no han sido visitados.

### 4. Búsqueda Avara 

- Utiliza una función heurística (manhattan) para estimar qué nodo está más cerca del objetivo.
- Expande siempre el nodo con el menor valor heurístico.
- Utiliza una cola de prioridad, donde la prioridad es el valor de la heurística.
- Es más rápida que las búsquedas no informadas, pero no garantiza la solución óptima.

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola de prioridad con su valor heurístico.
2. Mientras la cola no esté vacía:
   - Se saca el nodo con menor heurística.
   - Si es objetivo, termina.
   - Si no, se expanden sus hijos y se agregan a la cola de prioridad si no han sido visitados.

### 5. Búsqueda A* 

- Combina el costo acumulado con una estimación heurística.
- Expande el nodo con menor valor f(n) = g(n) + h(n), donde:
  - g(n) = costo acumulado desde el inicio
  - h(n) = estimación heurística hasta el objetivo (manhattan / 2)
- Garantiza encontrar la solución óptima si la heurística es admisible (nunca sobreestima el costo real).

**Funcionamiento básico:**
1. Se agrega el nodo inicial a la cola de prioridad con f(n) = h(n).
2. Mientras la cola no esté vacía:
   - Se saca el nodo con menor f(n).
   - Si es objetivo, termina.
   - Si no, se expanden sus hijos calculando f(n) = g(n) + h(n) para cada uno.
   - Se agregan a la cola de prioridad si no han sido visitados o se encontró un camino más barato.

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
- `search/uninformed/`: Algoritmos de búsqueda no informada (amplitud, profundidad, costo uniforme).
- `search/informed/`: Algoritmos de búsqueda informada (avara, A*) y funciones heurísticas.
- `ui/`: Interfaz gráfica con Tkinter.
