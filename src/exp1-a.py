from data_loader import load_snap_graph
from TCM_adjacency_matrix import TCMAdjacencyMatrix
import json, math, random, numbers, copy

d = 9
lowest_compression_rate = 70
highest_compression_rate = 10
step_size = 10
initial_edges_to_load = 100000

edge_freq_estimation_errors = []
# initially we load a fraction of the graph. Then we add edges to it in a stream to build the rest of the network.
graph_main, edges = load_snap_graph(
    data_path='../data/sx-superuser.txt',
    partial_loading_limit=initial_edges_to_load)
for step in range(((lowest_compression_rate - highest_compression_rate) // step_size) + 1):
    order_2 = len(edges) / (lowest_compression_rate - (step * step_size))
    order = round(math.sqrt(order_2))
    graph_copy = copy.deepcopy(graph_main)
    TCM_graph = TCMAdjacencyMatrix(order, d, directed=False)
    TCM_graph.constructGraph(graph_copy.matrix)

    edge_freq_estimation_error = 0
    sampled_count = 0
    for edge in edges[initial_edges_to_load:]:
        # updating the graphs
        TCM_graph.addEdge(edge[0], edge[1], 1)
        graph_copy.addEdge(edge[0], edge[1], 1)

        # sampling!
        if random.uniform(0, 1) > 0.01:
            continue
        weight = graph_copy.matrix[edge[0]][edge[1]]
        estimated_weight = TCM_graph.estimateEdgeWeight(edge[0], edge[1])

        if isinstance(estimated_weight, numbers.Number) and isinstance(weight, numbers.Number):
            edge_freq_estimation_error += abs(estimated_weight - weight)
            sampled_count += 1

    edge_freq_estimation_errors.append(edge_freq_estimation_error / sampled_count)
    print(
        "Pass {} completed, here's the error: {}".format(step, edge_freq_estimation_error / sampled_count))

with open('../data/exp1-a_superuser.json', 'w') as f:
    f.write(json.dumps(edge_freq_estimation_errors))
