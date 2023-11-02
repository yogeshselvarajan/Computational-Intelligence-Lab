# ID3 Decision Tree Implementation

This repository contains an ID3 Decision Tree implementation that builds a decision tree to classify data based on the information gain criteria.

## Overview

The implemented ID3 Decision Tree algorithm constructs the decision tree by finding the best feature to split the dataset at each node. The information gain is calculated to determine the feature that best separates the data based on the entropy.

## Process

### 1. Initializing the Decision Tree
- The Decision Tree is built using the ID3 algorithm.
- The tree can be trained on a dataset, and the maximum depth of the tree can be set to control overfitting.

### 2. Training the Decision Tree
- The `fit` method builds the decision tree by finding the best splits at each node based on information gain.

### 3. Making Predictions
- The `predict` method is used to classify new samples based on the constructed decision tree.

### 4. Visualizing the Tree
- The `visualize_tree` method uses the Graphviz library to visualize the decision tree graphically.

## Files

- `ID3_Decision_Tree.ipynb`: Jupyter Notebook containing the ID3 Decision Tree implementation.
- `data1.csv`: Sample dataset used in the implementation.
- `README.md`: Documentation file providing an overview of the ID3 Decision Tree implementation.

## Instructions

### Running the Notebook
1. Ensure necessary libraries (pandas, math, collections, graphviz) are installed.
2. Open the `ID3_Decision_Tree.ipynb` Jupyter Notebook.
3. Run the notebook cells in sequence to observe the ID3 Decision Tree implementation and visualize the decision tree.

### Dataset Information
- The dataset provided (data1.csv) contains information about attributes such as 'Department', 'Age_Range', 'Salary_class', and the target variable 'Status'.

### Summary
The implemented ID3 Decision Tree serves as a tool for binary classification based on the information gain criteria. The decision tree construction process and classification based on the tree are depicted within the notebook.

