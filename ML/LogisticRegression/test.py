#  Copyright (c) 2021. Oskar "Bocian" Możdżeń
#  All rights reserved.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from main import LogisticRegression

bc = load_breast_cancer()
X, y = bc.data, bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

def accuracy(y_true, y_pred):
    acc = np.sum(y_true == y_pred) / len(y_true)
    return acc

regressor = LogisticRegression(lr=0.0001, n_iters=1000)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)

print(f"LR classification accuracy: {accuracy(y_test, predictions)}")
