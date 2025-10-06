# Goal test function to determine if all samples have been collected
# receives the current state and the world
# returns True if the goal is achieved, otherwise False
def is_goal_state(state, world):
    # Check if the number of collected samples equals the total number of samples in the world
    return len(state.collected) == len(world.samples)