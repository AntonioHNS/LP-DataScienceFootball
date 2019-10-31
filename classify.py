import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from lib.functions import GenerateGameTable

jogos = GenerateGameTable()
treino = jogos.drop(columns=["awayScore","homeScore",'MatchId'])
teste = 2
print(jogos.columns)