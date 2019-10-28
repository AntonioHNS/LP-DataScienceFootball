from pmdarima import auto_arima
from tbats import TBATS, BATS
from matplotlib.ticker import MaxNLocator
import pandas as pd
import math
import matplotlib.pyplot as plt

#Variables
path_base = "dataset-brasileirao/"
#champ = "-Match-PremierLeague"
champ = "-Match-SerieA"
#years = ["2016-2017", "2017-2018", "2018-2019", "2019-2020"]
years = ["2017", "2018", "2019"]
column = "score"

#Team
#idTeam = "822bd0ba"
idTeam = "abdce579"
#abdce579
#639950ae
#5f232eb1
#nameTeam = "Liverpool"
nameTeam = "Palmeiras"

def CreateDataFrame(year):
    df = pd.read_csv(path_base + year + champ + ".csv", encoding="UTF-8", sep='\t')
    df["year"] = [year for x in range(df.shape[0])]
    return df

#dataFrame1, dataFrame2, dataFrame3, dataFrame4 = list(map(CreateDataFrame, years))
dataFrame1, dataFrame2, dataFrame3 = list(map(CreateDataFrame, years))
dataFrame1 = dataFrame1.groupby(["year", "matchWeek"]).score.mean().reset_index()
dataFrame2 = dataFrame2.groupby(["year", "matchWeek"]).score.mean().reset_index()
dataFrame3 = dataFrame3.groupby(["year", "matchWeek"]).score.mean().reset_index()

#dataFrameTotal = pd.concat([dataFrame1, dataFrame2, dataFrame3])
dataFrameTotal = pd.concat([dataFrame1, dataFrame2])
#dataFrameTotal = pd.concat([dataFrame1, dataFrame2, dataFrame3])

data            = dataFrameTotal
#data            = data.sort_values(by=['year', "matchWeek"])
#dataLastYear    = dataFrame4.loc[dataFrame4.teamId == idTeam]
dataLastYear    = dataFrame2
#dataLastYear    = dataFrame2.loc[dataFrame2.teamId == idTeam]
#dataLastYear    = dataLastYear.sort_values(by=['year', "matchWeek"])
#dataLastYear    = dataFrame1.loc[dataFrame1.teamId == idTeam]

rounds = len(list(dataLastYear[column].values))
roundsT = len(list(data[column]))
top = math.ceil(rounds * 0.80)
floor = rounds - top 
#matches         = len(testData)

#ARIMA Algorithm
column          = "score"
trainData       = data.head(68)[column].values
testData        = data.tail(8)[column].values
trainDataNew    = dataLastYear.head(top)[column].values
testDataNew     = dataLastYear.tail(floor)[column].values
arimaModel      = auto_arima(trainDataNew, seasonal=True, m=1)
arimaForecast   = arimaModel.predict(n_periods=8)
arimaModel1     = auto_arima(trainData, seasonal=True, m=1)
arimaForecast1  = arimaModel1.predict(n_periods=8)

arimaForecast  = list(map(math.floor, arimaForecast))
arimaForecast1  = list(map(math.floor, arimaForecast1))

print("Arima")
print(arimaForecast)
print("Arima1")
print(arimaForecast1)
print("Correto")
print(testDataNew)
print("Correto")
print(testData)
dataPlot = {"Real": testDataNew, "Last Year Arima": arimaForecast, "All Years Arima": arimaForecast1}
t = pd.DataFrame(data=dataPlot, index=[31, 32, 33, 34, 35, 36, 37, 38])
ax = t.plot()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlabel("Rodadas")
ax.set_ylabel("Gols")
ax.set_title('Palmeiras em 2018')
plt.show()
