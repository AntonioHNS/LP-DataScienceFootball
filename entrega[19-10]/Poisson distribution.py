import matplotlib.pyplot as plt
import seaborn
from scipy.stats import poisson,skellam
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

def prepareDataFrame(data):
    mandante = data.loc[(data['venue'] == 'home')]
    mandantes = pd.DataFrame()
    mandantes['MatchId'] = mandante['MatchId']
    mandantes['homeTeam'] = mandante['nameTeam'].str.replace('Athletico Paranaense', 'Atlético Paranaense')
    mandantes['homeGoals'] = mandante['score']
    visitante = data.loc[(data['venue'] == 'away')]
    visitantes = pd.DataFrame()
    visitantes['MatchId'] = visitante['MatchId']
    visitantes['awayTeam'] = visitante['nameTeam'].str.replace('Athletico Paranaense', 'Atlético Paranaense')
    visitantes['awayGoals'] = visitante['score']
    return pd.merge(mandantes, visitantes, left_on='MatchId', right_on='MatchId')



def prepareDataModel(dataFrame):
    goal_model_data = pd.concat([dataFrame[['homeTeam', 'awayTeam', 'homeGoals']].assign(home=1).rename(
        columns={'homeTeam': 'team', 'awayTeam': 'opponent', 'homeGoals': 'goals'}),
        dataFrame[['awayTeam', 'homeTeam', 'awayGoals']].assign(home=0).rename(
            columns={'awayTeam': 'team', 'homeTeam': 'opponent', 'awayGoals': 'goals'})])
    return goal_model_data

def getProbScore(model,homeTeam,awayTeam,homeScore,awayScore):
    resultMatrix = probMatrix(model, homeTeam, awayTeam, max_goals=6)
    return resultMatrix[homeScore][awayScore]

def printPredict(row):
    print(row[1]['homeTeam'] + " " + str(row[1]['homeGoals']) + "x" + str(row[1]['awayGoals']) + " " + row[1]['awayTeam'])
    print(getProbWin(model, row[1]['homeTeam'], row[1]['awayTeam']))
    print(getProbScore(model, row[1]['homeTeam'], row[1]['awayTeam'], row[1]['homeGoals'], row[1]['awayGoals']))
    print()

def printMatchweek(teams):
    h, d, a = getProbWin(model, teams[0], teams[1])
    print("Vitória do %s: %.2f%%" % (teams[0],h * 100))
    print("Empate: %.2f%%" % (d * 100))
    print("Vitória do %s: %.2f%%" % (teams[1],a * 100))
    print()

def probMatrix(model,homeTeam,awayTeam,max_goals = 10):
    home_goals = model.predict(pd.DataFrame(data={'team': homeTeam, 'opponent': awayTeam, 'home': 1}, index=[1])).values[0]
    away_goals = model.predict(pd.DataFrame(data={'team': awayTeam, 'opponent': homeTeam, 'home': 0}, index=[1])).values[0]
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals + 1)] for team_avg in [home_goals, away_goals]]
    # This matrix shows the probability of homeTeam (rows of the matrix) and awayTeam (matrix columns) scoring a specific number of goals
    return np.outer(np.array(team_pred[0]), np.array(team_pred[1]))

def getProbWin(model,homeTeam,awayTeam):
    resultMatrix = probMatrix(model,homeTeam,awayTeam,max_goals=6)
    home = np.sum(np.tril(resultMatrix, -1))
    draw = np.sum(np.diag(resultMatrix))
    away = np.sum(np.triu(resultMatrix, 1))
    return home, draw, away

data2017 = pd.read_csv("2017-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data2018 = pd.read_csv("2018-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data2019 = pd.read_csv("2019-Match-SerieA.csv",encoding = 'UTF-8', sep = '\t')
data = pd.concat([data2017,data2018,data2019])
dataFrame = prepareDataFrame(data)
model_data = prepareDataModel(dataFrame)
model = smf.glm(formula="goals ~ home + team + opponent", data=model_data,family=sm.families.Poisson()).fit()
homeWin, draw, awayWin = getProbWin(model,"Santa Cruz","Sport")











lastMatchweek = [['CSA','Atlético Mineiro'],
                 ['Grêmio','Bahia'],
                 ['Fortaleza','Flamengo'],
                 ['Cruzeiro','São Paulo'],
                 ['Palmeiras','Chapecoense'],
                 ['Goiás','Corinthians'],
                 ['Vasco da Gama','Botafogo (RJ)'],
                 ['Avaí','Internacional'],
                 ['Santos','Ceará'],
                 ['Fluminense','Atlético Paranaense']]

nextMatchweek = [['Fortaleza','Grêmio'],
                 ['Corinthians','Cruzeiro'],
                 ['São Paulo','Avaí'],
                 ['Atlético Mineiro','Santos'],
                 ['Internacional','Vasco da Gama'],
                 ['Flamengo','Fluminense'],
                 ['Chapecoense','Goiás'],
                 ['Atlético Paranaense','Palmeiras'],
                 ['Bahia','Ceará'],
                 ['Botafogo (RJ)','CSA']]

list(map(printMatchweek,nextMatchweek))

