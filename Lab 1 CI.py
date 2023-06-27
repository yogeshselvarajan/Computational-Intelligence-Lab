from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def init_base_graph():
    num_nodes = int(input("\nEnter the total number of nodes for the input graph: "))
    graph = {}
    for i in range(num_nodes):
        node_value = input("\nEnter the value of node {}: ".format(i + 1))
        if i == 0:
            graph[node_value] = set()
        else:
            graph[node_value] = set()

    num_edges = int(input("\n\nEnter the total number of edges for the input graph: "))
    for i in range(num_edges):
        source, destination, cost = input("\nEnter the source, destination, and cost of edge {}: ".format(i + 1)).split()
        graph[source].add((destination, int(cost)))
        graph[destination].add((source, int(cost)))
    return graph


def print_graph(graph):
    print("The whole graph is:")
    for node, adjacent_nodes in graph.items():
        print(f"{node}: ", end="")
        for adjacent_node, cost in adjacent_nodes:
            print(f"{adjacent_node}({cost}) ", end="")
        print()


def print_graph_visually(graph):
    G = nx.Graph()
    for node, adjacent_nodes in graph.items():
        for adjacent_node, cost in adjacent_nodes:
            G.add_edge(node, adjacent_node, weight=cost)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold',
            edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def print_adjacency_list(graph, node):
    print("\n\nThe adjacency list of node {} is: {}".format(node, graph[node]))


def breadthFirstSearch(graph, startnode, endnode):
    visited = set()
    queue = deque([(startnode, [])])
    while queue:
        node, path = queue.popleft()
        if node == endnode:
            print("\nOrder of traversal from {} to {}: {}".format(startnode, endnode, " -> ".join(path + [node])))
            return
        if node not in visited:
            visited.add(node)
            for adjacent_node, _ in graph[node]:
                queue.append((adjacent_node, path + [node]))
    print("\nPath from {} to {} is not reachable.".format(startnode, endnode))


def depthFirstSearch(graph, startnode, endnode):
    visited = set()
    stack = [(startnode, [])]
    while stack:
        node, path = stack.pop()
        if node == endnode:
            print("\nOrder of traversal from {} to {}: {}".format(startnode, endnode, " -> ".join(path + [node])))
            return
        if node not in visited:
            visited.add(node)
            for adjacent_node, _ in graph[node]:
                stack.append((adjacent_node, path + [node]))
    print("\nPath from {} to {} is not reachable.".format(startnode, endnode))


def uniformCostSearch(graph, startnode, endnode):
    visited = set()
    queue = [(0, startnode, [])]  # Priority queue elements: (cost, node, path)
    heapq.heapify(queue)
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == endnode:
            print("\nOrder of traversal from {} to {}: {}".format(startnode, endnode, " -> ".join(path + [node])))
            print("Minimum cost from {} to {} is: {}".format(startnode, endnode, cost))
            return
        if node not in visited:
            visited.add(node)
            for adjacent_node, edge_cost in graph[node]:
                new_cost = cost + edge_cost
                heapq.heappush(queue, (new_cost, adjacent_node, path + [node]))
    print("\nPath from {} to {} is not reachable.".format(startnode, endnode))


def main():
    graph = {}
    print("\t\tWelcome to the Computational Intelligence Laboratory Exercise 1 - Uninformed Search (Blind Search Implementation)")

    while True:
        print("--------------------------------")
        print("\t MAIN MENU")
        print("--------------------------------")
        print("1. Initialise Base Graph")
        print("2. Add Extra Node")
        print("3. Add Extra Edges")
        print("4. Print the whole graph visually")
        print("5. Print the Adjacency of a particular node")
        print("6. Breadth First Search")
        print("7. Depth First Search")
        print("8. Uniform Cost Search")
        print("9. Exit")
        print("--------------------------------")
        option = int(input("\nEnter your choice: "))

        if option == 1:
            graph = init_base_graph()

        elif option == 2:
            node_value = input("\nEnter the value of the new node: ")
            graph[node_value] = set()
            print("Node {} added successfully.".format(node_value))

        elif option == 3:
            source, destination, cost = input("\nEnter the source, destination, and cost of the new edge: ").split()
            graph[source].add((destination, int(cost)))
            graph[destination].add((source, int(cost)))
            print("Edge ({}, {}) added successfully.".format(source, destination))

        elif option == 4:
            print_graph_visually(graph)

        elif option == 5:
            node = input("\nEnter the node to print the adjacency nodes: ")
            print_adjacency_list(graph, node)

        elif option == 6:
            start_node = input("\nEnter the start node for the BFS: ")
            target_node = input("\nEnter the target node for the BFS: ")
            breadthFirstSearch(graph, start_node, target_node)

        elif option == 7:
            start_node = input("\nEnter the start node for the DFS: ")
            target_node = input("\nEnter the target node for the DFS: ")
            depthFirstSearch(graph, start_node, target_node)

        elif option == 8:
            start_node = input("\nEnter the start node for the Uniform Cost Search: ")
            target_node = input("\nEnter the target node for the Uniform Cost Search: ")
            uniformCostSearch(graph, start_node, target_node)

        elif option == 9:
            print("Thank you for using the program.")
            exit(0)

        else:
            print("Error: Invalid choice.")


if __name__ == "__main__":
    main()