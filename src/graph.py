from abc import ABC, abstractmethod

class Graph(ABC):
    @abstractmethod
    def constructGraph(self, input):
        pass
