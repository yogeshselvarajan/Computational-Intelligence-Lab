import random

class WumpusWorldSolver:
    def __init__(self, size, pits, wumpus, gold, start):
        self.size = size
        self.pits = pits
        self.wumpus = wumpus
        self.gold = gold
        self.start = start
        self.current_location = start
        self.visited = set()
        self.perceptions = {
            "breeze": False,
            "stench": False
        }

    def is_valid_location(self, location):
        x, y = location
        return 1 <= x <= self.size and 1 <= y <= self.size

    def is_safe_location(self, location):
        return (
            self.is_valid_location(location)
            and location not in self.pits
            and location != self.wumpus
        )

    def move(self, location):
        self.current_location = location
        self.visited.add(location)

    def update_perceptions(self):
        self.perceptions = {
            "breeze": self.current_location in self.adjacent_to_pits(),
            "stench":  self.current_location in self.adjacent_to_wumpus()
        }

    def adjacent_to_pits(self):
        adjacent_cells = [
            (self.current_location[0] + 1, self.current_location[1]),
            (self.current_location[0] - 1, self.current_location[1]),
            (self.current_location[0], self.current_location[1] + 1),
            (self.current_location[0], self.current_location[1] - 1)
        ]
        return [cell for cell in adjacent_cells if self.is_valid_location(cell) ]

    def adjacent_to_wumpus(self):
        adjacent_cells = [
            (self.wumpus[0] + 1, self.wumpus[1]),
            (self.wumpus[0] - 1, self.wumpus[1]),
            (self.wumpus[0], self.wumpus[1] + 1),
            (self.wumpus[0], self.wumpus[1] - 1)
        ]
        return [cell for cell in adjacent_cells if self.is_valid_location(cell)]
     
    def print_first_move(self):
        print("Initial state:")
        self.print_state()

        possible_moves = [
            (self.current_location[0] + 1, self.current_location[1]),
            (self.current_location[0] - 1, self.current_location[1]),
            (self.current_location[0], self.current_location[1] + 1),
            (self.current_location[0], self.current_location[1] - 1),
        ]

        valid_moves = [move for move in possible_moves if self.is_safe_location(move) and move not in self.visited]

        if valid_moves:
            print("\nFirst move:")
            print(f"Move 1: Agent moves from {self.current_location} to {valid_moves[0]}.")
        else:
            print("\nStuck! No safe moves.")


    def solve(self):
        moves = 0
        print("Initial state:")
        self.print_state()

        while self.current_location != self.gold:
            moves += 1
            possible_moves = [
                (self.current_location[0] + 1, self.current_location[1]),
                (self.current_location[0] - 1, self.current_location[1]),
                (self.current_location[0], self.current_location[1] + 1),
                (self.current_location[0], self.current_location[1] - 1),
            ]
            valid_moves = [move for move in possible_moves if self.is_safe_location(move) and move not in self.visited]

            if valid_moves:
                self.move(valid_moves[0])
                self.update_perceptions()

                print(f"\nMove {moves}:")
                self.print_state()
            else:
                print("\nStuck! No safe moves.")
                break

        if self.current_location == self.gold:
            print("\nFound gold in", moves, "moves.")
        else:
            print("\nGold could not be found.")

        print("\nFinal score:", self.score)

    def print_state(self):
     for i in range(self.size, 0, -1):
        row = []
        for j in range(1, self.size + 1):
            location = (i, j)
            cell_representation = ""
            if location == self.current_location:
                cell_representation += "A"  # Agent's current position
            if location in self.pits:
                cell_representation += "P"  # Pit
            if location == self.wumpus:
                cell_representation += "W"  # Wumpus
            if location == self.gold:
                cell_representation += "G"  # Gold
            if location in self.visited:
                cell_representation += "."  # Visited empty cell
            if "breeze" in self.perceptions and self.perceptions["breeze"]:
                cell_representation += "B"  # Breeze
            if "stench" in self.perceptions and self.perceptions["stench"]:
                cell_representation += "S"  # Stench

            # Check if there are characters already on the grid
            if len(cell_representation) == 0:
                cell_representation = "-"  # Unvisited empty cell

            row.append(cell_representation.center(4))
        print(" ".join(row))
     print("Current Location:", self.current_location)
     print("Score:", self.score)

def random_test_case():
    size = 4
    num_pits = random.randint(1, size)  # Generate random number of pits
    pits = [(random.randint(1, size), random.randint(1, size)) for _ in range(num_pits)]

    wumpus = (random.randint(1, size), random.randint(1, size))
    gold = (random.randint(1, size), random.randint(1, size))

    start = (1, 1)  # Start position remains fixed at (1, 1)

    # Create a WumpusWorldSolver instance and solve the problem
    solver = WumpusWorldSolver(size, pits, wumpus, gold, start)
    solver.solve()

# Call the random test case method to solve with randomly generated positions
random_test_case()

def classical_test_case():
    size = 4
    pits = [(1, 3), (3, 3), (4, 4)]
    wumpus = (1, 3)
    gold = (3, 2)
    start = (1, 1)

    # Create a WumpusWorldSolver instance and solve the problem
    solver = WumpusWorldSolver(size, pits, wumpus, gold, start)
    solver.solve()

# Call the method to test the no safe path scenario
classical_test_case()  