import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    Unit test for verifying the breadth-first traversal of the Graph class.
    The test ensures that all nodes in a small network are traversed correctly,
    both in terms of the number of nodes visited and the order of traversal.
    """
    # Initialize the Graph object with a small network
    tiny = graph.Graph("./data/tiny_network.adjlist")

    # Perform BFS starting from the first node in the graph
    my = tiny.bfs(list(tiny.graph)[0])

    # Create a list of nodes as traversed by networkx's bfs_tree for comparison
    true = list(nx.bfs_tree(tiny.graph, list(tiny.graph)[0]))

    # Assert that the number of nodes traversed by our BFS matches networkx's bfs_tree
    assert len(my) == len(true), "BFS traversal length doesn't match"

    # Assert that the order of nodes traversed matches that of networkx's bfs_tree
    assert my == true, "BFS traversal order doesn't match"


def test_bfs():
    """
    Unit test for verifying the breadth-first search pathfinding in the Graph class.
    This test uses a larger network and checks the BFS functionality for both
    connected and disconnected nodes, as well as non-existent nodes.
    """
    # Initialize the Graph object with a larger network
    All = graph.Graph("./data/citation_network.adjlist")

    # Define start and end nodes for a pathfinding test
    start = 'Atul Butte'
    end = 'Martin Kampmann'

    # Perform BFS to find the shortest path between the start and end nodes
    path = All.bfs(start, end)

    # Assert that a path exists for connected nodes
    assert path is not None, "Path should exist for connected nodes"

    # Assert that the path starts at the start node and ends at the end node
    assert path[0] == start and path[-1] == end, "Path should connect the right nodes"

    # Assert that the length of the path matches the expected shortest path length
    assert len(path) == nx.shortest_path_length(All.graph, start, end) + 1, "Path length is larger than the shortest"

    # Test BFS with a pair of nodes that are not connected
    disconnect_end = 'Reza Abbasi-Asl'
    path = All.bfs(start, disconnect_end)

    # Assert that BFS returns None for disconnected nodes
    assert path is None, "Path should not exist for disconnected nodes"

    # Test BFS with non-existent start and end nodes
    nonexist_start = 'fsasdf'
    nonexist_end = 'gdsfgd'

    # Assert that BFS raises an exception for a non-existent start node
    with pytest.raises(Exception) as excinfo:
        All.bfs(nonexist_start, 'Atul Butte')

    # Assert that BFS raises an exception for a non-existent end node
    with pytest.raises(Exception) as excinfo:
        All.bfs('Atul Butte', nonexist_end)
