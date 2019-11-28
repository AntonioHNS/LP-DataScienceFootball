from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from lib.functions import GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

recursoes = 150

attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

clfDummy = DummyClassifier()

clfNaiveBayes = GaussianNB()

clfAdaBoost = AdaBoostClassifier(n_estimators=200)

clfGradient = GradientBoostingClassifier()
clfGradient.fit(attribute_train, result_train)
forecast = clfGradient.predict(attribute_test)

classificationReport = classification_report(result_test, forecast)
print(classificationReport)

clfDecisionTree = DecisionTreeClassifier(
    random_state=0, max_depth=20, max_leaf_nodes=3, criterion="entropy", splitter="random")

clfRandomForest = RandomForestClassifier(n_jobs=2, random_state = 0)

clfSvc = SVC(kernel="rbf", degree=10)
clfSvc.fit(attribute_train, result_train)
forecast1 = clfSvc.predict(attribute_test)

classificationReport1 = classification_report(result_test, forecast1)
print(classificationReport1)

clfMultiLayerPerceptron = MLPClassifier(
    hidden_layer_sizes=(30, 17, 9, 3), 
    solver="adam", learning_rate="adaptive", alpha=0.000015, learning_rate_init=0.001)

#meanDummy, medianDummy = getMeanMedianAccuracyPredict(0, recursoes, [], clfDummy, attribute_train, attribute_test, result_train, result_test)
#meanNaive, medianNaive = getMeanMedianAccuracyPredict(0, recursoes, [], clfNaiveBayes, attribute_train, attribute_test, result_train, result_test)
#meanAdaBoost, medianAdaBoost = getMeanMedianAccuracyPredict(0, recursoes, [], clfAdaBoost, attribute_train, attribute_test, result_train, result_test)
meanGradient, medianGradient = getMeanMedianAccuracyPredict(0, recursoes, [], clfGradient, attribute_train, attribute_test, result_train, result_test)
#meanDecisionTree, medianDecisionTree = getMeanMedianAccuracyPredict(0, recursoes, [], clfDecisionTree, attribute_train, attribute_test, result_train, result_test)
meanRandomForest, medianRandomForest = getMeanMedianAccuracyPredict(0, recursoes, [], clfRandomForest, attribute_train, attribute_test, result_train, result_test)
meanSvc, medianSvc = getMeanMedianAccuracyPredict(0, recursoes, [], clfSvc, attribute_train, attribute_test, result_train, result_test)
meanMultiLayer, medianMultiLayer = getMeanMedianAccuracyPredict(0, recursoes, [], clfMultiLayerPerceptron, attribute_train, attribute_test, result_train, result_test)

#means = [meanDummy, meanNaive, meanAdaBoost, meanGradient, meanDecisionTree, meanRandomForest, meanSvc, meanMultiLayer]
means = [meanGradient, meanRandomForest, meanSvc, meanMultiLayer]
#medians = [medianDummy, medianNaive, medianAdaBoost, medianGradient, medianDecisionTree, medianRandomForest, medianSvc, medianMultiLayer]
algorithms = ["GradientBoosting", "Random Forest", "SVM", "Multilayer Perceptron"]

print(means)

arq = open("medias.txt", "a")

arq.write("Teste 4" + "\n")

arq.write("GradientBoosting " + str(means[0]) + "\n")
arq.write("Random Forest " + str(means[1]) + "\n")
arq.write("SVM " + str(means[2]) + "\n")
arq.write("Multilayer Perceptron " + str(means[3]) + "\n")

#print(medians)

df = pd.DataFrame({'Medias': means}, index=algorithms)
#df = pd.DataFrame({'Medias': means, 'Medianas': medians}, index=algorithms)

ax1 = df["Medias"].plot.bar(rot=0, color=['purple', 'blue', 'green', 'red'])
ax1.yaxis.label.set_color('blue')
plt.ylim(0, 100)
plt.ylabel("Acurácia Média")
plt.title("Comparação dos Algoritmos em 150 testes")
plt.show()

# ax2 = df["Medianas"].plot.bar(rot=0, color=['gray', 'black', 'green', 'red', 'brown', 'purple', 'cyan', 'blue'])
# ax2.yaxis.label.set_color('blue')
# plt.ylim(0, 100)
# plt.ylabel("Acurácia Mediana")
# plt.title("Comparação dos Algoritmos em 150 testes")
# plt.show()
