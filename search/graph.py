import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """ 
        if start not in list(self.graph):
            raise Exception("Start node " + start + " not in graph")
        if end and end not in list(self.graph):
            raise Exception("End node " + end + " not in graph")
        def trace(n, visited):
            if n == -1:
                return []
            for i in visited:
                if i[1] == n:
                    return trace(i[0], visited) + [n]
            return
        Q = []
        visited = []
        Q.append(start)
        visited.append((-1, start))
        while Q:
            v = Q.pop()
            N = self.graph.successors(v)
            for w in N:
                if w not in [i[1] for i in visited]:
                    visited.append((v, w))
                    Q.insert(0, w)
                if w == end:
                    path = trace(v, visited) + [w]
                    return path
        if end:
            return None
        return [i[1] for i in visited]




