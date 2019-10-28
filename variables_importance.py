from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import scale
from sklearn.svm import SVC
from lib.functions import GenerateGameTable

import pandas as pd
import numpy as np

jogos = GenerateGameTable()
jogos = jogos.drop(columns="awayScore")
jogos = jogos.drop(columns="homeScore")
jogos = pd.DataFrame(jogos,columns=['matchWeek','homeTotalShots','awayTotalShots','awayCorrectPassing','homeCorrectPassing','winner'])
print("----------------------")
jogos['isTrain'] = np.random.uniform(0,1,len(jogos)) <= .75
treino,teste = jogos[jogos['isTrain']==True], jogos[jogos['isTrain']==False]

print('qtd treino: ' + str(len(treino)))
print('qtd teste: ' + str(len(teste)))

columns = jogos.columns[:5]

resultados = pd.factorize(treino['winner'])[0]

classificador = RandomForestClassifier(n_jobs=2,random_state = 0)
classificador.fit(train,resultados)

classificador.predict(test)

#continuar amanhã

