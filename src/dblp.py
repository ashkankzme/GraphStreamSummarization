from graph import Graph
import json


def load_dblp_graph(data_path, partial_loading_limit = -1):
    with open(data_path) as coauthorship_file:
        coauthorship_graph_edges = json.load(coauthorship_file)

    # Coauthorship graph is an array of edges like
    # ['Alin Deutsch', 'Mary F. Fernandez', 1998]

    # Loading the undirected DBLP graph
    coauthorship_graph = Graph(directed = False)
    if partial_loading_limit > 0:
        coauthorship_graph.constructGraph(coauthorship_graph_edges[:partial_loading_limit])
    else:
        coauthorship_graph.constructGraph(coauthorship_graph_edges)

    return coauthorship_graph, coauthorship_graph_edges
