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
print("----------------------")
print(jogos.groupby("matchWeek").values)
print("----------------------")
print(jogos["awayMatchWeek"])
#03ff5eeb - Id de time para teste

teams = list(jogos.homeTeamId.unique())
qtTeams = len(teams)

championshipTables = []    
attChampionshipTable = pd.DataFrame()