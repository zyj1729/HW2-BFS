import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        SOLUTION: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        return




