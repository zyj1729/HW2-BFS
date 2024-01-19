![BuildStatus](https://github.com/zyj1729/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)
# Breadth-First Search (BFS) Implementation

## Overview
The Graph class in this project includes an implementation of the Breadth-First Search (BFS) algorithm. This algorithm is used for traversing or searching tree or graph data structures. It starts at a selected node (the 'start node') and explores all of the neighbor nodes at the present depth before moving on to nodes at the next depth level.

## Features

* **Traversal**: The BFS method can perform a complete traversal of the graph starting from a specified node. It returns a list of nodes in the order they were visited.

* **Pathfinding**: Given a start node and an end node, the BFS method can find the shortest path between these two nodes, if such a path exists. The path is returned as a list of nodes.

* **Error Handling**: The BFS method includes robust error handling. If the start or end node does not exist in the graph, it raises an exception.

* **Handling Disconnected Nodes**: If no path exists between the start and end nodes (i.e., if they are disconnected in the graph), the BFS method returns `None`.

## Example Usage

```python
from graph_module import Graph  # Replace with your actual import

# Create a graph from an adjacency list
graph = Graph("path/to/adjlist/file")

# Perform BFS traversal from a start node
traversal_order = graph.bfs("start_node")

# Find the shortest path between two nodes
path = graph.bfs("start_node", "end_node")


