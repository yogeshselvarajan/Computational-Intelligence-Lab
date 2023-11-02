import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""## Importing the dataset"""

# Replace 'file_id' with the file ID you extracted from the sharing link
file_id = '1Gb3AiXXEKhkaZZtIXxqcV0jIdVckcrLB'

# Construct the direct download link for the CSV file
download_link = f'https://drive.google.com/uc?id={file_id}'

# Read the CSV file into a DataFrame
dataset = pd.read_csv(download_link)

dataset

"""## Encoding the Categorical columns"""

# Categorical columns
categorical_columns = ['Sex', 'ChestPainType', 'FastingBS', 'RestingECG', 'ExerciseAngina', 'ST_Slope', 'HeartDisease']

# Apply label encoding
label_encoder = LabelEncoder()
for col in categorical_columns:
    dataset[col] = label_encoder.fit_transform(dataset[col])

# Convert all columns to integers (except 'Age' and 'Cholesterol' which are already integers)
dataset = dataset.astype(int)
dataset

# Now 'dataset' contains the preprocessed data with all columns as integers.
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""## Splitting the dataset into the Training set and Test set"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30,random_state = 42)

"""## Feature Scaling"""

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) #avoid data leakage

"""## Training the K-NN model on the Training set"""

from math import sqrt

class KNN():
    def __init__(self, k):
        self.k = k

    def fit(self, X_train, y_train):
        self.x_train = X_train
        self.y_train = y_train

    def calculate_euclidean(self, sample1, sample2):
        distance = np.sqrt(np.sum((sample1 - sample2)**2))
        return distance

    def nearest_neighbors(self, test_sample):
        distances = []
        for i in range(len(self.x_train)):
            distance = self.calculate_euclidean(self.x_train[i], test_sample)
            distances.append((self.y_train[i], distance))
        distances.sort(key=lambda x: x[1])
        return distances

    def predict(self, test_set):
        predictions = []
        for test_sample in test_set:
            neighbors = self.nearest_neighbors(test_sample)
            k_nearest_labels = [neighbor[0] for neighbor in neighbors[:self.k]]
            predictions.append((k_nearest_labels, neighbors[:self.k]))
        return predictions


    def majority_vote(self, predictions):
        counts = {}
        for labels, _ in predictions:
            for label in labels:
                if label in counts:
                    counts[label] += 1
                else:
                    counts[label] = 1
        max_label = max(counts, key=counts.get)
        return max_label

# Using our modified KNN model
model = KNN(25)
model.fit(X_train, y_train)

# Training the inbuilt K-NN model on the Training set
knn_classifier = KNeighborsClassifier(n_neighbors=25, p=2)
knn_classifier.fit(X_train, y_train)

"""## Predicting the Test set results

### a) Using the KNN Implemented Class
"""

predictions = model.predict(X_test)  # our model's predictions
print(predictions)

print("The majority class : ", model.majority_vote(predictions))

"""### b) Using the Inbuild KNN Class from sklearn"""

# Predicting the Test set results using inbuilt K-NN model
pred_knn_classifier = knn_classifier.predict(X_test)

"""## Making the Confusion Matrix to compare both models"""

# Extracting the k-nearest labels from the predictions
y_pred_custom_knn = [pred[0][0] for pred in predictions]

# Printing the confusion matrix and accuracy for our custom KNN model
cm_custom_knn = confusion_matrix(y_test, y_pred_custom_knn)
accuracy_custom_knn = accuracy_score(y_test, y_pred_custom_knn)

print("Confusion Matrix for Custom K-NN Model:")
print(cm_custom_knn)
print("Accuracy for Custom K-NN Model:", accuracy_custom_knn)

# Calculating accuracy and confusion matrix for inbuilt K-NN model
accuracy_knn_classifier = accuracy_score(y_test, pred_knn_classifier)
cm_knn_classifier = confusion_matrix(y_test, pred_knn_classifier)

# Printing the accuracy and confusion matrix for inbuilt K-NN model
print("Accuracy for inbuilt K-NN Model:", accuracy_knn_classifier)
print("Confusion Matrix for inbuilt K-NN Model:")
print(cm_knn_classifier)