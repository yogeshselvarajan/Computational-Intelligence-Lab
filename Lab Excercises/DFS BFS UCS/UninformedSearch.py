from QueueImplementation import Queue
from StackImplementation import Stack
from PriorityQueueImplementation import PriorityQueue
from GraphImplementation import Graph

def BFS(graph, start_node, goal_node):
    if start_node not in graph.graph or goal_node not in graph.graph:
        return None

    fringe = Queue()
    fringe.enqueue([(start_node, 0)])
    explored_set = set()

    while not fringe.is_empty():
        path = fringe.dequeue()
        node, cost = path[-1]

        if node == goal_node:
            return [node for node, _ in path], cost

        explored_set.add(node)

        for neighbor, edge_cost in graph.graph[node]:
            if neighbor not in explored_set:
                new_path = path + [(neighbor, cost + edge_cost)]
                fringe.enqueue(new_path)

    return None


def DFS(graph, start_node, goal_node):
    if start_node not in graph.graph or goal_node not in graph.graph:
        return None

    fringe = Stack()
    fringe.push([(start_node, 0)])
    explored_set = set()

    while not fringe.is_empty():
        path = fringe.pop()
        node, cost = path[-1]

        if node == goal_node:
            return [node for node, _ in path], cost

        explored_set.add(node)

        for neighbor, edge_cost in graph.graph[node]:
            if neighbor not in explored_set:
                new_path = path + [(neighbor, cost + edge_cost)]
                fringe.push(new_path)

    return None


def UCS(graph, start_node, goal_node):
    if start_node not in graph.graph or goal_node not in graph.graph:
        return None

    fringe = PriorityQueue()
    fringe.push([(start_node, 0)], 0)
    explored_set = set()

    while not fringe.is_empty():
        path = fringe.pop()
        node, cost = path[-1]

        if node == goal_node:
            return [node for node, _ in path], cost

        explored_set.add(node)

        for neighbor, edge_cost in graph.graph[node]:
            if neighbor not in explored_set:
                new_path = path + [(neighbor, cost + edge_cost)]
                fringe.push(new_path, cost + edge_cost)

    return None



def main():
    print("\t\tWelcome to the Computational Intelligence Laboratory Exercise 1 - Uninformed Search (Blind Search Implementation)")
    graph = Graph()

    while True:
        print("--------------------------------")
        print("\t MAIN MENU")
        print("--------------------------------")
        print("1. Initialize Custom Graph")
        print("2. Add Extra Node")
        print("3. Add Extra Edges")
        print("4. Delete Node")
        print("5. Delete Edge")
        print("6. Print the Whole Graph's Adjacency List")
        print("7. Print the Adjacency of a Particular Node")
        print("8. Breadth First Search")
        print("9. Depth First Search")
        print("10. Uniform Cost Search")
        print("11. Exit")
        print("--------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
             # Initialize a custom graph
            print("Initializing a custom graph...")
            graph.init_base_graph()
            print("Custom Graph initialized successfully!")

        elif choice == "2":
            node_value = input("Enter the input value to store in the new node: ")
            graph.graph[node_value] = set()
            print("Node with value {} added successfully!".format(node_value))

        elif choice == "3":
            source = input("Enter the source node: ")
            destination = input("Enter the destination node: ")
            cost = int(input("Enter the cost of the edge (enter 0 if not applicable): "))
            graph.graph[source].add((destination, cost))
            graph.graph[destination].add((source, cost))
            print("Edge between {} and {} added successfully!".format(source, destination))

        elif choice == "4":
            node_value = input("Enter the node value to delete: ")
            graph.delete_node(node_value)
            print("Node with value {} deleted successfully!".format(node_value))

        elif choice == "5":
            source = input("Enter the source node: ")
            destination = input("Enter the destination node: ")
            graph.delete_edge(source, destination)
            print("Edge between {} and {} deleted successfully!".format(source, destination))

        elif choice == "6":
            graph.print_graph()

        elif choice == "7":
            node_value = input("Enter the node value to print adjacency: ")
            graph.print_adjacency_list(node_value)

        elif choice == "8":
            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")
            result = BFS(graph, start_node, goal_node)
            if result:
                path, cost = result
                print("Breadth First Search Path:", path)
                print("Breadth First Search Cost:", cost)
            else:
                print("Goal node cannot be reached from the start node.")

        elif choice == "9":
            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")
            result = DFS(graph, start_node, goal_node)
            if result:
                path, cost = result
                print("Depth First Search Path:", path)
                print("Depth First Search Cost:", cost)
            else:
                print("Goal node cannot be reached from the start node.")

        elif choice == "10":
            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")
            result = UCS(graph, start_node, goal_node)
            if result:
                cost, path = result
                print("Uniform Cost Search Cost:", cost)
                print("Uniform Cost Search Path:", path)
            else:
                print("Goal node cannot be reached from the start node.")

        elif choice == "11":
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()