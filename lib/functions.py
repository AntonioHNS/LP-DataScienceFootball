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

def getTeamNames():
    path_base = "dataset-brasileirao/"
    data = pd.read_csv(path_base +"2019-Match-SerieA.csv",encoding = 'UTF-8', sep = ',')
    data = data.rename(columns={"teamId": "hash"})
    data['teamId'] = data['hash'].apply(int,base = 16)
    data = pd.DataFrame(data,columns = ['teamId','nameTeam','hash'])
    data = data.groupby(['nameTeam','hash']).mean()
    data.to_csv('times.csv', sep=',', encoding='utf-8')
    return data

# def a(teamId, hashId):
#     conditionHome = jogos.homeTeamId == hashId
#     conditionAway = jogos.awayTeamId == hashId
#     result = teamId
#     jogos.homeTeamId      = np.where(conditionHome, result, jogos.teamId)
#     jogos.awayTeamId      = np.where(conditionHome, result, jogos.teamId)

def GenerateGameTable():
    listaAnos = ["2016", "2017", "2018", "2019"]
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

    empatesDf = empatesDf.tail(341)
    derrotaDf = derrotaDf.tail(341)
    vitoriaDf = vitoriaDf.tail(341)

    jogos = pd.concat([empatesDf, derrotaDf, vitoriaDf], sort="True")

    #jogos['winner'] = np.select([jogos.winner == 1,jogos.winner == -1],['vitoria mandante','vitoria visitante'],'empate')
    
    #Teste 1
    data = jogos.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner", "awayAttendance", "awayMatchWeek"])

    #Teste 2
    # data = jogos.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner", "awayAttendance", "awayMatchWeek", "awayRedCards", "homeRedCards"])

    #Teste 3
    # data = jogos.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner", "awayAttendance", "awayMatchWeek", "awayRedCards", "homeRedCards", "homeYellowCards", "awayYellowCards", "homeOffsides", "awayOffsides", "homeCorners", "awayCorners"])

    #Teste 4
    # data = jogos.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner", "awayAttendance", "awayMatchWeek", "awayRedCards", "homeRedCards", "homeYellowCards", "awayYellowCards", "homeOffsides", "awayOffsides", "homeCorners", "awayCorners", "awayFouls", "awayTeamId", "awayTackles", "awayTotalShots", "homeGoalsKicks", "homeTotalShots", "homePossession"])

    colunas = data.columns
    
    result = jogos["winner"]
    X_train, X_test, y_train, y_test = train_test_split(data, result, test_size = 0.20)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)
    return X_train, X_test, y_train, y_test, data[colunas]

def getLastFiveRounds(dataSet, year, homeTeam, awayTeam, matchId, matchWeek):
    table = dataSet[dataSet["year"] == year]
    data = table.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner", "awayAttendance", "awayMatchWeek"])
    
    home = data[data.homeTeamId == homeTeam].tail(5)
    home = home.drop(columns=["homeTeamId", "awayTeamId"])
    home = home.median()
    
    away = data[data.awayTeamId == awayTeam].tail(5)
    away = away.drop(columns=["homeTeamId", "awayTeamId"])
    away = away.median()

    matches = pd.DataFrame()
    # matches["MatchId"]            =  [matchId]
    matches["matchWeek"]      	  =  [matchWeek]
    matches['homeTeamId']         =  [homeTeam]
    matches['homeShotsOnTarget']  =  home['homeShotsOnTarget']
    matches['homeAttendance']     =  home['homeAttendance']
    matches['homeFouls']          =  home['homeFouls']
    matches['homeCorners']        =  home['homeCorners']
    matches['homeCrosses']        =  home['homeCrosses']
    matches['homeTouches']        =  home['homeTouches']
    matches['homeTackles']        =  home['homeTackles']
    matches['homeInterceptions']  =  home['homeInterceptions']
    matches['homeAerialsWon']     =  home['homeAerialsWon']
    matches['homeClearances']     =  home['homeClearances']
    matches['homeOffsides']       =  home['homeOffsides']
    matches['homeGoalsKicks']     =  home['homeGoalsKicks'] 
    matches['homeThrowIns']       =  home['homeThrowIns'] 
    matches['homeLongBalls']      =  home['homeLongBalls'] 
    matches['homePossession']     =  home['homePossession']
    matches['homeTotalPassing']   =  home['homeTotalPassing']
    matches['homeCorrectPassing'] =  home['homeCorrectPassing']
    matches['homeTotalShots']     =  home['homeTotalShots']
    matches['homeShotsOnTarget']  =  home['homeShotsOnTarget']
    matches['homeSaves']          =  home['homeSaves']
    matches['homeYellowCards']    =  home['homeYellowCards']
    matches['homeRedCards']       =  home['homeRedCards']
    matches['awayTeamId']         =  [awayTeam]
    matches['awayShotsOnTarget']  =  away['awayShotsOnTarget']
    matches['awayFouls']          =  away['awayFouls']
    matches['awayCorners']        =  away['awayCorners']
    matches['awayCrosses']        =  away['awayCrosses']
    matches['awayTouches']        =  away['awayTouches']
    matches['awayTackles']        =  away['awayTackles']
    matches['awayInterceptions']  =  away['awayInterceptions']
    matches['awayAerialsWon']     =  away['awayAerialsWon']
    matches['awayClearances']     =  away['awayClearances']
    matches['awayOffsides']       =  away['awayOffsides']
    matches['awayGoalsKicks']     =  away['awayGoalsKicks'] 
    matches['awayThrowIns']       =  away['awayThrowIns'] 
    matches['awayLongBalls']      =  away['awayLongBalls'] 
    matches['awayPossession']     =  away['awayPossession']
    matches['awayTotalPassing']   =  away['awayTotalPassing']
    matches['awayCorrectPassing'] =  away['awayCorrectPassing']
    matches['awayTotalShots']     =  away['awayTotalShots']
    matches['awayShotsOnTarget']  =  away['awayShotsOnTarget']
    matches['awaySaves']          =  away['awaySaves']
    matches['awayYellowCards']    =  away['awayYellowCards']
    matches['awayRedCards']       =  away['awayRedCards']
    return matches

def calc(lastRound):
    if(lastRound == 0):
        return 1
    
    lastRound -= 1
    return calc(lastRound)

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

    
