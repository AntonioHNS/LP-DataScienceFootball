import matplotlib.pyplot as plt
import seaborn
from scipy.stats import poisson,skellam
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from lib.functions import getCSV

listaAnos = [2016,2017,2018,2019]
listaCSV = list(map(getCSV,listaAnos))
data = pd.concat(listaCSV)
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
