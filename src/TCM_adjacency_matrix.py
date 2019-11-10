from hash import hash


class TCMAdjacencyMatrix:
    def __init__(self, order, d, directed):
        self.matrices = [0] * d
        self.order = order
        self.d = d
        self.directed = directed

    def constructGraph(self, input_graph):
        # apply hash function on all nodes in graph
        # get buckets of nodes
        # convert the graph into its new representation
        for i in range(self.d):
            self.matrices[i] = {}
            matrix = self.matrices[i]
            for node in input_graph:
                hashed_node = hash(node, self.order, i)
                if hashed_node not in matrix:
                    matrix[hashed_node] = {}
                for adjacent_node in input_graph[node]:
                    hashed_adjacent_node = hash(adjacent_node, self.order, i)
                    if hashed_adjacent_node not in matrix[hashed_node]:
                        matrix[hashed_node][hashed_adjacent_node] = 0
                    matrix[hashed_node][hashed_adjacent_node] += input_graph[node][adjacent_node]


    def addEdge(self, a, b, weight):
        for i in range(self.d):
            hashed_a = hash(a, self.order, i)
            hashed_b = hash(b, self.order, i)
            if hashed_a not in self.matrices[i]:
                self.matrices[i][hashed_a] = {}
            if hashed_b not in self.matrices[i][hashed_a]:
                self.matrices[i][hashed_a][hashed_b] = 0
            self.matrices[i][hashed_a][hashed_b] += weight
            if not self.directed:
                if hashed_b not in self.matrices[i]:
                    self.matrices[i][hashed_b] = {}
                if hashed_a not in self.matrices[i][hashed_b]:
                    self.matrices[i][hashed_b][hashed_a] = 0
                self.matrices[i][hashed_b][hashed_a] += weight
