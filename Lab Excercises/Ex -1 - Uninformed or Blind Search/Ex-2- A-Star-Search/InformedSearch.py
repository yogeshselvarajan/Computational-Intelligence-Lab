from SetImplementation import ExploredSet
from PriorityQueueImplementation import PriorityQueue
from GraphImplementation import Graph
import pandas as pd


class NodeWithPriority:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority


def a_star(graph, start_node, end_node):
    if start_node == end_node:
        print("Start node and end node are the same.")
        return

    if start_node not in graph.graph:
        print("Start node does not exist in the graph. Please enter a valid start node.")
        return

    if end_node not in graph.graph:
        print("End node does not exist in the graph. Please enter a valid end node.")
        return

    # Create a Priority Queue for open list
    open_list = PriorityQueue()

    # Create a set to store explored nodes
    explored_set = set()

    # Create dictionaries for g(n), h(n), and f(n) values
    g_values = {node: float('inf') for node in graph.graph}
    h_values = {node: graph.get_heuristic(node) for node in graph.graph}
    f_values = {node: float('inf') for node in graph.graph}

    # Create dictionaries for storing the parent nodes and the similarity values of the shortest path
    parent_nodes = {node: None for node in graph.graph}
    similarity_values = {node: None for node in graph.graph}

    # Initialize the start node
    g_values[start_node] = 0
    f_values[start_node] = g_values[start_node] + h_values[start_node]
    open_list.enqueue(NodeWithPriority(start_node, f_values[start_node]))

    while not open_list.is_empty():
        current_node = open_list.dequeue().data

        if current_node == end_node:
            # Path found, print the path and total cost
            path = []
            total_cost = g_values[current_node]

            while current_node is not None:
                path.append(current_node)
                current_node = parent_nodes[current_node]

            path.reverse()
            print("Path:", " -> ".join(path))
            print("Total Cost:", total_cost)

            return

        if current_node in explored_set:
            continue

        explored_set.add(current_node)

        for neighbor, similarity in graph.graph[current_node].items():
            if neighbor in explored_set:
                continue

            # Calculate g(n) for the neighbor node
            g_score = g_values[current_node] + similarity

            if g_score < g_values[neighbor]:
                g_values[neighbor] = g_score
                f_values[neighbor] = g_values[neighbor] + h_values[neighbor]
                open_list.enqueue(NodeWithPriority(neighbor, f_values[neighbor]))

                # Update parent and similarity values for the neighbor node
                parent_nodes[neighbor] = current_node
                similarity_values[neighbor] = similarity

    print("Path not found.")


def main():
    base_graph = None

    while True:
        print("\n----- Menu -----")
        print("1. Input base graph")
        print("2. Add Extra Nucleotide Node")
        print("3. Add Extra Similarity Edge")
        print("4. Print the whole DNA Sequence Graph")
        print("5. Find Shortest Path (A* Algorithm)")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            base_graph = Graph.initialise_base_graph()
            if base_graph:
                print("Base graph initialized successfully!")

        elif choice == '2':
            if base_graph:
                while True:
                    try:
                        nucleotide, heuristic = input("Enter nucleotide and its heuristic value (separated by space): ").split()
                        heuristic = float(heuristic)
                        base_graph.add_node(nucleotide, heuristic)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid nucleotide and its heuristic value.")

            else:
                print("Please input the base graph first.")

        elif choice == '3':
            if base_graph:
                while True:
                    try:
                        src, dest, similarity = input("Enter source, destination, and similarity (separated by space): ").split()
                        similarity = float(similarity)
                        base_graph.add_edge(src, dest, similarity)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid source, destination, and similarity.")

            else:
                print("Please input the base graph first.")

        elif choice == '4':
            if base_graph:
                base_graph.print_adjacency_list()
            else:
                print("Please input the base graph first.")

        elif choice == '5':
            if base_graph:
                start_nucleotide = input("Enter the start nucleotide: ")
                end_nucleotide = input("Enter the end nucleotide: ")

                a_star(base_graph, start_nucleotide, end_nucleotide)

            else:
                print("Please input the base graph first.")

        elif choice == '6':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).")


if __name__ == "__main__":
    main()
