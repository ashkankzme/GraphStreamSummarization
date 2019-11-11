from data_loader import load_dblp_graph, load_snap_graph
from TCM_adjacency_matrix import TCMAdjacencyMatrix
from hash import hash
import json, math, random, numbers

d = 9
lowest_compression_rate = 160
highest_compression_rate = 40
step_size = 20

edge_freq_estimation_errors = []
dblp_coauthorship_graph, dblp_coauthorship_graph_edges = load_dblp_graph('../data/dblp_coauthorship.json', 300000)
for compression_rate in range(((lowest_compression_rate - highest_compression_rate) // step_size) + 1):
    order_2 = len(dblp_coauthorship_graph_edges) / (lowest_compression_rate - (compression_rate * step_size))
    order = round(math.sqrt(order_2))
    dblp_TCM_graph = TCMAdjacencyMatrix(order, d, directed=False)
    dblp_TCM_graph.constructGraph(dblp_coauthorship_graph.matrix)

    edge_freq_estimation_error = 0
    sampled_count = 0
    error_counter = 0
    for edge in dblp_coauthorship_graph_edges[:300000]:
        # sampling!
        if random.uniform(0, 1) > 0.01:
            continue
        weight = dblp_coauthorship_graph.matrix[edge[0]][edge[1]]
        estimated_weight = dblp_TCM_graph.estimateEdgeWeight(edge[0], edge[1])

        if isinstance(estimated_weight, numbers.Number) and isinstance(weight, numbers.Number):
            edge_freq_estimation_error += abs(estimated_weight - weight)
            sampled_count += 1

    edge_freq_estimation_errors.append(edge_freq_estimation_error / sampled_count)
    print(
        "Pass {} completed, here's the error: {}".format(compression_rate, edge_freq_estimation_error / sampled_count))

with open('../data/exp1-a_static.json', 'w') as f:
    f.write(json.dumps(edge_freq_estimation_errors))
