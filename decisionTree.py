from sklearn.datasets import load_iris
from sklearn import tree
from lib.functions import GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import numpy as np


attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

clf = tree.DecisionTreeClassifier(random_state=0, max_depth=2, max_leaf_nodes=3)

mean, median = getMeanMedianAccuracyPredict(0, 500, [], clf, attribute_train, attribute_test, result_train, result_test)
print("Median Accuracy: " + str(median))
print("Mean Accuracy: " + str(mean))

