import matplotlib.pyplot as plt
import seaborn
from scipy.stats import poisson,skellam
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

from lib.functions import *


times = pd.read_csv("./dataset-brasileirao/Teams-Brasileirao.csv",encoding = 'UTF-8', sep = '\t')
listaAnos = [2016,2017,2018,2019]
listaCSV = list(map(getCSV,listaAnos))
data = pd.concat(listaCSV)
data = data.merge(times,left_on = 'teamId',right_on = 'hash' )




partidas = pd.DataFrame()
partidas['partida_id'] = data['MatchId'].apply(int, base=16)
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

partidas.to_csv("MatchTeam-Brasileirao.csv", sep='\t', encoding='utf-8')












