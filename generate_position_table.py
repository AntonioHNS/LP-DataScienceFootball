import pandas as pd
import numpy as np

from lib.functions import GenerateGameTable

jogos = GenerateGameTable()
teams = list(jogos.homeTeamId.unique())
qtMatches = len(list(jogos.MatchId.unique()))
qtTeams = len(teams)

championshipTables                      = []    
attChampionshipTable                    = pd.DataFrame() #Tabela Atualizada constantemente
attChampionshipTable["teamId"]          = teams
attChampionshipTable["points"]          = [0] * qtTeams
attChampionshipTable["wins"]            = [0] * qtTeams
attChampionshipTable["goalsBalance"]    = [0] * qtTeams
attChampionshipTable["goals"]           = [0] * qtTeams
attChampionshipTable["status"]          = ["home"] * qtTeams

def CalcularPontos(matches, c, table):
    t = table
    if c == len(matches): return t
    else:
        partida             = jogos[jogos["MatchId"] == matches[c]]
        winner              = partida["winner"].values[0]

        homeId              = partida["homeTeamId"].values[0]
        homeScore           = partida["homeScore"].values[0]
        home                = t[t.teamId == homeId]
        conditionHome       = t.teamId == homeId

        awayId              = partida["awayTeamId"].values[0]
        awayScore           = partida["awayScore"].values[0]
        away                = t[t.teamId == awayId]
        conditionAway       = t.teamId == awayId

        resultHomeBalance   =  home["goalsBalance"] + (homeScore - awayScore)
        resultHomeGoals     =  home["goals"] + homeScore
        resultHomeStatus    = "home"
        resultAwayBalance   =  away["goalsBalance"] + (awayScore - homeScore)
        resultAwayGoals     =  away["goals"] + awayScore
        resultAwayStatus    = "away"
        
        t.goalsBalance      = np.where(conditionHome, resultHomeBalance, t.goalsBalance)
        t.goals             = np.where(conditionHome, resultHomeGoals, t.goals)
        t.status            = np.where(conditionHome, resultHomeStatus, t.status)

        t.goalsBalance      = np.where(conditionAway, resultAwayBalance, t.goalsBalance)
        t.goals             = np.where(conditionAway, resultAwayGoals, t.goals)
        t.status            = np.where(conditionAway, resultAwayStatus, t.status)
        if winner == 1:            
            resultHomePoints    =  home["points"] + 3
            resultHomeWins      =  home["wins"] + 1
            t.points = np.where(conditionHome, resultHomePoints, t.points)
            t.wins = np.where(conditionHome, resultHomeWins, t.wins)
        if winner == 0:
            result1     =  home["points"] + 1
            result2     =  away["points"] + 1
            t.points = np.where(conditionHome, result1, t.points)
            t.points = np.where(conditionAway, result2, t.points)
        if winner == -1:
            result1     =  away["points"] + 3
            result2     =  away["wins"] + 1
            t.points = np.where(conditionAway, result1, t.points)
            t.wins = np.where(conditionAway, result2, t.wins)
        c += 1
        return CalcularPontos(matches, c, t)

def GerarTabela(matchWeek):
    positionTable = pd.DataFrame()
    if(matchWeek == 1):
        positionTable["teamId"] = teams
        positionTable["position"] = [1] * qtTeams
        temp = pd.DataFrame()
        temp["teamId"]          = teams
        temp["points"]          = [0] * qtTeams
        temp["wins"]            = [0] * qtTeams
        temp["goalsBalance"]    = [0] * qtTeams
        temp["goals"]           = [0] * qtTeams
        return {
            "matchWeek": matchWeek, 
            "table": temp.sort_values(by=["points", "wins", "goalsBalance", "goals"], 
            ascending=False)}
    else:
        mWeek = matchWeek - 1
        mWeekTable = jogos[jogos["matchWeek"] == mWeek]
        matches = list(mWeekTable.MatchId.unique())
        finalTable = CalcularPontos(matches, 0, attChampionshipTable)
        finalTable = finalTable.sort_values(by=["points", "wins", "goalsBalance", "goals"], ascending=False)
        return {
            "matchWeek": matchWeek, 
            "matches": matches,
            "table": finalTable}

jogos["homePosition"] = [1] * qtMatches
jogos["awayPosition"] = [1] * qtMatches
matchWeeks = list(jogos.matchWeek.unique())
finalTable = pd.DataFrame()
matchWeekTables = list(map(GerarTabela, matchWeeks))
print(matchWeekTables[5]["table"]["status"])
print(jogos)