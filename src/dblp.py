import json


def load_dblp_graph():
    with open('../data/dblp_coauthorship.json') as coauthorship_file:
        coauthorship_graph_edges = json.load(coauthorship_file)

    # Coauthorship graph is an array of edges like
    # ['Alin Deutsch', 'Mary F. Fernandez', 1998]

    # Loading the undirected DBLP graph
    coauthorship_graph = {}
    for edge in coauthorship_graph_edges:
        x = edge[0]
        y = edge[1]

        if x not in coauthorship_graph:
            coauthorship_graph[x] = {}
        if y not in coauthorship_graph[x]:
            coauthorship_graph[x][y] = 1
        else: coauthorship_graph[x][y] += 1

        if y not in coauthorship_graph:
            coauthorship_graph[y] = {}
        if x not in coauthorship_graph[y]:
            coauthorship_graph[y][x] = 1
        else: coauthorship_graph[y][x] += 1

    return coauthorship_graph, coauthorship_graph_edges
