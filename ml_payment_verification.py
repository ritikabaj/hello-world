import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

X_train = X_train.reshape(len(X_train), -1)
X_test = X_test.reshape(len(X_test), -1)



svm_classifier = svm.SVC(C=1)
svm_classifier.fit(X_train, y_train)


y_pred = svm_classifier.predict(X_test)

accuracy = print("Accuracy:" + accuracy_score(y_test, y_pred))
