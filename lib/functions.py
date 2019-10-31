import pandas as pd
import numpy as np
import os


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
    # listaAnos = ["2016", "2017", "2018", "2019"]
    listaAnos = ["2018"]
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
    jogos['winner'] = np.select([jogos.homeScore < jogos.awayScore, jogos.homeScore > jogos.awayScore], [-1, 1], 0)
    return jogos



    
    
    
