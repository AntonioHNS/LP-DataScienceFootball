from sklearn.preprocessing import StandardScaler
from lib.functions import GenerateGameTable, getLastFiveRounds, GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.svm import SVC

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from lib.functions import GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import threading

jogos = GenerateGameTable()

#Treinando SVM
attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

clfSvc = SVC(kernel="rbf", degree=10)



clfRandomForest = RandomForestClassifier(n_jobs=2, random_state = 0)
clfRandomForest.fit(attribute_train, result_train)


clfMultiLayerPerceptron = MLPClassifier(
    hidden_layer_sizes=(30, 17, 9, 3), 
    solver="adam", learning_rate="adaptive", alpha=0.000015, learning_rate_init=0.001)
clfMultiLayerPerceptron.fit(attribute_train, result_train)


def predictMatch(init, exit, result, matches,  year, homeId, awayId, matchId, matchweek, clf):
    if init == exit:
        print(homeId, awayId, result.count(2),result.count(1), result.count(0))
        return result.count(2),result.count(1), result.count(0)
    rodadaDataFrame = getLastFiveRounds(matches, year, homeId, awayId, matchId, matchweek)
    print(rodadaDataFrame)
    forecast = clf.predict(rodadaDataFrame)
    result.append(forecast[0])
    init+=1
    
    return predictMatch(init, exit,result, matches,  year, homeId, awayId, matchId, matchweek, clf)


x1 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 3131217581, 3657292249, 12, 35, clfMultiLayerPerceptron), daemon=True )
'''x2 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 1870536451, 1596141233, 12, 35, clfMultiLayerPerceptron), daemon=True )
x3 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 1596141233, 95417625, 12, 35, clfMultiLayerPerceptron), daemon=True )
x4 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 95417625, 1596141233, 12, 35, clfMultiLayerPerceptron), daemon=True )
x5 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 1596141233, 95417625, 12, 35, clfMultiLayerPerceptron), daemon=True )
x6 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 1596141233, 95417625, 12, 35, clfMultiLayerPerceptron), daemon=True )
x7 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 95417625, 1596141233, 12, 35, clfMultiLayerPerceptron), daemon=True )
x8 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 1596141233, 95417625, 12, 35, clfMultiLayerPerceptron), daemon=True )
x9 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 95417625, 1596141233, 12, 35, clfMultiLayerPerceptron), daemon=True )
x10 = threading.Thread(target=predictMatch, args=(0, 100, [], jogos, 2019, 1596141233, 95417625, 12, 35, clfMultiLayerPerceptron), daemon=True )


x2.start()
x3.start()
x4.start()
x5.start()
x6.start()
x7.start()
x8.start()
x9.start()
x10.start()'''
x1.start()


