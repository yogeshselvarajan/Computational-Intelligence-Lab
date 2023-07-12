# Uniform Cost Search Network Routing Application

This program demonstrates the Uniform Cost Search (UCS) algorithm for finding the minimum latency delivery path in a network routing application. The program allows users to input the network environment, add connection points and latencies, print the network topology, find reachable nodes from a given connection point, and perform UCS to find the minimum latency path.

## Classes

### PriorityQueue

The `PriorityQueue` class is implemented to maintain a priority queue based on the cost. It provides the following functions:

- `is_empty()`: Check if the priority queue is empty.
- `size()`: Get the size of the priority queue.
- `enqueue(item, priority)`: Enqueue an item with a given priority.
- `dequeue()`: Dequeue the item with the minimum priority.

### Graph

The `Graph` class represents the network graph and provides functions to manipulate and analyze it. It includes the following functions:

- `add_node(node_value)`: Add a connection point to the network graph.
- `add_edge(source, destination, latency)`: Add a connection latency between two connection points.
- `init_base_graph()`: Initialize the network graph based on user input.
- `print_network_structure()`: Print the whole network topology.
- `print_possible_neighbours(node)`: Print the nodes that can be reached from a given connection point.
- `ucs(start, goal)`: Perform Uniform Cost Search to find the minimum latency delivery path.

### Screenshots

![Sample Input Network Graph](img/input_graph.png)
*Example screenshot of the input network graph.*

![Network Routing Topology](img/network_routing_topology.png)
*Example screenshot of the network topology.*

![UCS Path](img/ucs_path.png)
*Example screenshot of the minimum latency delivery path found using UCS.*

## Usage

To run the program:

1. Install the required dependencies, such as Python.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the repository's directory.
4. Run the program using the command: `python3 NetworkRoutingUCS.py` or `python NetworkRoutingUCS.py` depending on your Python installation. 

## Credits

This program was created by [Yogesh S](https://github.com/yogeshselvarajan). Feel free to contribute and improve the code.


