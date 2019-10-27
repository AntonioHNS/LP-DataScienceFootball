import pandas as pd
import numpy as np

from lib_functions import generateGameTable

jogos = generateGameTable()
teams = list(jogos.homeTeamId.unique())
qtTeams = len(teams)

championshipTables = []    
attChampionshipTable = pd.DataFrame() #Tabela Atualizada constantemente
attChampionshipTable["teamId"] = teams
__temp = [0] * qtTeams
attChampionshipTable["points"] = __temp
attChampionshipTable["wins"] = [0] * qtTeams
attChampionshipTable["goalsBalance"] = [0] * qtTeams
attChampionshipTable["goals"] = [0] * qtTeams
def calculaPontos(matches, c, table):
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
        resultAwayBalance   =  away["goalsBalance"] + (awayScore - homeScore)
        resultAwayGoals     =  away["goals"] + awayScore
        
        t.goalsBalance      = np.where(conditionHome, resultHomeBalance, t.goalsBalance)
        t.goals             = np.where(conditionHome, resultHomeGoals, t.goals)
        t.goalsBalance      = np.where(conditionAway, resultAwayBalance, t.goalsBalance)
        t.goals             = np.where(conditionAway, resultAwayGoals, t.goals)
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
        return calculaPontos(matches, c, t)

matchWeeks = list(jogos.matchWeek.unique())
finalTable = pd.DataFrame()
matchWeekTables = []
for i in range(len(matchWeeks)):
    positionTable = pd.DataFrame()
    if(i == 0):
        positionTable["teamId"] = teams
        positionTable["position"] = [1] * qtTeams
    else:
        tempTable = pd.DataFrame()
        mWeek = matchWeeks[i-1]
        print(mWeek)
        mWeekTable = jogos[jogos["matchWeek"] == mWeek]
        matches = list(mWeekTable.MatchId.unique())
        finalTable = calculaPontos(matches, 0, attChampionshipTable)
        matchWeekTables.append({"matchWeek": i + 1, "table": finalTable.sort_values(by=["points", "wins", "goalsBalance", "goals"], ascending=False)})
print("----------------------------------------------------")
print(matchWeekTables[36]["table"])
print("----------------------------------------------------")