from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import math

#Variables
path_base = "C:/Users/filip/PycharmProjects/learn-pandas/"
campeonato = "-Match-PremierLeague"
ano = "2018-2019"
top = 28
floor = 10
rounds = 38
column = "correctPassing"
nameTeam = "Liverpool"


dataFrame = pd.read_csv(path_base + ano + campeonato + ".csv", encoding="UTF-8", sep='\t')

data            = dataFrame.loc[dataFrame.nameTeam == nameTeam]
print(data.teamId)
dataPrev        = list(data.tail(10)[column].values)
tdata           = list(data.head(top)[column].values)
indexsToPredict = list(data.tail(floor).matchWeek.values)

#Functions
def Predict(indice):
    trainingData = data.head(indice)
    trainingList = list(trainingData[column].values)
    model = ARIMA(trainingList, order=(1, 1, 1))
    model_fit = model.fit(disp=False)
    # make prediction
    predict_value = model_fit.predict(len(trainingList), len(trainingList), typ='levels')
    value = math.ceil(predict_value)
    return value

def RetornarPredict(indice_predicts):
    return list(map(Predict, indice_predicts))

def RetornarAutoPredict(total, trainingList):
    if(len(trainingList) == total):
        return trainingList[28:]
    else:
        model = ARIMA(trainingList, order=(1, 1, 1))
        model_fit = model.fit(disp=False)
        # make prediction
        predictValue = model_fit.predict(len(trainingList), len(trainingList), typ='levels')
        value = math.ceil(predictValue)
        trainingList.append(value)
        print(len(trainingList))
        return RetornarAutoPredict(total, trainingList)

#Predicts
predicts1 = RetornarPredict(indexsToPredict)
predicts2 = RetornarAutoPredict(rounds, tdata)

print("Predict Values")
print(predicts1)
print("Auto Predict Values")
print(predicts2)
print("Origin Values")
print(dataPrev)