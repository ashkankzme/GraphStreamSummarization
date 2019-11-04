from .graph import Graph
import numpy as np
from .hash import hash


class TCMAdjacencyMatrix(Graph):
    def __init__(self, order):
        self.matrix = {}
        self.order = order

    def constructGraph(self, input_graph):
        # apply hash function on all nodes in graph
        # get buckets of nodes
        # convert the graph into its new representation
        for node in input_graph:
            hashed_node = hash(node, self.order)
            if hashed_node not in self.matrix:
                input_graph[hashed_node] = {}
            for adjacent_node in input_graph[node]:
                hashed_adjacent_node = hash(adjacent_node, self.order)
                if hashed_adjacent_node not in self.matrix[hashed_node]:
                    self.matrix[hashed_node][hashed_adjacent_node] = 0
                self.matrix[hashed_node][hashed_adjacent_node] += 1

    def insertEdge(self, edge):
        return

    def removeEdge(self, edge):
        return

    def updateEdge(self, edge):