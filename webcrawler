import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

baseURL = "https://fbref.com"
url = "https://fbref.com/en/comps/9/1889/2018-2019-Premier-League-Stats"

players = []


def GetUrlClubes(url):
    urlClubes = []
    code = requests.get(url)
    if code.status_code == 200:
        plain = code.text
        soup = BeautifulSoup(plain, "html.parser")
        tabela = soup.find("div", {"class": "table_outer_container"})
        for item in tabela.findAll("a"):
            link = item.get('href')
            if 'squads' in link:
                temp = link.split('/')
                urlClubes.append({"team": temp[5], "link": link})
    return urlClubes

def GetUrlPlayer(json):
    url = baseURL + json["link"]
    code = requests.get(url)
    if code.status_code == 200:
        plain = code.text
        soup = BeautifulSoup(plain, "html.parser")
        tabela = soup.find("div", {"class": "table_outer_container"})
        for item in tabela.findAll("a"):
            if 'Matches' in item:
                link = item.get('href')
                temp = link.split('/')
                player = {"player": temp[3], "team": json["team"], "link": baseURL + link}
                players.append(player)
    return []

def GetStatsPlayers(players):
    cont = 0
    dados = []
    col = ['IdPlayer', 'NamePlayer', 'Day', 'Competition', 'Round', 'Venue', 'Result', 'Squad', 'Opponent',
           'Start',
           'Minutes Played', 'Goals', 'Assists', 'Shots Total', 'Shots on Target', 'Crosses', 'Fouls Drawn',
           'Penalts Kicks Made', 'Penalts Kicks Attempted', 'Tackles Won', 'Interceptions', 'Fouls Committed',
           'Yellow Cards', 'Red Cards', 'Clean Sheets', 'Gols Against', 'Saves', 'Shots on Target Against',
           '%Saves']

    for player in players:
        cont += 1
        print(cont)
        playerURL = player["link"]
        #playerURL = 'https://fbref.com/en/players/ed1e53f3/matchlogs/2018-2019/-Match-Logs'
        resp = requests.get(playerURL)

        if resp.status_code == 200:
            #Pegando o nome do jogador
            soup = BeautifulSoup(resp.text, 'html.parser')
            personalinfo = soup.find("div", {"id": "meta"})
            name = personalinfo.findAll("strong")[0].contents[0]
            if(name.strip() == 'Position:' or name.strip() == 'Footed:'):
                name = personalinfo.findAll("h1")[0].contents[0]
                print(name)
            #Pegando os dados por partida do jogador
            scouts = soup.find("div", {"class": "table_outer_container"})
            td = scouts.findAll("td")
            dataPerWeek = []
            dataPerWeek.append(player["player"])
            dataPerWeek.append(name)
            for i in range(len(td)):
                add = True;
                try:
                    dado = td[i].contents[0]
                    try:
                        statsTemp = dado.contents[0]
                        statsTemp = statsTemp.strip()
                        if statsTemp == 'Match Report':
                            while len(dataPerWeek) < 29:
                                dataPerWeek.append(-1)
                            if add == True:
                                dados.append(dataPerWeek)
                            dataPerWeek = []
                            dataPerWeek.append(player["player"])
                            dataPerWeek.append(name)
                        # elif(statsTemp == 'Premier League'):
                        #    add = True
                        # elif(statsTemp != 'Premier League'):
                        #    add = False
                        else:
                            dataPerWeek.append(statsTemp)
                    except:
                        dataPerWeek.append(dado)
                except:
                    print("EXCEPT")
    return dados, col

ini = time.time()
urlClubes = GetUrlClubes(url)
urlPlayers = list(map(GetUrlPlayer, urlClubes))

#Dado para teste
#p1 = [{"player": 'ed1e53f3', "team": "Manchester City", "link": 'https://fbref.com/en/players/ed1e53f3/matchlogs/2018-2019/-Match-Logs'}]
dados, col = GetStatsPlayers(players)

stats = pd.DataFrame(dados, columns=col)
export_csv = stats.to_csv (r'C:/Users/filip/PycharmProjects/learn-pandas/player_match_stats_clear.csv', index = None, header=True)
fim = time.time()
print(fim)
