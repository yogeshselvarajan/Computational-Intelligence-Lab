# Ensemble Classifier using Decision Trees and Random Forest

This code demonstrates building an ensemble classifier by utilizing individual Decision Trees and a Random Forest Classifier.

## Methodology

### Individual Decision Trees
- The code creates multiple Decision Trees by performing bootstrap sampling on the given dataset.
- Bootstrap sampling generates random subsets of the data for each Decision Tree.
- Categorical columns in the dataset are label-encoded for processing.
- For each split, the code trains an individual Decision Tree on the respective sampled data.
- The accuracy for each individual Decision Tree is calculated and displayed.

### Random Forest Classifier
- The code constructs a Random Forest Classifier using the previously trained individual Decision Trees.
- The number of estimators for the Random Forest equals the number of splits/individual Decision Trees.
- The Random Forest Classifier is fitted using the training data.

### Evaluation
- The Random Forest Classifier makes predictions on the test dataset.
- Accuracy is calculated for the Random Forest Classifier.
- A confusion matrix is generated to assess the performance of the Random Forest.

## File Overview

- `EnsembleClassifier.py`: Python code implementing the ensemble classifier.
- `README.md`: Documentation providing an overview of the ensemble classifier code.

## Usage

### Running the Code
- The code can be executed to build individual Decision Trees and create a Random Forest Classifier.
- The user can input the number of splits to create individual Decision Trees.

### Implementation Details
- The code reads a dataset from a Google Drive link and utilizes it to build the ensemble classifier.
- Categorical columns are label-encoded, and the dataset is split into training and test sets for evaluation.

### Results
- The code displays the accuracy for each individual Decision Tree and the overall accuracy for the Random Forest Classifier.
- The confusion matrix provides insights into the performance of the Random Forest.

## Summary

The provided code showcases the creation of an ensemble classifier by training individual Decision Trees using bootstrapped random subsets of the given dataset. It then assembles these trees into a Random Forest Classifier, demonstrating the power of ensemble learning in classification tasks.
