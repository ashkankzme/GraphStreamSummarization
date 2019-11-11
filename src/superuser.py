from graph import Graph


def load_superuser_graph(data_path, partial_loading_limit = -1):
    with open(data_path) as f:
        superuser_lines = f.readlines()

    superuser_edges = []
    for line in superuser_lines:
        edge = line.split()
        superuser_edges.append(edge)

    superuser_graph = Graph(directed=True)
    if partial_loading_limit > 0:
        superuser_graph.constructGraph(superuser_edges[:partial_loading_limit])
    else:
        superuser_graph.constructGraph(superuser_edges)

    return superuser_graph, superuser_edges
