class Perceptron:
    def __init__(self, gate_type, activation_type, initial_weights, initial_bias, learning_rate, max_epochs):
        self.gate_type = gate_type.lower()
        self.activation_type = activation_type.lower()
        self.initial_weights = initial_weights.copy()
        self.initial_bias = initial_bias
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs

        self.truth_tables = {
            "and": {
                "binary": {"inputs": [[0, 0], [0, 1], [1, 0], [1, 1]], "targets": [0, 0, 0, 1]},
                "bipolar": {"inputs": [[-1, -1], [-1, 1], [1, -1], [1, 1]], "targets": [-1, -1, -1, 1]}
            },
            "or": {
                "binary": {"inputs": [[0, 0], [0, 1], [1, 0], [1, 1]], "targets": [0, 1, 1, 1]},
                "bipolar": {"inputs": [[-1, -1], [-1, 1], [1, -1], [1, 1]], "targets": [-1, 1, 1, 1]}
            },
            "xor": {
                "binary": {"inputs": [[0, 0], [0, 1], [1, 0], [1, 1]], "targets": [0, 1, 1, 0]},
                "bipolar": {"inputs": [[-1, -1], [-1, 1], [1, -1], [1, 1]], "targets": [-1, 1, 1, -1]}
            },
            "nand": {
                "binary": {"inputs": [[0, 0], [0, 1], [1, 0], [1, 1]], "targets": [1, 1, 1, 0]},
                "bipolar": {"inputs": [[-1, -1], [-1, 1], [1, -1], [1, 1]], "targets": [1, 1, 1, -1]}
            }
        }

    def calculateYin(self, inputs, weights, bias):
        return sum(x * w for x, w in zip(inputs, weights)) + bias

    def applyActivation(self, yin):
        return 1 if (yin > 0) else (0 if self.activation_type == "binary" else -1)

    def updateWeightsBias(self, inputs, weights, bias, error):
        new_weights = [w + self.learning_rate * x * error for x, w in zip(inputs, weights)]
        new_bias = bias + self.learning_rate * error
        return new_weights, new_bias

        def train(self):
            table = self.truth_tables[self.gate_type][self.activation_type]
            inputs, targets = table["inputs"], table["targets"]
            weights, bias = self.initial_weights.copy(), self.initial_bias

            for epoch in range(self.max_epochs):
                changesCount = 0
                print("Epoch:", epoch + 1)
                for i in range(len(inputs)):
                    yin = self.calculateYin(inputs[i], weights, bias)
                    y = self.applyActivation(yin)
                    error = targets[i] - y

                    print(f"Input: {inputs[i]}, Target: {targets[i]}")
                    print(f"Y_in: {yin}, Y_out: {y}")

                    if error != 0:
                        changesCount += 1
                        print(f"Before Update - Weights: {weights}, Bias: {bias}")
                        weights, bias = self.updateWeightsBias(inputs[i], weights, bias, error)
                        print(f"After Update - Weights: {weights}, Bias: {bias}")

                if changesCount == 0:
                    print("Training converged.")
                    return weights, bias
            print("Training stopped without convergence.")
            return weights, bias


def main():
    while True:
        gate_choice = input("Choose the gate type (AND, OR, XOR, NAND) or 'exit' to quit: ").lower()
        if gate_choice == 'exit':
            break
        activation_choice = input("Choose the activation function (Binary or Bipolar): ").lower()
        initial_weights = list(map(float, input("Enter initial weights (w1 w2): ").split()))
        initial_bias = float(input("Enter initial bias: "))
        learning_rate = float(input("Enter learning rate: "))
        max_epochs = 100

        perceptron = Perceptron(gate_choice, activation_choice, initial_weights, initial_bias, learning_rate, max_epochs)
        final_weights, final_bias = perceptron.train()

        print(f"Final weights: {final_weights}")
        print(f"Final bias: {final_bias}")

        try_again = input("Do you want to try another choice of perceptron? (yes/no): ").lower()
        if try_again != 'yes':
            print("Press Ctrl+C to exit the program.")
            break

if __name__ == "__main__":
    main()
