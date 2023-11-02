from GraphImplementation import DirectedGraph as Graph
from SetImplementation import Set

def aStarAlgo(start_node, stop_node, graph):
    if start_node not in graph.nodes:
        print("Start node {} is not present in the graph!".format(start_node))
        return
    if stop_node not in graph.nodes:
        print("Stop node {} is not present in the graph!".format(stop_node))
        return

    open_set = Set()
    open_set.add(start_node)
    closed_set = Set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    paths = {start_node: [start_node]}
    cost = {start_node: 0}

    while len(open_set) > 0:
        n = None
        for v in open_set.items:
            if n is None or g[v] + graph.nodes[v] < g[n] + graph.nodes[n]:
                n = v
        if n == stop_node or graph.nodes[n] is None:
            break

        for m, weight in graph.get_neighbors(n):
            if not open_set.contains(m) and not closed_set.contains(m):
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
                paths[m] = paths[n] + [m]
                cost[m] = g[m] + graph.nodes[m]
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    paths[m] = paths[n] + [m]
                    cost[m] = g[m] + graph.nodes[m]
                    if closed_set.contains(m):
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    optimal_path = ' -> '.join(paths[n])
    optimal_cost = cost[n]
    print("\tOptimal Path:", optimal_path)
    print("\tOptimal Cost:", optimal_cost)
    return optimal_path

def traverseGraph(start_node, end_node, current_path, current_cost, graph):
    if start_node == end_node:
        path_str = ' -> '.join(current_path)
        print("\tPath:", path_str, "(Cost:", current_cost, ")")
        return

    neighbors = graph.get_neighbors(start_node)
    if neighbors is not None:
        for neighbor, weight in neighbors:
            if neighbor not in current_path:
                traverseGraph(
                    neighbor,
                    end_node,
                    current_path + [neighbor],
                    current_cost + weight,
                    graph
                )

def main():
    print("\t\tWelcome to the CI Lab Ex 2 - Informed Search Techniques")
    graph = Graph()
    test_graph_created = False
    
    while True:
        print("--------------------------------")
        print("\tMAIN MENU")
        print("--------------------------------")
        print("1. Create Test Graph")
        print("2. Input a Directed Graph")
        print("3. Add New Node")
        print("4. Add New Edge")
        print("5. Print Directed Graph Info")
        print("6. Get Neighbors of a Node")
        print("7. A* Algorithm")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        print()

        if choice == "1":
            if test_graph_created:
                print("Test graph already created.")
            else:
                graph.test_input_graph()
                test_graph_created = True
        elif choice == "2":
            graph.initialize()
        elif choice == "3":
            dna_seq = input("Enter the DNA sequence to add to the graph: ")
            heuristic = int(input("Enter the heuristic value for the DNA sequence: "))
            graph.add_node(dna_seq, heuristic)
        elif choice == "4":
            src_node = input("Enter the source DNA sequence to add the edge from: ")
            dest_node = input("Enter the destination DNA sequence to add the edge to: ")
            similarity = int(input("Enter the similarity value between {} and {} to add: ".format(src_node, dest_node)))
            graph.add_edge(src_node, dest_node, similarity)
        elif choice == "5":
            graph.print_graph()
        elif choice == "6":
            node = input("Enter the DNA sequence to get the neighbors of: ")
            neighbors = graph.get_neighbors(node)
            if neighbors is not None:
                print("Neighbors of node {} are:".format(node))
                for neighbor, weight in neighbors:
                    print("Neighbor: {}, Similarity: {}".format(neighbor, weight))
            else:
                print("Node {} does not exist in the graph.".format(node))
        elif choice == "7":
            start_node = input("Enter the start DNA sequence: ")
            stop_node = input("Enter the goal DNA sequence: ")
            print("\nAll Possible Paths to reach {} from {} are:".format(stop_node, start_node))
            traverseGraph(start_node, stop_node, [start_node], 0, graph)

            print("\nThe optimal path through the A* algorithm is:")
            aStarAlgo(start_node, stop_node, graph)
        elif choice == "8":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
