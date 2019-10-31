# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:26:49 2019

@author: filip
"""
import pandas as pd
import webcrawlerteam as wb

idCampeonato = [24]

nomesDocumentos = ["2016-Match-serieA.csv"]

anos = ["/1495/schedule/2016-Serie-A-Fixtures"]

for indice in range(len(anos)):
    
    specificURL = "https://fbref.com/en/comps/" + str(idCampeonato[0]) + anos[indice]
    
    urlsMatch = wb.getUrlMatches(specificURL)
    #urlsMatch = [urlsMatch[0]]
    
     
    infoPartidas = list(map(wb.getInfoMatches, urlsMatch))
    
    matchId=[] 
    teamId =[]
    nameTeam =[]
    matchWeek =[] 
    score =[]
    venue =[]
    stadium =[]
    attendance =[] 
    fouls =[]
    corners =[]
    crosses =[]
    touches =[]
    tackles =[]
    interceptions =[] 
    aerialsWon =[]
    clearances =[]
    offsides =[]
    goalsKicks = []
    throwIns =[]
    longBalls =[]
    possession =[]
    totalPassing =[]
    correctPassing =[]
    totalShots =[]
    shotsOnTarget =[]
    saves =[]
    yellowCards =[]
    redCards = []

    for i in range(len(infoPartidas)):
        if infoPartidas[i] == None:
            continue
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
    file_name = nomesDocumentos[indice]
    dataMatch.to_csv(file_name, sep='\t', encoding='utf-8')
