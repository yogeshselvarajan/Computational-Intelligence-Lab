class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item, priority):
        self.queue.append((item, priority))

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")

        min_priority = float('inf')
        min_index = -1

        for i, (_, priority) in enumerate(self.queue):
            if priority < min_priority:
                min_priority = priority
                min_index = i

        return self.queue.pop(min_index)[0]


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node_value):
        if node_value in self.graph:
            print("Connection point already exists in the network graph.")
        else:
            self.graph[node_value] = set()
            print("Connection point {} added.".format(node_value))

    def add_edge(self, source, destination, latency):
        if source == destination:
            print("Source and destination connection points cannot be the same. Please enter valid connection points.")
            return

        if source not in self.graph or destination not in self.graph:
            print("Source or destination connection point does not exist in the network graph. Please enter valid connection points.")
            return

        try:
            latency = float(latency)
            self.graph[source].add((destination, latency))
            self.graph[destination].add((source, latency))
            print("Latency of {} ms between connection points {} and {} added.".format(latency, source, destination))
        except ValueError:
            print("Latency should be a numeric value. Please enter a valid latency.")

    def init_base_graph(self):
        total_nodes = input("Enter the total number of connection points in the environment: ")
        if not total_nodes.isdigit():
            print("Invalid input. Please enter a valid number.")
            return

        total_nodes = int(total_nodes)

        for _ in range(total_nodes):
            node_value = input("Enter the value of the connection point: ")
            self.add_node(node_value)

        total_edges = input("Enter the total number of connection latencies in the environment: ")
        if not total_edges.isdigit():
            print("Invalid input. Please enter a valid number.")
            return

        total_edges = int(total_edges)

        for i in range(total_edges):
            print("\n--- Edge", i + 1, "---")
            source = input("Enter the source connection point: ")
            destination = input("Enter the destination connection point: ")
            latency = input("Enter the latency between the connection points: ")
            self.add_edge(source, destination, latency)

    def print_network_structure(self):
        print("Network Structure (Adjacency List):")
        for node, connections in self.graph.items():
            print("Connection point", node)
            if connections:
                for connection, latency in connections:
                    print("  -> Connection point:", connection, "(Latency:", latency, "ms)")
            else:
                print("  -> No connections")

    def print_possible_neighbours(self, node):
        if node not in self.graph:
            print("Connection point does not exist in the network graph. Please enter a valid connection point.")
            return

        connections = self.graph[node]
        print("Possible neighbors of Connection point", node)
        if connections:
            for connection, latency in connections:
                print("  -> Connection point:", connection, "(Latency:", latency, "ms)")
        else:
            print("No neighbors for Connection point", node)

    def ucs(self, start, goal):
        if start == goal:
            print("Starting and destination connection points cannot be the same. Please enter valid connection points.")
            return

        if start not in self.graph or goal not in self.graph:
            print("Starting or destination connection point does not exist in the network graph. Please enter valid connection points.")
            return

        fringe = PriorityQueue()
        fringe.enqueue((start, [(start, 0)]), 0)
        visited_nodes = set()

        while not fringe.is_empty():
            current_node, path = fringe.dequeue()
            current_cost = path[-1][1]

            if current_node == goal:
                return [node for node, _ in path], current_cost

            if current_node in visited_nodes:
                continue

            visited_nodes.add(current_node)

            for neighbor, latency in self.graph[current_node]:
                if neighbor not in visited_nodes:
                    new_path = path + [(neighbor, current_cost + latency)]
                    fringe.enqueue((neighbor, new_path), current_cost + latency)

        return None, None


def is_numeric_string(string):
    return string.isdigit()


def main():
    print("Network Graph Initialization")
    graph = Graph()
    option = 0

    while option != 7:
        print("\n---- Main Menu ----")
        print("1. Input the network environment")
        print("2. Add a connection point")
        print("3. Add a connection latency between 2 connection points")
        print("4. Print the whole network topology")
        print("5. Find the nodes that can be reached from a given connection point")
        print("6. UCS - Find the minimum latency delivery path")
        print("7. Exit")

        option = input("Enter your choice (1-7): ")

        if not option.isdigit() or int(option) not in range(1, 8):
            print("Invalid option. Please enter a valid choice.")
            continue

        option = int(option)

        if option == 1:
            graph.init_base_graph()

        elif option == 2:
            node_value = input("Enter the value of theconnection point: ")

            if is_numeric_string(node_value):
                node_value = int(node_value)

            graph.add_node(node_value)

        elif option == 3:
            source = input("Enter the source connection point: ")
            destination = input("Enter the destination connection point: ")
            latency = input("Enter the latency between the connection points: ")

            graph.add_edge(source, destination, latency)

        elif option == 4:
            graph.print_network_structure()

        elif option == 5:
            node = input("Enter the connection point: ")
            graph.print_possible_neighbours(node)

        elif option == 6:
            start = input("Enter the starting connection point: ")
            goal = input("Enter the destination connection point: ")

            path, cost = graph.ucs(start, goal)

            if path is None:
                print("No path found between the connection points.")
            else:
                print("Minimum latency delivery path:", path)
                print("Minimum latency:", cost, "ms")

        elif option == 7:
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
