from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from lib.functions import GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

clfDummy = DummyClassifier()

clfNaiveBayes = GaussianNB()

clfAdaBoost = AdaBoostClassifier(n_estimators=200)

clfGradient = GradientBoostingClassifier()

clfDecisionTree = DecisionTreeClassifier(
    random_state=0, max_depth=20, max_leaf_nodes=3, criterion="entropy", splitter="random")

clfRandomForest = RandomForestClassifier(n_jobs=2, random_state = 0)

clfSvc = SVC(kernel="rbf", degree=10)

clfMultiLayerPerceptron = MLPClassifier(
    hidden_layer_sizes=(30, 17, 9, 3), 
    solver="adam", learning_rate="adaptive", alpha=0.000015, learning_rate_init=0.001)

meanDummy, medianDummy = getMeanMedianAccuracyPredict(0, 50, [], clfDummy, attribute_train, attribute_test, result_train, result_test)
meanNaive, medianNaive = getMeanMedianAccuracyPredict(0, 50, [], clfNaiveBayes, attribute_train, attribute_test, result_train, result_test)
meanAdaBoost, medianAdaBoost = getMeanMedianAccuracyPredict(0, 50, [], clfAdaBoost, attribute_train, attribute_test, result_train, result_test)
meanGradient, medianGradient = getMeanMedianAccuracyPredict(0, 50, [], clfGradient, attribute_train, attribute_test, result_train, result_test)
meanDecisionTree, medianDecisionTree = getMeanMedianAccuracyPredict(0, 50, [], clfDecisionTree, attribute_train, attribute_test, result_train, result_test)
meanRandomForest, medianRandomForest = getMeanMedianAccuracyPredict(0, 50, [], clfRandomForest, attribute_train, attribute_test, result_train, result_test)
meanSvc, medianSvc = getMeanMedianAccuracyPredict(0, 50, [], clfSvc, attribute_train, attribute_test, result_train, result_test)
meanMultiLayer, medianMultiLayer = getMeanMedianAccuracyPredict(0, 50, [], clfMultiLayerPerceptron, attribute_train, attribute_test, result_train, result_test)

means = [meanDummy, meanNaive, meanAdaBoost, meanGradient, meanDecisionTree, meanRandomForest, meanSvc, meanMultiLayer]
medians = [medianDummy, medianNaive, medianAdaBoost, medianGradient, medianDecisionTree, medianRandomForest, medianSvc, medianMultiLayer]
algorithms = ["DummyClassifier", "Naive Bayes", "AdaBoost", "GradientBoosting", "Decision Tree", "Random Forest", "SVM", "Multilayer Perceptron"]

df = pd.DataFrame({'Médias': means, 'Medianas': medians}, index=algorithms)

axes = df.plot.bar(rot=0, subplots=True)
# axes[1].legend(loc=2)
plt.show()