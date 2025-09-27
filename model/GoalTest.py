def is_goal_state(state, world):
    return len(state.collected) == len(world.samples)