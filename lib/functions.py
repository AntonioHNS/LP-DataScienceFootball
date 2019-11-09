import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def getCSV(ano):
    path_base = "dataset-brasileirao/"
    data = pd.read_csv(path_base +str(ano)+"-Match-SerieA.csv",encoding = 'UTF-8', sep = ',')
    data['year'] = int(ano)
    return data

# def a(teamId, hashId):
#     conditionHome = jogos.homeTeamId == hashId
#     conditionAway = jogos.awayTeamId == hashId
#     result = teamId
#     jogos.homeTeamId      = np.where(conditionHome, result, jogos.teamId)
#     jogos.awayTeamId      = np.where(conditionHome, result, jogos.teamId)

def GenerateGameTable():
    listaAnos = ["2016", "2017", "2018"]
    #listaAnos = ["2018"]
    listaCSV = list(map(getCSV,listaAnos))
    data = pd.concat(listaCSV)
    # times = pd.read_csv(path_base+"Teams-Brasileirao.csv",encoding = 'UTF-8',sep="/t")
    # data = pd.merge(data,times,right_on='MatchId',left_on='hash')    
    
    mandante = data.loc[(data['venue'] == 'home')]
    mandantes = pd.DataFrame()
    mandantes['MatchId'] = mandante['MatchId']
    mandantes["matchWeek"] = mandante["matchWeek"]
    mandantes['homeTeamId'] = mandante['teamId'].apply(int,base = 16)
    mandantes['homeScore'] = mandante['score']
    mandantes['homeShotsOnTarget'] = mandante['shotsOnTarget']
    mandantes['homeAttendance'] =  mandante['attendance'].str.replace(',','.').astype(float)
    mandantes['homeFouls'] =  mandante['fouls']
    mandantes['homeCorners'] = mandante['corners']
    mandantes['homeCrosses'] = mandante['crosses']
    mandantes['homeTouches'] = mandante['touches']
    mandantes['homeTackles'] = mandante['tackles']
    mandantes['homeInterceptions'] = mandante['interceptions']
    mandantes['homeAerialsWon'] = mandante['aerialsWon']
    mandantes['homeClearances'] = mandante['clearances']
    mandantes['homeOffsides'] = mandante['offsides']
    mandantes['homeGoalsKicks'] = mandante['goalsKicks']
    mandantes['homeThrowIns'] = mandante['throwIns']
    mandantes['homeLongBalls'] = mandante['longBalls']
    mandantes['homePossession'] = mandante['possession'].str.replace('%','').astype(float)
    mandantes['homeTotalPassing'] = mandante['totalPassing']
    mandantes['homeCorrectPassing'] = mandante['correctPassing']
    mandantes['homeTotalShots'] = mandante['totalShots']
    mandantes['homeShotsOnTarget'] = mandante['shotsOnTarget']
    mandantes['homeSaves'] = mandante['saves']
    mandantes['homeYellowCards'] = mandante['yellowCards']
    mandantes['homeRedCards'] = mandante['redCards']
    mandantes['year'] = mandante['year']

    visitante = data.loc[(data['venue'] == 'away')]
    visitantes = pd.DataFrame()
    visitantes['MatchId'] = visitante['MatchId']
    visitantes["awayMatchWeek"] = visitante["matchWeek"]
    visitantes['awayTeamId'] = visitante['teamId'].apply(int,base = 16)
    visitantes['awayScore'] = visitante['score']
    visitantes['awayShotsOnTarget'] = visitante['shotsOnTarget']
    visitantes['awayAttendance'] =  visitante['attendance'].str.replace(',','.').astype(float)
    visitantes['awayFouls'] =  visitante['fouls']
    visitantes['awayCorners'] = visitante['corners']
    visitantes['awayCrosses'] = visitante['crosses']
    visitantes['awayTouches'] = visitante['touches']
    visitantes['awayTackles'] = visitante['tackles']
    visitantes['awayInterceptions'] = visitante['interceptions']
    visitantes['awayAerialsWon'] = visitante['aerialsWon']
    visitantes['awayClearances'] = visitante['clearances']
    visitantes['awayOffsides'] = visitante['offsides']
    visitantes['awayGoalsKicks'] = visitante['goalsKicks']
    visitantes['awayThrowIns'] = visitante['throwIns']
    visitantes['awayLongBalls'] = visitante['longBalls']
    visitantes['awayPossession'] = visitante['possession'].str.replace('%','').astype(float)
    visitantes['awayTotalPassing'] = visitante['totalPassing']
    visitantes['awayCorrectPassing'] = visitante['correctPassing']
    visitantes['awayTotalShots'] = visitante['totalShots']
    visitantes['awayShotsOnTarget'] = visitante['shotsOnTarget']
    visitantes['awaySaves'] = visitante['saves']
    visitantes['awayYellowCards'] = visitante['yellowCards']
    visitantes['awayRedCards'] = visitante['redCards']
    jogos = pd.merge(mandantes,visitantes,left_on='MatchId',right_on='MatchId')

    # -1: Vencedor Away Team
    # 0: Empate
    # 1: Vencedor Home Team
    jogos['winner'] = np.select([jogos.homeScore < jogos.awayScore, jogos.homeScore > jogos.awayScore], [0, 2], 1)
    return jogos

def GetTrainTest():
    jogos = GenerateGameTable()
    empatesDf = jogos.loc[jogos['winner'] == 1]
    derrotaDf = jogos.loc[jogos['winner'] == 0]
    vitoriaDf = jogos.loc[jogos['winner'] == 2]

    empatesDf = empatesDf.head(261)
    derrotaDf = derrotaDf.head(261)
    vitoriaDf = vitoriaDf.head(261)

    jogos = pd.concat([empatesDf, derrotaDf, vitoriaDf], sort="True")

    #jogos['winner'] = np.select([jogos.winner == 1,jogos.winner == -1],['vitoria mandante','vitoria visitante'],'empate')
    data = jogos.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner", "awayAttendance", "awayMatchWeek","awayTeamId", "homeTeamId"])

    colunas = data.columns
    
    print(len(colunas))
    result = jogos["winner"]
    X_train, X_test, y_train, y_test = train_test_split(data, result, test_size = 0.20)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)
    return X_train, X_test, y_train, y_test, data[colunas]

    
def getMeanMedianAccuracyPredict(init, exit, score, clf, att_train, att_test, r_train, r_test):
    if init == exit:
        median = np.median(score)
        mean = np.mean(score)
        return mean*100, median*100
    clf.fit(att_train, r_train)
    forecast = clf.predict(att_test)
    score.append(accuracy_score(r_test, forecast))
    init += 1
    return getMeanMedianAccuracyPredict(init, exit, score, clf, att_train, att_test, r_train, r_test)

def returnPercentage(value):
    return value*100

def GetImportanceList(forecast, classificador):
    trainTest, columnsArray = GetTrainTest()
    attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]
    listaImportancia = list( zip( columnsArray, list( map( returnPercentage, classificador.feature_importances_ ) ) ) )
    importancia = list(list(zip(*listaImportancia))[1])
    stats = list(list(zip(*listaImportancia))[0])
    print(stats)
    df = pd.DataFrame({'importancia': importancia, 'stats': stats })
    return df, importancia


# teste.plot.barh(x="stats", y= "importancia")
# plt.show()
    
    
    
