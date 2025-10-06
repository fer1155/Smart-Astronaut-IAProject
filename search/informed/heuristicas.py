
# Heurística de distancia Manhattan para el problema del astronauta


def heuristica_manhattan(state, world):
    # Ejemplo: distancia a la muestra más cercana
    astronauta = state.position
    muestras_restantes = [pos for pos in world.samples if pos not in state.collected]
    if not muestras_restantes:
        return 0
    return min(abs(astronauta[0] - m[0]) + abs(astronauta[1] - m[1]) for m in muestras_restantes)