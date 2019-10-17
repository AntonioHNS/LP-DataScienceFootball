import pandas as pd
import matplotlib.pyplot as plt

path = "C:/Users/soare/Desktop/Data/"

"""posicoes = pd.read_csv(path+"posicoes.csv",encoding ="UTF-8", sep=',')

atletas2014 = pd.read_csv(path+"2014_atletas.csv",encoding = "UTF-8", sep=',')
times2014 = pd.read_csv(path+"2014_clubes.csv",encoding ="UTF-8", sep=',')
stats2014 = pd.read_csv(path+"2014_scouts.csv",encoding ="UTF-8", sep=',')
jogos2014 = pd.read_csv(path+"2014_partidas.csv",encoding ="UTF-8", sep=',')


atletas2015 = pd.read_csv(path+"2015_atletas.csv",encoding ="UTF-8", sep=',')
times2015 = pd.read_csv(path+"2015_clubes.csv",encoding ="UTF-8", sep=',')
stats2015 = pd.read_csv(path+"2015_scouts.csv",encoding ="UTF-8", sep=',')
jogos2015 = pd.read_csv(path+"2015_partidas.csv",encoding ="UTF-8", sep=',')

atletas2016 = pd.read_csv(path+"2015_atletas.csv",encoding ="UTF-8", sep=',')
times2016 = pd.read_csv(path+"2016_clubes.csv",encoding ="UTF-8", sep=',')
stats2016 = pd.read_csv(path+"2016_scouts.csv",encoding ="UTF-8", sep=',')
jogos2016 = pd.read_csv(path+"2016_partidas.csv",encoding ="UTF-8", sep=',')

atletas2017 = pd.read_csv(path+"2017_atletas.csv",encoding ="UTF-8", sep=',')
times2017 = pd.read_csv(path+"2017_clubes.csv",encoding ="UTF-8", sep=',')
stats2017 = pd.read_csv(path+"2017_scouts.csv",encoding ="UTF-8", sep=',')
jogos2017 = pd.read_csv(path+"2017_partidas.csv",encoding ="UTF-8", sep=',')"""

def golsPorRodada(ano):
    jogos = pd.read_csv(path + str(ano) +"_partidas.csv", encoding="UTF-8", sep=',')
    jogos["totalgols"] = jogos["placar_oficial_mandante"] + jogos["placar_oficial_visitante"]
    return pd.DataFrame(jogos,columns=['rodada','totalgols']).groupby(["rodada"]).sum()


def chutesPorGol(ano):
    times = pd.read_csv(path + str(ano) + "_clubes.csv", encoding="UTF-8", sep=',')
    estat = pd.read_csv(path + str(ano) + "_scouts.csv", encoding="UTF-8", sep=',')
    info = pd.merge(estat,times,left_on='clube_id',right_on='id')
    info  = pd.DataFrame(info,columns=['abreviacao','FD','FT','FF','G'])
    info = info.groupby(['abreviacao']).sum()
    info['Chutes/Gol'] = (info['FD'] + info['FF'] + info['FT'] + info['G']) / info['G']
    info = info.loc[(info['G'] > 0) & info['Chutes/Gol'] > 0]
    info = pd.DataFrame(info, columns=['Chutes/Gol'])
    return info


def graphChutesPorGol():
    info2014 = chutesPorGol(2014)
    info2015 = chutesPorGol(2015)
    info2016 = chutesPorGol(2016)
    info = info2014
    info['2015'] = info2015['Chutes/Gol']
    info['2016'] = info2016['Chutes/Gol']
    info['2014'] = info2014['Chutes/Gol']
    info = pd.DataFrame(info2014, columns=['2014', '2015', '2016'])
    ax = info.plot.bar(rot=0)
    ax.grid(linestyle='--', color='gray')
    ax.set_title("Média de chutes necessários para fazer um gol")
    plt.plot()
    plt.show()
    return info


graphChutesPorGol()















