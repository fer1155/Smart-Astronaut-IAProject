
# Generación de reportes
# Function to generate a report of the results after the search (amplitud search)
def generate_report(resultado, tiempo_transcurrido):
    # Unpack the results
    node_solution, nodes_expanded = resultado
    depth = node_solution.depth

    # Validate if a solution was found
    if node_solution is None:
        print("No solution found.")
        return
    
    # Print the report
    print("Solution found:")
    path = node_solution.get_path()
    for step in path:
        print(step)

    print(f"Total nodes expanded: {nodes_expanded}")
    print(f"Depth of solution: {depth}")
    print(f"Total cost of solution: {node_solution.cost}")
    print(f"Time taken: {tiempo_transcurrido:.4f} seconds")
