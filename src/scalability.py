from data_loader import load_snap_graph
from TCM_adjacency_matrix import TCMAdjacencyMatrix
from hash import clear_cache
import json, math, random, numbers, copy, time

d = 9
lowest_compression_rate = 300
step_size = 10000000
initial_edges_to_load = 1000000

# initially we load a fraction of the graph. Then we add edges to it in a stream to build the rest of the network.
graph_main, edges = load_snap_graph(
    data_path='../data/sx-stackoverflow.txt',
    partial_loading_limit=initial_edges_to_load)
times = []
for step in range(6):
    order_2 = ((step + 1) * step_size) / (lowest_compression_rate - (step * step_size))
    order = round(math.sqrt(order_2))
    graph_copy = copy.deepcopy(graph_main)
    clear_cache()

    # from here we time!
    start = time.time()
    TCM_graph = TCMAdjacencyMatrix(order, d, directed=False)
    TCM_graph.constructGraph(graph_copy.matrix)

    edge_freq_estimation_error = 0
    sampled_count = 0
    for edge in edges[initial_edges_to_load:(step + 1) * step_size]:
        # updating the graphs
        TCM_graph.addEdge(edge[0], edge[1], 1)
        graph_copy.addEdge(edge[0], edge[1], 1)

        # sampling!
        if random.uniform(0, 1) > 0.0001:
            continue
        weight = graph_copy.matrix[edge[0]][edge[1]]
        estimated_weight = TCM_graph.estimateEdgeWeight(edge[0], edge[1])

        if isinstance(estimated_weight, numbers.Number) and isinstance(weight, numbers.Number):
            edge_freq_estimation_error += abs(estimated_weight - weight)
            sampled_count += 1

    print(
        "Pass {} completed, here's the error: {}".format(step, edge_freq_estimation_error / sampled_count))
    end = time.time()
    # here we stop timing
    times.append(end - start)
    print("time elapsed: {}".format(end - start))

with open('../data/scalability.json', 'w') as f:
    f.write(json.dumps(times))
