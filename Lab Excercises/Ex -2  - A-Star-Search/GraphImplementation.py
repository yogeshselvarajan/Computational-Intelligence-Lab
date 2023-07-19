import pandas as pd

class DirectedGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def initialize(self):
        num_nodes = int(input("Enter the total number of DNA sequences in the graph: "))
        num_edges = int(input("Enter the total number of similarity connections in the graph: "))
        print()

        for i in range(num_nodes):
            try:
                sequence, heuristic = input("Enter DNA sequence {} and its heuristic value: ".format(i + 1)).split()
                self.add_node(sequence, int(heuristic))
            except ValueError:
                print("Invalid input! Please enter both the DNA sequence and its heuristic value.")
                

        print()

        for i in range(num_edges):
            try:
                src, dest, similarity = input("Similarity connection {} - Enter source, destination, and similarity info: ".format(i + 1)).split()
                self.add_edge(src, dest, int(similarity))
            except ValueError:
                print("Invalid input. Please enter the source, destination, and similarity value.")

    def add_node(self, sequence, heuristic):
        self.nodes[sequence] = heuristic
        print("DNA sequence {} added with heuristic value {}".format(sequence, heuristic))

    def add_edge(self, src, dest, similarity):
        if src in self.nodes and dest in self.nodes:
            if src not in self.edges:
                self.edges[src] = []
            self.edges[src].append((dest, similarity))
            print("Similarity connection added from {} to {} with similarity {}".format(src, dest, similarity))
        else:
            print("Both source and destination nodes must exist in the graph.")

    def print_graph(self):
        data = {'Source Sequence': [], 'H(Parent)': [], 'Destination Sequences': []}

        for source, heuristic in self.nodes.items():
            if source in self.edges:
                destinations = self.edges[source]
                dest_str = ', '.join(f'{dest} ({similarity})' for dest, similarity in destinations)
            else:
                dest_str = '-'

            data['Source Sequence'].append(source)
            data['H(Parent)'].append(heuristic)
            data['Destination Sequences'].append(dest_str)

        df = pd.DataFrame(data)
        df.index = range(1, len(df) + 1)
        print("\nThe DNA Sequence Similarity Graph Setup is as follows:\n")
        print(df)

    def get_neighbors(self, sequence):
        if sequence in self.nodes:
            return self.edges.get(sequence, [])
        else:
            return None
        
    def test_input_graph(self):
        self.add_node('AGT', 13)
        self.add_node('TTC', 12)
        self.add_node('GAC', 10)
        self.add_node('ACG', 15)
        self.add_node('TGC', 9)
        self.add_node('CTG', 6)
        self.add_node('TAC', 3)
        self.add_node('AGC', 7)
        self.add_node('GCT', 7)
        self.add_node('CTA', 0)

        self.add_edge('AGT', 'TTC', 5)
        self.add_edge('AGT', 'GAC', 2)
        self.add_edge('AGT', 'ACG', 4)
        self.add_edge('TTC', 'TGC', 9)
        self.add_edge('TTC', 'CTG', 4)
        self.add_edge('GAC', 'TAC', 7)
        self.add_edge('ACG', 'AGC', 6)
        self.add_edge('AGC', 'TAC', 6)
        self.add_edge('CTG', 'TAC', 3)
        self.add_edge('TGC', 'GCT', 2)
        self.add_edge('GCT', 'CTG', 1)
        self.add_edge('TAC', 'CTA', 2)
        self.add_edge('AGC', 'CTA', 3)
