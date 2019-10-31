import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from lib.functions import GenerateGameTable

jogos = GenerateGameTable()
empatesDf = jogos.loc[jogos['winner'] == 0]
derrotaDf = jogos.loc[jogos['winner'] == -1]
vitoriaDf = jogos.loc[jogos['winner'] == 1]
empatesDf = empatesDf.head(68)
derrotaDf = derrotaDf.head(68)
vitoriaDf = vitoriaDf.head(68)

jogos = pd.concat([empatesDf, derrotaDf, vitoriaDf])

#jogos['winner'] = np.select([jogos.winner == 1,jogos.winner == -1],['vitoria mandante','vitoria visitante'],'empate')
data = jogos.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner", "awayAttendance"])#, "homeTeamId", "awayTeamId"])
data = data.values
result = jogos["winner"]

attribute_train, attribute_test, result_train, result_test = train_test_split(data, result, test_size = 0.20)

classificador = RandomForestClassifier(n_jobs=2,random_state = 0)
classificador.fit(attribute_train,result_train)
forecast = classificador.predict(attribute_test)


print(confusion_matrix(result_test, forecast))
print(classification_report(result_test, forecast))
