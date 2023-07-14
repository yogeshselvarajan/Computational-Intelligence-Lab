import pandas as pd 

class Graph:
    def __init__(self):
        self.graph = {}
        self.heuristics = {}

    @staticmethod
    def initialise_base_graph():
        g = Graph()

        # Get the total number of nucleotide sequences
        total_sequences = int(input("Enter the total number of nucleotide sequences: "))

        # Get nucleotide sequences and their heuristic values
        for i in range(total_sequences):
            while True:
                try:
                    nucleotide_seq, heuristic = input("Enter nucleotide {0} and its heuristic value (separated by space): ".format(i+1)).split()
                    heuristic = float(heuristic)

                    # Check if nucleotide sequence is valid
                    valid = True
                    if not all(nucleotide in ['A', 'T', 'C', 'G'] for nucleotide in nucleotide_seq):
                     print("Invalid nucleotide sequence. Please enter a sequence using only A, T, C, or G.")
                     valid = False
                    elif 'A' in nucleotide_seq and 'T' not in nucleotide_seq:
                         print("Invalid nucleotide sequence. A must be paired with T.")
                         valid = False
                    elif 'T' in nucleotide_seq and 'A' not in nucleotide_seq:
                         print("Invalid nucleotide sequence. T must be paired with A.")
                         valid = False
                    elif 'C' in nucleotide_seq and 'G' not in nucleotide_seq:
                         print("Invalid nucleotide sequence. C must be paired with G.")
                         valid = False
                    elif 'G' in nucleotide_seq and 'C' not in nucleotide_seq:
                         print("Invalid nucleotide sequence. G must be paired with C.")
                         valid = False

                    if valid:
                     # Add nucleotide sequence and heuristic to the graph
                        g.add_node(nucleotide_seq, heuristic)
                        break

                except ValueError:
                    print("Invalid input. Please enter a valid nucleotide and its heuristic value.")

        # Get the number of similarity edges
        total_edges = int(input("Enter the number of similarity edges: "))

        # Get similarity edges
        for i in range(total_edges):
            while True:
                try:
                    src, dest, similarity = input("Edge {0}: Enter source, destination, and similarity (separated by space): ".format(i+1)).split()
                    similarity = float(similarity)

                    # Check if similarity is valid
                    if not (0 <= similarity <= 1):
                        print("Similarity should be between 0 and 1.")
                    else:
                        # Add similarity edge to the graph
                        g.add_edge(src, dest, similarity)
                    break

                except ValueError:
                    print("Invalid input. Please enter a valid source, destination, and similarity.")

        return g

    def add_node(self, nucleotide, heuristic):
        if nucleotide in self.graph:
            print("Nucleotide already exists in the graph.")
        else:
            self.graph[nucleotide] = {}
            self.heuristics[nucleotide] = heuristic

    def add_edge(self, source, destination, similarity):
        if source not in self.graph:
            print("Source nucleotide does not exist in the graph. Please enter a valid nucleotide.")
            return
        if destination not in self.graph:
            print("Destination nucleotide does not exist in the graph. Please enter a valid nucleotide.")
            return

        try:
            similarity = float(similarity)
            if 0 <= similarity <= 1:
                self.graph[source][destination] = similarity
                self.graph[destination][source] = similarity
            else:
                print("Similarity value should be between 0 and 1. Please enter a valid similarity.")
        except ValueError:
            print("Similarity should be a numeric value. Please enter a valid similarity.")

    def get_heuristic(self, nucleotide):
        if nucleotide in self.heuristics:
            return self.heuristics[nucleotide]
        else:
            print("Nucleotide not found in the graph.")
            return None

    def get_similarity(self, source, destination):
        if source in self.graph and destination in self.graph[source]:
            return self.graph[source][destination]
        else:
            print("Edge not found in the graph.")
            return None

    

    def print_adjacency_list(self):
        data = {
            'Parent Nucleotide': [],
            "Node's Heuristic Value": [],
            'Child Nodes': [],
            'Similarity Measure': []
        }

        for nucleotide, neighbors in self.graph.items():
            data['Parent Nucleotide'].append(nucleotide)
            data["Node's Heuristic Value"].append(self.get_heuristic(nucleotide))
            data['Child Nodes'].append(', '.join(neighbors.keys()))
            data['Similarity Measure'].append(', '.join(str(similarity) for similarity in neighbors.values()))

        df = pd.DataFrame(data)
        df.index += 1
        print(df)


def main():
    base_graph = None

    while True:
        print("\n----- Menu -----")
        print("1. Input base graph")
        print("2. Add Extra Nucleotide Node")
        print("3. Add Extra Similarity Edge")
        print("4. Print the whole DNA Sequence Graph")
        print("5. Exit")

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
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).")


if __name__ == "__main__":
    main()
