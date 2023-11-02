# K-Nearest Neighbors (K-NN) Implementation

This repository contains an implementation of the K-Nearest Neighbors (K-NN) algorithm and a comparison with the inbuilt K-NN model provided by scikit-learn.

## Dataset
The dataset used in this implementation contains both numerical and categorical columns. The categorical columns have been encoded using Label Encoding to prepare the data for the K-NN algorithm.

## Process

### 1. Encoding the Categorical Columns
The categorical columns in the dataset were encoded using Label Encoding for use in the K-NN algorithm.

### 2. Splitting the Dataset
The dataset was split into training and test sets with a test size of 30% to train and evaluate the models.

### 3. Feature Scaling
Standard Scaling was applied to the feature vectors to ensure all features contribute equally to the distance computations.

### 4. K-NN Algorithm Implementation

#### Custom KNN Class
A custom KNN class was developed, including:
- `fit`: Training the K-NN model with the training data.
- `predict`: Making predictions on the test set.
- `majority_vote`: Selecting the majority class among the k-nearest neighbors.

### 5. Comparison with Inbuilt K-NN Model

#### Inbuilt KNN Model
An inbuilt K-NN model provided by scikit-learn was trained and used to make predictions on the test set.

### 6. Evaluation
The evaluation involved predicting the test set results using both the custom K-NN model and the inbuilt K-NN model. The Confusion Matrix and Accuracy Scores were computed for both models.

## Files

- `KNN_Implementation.ipynb`: Jupyter Notebook containing the K-NN implementation and comparison with inbuilt K-NN model.
- `dataset.csv`: The dataset used for this implementation.
- `README.md`: Documentation file providing an overview of the implementation.

## Instructions

### Running the Notebook
1. Ensure the necessary libraries (numpy, pandas, scikit-learn) are installed.
2. Open the `KNN_Implementation.ipynb` Jupyter Notebook.
3. Run the notebook cells in sequence to observe the K-NN implementation and model comparison.

### Dataset Information
- The dataset provided contains information about various attributes and the target variable 'HeartDisease'.
- Columns such as 'Sex', 'ChestPainType', 'FastingBS', and others are part of the dataset.

### Summary
The K-NN implementation and comparison provide insights into the differences between the custom K-NN model and the inbuilt scikit-learn K-NN model.

