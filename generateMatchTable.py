import matplotlib.pyplot as plt
import seaborn
from scipy.stats import poisson,skellam
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

from lib.functions import GenerateGameTable

data = GenerateGameTable()

times = pd.read_csv("./dataset-brasileirao/Teams-Brasileirao.csv",encoding = 'UTF-8', sep = '\t')
visitantes = pd.DataFrame(times,columns=['hash','clube_id'])
mandantes = pd.DataFrame(times,columns=['hash','clube_id'])
mandantes.rename(columns={'clube_id':'mandante'},inplace = True)
visitantes.rename(columns={'clube_id':'visitante'},inplace = True)
data = pd.merge(data,mandantes,left_on='homeTeamId',right_on='hash')
data = pd.merge(data,visitantes,left_on='awayTeamId',right_on='hash')


partidas = pd.DataFrame()
partidas['partidaId'] = data['MatchId'].apply(int, base=16)
partidas['mandanteId'] = data['mandante']
partidas['visitanteId'] = data['visitante']
partidas['placarMandante'] = data['homeScore']
partidas['placarVisitante'] = data['awayScore']
partidas['publico'] = data['homeAttendance']
partidas['vencedor'] = data['winner']
partidas['rodada'] = data['matchWeek']
partidas['ano'] = data['year']

partidas.to_csv("Matchs-Brasileirao.csv", sep='\t', encoding='utf-8')


'''
-partida_id
-mandante_id
-visitante_id
-rodada
-posicao_mandante
-posicao_visitante
-placar_mandante
-placar_visitante
-vencedor
-público
'''

















