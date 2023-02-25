import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn import svm
import os

Categories = ['Real','Fake']
flat_data = [] #input array 
target_output = [] #output array 
locationdata = '/Users/samyukthapugal/Documents/MLimages' #path to datasets
for i in Categories:
    path = os.path.join(locationdata,i)
    for img in os.listdir(path):
        images = imread(os.path.join(path,img)) #img_array
        image_resized = resize(images,(150,150,3)) #resized to a fixed size
        flat_data.append(image_resized.flatten()) 
        target_output.append(Categories.index(i))
        
flat_data = np.array(flat_data) ##array with all resized pictures
target_array = np.array(target_array) ##array with binary set

X = flat_data.reshape(len(flat_data), -1) #input data

np.unique(target_array) 
X.shape
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

#split the model
xtrain, xtest, ytrain, ytest = train_test_split(X, target_array, random_state=10,
                                               test_size=.20)

#train the model
svm_classifier = svm.SVC(C=1)
svm_classifier.fit(xtrain,ytrain)

# Perform prediction with the model
y_pred = svm_classifier.predict(xtest)
print(y_pred)

# Evaluate the accuracy of the model
accuracy = print("Accuracy:")
print(accuracy_score(ytest, y_pred))

#get ouput
image='/Users/samyukthapugal/Documents/MLimages' #just an example
y_pred = svm_classifier.predict(image)

if y_pred==1:
    print("Payment is real")
else:
    print("Payment is fake")