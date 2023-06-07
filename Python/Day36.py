from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification


# Create custom dataset
X, y = make_classification(n_samples=800, n_features=10, n_informative=5, n_redundant=0, random_stte=42)


# Split dataset into training and testion sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Implement forward feature selection
selected_features = []
for i in range(X_train.shape[1]):
    best_accuracy = 0
    best_feature = None
    for j in range(X_train.shape[1]):
        if j not in selected_features:
            features = selected_features + [j]
            model = LogisticRegression()
            model.fit(X_train[:, features], y_train)
            accuracy = model.score(X_test[:, features], y_test)
            if accuracy> best_accuracy:
                best_accuracy = accuracy
                best_feature = j
    selected_features.append(best_feature)
    print("Selected Featues (Forward):", selected_features, "Score:", accuracy)
            
    