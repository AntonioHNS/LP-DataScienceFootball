import matplotlib.pyplot as plt
import seaborn
from scipy.stats import poisson,skellam
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np


times = pd.read_csv("./dataset-brasileirao/Teams-Brasileirao.csv",encoding = 'UTF-8', sep = '\t')
data2017 = pd.read_csv("./dataset-brasileirao/2017-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data2017['ano'] = 2017
data2018 = pd.read_csv("./dataset-brasileirao/2018-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data2018['ano'] = 2018
data2019 = pd.read_csv("./dataset-brasileirao/2019-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data2019['ano'] = 2019
data = pd.concat([data2017,data2018,data2019])
data = data.merge(times,left_on = 'teamId',right_on = 'hash' )


partidas = pd.DataFrame()
partidas['partida_id'] = data['MatchId']
partidas['clube_id'] = data['clube_id']
partidas['faltas'] = data['fouls']
partidas['escanteios'] = data['corners']
partidas['cruzamentos'] = data['crosses']
partidas['toques'] = data['touches']
partidas['carrinhos'] = data['tackles']
partidas['interceptacoes'] = data['interceptions']
partidas['divididasVencidasPeloAlto'] = data['aerialsWon']
partidas['chutoes'] = data['clearances']
partidas['impedimentos'] = data['offsides']
partidas['tirosDeMeta'] = data['goalsKicks']
partidas['laterais'] = data['throwIns']
partidas['lancamentos'] = data['longBalls']
partidas['posseBola'] = data['possession']
partidas['totalPasses'] = data['totalPassing']
partidas['passesCorretos'] = data['correctPassing']
partidas['chutes'] = data['totalShots']
partidas['chutesCertos'] = data['shotsOnTarget']
partidas['defesas'] = data['saves']
partidas['cartoesAmarelos'] = data['yellowCards']
partidas['cartoesVermelhos'] = data['redCards']














