def is_goal_state(state, world):
    return state.collected == len(world.samples)