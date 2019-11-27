from sklearn.dummy import DummyClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from lib.functions import GenerateGameTable, getLastFiveRounds, GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import threading

jogos = GenerateGameTable()

# #Treinando SVM
# attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

# clfSvc = GradientBoostingClassifier()
# # clfSvc = SVC(kernel="rbf", degree=10)
# clfSvc.fit(attribute_train, result_train)

attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()


clfGradient = GradientBoostingClassifier(learning_rate=0.001, max_leaf_nodes=3, max_depth=20)
clfGradient.fit(attribute_train, result_train)

clfMLP = clfMultiLayerPerceptron = MLPClassifier(
    hidden_layer_sizes=(30, 17, 9, 3), 
    solver="adam", learning_rate="adaptive", alpha=0.000015, learning_rate_init=0.001)
clfMLP.fit(attribute_train, result_train)

clfRF = RandomForestClassifier(n_jobs=2, random_state = 0, max_depth=20, max_leaf_nodes=3)
clfRF.fit(attribute_train, result_train)

clfSvc = SVC(kernel="rbf", degree=10, C=10000)
clfSvc.fit(attribute_train, result_train)

predictsGradient = []
predictsSVM = []
predictsRandomForest = []
predictsMultiLayerPerceptron = []

def addRoundToListPredict(matches, year, homeId, awayId, matchId, matchweek):
    rodadaDataFrame = getLastFiveRounds(matches, year, homeId, awayId, matchId, matchweek)
    json1 = {"matchId": matchId, "value": clfGradient.predict(rodadaDataFrame)[0] }
    json2 = {"matchId": matchId, "value": clfMLP.predict(rodadaDataFrame)[0] }
    json3 = {"matchId": matchId, "value": clfRF.predict(rodadaDataFrame)[0] }
    json4 = {"matchId": matchId, "value": clfSvc.predict(rodadaDataFrame)[0] }
    predictsGradient.append(json1)
    predictsMultiLayerPerceptron.append(json2)
    predictsRandomForest.append(json3)
    predictsSVM.append(json4)

# Chapecoense x Botafogo
x1 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 3131217581, 3657292249, 1, 35), daemon=True )

# Internacional x Goiás
x2 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1870536451, 2026248140, 2, 35), daemon=True )

# Bahia x Atlético Mineiro
x3 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 360415214, 1110161204, 3, 35), daemon=True )

# Corinthians x Avaí
x4 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 3209350440, 4060423562, 4, 35), daemon=True )

# Athletico Paranaense x Grêmio
x5 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 546424345, 3584964355, 5, 35), daemon=True )

# Flamengo x Ceará
x6 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1670992046, 791895575, 6, 35), daemon=True )

# Fluminense x Palmeiras
x7 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 2228842524, 2883380601, 7, 35), daemon=True )

# Fortaleza x Santos
x8 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 2849024782, 1898730127, 8, 35), daemon=True )

# São Paulo x Vasco da Gama
x9 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1596141233, 2213895614, 9, 35), daemon=True )

# Cruzeiro x CSA
x10 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 67067627, 95417625, 10, 35), daemon=True )

x1.start()
x2.start()
x3.start()
x4.start()
x5.start()
x6.start()
x7.start()
x8.start()
x9.start()
x10.start()

while len(predictsGradient) < 10 and len(predictsMultiLayerPerceptron) < 10 and len(predictsRandomForest) < 10 and len(predictsSVM) < 10:
    print("Espere as threads terminarem...")

print("Gradient")
for algGR in predictsGradient:
    print(algGR)

print("MultiLayerPerceptron")
for algGR in predictsMultiLayerPerceptron:
    print(algGR)

print("Random Forest")
for algGR in predictsRandomForest:
    print(algGR)

print("SVM")
for algGR in predictsSVM:
    print(algGR)