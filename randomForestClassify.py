from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from lib.functions import GetTrainTest, getMeanMedianAccuracyPredict

import numpy as np

trainTest, columnsArray = GetTrainTest()

def returnPercentage(value):
    return value*100

attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]
clf = RandomForestClassifier(n_jobs=2, random_state = 0)

mean, median = getMeanMedianAccuracyPredict(0, 500, [], clf, attribute_train, attribute_test, result_train, result_test)
print("Median Accuracy: " + str(median))
print("Mean Accuracy: " + str(mean))

