from dblp import load_dblp_graph
from TCM_adjacency_matrix import TCMAdjacencyMatrix
import json

d = 9
lowest_compression_rate = 160
highest_compression_rate = 40
step_size = 20

distributions = []
dblp_coauthorship_graph = load_dblp_graph()
for i in range(((lowest_compression_rate - highest_compression_rate) // step_size) + 1):
    order = len(dblp_coauthorship_graph) // (lowest_compression_rate - (i * step_size))
    dblp_TCM_graph = TCMAdjacencyMatrix(order, d)
    dblp_TCM_graph.constructGraph(dblp_coauthorship_graph)

    distribution = {}
    for i in range(d):
        for node in dblp_TCM_graph.matrices[i]:
            for adj_node in dblp_TCM_graph.matrices[i][node]:
                if dblp_TCM_graph.matrices[i][node][adj_node] not in distribution:
                    distribution[dblp_TCM_graph.matrices[i][node][adj_node]] = 0
                distribution[dblp_TCM_graph.matrices[i][node][adj_node]] += 1 / d

    distributions.append(distribution)

with open('../data/exp1-a.json', 'w') as f:
    f.write(json.dumps(distributions))
