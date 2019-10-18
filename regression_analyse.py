from pmdarima import auto_arima
from tbats import TBATS, BATS
import pandas as pd
import math
import matplotlib.pyplot as plt

#Variables
path_base = "C:/Users/filip/PycharmProjects/learn-pandas/"
#champ = "-Match-PremierLeague"
champ = "-Match-SerieA"
#years = ["2016-2017", "2017-2018", "2018-2019", "2019-2020"]
years = ["2017", "2018", "2019"]
column = "fouls"

#Team
idTeam = "822bd0ba"
nameTeam = "Liverpool"

def CreateDataFrame(year):
    df = pd.read_csv(path_base + year + champ + ".csv", encoding="UTF-8", sep='\t')
    df["year"] = [year for x in range(df.shape[0])]
    return df

#dataFrame1, dataFrame2, dataFrame3, dataFrame4 = list(map(CreateDataFrame, years))
dataFrame1, dataFrame2, dataFrame3 = list(map(CreateDataFrame, years))

#dataFrameTotal = pd.concat([dataFrame1, dataFrame2, dataFrame3])
dataFrameTotal = pd.concat([dataFrame1, dataFrame2])

data            = dataFrameTotal.loc[dataFrameTotal.teamId == idTeam]
#dataLastYear    = dataFrame4.loc[dataFrame4.teamId == idTeam]
dataLastYear    = dataFrame3.loc[dataFrame3.teamId == idTeam]

trainData       = data[column].values
testData        = dataLastYear[column].values
matches         = len(testData)

#ARIMA Algorithm
arimaModel     = auto_arima(trainData, seasonal=True, m=3)
arimaForecast  = arimaModel.predict(n_periods=matches)
#arimaForecast  = list(map(math.floor, arimaForecast))
print("Arima")
print(arimaForecast)
print("Correto")
print(testData)
dataPlot = {"Real": testData, "Arima": arimaForecast}
t = pd.DataFrame(data=dataPlot)
t.plot()
plt.show()
