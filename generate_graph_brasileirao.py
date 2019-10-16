import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import host_subplot

path_base = "C:/Users/filip/PycharmProjects/learn-pandas/"
campeonato = "MatchSerieA"


def CalcularMediaGolsPorAno(ano):
    data = pd.read_csv(path_base + ano + campeonato + ".csv", encoding="UTF-8", sep='\t')
    average = data.groupby('MatchId')['score'].sum().mean()
    return average


def CalcularMediaGolsPorAnoMandante(ano):
    table = pd.read_csv(path_base + str(ano) + "_partidas.csv", encoding="UTF-8", sep=',')
    average = table["placar_oficial_mandante"].sum()/table.shape[0]
    return average

def CalcularMediaGolsPorAnoVisitante(ano):
    table = pd.read_csv(path_base + str(ano) + "_partidas.csv", encoding="UTF-8", sep=',')
    average = table["placar_oficial_visitante"].sum()/table.shape[0]
    return average

#SELECT COUNT(*) FROM T WHERE A + B = 0
def CalcularPartidasSemGol(ano):
    table = pd.read_csv(path_base + str(ano) + "_partidas.csv", encoding="UTF-8", sep=',')
    table["qtgols"] = table["placar_oficial_visitante"] + table["placar_oficial_mandante"]
    result = table[table["qtgols"] == 0].qtgols.count()
    return result
def CalcularPartidasComGol(ano):
    table = pd.read_csv(path_base + str(ano) + "_partidas.csv", encoding="UTF-8", sep=',')
    table["qtgols"] = table["placar_oficial_visitante"] + table["placar_oficial_mandante"]
    result = table[table["qtgols"] > 0].qtgols.count()
    return result
#years = [2014, 2015, 2016, 2017]
years = [""]

medias_gols_por_ano = list(map(CalcularMediaGolsPorAno, years))
print(medias_gols_por_ano)
#medias_gols_mandante_por_ano = list(map(CalcularMediaGolsPorAnoMandante, years))
#medias_gols_visitante_por_ano = list(map(CalcularMediaGolsPorAnoVisitante, years))
#qt_partidas_sem_gol = list(map(CalcularPartidasSemGol, years))
#qt_partidas_com_gol = list(map(CalcularPartidasComGol, years))

#Gráfico 1 - Média de gols por jogo anual
#data = {'Ano': years, 'Média': medias_gols_por_ano}
#tabela_final = pd.DataFrame(data=data)

#print(tabela_final.head(4))
#ax = tabela_final.plot(x='Ano', y='Média', kind='line')
#ax.locator_params(integer=True)
#plt.show()

#Gráfico 2 - Comparativo entre a Média de gols em casa e fora anualmente

#data1 = {'Ano': years, 'Média Mandante': medias_gols_mandante_por_ano, "Média Visitante": medias_gols_visitante_por_ano}
#tabela_final1 = pd.DataFrame(data=data1)

#ax1 = tabela_final1.plot(x='Ano', y='Média Mandante', kind='line', color='orange')
#ax2 = tabela_final1.plot(x='Ano', y='Média Visitante', kind='line', color='g')
#ax1.locator_params(integer=True)
#ax2.locator_params(integer=True)
#plt.show()

#graf2 = host_subplot(111)

#graf2.set_xlabel("Ano")
#graf2.set_ylabel("Média de Gols por Partida")

#p1, = graf2.plot(years, medias_gols_mandante_por_ano, color='orange', label="Média Mandante")
#p2, = graf2.plot(years, medias_gols_visitante_por_ano, color='g', label="Média Visitante")

#leg = plt.legend()

#graf2.xaxis.get_label().set_color('r')
#graf2.xaxis.set_major_locator(MaxNLocator(integer=True))

#graf2.yaxis.get_label().set_color('c')

#leg.texts[0].set_color(p1.get_color())
#leg.texts[1].set_color(p2.get_color())

#plt.show()

#Gráfico 3

#print(qt_partidas_sem_gol)
#print(qt_partidas_com_gol)
#labels = years
#men_means = qt_partidas_sem_gol
#women_means = qt_partidas_com_gol

#x = np.arange(len(labels))  # the label locations
#width = 0.35  # the width of the bars

#fig, ax = plt.subplots()
#rects1 = ax.bar(x - width/2, men_means, width, label='Sem Gols')
#rects2 = ax.bar(x + width/2, women_means, width, label='Com Gols')

# Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Partidas')
#ax.set_title('Partidas com Gols x Partida sem Gols')
#ax.set_xticks(x)
#ax.set_xticklabels(labels)
#ax.legend()


# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')


#autolabel(rects1)
#autolabel(rects2)

#fig.tight_layout()

#plt.show()


