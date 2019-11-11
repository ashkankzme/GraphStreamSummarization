from dblp import load_dblp_graph
from TCM_adjacency_matrix import TCMAdjacencyMatrix
from hash import hash
import json, math, random, numbers

d = 9
lowest_compression_rate = 160
highest_compression_rate = 40
step_size = 20

edge_freq_estimation_errors = []
dblp_coauthorship_graph, dblp_coauthorship_graph_edges = load_dblp_graph()
for i in range(((lowest_compression_rate - highest_compression_rate) // step_size) + 1):
    order = len(dblp_coauthorship_graph) // (lowest_compression_rate - (i * step_size))
    dblp_TCM_graph = TCMAdjacencyMatrix(order, d)
    dblp_TCM_graph.constructGraph(dblp_coauthorship_graph)

    edge_freq_estimation_error = 0
    sampled_count = 0
    error_counter = 0
    for edge in dblp_coauthorship_graph_edges:
        # sampling!
        if random.uniform(0, 1) > 0.01:
            continue
        weight = dblp_coauthorship_graph[edge[0]][edge[1]]
        estimated_weight = math.inf
        for i in range(d):
            node_a = hash(edge[0], order, i)
            node_b = hash(edge[1], order, i)
            if dblp_TCM_graph.matrices[i][node_a][node_b] < estimated_weight:
                estimated_weight = dblp_TCM_graph.matrices[i][node_a][node_b]

        if isinstance(estimated_weight, numbers.Number) and isinstance(weight, numbers.Number):
            edge_freq_estimation_error += abs(estimated_weight - weight)
            sampled_count += 1

    edge_freq_estimation_errors.append(edge_freq_estimation_error/sampled_count)

with open('../data/exp1-a_static.json', 'w') as f:
    f.write(json.dumps(edge_freq_estimation_errors))