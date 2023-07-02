import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def init_base_graph(self):
        num_nodes = int(input("\nEnter the total number of nodes for the input graph: "))
        for i in range(num_nodes):
            while True:
                node_value = input("\nEnter the value of node {}: ".format(i + 1))
                if node_value not in self.graph:
                    self.graph[node_value] = set()
                    break
                else:
                    print("Node already exists in the graph. Please enter a different node value.")

        num_edges = int(input("\n\nEnter the total number of edges for the input graph: "))
        for i in range(num_edges):
            while True:
                source, destination, cost = input("\nEnter the source, destination, and cost of edge {}: ".format(i + 1)).split()
                if source in self.graph and destination in self.graph:
                    try:
                        cost = int(cost)
                        self.graph[source].add((destination, cost))
                        self.graph[destination].add((source, cost))
                        break
                    except ValueError:
                        print("Cost should be a numeric value. Please enter a valid cost.")
                else:
                    print("Source or destination node does not exist in the graph. Please enter valid nodes.")

    def print_graph(self):
        print("The whole graph is:")
        for node, adjacent_nodes in self.graph.items():
            print(f"{node}: ", end="")
            for adjacent_node, cost in adjacent_nodes:
                print(f"{adjacent_node}({cost}) ", end="")
            print()

    def print_graph_visually(self):
        G = nx.Graph()
        for node, adjacent_nodes in self.graph.items():
            for adjacent_node, cost in adjacent_nodes:
                G.add_edge(node, adjacent_node, weight=cost)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold',
                edge_color='gray')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def print_adjacency_list(self, node):
        if node in self.graph:
            print("\n\nThe adjacency list of node {} is: {}".format(node, self.graph[node]))
        else:
            print("Node does not exist in the graph.")

    def delete_edge(self, source, destination):
        if source in self.graph and destination in self.graph:
            self.graph[source] = {(adjacent_node, cost) for adjacent_node, cost in self.graph[source] if adjacent_node != destination}
            self.graph[destination] = {(adjacent_node, cost) for adjacent_node, cost in self.graph[destination] if adjacent_node != source}
            print("Edge between {} and {} deleted.".format(source, destination))
        else:
            print("Source or destination node does not exist in the graph. Please enter valid nodes.")

    def delete_node(self, node):
        if node in self.graph:
            for adjacent_node, _ in self.graph[node]:
                self.graph[adjacent_node] = {(n, cost) for n, cost in self.graph[adjacent_node] if n != node}
            del self.graph[node]
            print("Node {} and its corresponding edges deleted.".format(node))
        else:
            print("Node does not exist in the graph.")
