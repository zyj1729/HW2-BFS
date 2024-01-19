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
        Perform a breadth-first search on the graph. If an end node is specified, 
        find the shortest path to that node. If no end node is specified, return 
        the order of nodes as they are visited in the BFS.

        Args:
            start (str): The starting node for the BFS.
            end (str, optional): The end node for the BFS. Defaults to None.

        Returns:
            list: A list of nodes representing the BFS traversal order, or the shortest path
                  to the end node, if specified. Returns None if the end node is specified but
                  not reachable.

        Raises:
            Exception: If the start or end node is not present in the graph.
        """ 
        # Check if the start node exists in the graph
        if start not in list(self.graph):
            raise Exception("Start node " + start + " not in graph")
        # Check if the end node exists in the graph (if specified)
        if end and end not in list(self.graph):
            raise Exception("End node " + end + " not in graph")

        def trace(n, visited):
            """
            Helper function to trace back the path from an end node to the start node
            using the 'visited' list.

            Args:
                n (str): The current node to trace back from.
                visited (list): The list of visited nodes along with their predecessors.

            Returns:
                list: The path from the start node to the current node.
            """
            if n == -1:
                return []
            for i in visited:
                if i[1] == n:
                    return trace(i[0], visited) + [n]
            return

        # Initialize the queue and visited list
        Q = []
        visited = []
        Q.append(start)
        visited.append((-1, start))

        # Perform BFS
        while Q:
            v = Q.pop()
            N = self.graph.successors(v)
            for w in N:
                if w not in [i[1] for i in visited]:
                    visited.append((v, w))
                    Q.insert(0, w)
                    if w == end:
                        # If the end node is found, trace back the path and return
                        path = trace(v, visited) + [w]
                        return path

        # If an end node is specified and not found, return None
        if end:
            return None
        # If no end node is specified, return the BFS traversal order
        return [i[1] for i in visited]