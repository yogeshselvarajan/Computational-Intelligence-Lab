# Perceptron Implementation for Logical Gates

The Perceptron code allows users to train a Perceptron model for different logical gates (AND, OR, XOR, NAND) with customizable configurations.

## Features

### Gate Types
- Supports logical gates: AND, OR, XOR, NAND.
- Each gate type operates under two activation function choices: Binary or Bipolar.

### Training and Configuration
- Users can input initial weights, initial bias, learning rate, and a maximum number of training epochs.
- Trains the Perceptron model on the chosen logical gate with specified configurations.

## Module Description

### `Perceptron` Class
- Utilizes perceptron architecture to simulate logical gates.
- Dynamically adjusts initial weights and biases for training on different gates.
- Employs binary or bipolar activation functions based on user selection.
- Conducts the training process, updating weights and bias until convergence or reaching the maximum epochs.

### `main()` Function
- Provides an interactive session to select gate type, activation function, and configure the Perceptron.
- Trains the Perceptron with user-defined parameters and displays the final weights and bias.
- Allows users to try another configuration or exit the program.

## Usage

1. Run the script `Perceptron.py`.
2. Choose the logical gate (AND, OR, XOR, NAND) and the desired activation function (Binary or Bipolar).
3. Input initial weights, initial bias, learning rate, and proceed to train the Perceptron.
4. View the final weights and bias obtained after training.
5. Choose to try another configuration or exit the program.

## Example Usage
- Select the logical gate and activation type.
- Define initial weights, bias, and learning rate for the Perceptron.
- Review the training process and observe the final weights and bias.

## Note
- The code allows a variety of gate types and activation functions.
- Use it to simulate and train Perceptrons for different logical gates.

