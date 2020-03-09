#!/usr/bin/python3

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### make sure you use // when dividing for integer division


#########################################################
### your code goes here ###

clf = SVC(C=10000, kernel='rbf')
# features_train = features_train[:len(features_train)//100]
# labels_train = labels_train[:len(labels_train)//100]
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = accuracy_score(pred, labels_test)
count = 0
for i in range(len(pred)):
    if pred[i] == 1:
        count += 1

print(count)

print(acc)


#########################################################


