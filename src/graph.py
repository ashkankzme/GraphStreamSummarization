class Graph:
    def __init__(self, directed):
        self.matrix = {}
        self.directed = directed

    def constructGraph(self, edges):
        for edge in edges:
            x = edge[0]
            y = edge[1]

            if x not in self.matrix:
                self.matrix[x] = {}
            if y not in self.matrix[x]:
                self.matrix[x][y] = 1
            else:
                self.matrix[x][y] += 1

            if not self.directed:
                if y not in self.matrix:
                    self.matrix[y] = {}
                if x not in self.matrix[y]:
                    self.matrix[y][x] = 1
                else:
                    self.matrix[y][x] += 1

    def addEdge(self, a, b, weight):
        if a not in self.matrix:
            self.matrix[a] = {}
        if b not in self.matrix[a]:
            self.matrix[a][b] = 0
        self.matrix[a][b] += weight

        if not self.directed:
            if b not in self.matrix:
                self.matrix[b] = {}
            if a not in self.matrix[b]:
                self.matrix[b][a] = 0
            self.matrix[b][a] += weight
