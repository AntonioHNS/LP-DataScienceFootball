# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:48:06 2019

@author: filip
"""

import requests
#import time
#import pandas as pd
from bs4 import BeautifulSoup

baseURL = "https://fbref.com"
idtime = [9, 24]
specificURL = "https://fbref.com/en/comps/" + str(idtime[1]) + "/schedule/-Fixtures"
classTable = "min_width sortable stats_table now_sortable sliding_cols"

class Team:
    def __init__(self, teamId, name):
        self.teamId = teamId
        self.name = name

class TeamExtraStats:
    def __init__(self, teamId, fouls, corners, crosses, touches, tackles, interceptions, aerialsWon,
                 clearances, offsides, goalsKicks, throwIns, longBalls):
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

class TeamStats:
    def __init__(self, teamId, possession, passingAccuracy,shotsOnTarget,saves,yellowCards,redCards):
        self.teamId = teamId
        self.possession = possession
        self.totalPassing = totalPassing
        self.correctPassing = correctPassing
        self.totalShots = totalShot
        self.shotsOnTarget = shotsOnTarget
        self.saves = saves
        self.yellowCards = yellowCards
        self.redCards = redCards

class Match:
    def __init__(self, matchId, matchweek,hometeamId, awayTeamId, homeTeamScore, awayTeamScore, stadium, attendance):
        self.matchId = matchId
        self.matchweek = matchweek
        self.homeTeamId = hometeamId
        self.awayTeamId = awayTeamId
        self.homeTeamScore = homeTeamScore
        self.awayTeamScore = awayTeamScore
        self.stadium = stadium
        self.attendance = attendance

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
                if(idPartida.count("-") == 0 and idPartida not in partidaIds):
                    partidaIds.add(idPartida)
                    urlPartidas.append({"match": idPartida, "link": baseURL + link})
    return urlPartidas

def tratarStats(stats,homeTeamId,awayTeamId):
    homePossession = None
    awayPossession = None
    homePassingAccuracy = None
    awayPassingAccuracy = None
    homeShotsOnTarget = None
    awayShotsOnTarget = None
    table = stats.findAll("tr")
    for i in range (len(table)):
        row = table[i]
        if "Possession" in row.contents[0]:
            content = table[i+1]
            data = content.findAll("strong")
            homePossession = data[0].contents[0]
            awayPossession = data[1].contents[0]
        elif "Passing Accuracy" in row.contents[0]:
            content = table[i+1]
            data = content.findAll("div")
            for div in data:
                lis = div.findAll("div")
                for i in lis:
                    print(i.contents)
                    print()
            #homePassingAccuracy = data[0].contents[0]
            #awayPassingAccuracy = data[1].contents[0]
        elif "Shots on Target" in row.contents[0]:
            content = table[i+1]
            data = content.findAll("strong")
            homeShotsOnTarget = data[0].contents[0]
            awayShotsOnTarget = data[1].contents[0]
        elif "Saves" in row.contents[0]:
            content = table[i+1]
            print()
        elif "Cards" in row.contents[0]:
            content = table[i+1]
            print()
    return 1,2

def tratarStatsExtra(stats,homeTeamId,awayTeamId):
    items = stats.findAll("div")  
    homefouls = ""
    homecorners = ""
    homecrosses = ""
    hometouches = ""
    hometackles = ""
    homeinterceptions = ""
    homeaerialsWon = ""
    homeclearances = ""
    homeoffsides = ""
    homegoalKicks = ""
    homethrowIns = ""
    homelongBalls = ""
    awayfouls = ""
    awaycorners = ""
    awaycrosses = ""
    awaytouches = ""
    awaytackles = ""
    awayinterceptions = ""
    awayaerialsWon = ""
    awayclearances = ""
    awayoffsides = ""
    awaygoalKicks = ""
    awaythrowIns = ""
    awaylongBalls = ""
    for i in range(len(items)):
        item = items[i]
        if 'Fouls' in item:
        	homefouls = items[i-1]
        	awayfouls = items[i-1]
        if 'Corners' in item:
        	homecorners = items[i-1]
        	awaycorners = items[i+1]
        if 'Crosses' in item:
        	homecrosses = items[i-1]
        	awaycrosses = items[i+1]
        if 'Touches' in item:
        	hometouches = items[i-1]
        	awaytouches = items[i+1]
        if 'Tackles' in item:
        	hometackles = items[i-1]
        	awaytackles = items[i+1]
        if 'Interceptions' in item:
        	homeinterceptions = items[i-1]
        	awayinterceptions = items[i+1]
        if 'Aerials' in item and 'Won' in item:
        	homeaerialsWon = items[i-1]
        	awayaerialsWon = items[i+1]
        if 'Clearances' in item:
        	homeclearances = items[i-1]
        	awayclearances = items[i+1]
        if 'Offsides' in item:
        	homeoffsides = items[i-1]
        	awayoffsides = items[i+1]
        if 'Goal' in item and 'Kicks' in item:
        	homegoalKicks = items[i-1]
        	awaygoalKicks = items[i+1]
        if 'Throw' in item and 'Ins' in item:
        	homethrowIns = items[i-1]
        	awaythrowIns = items[i+1]
        if 'Long' in item and 'Balls' in item:
        	homelongBalls = items[i-1]
        	awaylongBalls = items[i+1]
    home = TeamExtraStats(homeTeamId,homefouls, homecorners, homecrosses, hometouches, hometackles, 
                          homeinterceptions, homeaerialsWon, homeclearances, homeoffsides,
                          homegoalKicks, homethrowIns, homelongBalls)
    away = TeamExtraStats(awayTeamId,awayfouls, awaycorners, awaycrosses, awaytouches, awaytackles,
                          awayinterceptions, awayaerialsWon, awayclearances, awayoffsides, 
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
    scores = scorebox.findAll("div",{"class":"score"})
    for score in scores:
        if homeTeamScore == None:
            homeTeamScore = score.contents[0]
        else:
            awayTeamScore = score.contents[0]
    #pega todas as outras informações
    info = scorebox.findAll("div",{"class":"scorebox_meta"})
    info = info[0].findAll("div")
    matchweek = info[1].contents[1].replace(" (Matchweek ","").replace(")","")
    attendance = info[3].contents[2].contents[0]
    stadium = info[4].contents[2].contents[0]
    #cria objetos
    homeTeam = Team(homeTeamId,homeTeamName)
    awayTeam = Team(awayTeamId,awayTeamName)
    match = Match(0, matchweek,homeTeamId, awayTeamId, homeTeamScore, awayTeamScore, stadium, attendance)
    return {"home":homeTeam,"away":awayTeam,"match":match}

def getInfoMatches(match):
    matchId = match["link"][29:37]
    code = requests.get(match["link"])
    if code.status_code == 200:
        plain = code.text
        soup = BeautifulSoup(plain, "html.parser")
        score = soup.find("div", {"class":"scorebox"})
        score = getMatchInfo(score)
        score["match"].matchId = matchId
        stats = soup.find("div", {"id": "team_stats"})
        statsExtra = soup.find("div", {"id": "team_stats_extra"})
        homeTeamExtra, awayTeamExtra = tratarStatsExtra(statsExtra,score["match"].homeTeamId,score["match"].awayTeamId)
        homeTeamStats, awayTeamStats = tratarStats(stats,score["match"].homeTeamId,score["match"].awayTeamId)
        obj = {"match":score["match"],
               "homeTeam":score["home"],
               "awayTeam":score["away"],
               "awayStatsExtra": awayTeamExtra,
               "homeStatsExtra": homeTeamExtra,
               "homeStats":"",
               "awayStats":""}
        return obj



urlsMatch = getUrlMatches(specificURL)
urlsMatch = [urlsMatch[0]]


infoPartidas = list(map(getInfoMatches, urlsMatch))
print(infoPartidas)
