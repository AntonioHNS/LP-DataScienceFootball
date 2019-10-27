import matplotlib.pyplot as plt
import seaborn
from scipy.stats import poisson,skellam
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np


data2017 = pd.read_csv("./dataset-brasileirao/2017-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data2018 = pd.read_csv("./dataset-brasileirao/2018-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data2019 = pd.read_csv("./dataset-brasileirao/2019-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data = pd.concat([data2017,data2018,data2019])
data = data.loc[(data["venue"] == 'home')]
data = pd.DataFrame(data,columns = ['teamId','nameTeam','stadium'])
data.rename(columns = {'teamId':'hash'},inplace = True)
data = data.groupby(["hash"]).first()
data['newId'] = np.arange(len(data))
#print(data)
teams = pd.DataFrame()
teams['clube_id'] = data['newId'] + 1
teams['nome'] = data['nameTeam']
teams['estadio'] = data['stadium']
#print(teams)
teams.to_csv("Teams-Brasileirao.csv", sep='\t', encoding='utf-8')
