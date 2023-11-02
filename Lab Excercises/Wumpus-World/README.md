# Wumpus World Solver

This repository contains a Python implementation to solve the Wumpus World problem. The Wumpus World is a classic AI problem that simulates an environment where an agent must navigate through a cave to find gold while avoiding pitfalls (pits) and a dangerous Wumpus creature.

## Wumpus World Problem

The Wumpus World is represented as a cave with pits, a Wumpus creature, gold, and an agent navigating through the cave. The key elements include:

- **Pits:** Deadly locations the agent must avoid falling into.
- **Wumpus:** A dangerous creature that can kill the agent.
- **Gold:** The goal of the agent is to find the gold.
- **Agent:** The player navigating the cave, avoiding dangers, and seeking the gold.

## Features

The Wumpus World Solver contains the following features:

### Initialization
- The environment size, locations of pits, Wumpus, gold, and the starting position of the agent are set upon initialization.

### Movement
- The agent can move around the cave, avoiding pits and the Wumpus.
- The solver attempts to reach the gold while considering the agent's safety.

### Perception Update
- The agent receives perceptions such as breeze and stench based on the surrounding locations (indicating nearby pits or the Wumpus).

### Printing the Environment State
- Displays the current state of the environment, including the agent's location, pit locations, Wumpus location, gold location, visited cells, and perceptions (breeze and stench).

### Solving the Wumpus World
- The solver navigates the environment to reach the gold while avoiding pits and the Wumpus.
- It provides information about the number of moves taken and if the gold was found.

### Random Test Case
- Generates random positions for pits, the Wumpus, and gold, and then solves the Wumpus World using these positions.

### Classical Test Case
- Solves a predefined scenario to demonstrate a no-safe-path scenario in the Wumpus World.

## Instructions

### Running the Solver
- The solver can be executed by creating an instance of the `WumpusWorldSolver` class and providing the required parameters such as the environment size, pit locations, Wumpus location, gold location, and the agent's starting position.
- Utilize the `solve()` method to navigate the Wumpus World.

### Running Test Cases
- The `random_test_case()` and `classical_test_case()` methods allow running random and predefined scenarios, respectively, to test the solver in different environments.

## File Overview

- `WumpusWorldSolver.py`: Python code containing the Wumpus World Solver.
- `README.md`: Documentation providing an overview of the Wumpus World problem and the functionality of the Wumpus World Solver.

## Summary

The Wumpus World Solver demonstrates an agent's navigation through a cave-like environment, seeking the gold while avoiding pits and the Wumpus. The code provides functionalities to solve random and predefined scenarios in the Wumpus World.

