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
                edge_input = input("\nEnter the source, destination, and cost of edge {} (separated by space): ".format(i + 1))
                edge_parts = edge_input.split()
                if len(edge_parts) != 3:
                    print("Invalid input. Please provide source, destination, and cost separated by space.")
                    continue
                source, destination, cost = edge_parts
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

    def delete_node(self, node_value):
        if node_value in self.graph:
            del self.graph[node_value]
            for node in self.graph:
                self.graph[node] = {(n, c) for n, c in self.graph[node] if n != node_value}
