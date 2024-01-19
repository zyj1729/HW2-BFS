# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    tiny = graph.Graph("./data/tiny_network.adjlist")
    my = tiny.bfs(list(tiny.graph)[0])
    true = list(nx.bfs_tree(tiny.graph, list(tiny.graph)[0]))
    assert len(my) == len(true), "BFS traversal length doesn't match"
    assert my == true, "BFS traversal order doesn't match"
    pass


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    All = graph.Graph("./data/citation_network.adjlist")
    start = 'Atul Butte'
    end = 'Martin Kampmann'
    path = All.bfs(start, end)
    assert path is not None, "Path should exist for connected nodes"
    assert path[0] == start and path[-1] == end, "Path should connect the right nodes"
    assert len(path) == nx.shortest_path_length(All.graph, start, end) + 1, "Path length is larger than the shortest"

    disconnect_end = 'Reza Abbasi-Asl'
    path = All.bfs(start, disconnect_end)
    assert path is None, "Path should not exist for disconnected nodes"
    
    nonexist_start = 'fsasdf'
    nonexist_end = 'gdsfgd'
    with pytest.raises(Exception) as excinfo:
        All.bfs(nonexist_start, 'Atul Butte')
    with pytest.raises(Exception) as excinfo:
        All.bfs('Atul Butte', nonexist_end)
    pass
