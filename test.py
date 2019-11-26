from sklearn.preprocessing import StandardScaler
from lib.functions import GenerateGameTable, getLastFiveRounds, GetTrainTest, getMeanMedianAccuracyPredict
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

jogos = GenerateGameTable()

#Para pegar o id dos times e testar
# print(jogos.homeTeamId.unique())

#Criando Rodada
rodadaDataFrame = getLastFiveRounds(jogos, 2019, 1596141233, 95417625, 12, 35)

#Treinando SVM
attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

clfSvc = SVC(kernel="rbf", degree=10)
clfSvc.fit(attribute_train, result_train)
# forecast1 = clfSvc.predict(attribute_test)
forecastTest = clfSvc.predict(rodadaDataFrame)

# classificationReport1 = classification_report(result_test, forecast1)

print(forecastTest)
