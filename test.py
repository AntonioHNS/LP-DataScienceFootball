from sklearn.preprocessing import StandardScaler
from lib.functions import GenerateGameTable, getLastFiveRounds, GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import threading

jogos = GenerateGameTable()

#Treinando SVM
attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

clfSvc = SVC(kernel="rbf", degree=10)
clfSvc.fit(attribute_train, result_train)

listToPredict = []

def addRoundToListPredict(matches, year, homeId, awayId, matchId, matchweek, clf):
    rodadaDataFrame = getLastFiveRounds(matches, year, homeId, awayId, matchId, matchweek)
    listToPredict.append(rodadaDataFrame.homeTeamId)

#
x1 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 3131217581, 3657292249, 12, 35), daemon=True )
#
x2 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1870536451, 1596141233, 12, 35), daemon=True )
x3 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1596141233, 95417625, 12, 35), daemon=True )
x4 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 95417625, 1596141233, 12, 35), daemon=True )
x5 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1596141233, 95417625, 12, 35), daemon=True )
x6 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1596141233, 95417625, 12, 35), daemon=True )
x7 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 95417625, 1596141233, 12, 35), daemon=True )
x8 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1596141233, 95417625, 12, 35), daemon=True )
x9 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 95417625, 1596141233, 12, 35), daemon=True )
x10 = threading.Thread(target=addRoundToListPredict, args=( jogos, 2019, 1596141233, 95417625, 12, 35), daemon=True )

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


print(listToPredict)