import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize
from scipy.stats import ttest_rel

#Region Atributos
path_base = "C:/Users/filip/PycharmProjects/learn-pandas/english-premier-league-match-data/"
arquivo = open(path_base + "season17-18/" + "season_match_stats.json")
data = json.load(arquivo)
json_normalize(data)

tableStats = pd.read_json(path_base + "season17-18/" + "season_stats.json", "index")
tableMatchStats = pd.read_json(path_base + "season17-18/" + "season_match_stats.json", "index")

newTable = tableMatchStats["full_time_score"].str.split(" : ", n=1, expand=True)

tableMatchStats["score_home_team"] = pd.to_numeric(newTable[0])
tableMatchStats["score_away_team"] = pd.to_numeric(newTable[1])

# Vencedor:  O time de casa se for maior que ZERO, O time de fora se for menor que ZERO;
# Empate: se for igual a ZERO
tableMatchStats["final_result"] = tableMatchStats["score_home_team"] - tableMatchStats["score_away_team"]

#Dados para o mapeamento
partidas = data.keys()
home_teams = list(tableMatchStats["home_team_id"])
away_teams = list(tableMatchStats["away_team_id"])
#endregion

#endregion

#Region Funções
def ReturnLosers(id_partida, id_home_team, id_away_team):

    linha = []

    aux = tableMatchStats.loc[int(id_partida)]["final_result"]

    if (aux < 0):
        linha.append(int(id_partida))
        linha.append(id_home_team)
        linha.append(tableStats.loc[int(id_partida)][id_home_team]["team_details"]["team_name"])
        linha.append("home")
        linha.append(tableStats.loc[int(id_partida)][id_home_team]["team_details"]["date"])
        linha.append("lose")
        linha.append(float(tableStats.loc[int(id_partida)][id_home_team]["team_details"]["team_rating"]))
        try:
            linha.append(float(tableStats.loc[int(id_partida)][id_home_team]["aggregate_stats"]["possession_percentage"])/100)
        except:
            linha.append(0)

        return linha
    elif (aux > 0):
        linha.append(int(id_partida))
        linha.append(id_away_team)
        linha.append(tableStats.loc[int(id_partida)][id_away_team]["team_details"]["team_name"])
        linha.append("away")
        linha.append(tableStats.loc[int(id_partida)][id_away_team]["team_details"]["date"])
        linha.append("lose")
        linha.append(float(tableStats.loc[int(id_partida)][id_away_team]["team_details"]["team_rating"]))
        try:
            linha.append(float(tableStats.loc[int(id_partida)][id_away_team]["aggregate_stats"]["possession_percentage"])/100)
        except:
            linha.append(0)
        return linha

    else:
        return None

def ReturnWinners(id_partida, id_home_team, id_away_team):

    linha = []

    aux = tableMatchStats.loc[int(id_partida)]["final_result"]

    if (aux > 0):
        linha.append(int(id_partida))
        linha.append(id_home_team)
        linha.append(tableStats.loc[int(id_partida)][id_home_team]["team_details"]["team_name"])
        linha.append("home")
        linha.append(tableStats.loc[int(id_partida)][id_home_team]["team_details"]["date"])
        linha.append("win")
        linha.append(float(tableStats.loc[int(id_partida)][id_home_team]["team_details"]["team_rating"]))
        try:
            linha.append(float(tableStats.loc[int(id_partida)][id_home_team]["aggregate_stats"]["possession_percentage"])/100)
        except:
            linha.append(0)

        return linha

    elif (aux < 0):
        linha.append(int(id_partida))
        linha.append(id_away_team)
        linha.append(tableStats.loc[int(id_partida)][id_away_team]["team_details"]["team_name"])
        linha.append("away")
        linha.append(tableStats.loc[int(id_partida)][id_away_team]["team_details"]["date"])
        linha.append("win")
        linha.append(float(tableStats.loc[int(id_partida)][id_away_team]["team_details"]["team_rating"]))
        try:
            linha.append(float(tableStats.loc[int(id_partida)][id_away_team]["aggregate_stats"]["possession_percentage"])/100)
        except:
            linha.append(0)
        return linha

#endregion

#Pegando os dados dos vencedores e perdedores das partidas
win         = list(map(ReturnWinners, partidas, home_teams, away_teams))
lose        = list(map(ReturnLosers, partidas, home_teams, away_teams))

#Retirando valores nulos do retorno das funções
winClear    = list(filter(None,  win))
loseClear   = list(filter(None,  lose))

#Mostrando quantos jogos não tiveram empate e averiguando se as  duas listas tem o mesmo tamanho
print(len(winClear))
print(len(loseClear))

winners     = pd.DataFrame(winClear, columns=['idpartida', 'idclube', 'nomeclube', 'estadio', 'datajogo', 'resultado', 'notaclube', 'Porcentagem de Posse de Bola'])
losers      = pd.DataFrame(loseClear, columns=['idpartida', 'idclube', 'nomeclube', 'estadio', 'datajogo', 'resultado', 'notaclube', 'Porcentagem de Posse de Bola'])

print("-------------")
print(winners["Porcentagem de Posse de Bola"])
print("-------------")
print(losers["Porcentagem de Posse de Bola"])

ttest,pval = ttest_rel(winners["Porcentagem de Posse de Bola"],losers["Porcentagem de Posse de Bola"])

print("p-value",pval)

if pval <0.05:
  print("we reject null hypothesis")
else:
  print("we accept null hypothesis")

sns.set(style="whitegrid")

ax = sns.boxplot(x=winners["Porcentagem de Posse de Bola"])
ax.set_title("Vencedores das Partidas - 2016/2017")
plt.show()

ax1 = sns.boxplot(x=losers["Porcentagem de Posse de Bola"])
ax1.set_title("Perdedores das Partidas - 2016/2017")
plt.show()
#export_csv = df.to_csv (r'C:/Users/filip/PycharmProjects/learn-pandas/english-premier-league-match-data/season16-17/season_match_stats_clear.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
