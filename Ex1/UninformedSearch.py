from QueueImplementation import Queue
from StackImplementation import Stack
from PriorityQueueImplementation import PriorityQueue
from GraphImplementation import Graph


def BFS(graph, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        raise Exception("Start node or goal node is not in the graph")

    fringe = Queue()
    explored_set = set()

    fringe.enqueue(start_node)
    explored_set.add(start_node)

    path = []

    while not fringe.is_empty():
        node = fringe.dequeue()
        path.append(node)

        if node == goal_node:
            return path

        for neighbor in graph.get_adjacency_list(node):
            if neighbor not in explored_set:
                fringe.enqueue(neighbor)
                explored_set.add(neighbor)

    return None


def DFS(graph, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        raise Exception("Start node or goal node is not in the graph")

    fringe = Stack()
    explored_set = set()

    fringe.push(start_node)
    explored_set.add(start_node)

    path = []

    while not fringe.is_empty():
        node = fringe.pop()
        path.append(node)

        if node == goal_node:
            return path

        for neighbor in graph.get_adjacency_list(node):
            if neighbor not in explored_set:
                fringe.push(neighbor)
                explored_set.add(neighbor)

    return None


def UCS(graph, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        raise Exception("Start node or goal node is not in the graph")

    fringe = PriorityQueue()
    explored_set = set()

    # Each item in the fringe will be a tuple: (node, path_cost)
    fringe.enqueue((start_node, 0))
    explored_set.add(start_node)

    while not fringe.is_empty():
        node, path_cost = fringe.dequeue()

        if node == goal_node:
            return path_cost

        for neighbor, cost in graph.get_adjacency_list(node):
            if neighbor not in explored_set:
                fringe.enqueue((neighbor, path_cost + cost))
                explored_set.add(neighbor)

    return None


def main():
    print("\t\tWelcome to the Computational Intelligence Laboratory Exercise 1 - Uninformed Search (Blind Search Implementation)")
    graph = Graph()

    while True:
        print("--------------------------------")
        print("\t MAIN MENU")
        print("--------------------------------")
        print("1. Initialize Base Graph")
        print("2. Add Extra Node")
        print("3. Add Extra Edges")
        print("4. Delete Node")
        print("5. Delete Edge")
        print("6. Print the Whole Graph Visually")
        print("7. Print the Adjacency of a Particular Node")
        print("8. Breadth First Search")
        print("9. Depth First Search")
        print("10. Uniform Cost Search")
        print("11. Exit")
        print("--------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            graph.init_base_graph()

        elif choice == "2":
            node_value = input("Enter the input value to store in the new node: ")
            graph.graph[node_value] = set()
            print("Node added successfully!")

        elif choice == "3":
            source = input("Enter the source node: ")
            destination = input("Enter the destination node: ")
            cost = int(input("Enter the cost of the edge (enter 0 if not applicable): "))
            graph.graph[source].add((destination, cost))
            graph.graph[destination].add((source, cost))
            print("Edge added successfully!")

        elif choice == "4":
            node_value = input("Enter the node value to delete: ")
            graph.delete_node(node_value)
            print("Node deleted successfully!")

        elif choice == "5":
            source = input("Enter the source node: ")
            destination = input("Enter the destination node: ")
            graph.delete_edge(source, destination)
            print("Edge deleted successfully!")

        elif choice == "6":
            graph.print_graph_visually()

        elif choice == "7":
            node_value = input("Enter the node value to print adjacency: ")
            graph.print_adjacency_list(node_value)

        elif choice == "8":
            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")
            path = BFS(graph, start_node, goal_node)
            if path:
                print("Breadth First Search Path:", path)
            else:
                print("No path found.")

        elif choice == "9":
            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")
            path = DFS(graph, start_node, goal_node)
            if path:
                print("Depth First Search Path:", path)
            else:
                print("No path found.")

        elif choice == "10":
            start_node = input("Enter the start node: ")
            goal_node = input("Enter the goal node: ")
            cost = UCS(graph, start_node, goal_node)
            if cost is not None:
                print("Uniform Cost Search Cost:", cost)
            else:
                print("No path found.")

        elif choice == "11":
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
