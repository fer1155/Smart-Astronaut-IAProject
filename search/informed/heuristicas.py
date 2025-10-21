
# Heurística de distancia Manhattan para el problema del astronauta


def heuristica_manhattan(state, world):
    # Ejemplo: distancia a la muestra más cercana
    astronauta = state.position
    muestras_restantes = [pos for pos in world.samples if pos not in state.collected]
    if not muestras_restantes:
        return 0
    return min(abs(astronauta[0] - m[0]) + abs(astronauta[1] - m[1]) for m in muestras_restantes)


def heuristica_manhattan_admisible(state, world):
    """
    Heurística Manhattan/2 (admisible)
    Calcula una estimación del costo restante desde la posición actual del astronauta
    hasta el objetivo (recolectar todas las muestras y/o llegar a la nave).

    Parámetros:
    - state: Estado actual (objeto State)
    - world: Mundo actual (objeto World)

    Retorna:
    - Un valor numérico con la estimación heurística.
    """

    # Si ya se recolectaron todas las muestras, la meta es la nave
    if len(state.collected) == len(world.samples):
        goal = world.spaceship_position
        return (abs(state.position[0] - goal[0]) + abs(state.position[1] - goal[1])) / 2

    # Si faltan muestras por recolectar:
    # Se toma la muestra más cercana como referencia para estimar la distancia
    remaining_samples = [s for s in world.samples if s not in state.collected]
    
    if not remaining_samples:
        return 0  # No quedan muestras
    
    # Calcula distancia Manhattan a cada muestra faltante
    distances = [
        abs(state.position[0] - sample[0]) + abs(state.position[1] - sample[1])
        for sample in remaining_samples
    ]
    
    # Usa la menor distancia / 2 como estimación admisible
    return min(distances) / 2