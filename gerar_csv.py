# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:26:49 2019

@author: filip
"""
import pandas as pd
import webcrawlerteam as wb

idCampeonato = [9, 24, 62]
nomeCampeonato = ["PremierLeague", "SerieA", "ChineseLeague"]
#ano2019 = "/schedule/2019-Fixtures"

#anosBrasileirao = ["/schedule/2019-Fixtures", "/1760/schedule/2018-Fixtures", "/1559/schedule/2017-Fixtures"]
anosBrasileirao = ["/1495/schedule/2016-Serie-A-Fixtures"]
anosChineseLeague = ["/schedule/Super-League-Fixtures"]
anosPremier = ["/schedule/-Fixtures", "/1889/schedule/2018-2019-Fixtures", "/1631/schedule/2017-2018-Fixtures", "/1526/schedule/2016-2017-Fixtures"]
#nomesDocumentosTemporadaAnual = ["2019-Match-SerieA.csv", "2018-Match-SerieA.csv", "2017-Match-SerieA.csv"]
nomesDocumentosCsl = ["2019-Match-" + nomeCampeonato[2] + ".csv"]
nomesDocumentosBrasilSerieA = ["2016-Match-SerieA.csv"]
nomesDocumentosPremier = ["2019-2020-Match-"+ nomeCampeonato[1] + ".csv", "2018-2019-Match-" + nomeCampeonato[0] + ".csv", "2017-2018-Match-" + nomeCampeonato[0] + ".csv", "2016-2017-Match-" + nomeCampeonato[0] + ".csv"]

for indice in range(len(anosChineseLeague)):
    
    specificURL = "https://fbref.com/en/comps/" + str(idCampeonato[2]) + anosChineseLeague[indice]
    
    urlsMatch = wb.getUrlMatches(specificURL)
    #urlsMatch = [urlsMatch[0]]
    
    
    infoPartidas = list(map(wb.getInfoMatches, urlsMatch))
    
    matchId = []
    teamId = []
    nameTeam = []
    matchWeek = []
    score = []
    venue = [] #local
    stadium = []
    attendance = [] #publico
    fouls = []
    corners = []
    crosses = []
    touches = []
    tackles = []
    interceptions = []
    aerialsWon = []
    clearances = []
    offsides = []
    goalsKicks = []
    throwIns = []
    longBalls = []
    possession = []
    totalPassing = []
    correctPassing = []
    totalShots = []
    shotsOnTarget = []
    saves = []
    yellowCards = []
    redCards = []
    for i in range(len(infoPartidas)):
        p = infoPartidas[i]
        roundCamp = i//10
        if roundCamp == 0:
            print("Round:" + str(1))
        else:
            print("Round:" + str(roundCamp))
        print("Match: " + str(i))
        match = p["match"]
        homeInfo = p["homeTeam"]
        awayInfo = p["awayTeam"]
        homeStats = p["homeStats"]
        awayStats = p["awayStats"]
        homeStatsExtra = p["homeStatsExtra"]
        awayStatsExtra = p["awayStatsExtra"]
        
        #Add home team info to specific list
        matchId.append(match.matchId)
        teamId.append(homeInfo.teamId)
        nameTeam.append(homeInfo.name)
        matchWeek.append(match.matchweek)
        score.append(match.homeTeamScore)
        venue.append("home")
        stadium.append(match.stadium)
        attendance.append(match.attendance)
        fouls.append(homeStatsExtra.fouls)
        corners.append(homeStatsExtra.corners)
        crosses.append(homeStatsExtra.crosses)
        touches.append(homeStatsExtra.touches)
        tackles.append(homeStatsExtra.tackles)
        interceptions.append(homeStatsExtra.interceptions)
        aerialsWon.append(homeStatsExtra.aerialsWon)
        clearances.append(homeStatsExtra.clearances)
        offsides.append(homeStatsExtra.offsides)
        goalsKicks.append(homeStatsExtra.goalsKicks)
        throwIns.append(homeStatsExtra.throwIns)
        longBalls.append(homeStatsExtra.longBalls)
        possession.append(homeStats.possession)
        totalPassing.append(homeStats.totalPassing)
        correctPassing.append(homeStats.correctPassing)
        totalShots.append(homeStats.totalShots)
        shotsOnTarget.append(homeStats.shotsOnTarget)
        saves.append(homeStats.saves)
        yellowCards.append(homeStats.yellowCards)
        redCards.append(homeStats.redCards)
        
        #Add away team info to specific list
        matchId.append(match.matchId)
        teamId.append(awayInfo.teamId)
        nameTeam.append(awayInfo.name)
        matchWeek.append(match.matchweek)
        score.append(match.awayTeamScore)
        venue.append("away")
        stadium.append(match.stadium)
        attendance.append(match.attendance)
        fouls.append(awayStatsExtra.fouls)
        corners.append(awayStatsExtra.corners)
        crosses.append(awayStatsExtra.crosses)
        touches.append(awayStatsExtra.touches)
        tackles.append(awayStatsExtra.tackles)
        interceptions.append(awayStatsExtra.interceptions)
        aerialsWon.append(awayStatsExtra.aerialsWon)
        clearances.append(awayStatsExtra.clearances)
        offsides.append(awayStatsExtra.offsides)
        goalsKicks.append(awayStatsExtra.goalsKicks)
        throwIns.append(awayStatsExtra.throwIns)
        longBalls.append(awayStatsExtra.longBalls)
        possession.append(awayStats.possession)
        totalPassing.append(awayStats.totalPassing)
        correctPassing.append(awayStats.correctPassing)
        totalShots.append(awayStats.totalShots)
        shotsOnTarget.append(awayStats.shotsOnTarget)
        saves.append(awayStats.saves)
        yellowCards.append(awayStats.yellowCards)
        redCards.append(awayStats.redCards)
        
        
    data = {"MatchId": matchId,
            "teamId": teamId,
            "nameTeam": nameTeam,
            "matchWeek": matchWeek,
            "score": score,
            "venue": venue,
            "stadium": stadium,
            "attendance": attendance,
            "fouls": fouls,
            "corners": corners,
            "crosses": crosses,
            "touches": touches,
            "tackles": tackles,
            "interceptions": interceptions,
            "aerialsWon": aerialsWon,
            "clearances": clearances,
            "offsides": offsides,
            "goalsKicks": goalsKicks,
            "throwIns": throwIns,
            "longBalls": longBalls,
            "possession" : possession,
            "totalPassing" : totalPassing,
            "correctPassing" : correctPassing,
            "totalShots" : totalShots,
            "shotsOnTarget" : shotsOnTarget,
            "saves" : saves,
            "yellowCards" : yellowCards,
            "redCards" : redCards}
    dataMatch = pd.DataFrame(data)
    print(dataMatch.head(5))
    file_name = nomesDocumentosCsl[indice]
    dataMatch.to_csv(file_name, sep='\t', encoding='utf-8')



#obj = {"match":score["match"],
#               "homeTeam":score["home"],
#               "awayTeam":score["away"],
#               "awayStatsExtra": awayTeamExtra,
#               "homeStatsExtra": homeTeamExtra,
#               "homeStats":"",
#               "awayStats