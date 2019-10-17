# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:48:06 2019

@author: filip
"""

import requests
from bs4 import BeautifulSoup

baseURL = "https://fbref.com"
idcampeonato = [9, 24]
specificURL = baseURL + "/en/comps/" + str(
    idcampeonato[1]) + "/schedule/-Fixtures"
classTable = "min_width sortable stats_table now_sortable sliding_cols"

class Team:
    def __init__(self, teamId, name):
        self.teamId = teamId
        self.name = name

    def __str__(self):
        dado = ""
        dado += "TeamId: " + self.teamId + "\n"
        dado += "Name: " + self.name + "\n"
        return dado


class TeamExtraStats:
    def __init__(self, teamId, fouls, corners, crosses, touches, tackles,
                 interceptions, aerialsWon, clearances, offsides, goalsKicks,
                 throwIns, longBalls):
        self.teamId = teamId
        self.fouls = fouls
        self.corners = corners
        self.crosses = crosses
        self.touches = touches
        self.tackles = tackles
        self.interceptions = interceptions
        self.aerialsWon = aerialsWon
        self.clearances = clearances
        self.offsides = offsides
        self.goalsKicks = goalsKicks
        self.throwIns = throwIns
        self.longBalls = longBalls

    def __str__(self):
        dado = "TeamId: " + self.teamId + "\n"
        dado += "Fouls: " + self.fouls + "\n"
        dado += "Corners: " + self.corners + "\n"
        dado += "Crosses: " + self.crosses + "\n"
        dado += "Touches: " + self.touches + "\n"
        dado += "Tackles: " + self.tackles + "\n"
        dado += "Interceptions: " + self.interceptions + "\n"
        dado += "AerialWon: " + self.aerialsWon + "\n"
        dado += "Clearances: " + self.clearances + "\n"
        dado += "Offsides: " + self.offsides + "\n"
        dado += "GoalsKicks: " + self.goalsKicks + "\n"
        dado += "ThrownIns: " + self.throwIns + "\n"
        dado += "LongBalls: " + self.longBalls + "\n"
        return dado


class TeamStats:
    def __init__(self, teamId, possession, totalPassing, correctPassing,totalShot,shotsOnTarget,
                 saves, yellowCards, redCards):
        self.teamId = teamId
        self.possession = possession
        self.totalPassing = totalPassing
        self.correctPassing = correctPassing
        self.totalShots = totalShot
        self.shotsOnTarget = shotsOnTarget
        self.saves = saves
        self.yellowCards = yellowCards
        self.redCards = redCards

    def __str__(self):
        dado = ""
        dado += "TeamId         : " + self.teamId + "\n"
        dado += "Possession     : " + self.possession + "\n"
        dado += "TotalPassing   : " + self.totalPassing + "\n"
        dado += "CorrectPassing : " + self.correctPassing + "\n"
        dado += "TotalShots     : " + self.totalShots + "\n"
        dado += "ShotsOnTarget  : " + self.shotsOnTarget + "\n"
        dado += "Saves          : " + self.saves + "\n"
        dado += "YellowCards    : " + self.yellowCards + "\n"
        dado += "RedCards		: " + self.redCards + "\n"
        return dado


class Match:
    def __init__(self, matchId, matchweek, hometeamId, awayTeamId,
                 homeTeamScore, awayTeamScore, stadium, attendance):
        self.matchId = matchId
        self.matchweek = matchweek
        self.homeTeamId = hometeamId
        self.awayTeamId = awayTeamId
        self.homeTeamScore = homeTeamScore
        self.awayTeamScore = awayTeamScore
        self.stadium = stadium
        self.attendance = attendance

    def __str__(self):
        dado = ""
        dado += "MatchId :" + self.matchId + "\n"
        dado += "Matchweek :" + self.matchweek + "\n"
        dado += "HomeTeamId :" + self.homeTeamId + "\n"
        dado += "AwayTeamId :" + self.awayTeamId + "\n"
        dado += "HomeTeamScore :" + self.homeTeamScore + "\n"
        dado += "AwayTeamScore :" + self.awayTeamScore + "\n"
        dado += "Stadium :" + self.stadium + "\n"
        dado += "Attendance :" + self.attendance + "\n"
        return dado


def getUrlMatches(url):
    urlPartidas = []
    partidaIds = []
    partidaIds = set(partidaIds)
    code = requests.get(url)
    if code.status_code == 200:
        plain = code.text
        soup = BeautifulSoup(plain, "html.parser")
        tabela = soup.find("table", {"class": "stats_table"})
        for item in tabela.findAll("a"):
            link = item.get('href')
            if 'matches' in link:
                temp = link.split('/')
                idPartida = temp[3]
                if (idPartida.count("-") == 0 and idPartida not in partidaIds):
                    partidaIds.add(idPartida)
                    urlPartidas.append({
                        "match": idPartida,
                        "link": baseURL + link
                    })
    return urlPartidas


def tratarStats(stats, homeTeamId, awayTeamId):
    homePossession = None
    awayPossession = None
    homeCorrectPassing = None
    homeTotalPassing = None
    awayCorrectPassing = None
    awayTotalPassing = None
    homeShotsOnTarget = None
    homeTotalShots = None
    awayShotsOnTarget = None
    awayTotalShots = None
    homeSave = None
    awaySave = None
    homeYellowCard = None
    homeRedCard = None
    awayYellowCard = None
    awayRedCard = None

    table = stats.findAll("tr")
    for i in range(len(table)):
        row = table[i]
        if "Possession" in row.contents[0]:
            content = table[i + 1]
            data = content.findAll("strong")
            homePossession = data[0].contents[0]
            awayPossession = data[1].contents[0]
        elif "Passing Accuracy" in row.contents[0]:
            homeInfo, awayInfo = getInfo(table[i + 1])
            
            homeCorrectPassing = homeInfo[0]
            homeTotalPassing = homeInfo[1]
            awayCorrectPassing = awayInfo[0]
            awayTotalPassing = awayInfo[1]

        elif "Shots on Target" in row.contents[0]:
            homeInfo, awayInfo = getInfo(table[i + 1])

            homeShotsOnTarget = homeInfo[0]
            homeTotalShots = homeInfo[1]
            awayShotsOnTarget = awayInfo[0]
            awayTotalShots = awayInfo[1]
        elif "Saves" in row.contents[0]:
            homeInfo, awayInfo = getInfo(table[i + 1])
    
            homeSave = homeInfo[1]
            awaySave = homeInfo[1]
        elif "Cards" in row.contents[0]:
            content = table[i + 1]
            data = content.findAll("div", {"class": "cards"})
            homeYellowCard = str(len(data[0].findAll("span", {"class": "yellow_card"})) + len(data[0].findAll("span", {"class": "yellow_red_card"})))
            homeRedCard = str(len(data[0].findAll("span", {"class": "red_card"})) + len(data[0].findAll("span", {"class": "yellow_red_card"})))
            awayYellowCard = str(len(data[1].findAll("span", {"class": "yellow_card"})) + len(data[1].findAll("span", {"class": "yellow_red_card"})))
            awayRedCard = str(len(data[1].findAll("span", {"class": "red_card"})) + len(data[1].findAll("span", {"class": "yellow_red_card"})))
    
    home = TeamStats(homeTeamId ,homePossession, homeTotalPassing, homeCorrectPassing, homeTotalShots,
                    homeShotsOnTarget, homeSave,homeYellowCard, homeRedCard)
    away = TeamStats(awayTeamId , awayPossession, awayTotalPassing, awayCorrectPassing, awayTotalShots, 
                    awayShotsOnTarget,awaySave, awayYellowCard, awayRedCard)
    return home, away

def getInfo(content):
    data = content.findAll("div")
    homeInfo = data[1].contents[0].replace("—", '').replace(" ","").replace("\xa0\xa0", "").split("of")
    awayInfo = data[6].contents[1].replace("—", '').replace(" ","").replace("\xa0\xa0", "").split("of")

    return homeInfo, awayInfo

def tratarStatsExtra(stats, homeTeamId, awayTeamId):
    homefouls = None
    homecorners = None
    homecrosses = None
    hometouches = None
    hometackles = None
    homeinterceptions = None
    homeaerialsWon = None
    homeclearances = None
    homeoffsides = None
    homegoalKicks = None
    homethrowIns = None
    homelongBalls = None
    awayfouls = None
    awaycorners = None
    awaycrosses = None
    awaytouches = None
    awaytackles = None
    awayinterceptions = None
    awayaerialsWon = None
    awayclearances = None
    awayoffsides = None
    awaygoalKicks = None
    awaythrowIns = None
    awaylongBalls = None
    items = stats.findAll("div")
    
    for i in range(len(items)):
        item = items[i]
        if 'Fouls' in item:
            homefouls = items[i - 1].contents[0]
            awayfouls = items[i + 1].contents[0]
        if 'Corners' in item:
            homecorners = items[i - 1].contents[0]
            awaycorners = items[i + 1].contents[0]
        if 'Crosses' in item:
            homecrosses = items[i - 1].contents[0]
            awaycrosses = items[i + 1].contents[0]
        if 'Touches' in item:
            hometouches = items[i - 1].contents[0]
            awaytouches = items[i + 1].contents[0]
        if 'Tackles' in item:
            hometackles = items[i - 1].contents[0]
            awaytackles = items[i + 1].contents[0]
        if 'Interceptions' in item:
            homeinterceptions = items[i - 1].contents[0]
            awayinterceptions = items[i + 1].contents[0]
        if 'Aerials Won' in item:
            homeaerialsWon = items[i - 1].contents[0]
            awayaerialsWon = items[i + 1].contents[0]
        if 'Clearances' in item:
            homeclearances = items[i - 1].contents[0]
            awayclearances = items[i + 1].contents[0]
        if 'Offsides' in item:
            homeoffsides = items[i - 1].contents[0]
            awayoffsides = items[i + 1].contents[0]
        if 'Goal Kicks' in item:
            homegoalKicks = items[i - 1].contents[0]
            awaygoalKicks = items[i + 1].contents[0]
        if 'Throw Ins' in item:
            homethrowIns = items[i - 1].contents[0]
            awaythrowIns = items[i + 1].contents[0]
        if 'Long Balls' in item:
            homelongBalls = items[i - 1].contents[0]
            awaylongBalls = items[i + 1].contents[0]
    home = TeamExtraStats(homeTeamId, homefouls, homecorners, homecrosses,
                          hometouches, hometackles, homeinterceptions,
                          homeaerialsWon, homeclearances, homeoffsides,
                          homegoalKicks, homethrowIns, homelongBalls)
    away = TeamExtraStats(awayTeamId, awayfouls, awaycorners, awaycrosses,
                          awaytouches, awaytackles, awayinterceptions,
                          awayaerialsWon, awayclearances, awayoffsides,
                          awaygoalKicks, awaythrowIns, awaylongBalls)
    return home, away


def getMatchInfo(scorebox):
    homeTeamId = None
    homeTeamName = None
    homeTeamScore = None
    awayTeamId = None
    awayTeamName = None
    awayTeamScore = None
    matchweek = None
    stadium = None
    attendance = None
    times = scorebox.findAll("a")
    #pega nome e Id do time
    for time in times:
        if time.get("itemprop") == "name":
            id = time.get("href")[11:19]
            teamName = time.contents[0]
            if homeTeamId == None:
                homeTeamId = id
                homeTeamName = teamName
            else:
                awayTeamId = id
                awayTeamName = teamName
    #pega o placar
    scores = scorebox.findAll("div", {"class": "score"})
    for score in scores:
        if homeTeamScore == None:
            homeTeamScore = score.contents[0]
        else:
            awayTeamScore = score.contents[0]
    #pega todas as outras informações
    info = scorebox.findAll("div", {"class": "scorebox_meta"})
    info = info[0].findAll("div")
    matchweek = info[1].contents[1].replace(" (Matchweek ",
                                            "").replace(")", "")
    attendance = info[3].contents[2].contents[0]
    stadium = info[4].contents[2].contents[0]
    #cria objetos
    homeTeam = Team(homeTeamId, homeTeamName)
    awayTeam = Team(awayTeamId, awayTeamName)
    match = Match(0, matchweek, homeTeamId, awayTeamId, homeTeamScore,
                  awayTeamScore, stadium, attendance)
    return {"home": homeTeam, "away": awayTeam, "match": match}


def getInfoMatches(match):
    matchId = match["link"][29:37]
    code = requests.get(match["link"])
    if code.status_code == 200:
        plain = code.text
        soup = BeautifulSoup(plain, "html.parser")
        score = soup.find("div", {"class": "scorebox"})
        score = getMatchInfo(score)
        score["match"].matchId = matchId
        stats = soup.find("div", {"id": "team_stats"})
        statsExtra = soup.find("div", {"id": "team_stats_extra"})
        homeTeamExtra, awayTeamExtra = tratarStatsExtra(
            statsExtra, score["match"].homeTeamId, score["match"].awayTeamId)
        homeTeamStats, awayTeamStats = tratarStats(stats,
                                                   score["match"].homeTeamId,
                                                   score["match"].awayTeamId)
        obj = {
            "match": score["match"],
            "homeTeam": score["home"],
            "awayTeam": score["away"],
            "awayStatsExtra": awayTeamExtra,
            "homeStatsExtra": homeTeamExtra,
            "homeStats": homeTeamStats,
            "awayStats": awayTeamStats
        }
        print("o jogo " + match["link"])

        return obj