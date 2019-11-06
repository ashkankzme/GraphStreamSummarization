from dblp import load_dblp_graph
from TCM_adjacency_matrix import TCMAdjacencyMatrix


lowest_compression_rate = 160
highest_compression_rate = 40
step_size = 20

distributions = []
for i in range(((highest_compression_rate-lowest_compression_rate)/step_size)+1):
    dblp_coauthorship_graph = load_dblp_graph()
    order = len(dblp_coauthorship_graph)/(lowest_compression_rate - (i*step_size))
    dblp_TCM_graph = TCMAdjacencyMatrix(order, 9)
    dblp_TCM_graph.constructGraph(dblp_coauthorship_graph)

    for i in range(d):
        for node in dblp_TCM_graph.matrices[i]:

