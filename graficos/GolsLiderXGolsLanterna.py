import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel
import pandas as pd

path_base = "C:/Users/filip/PycharmProjects/learn-pandas/Dataset Brasileirão/"
jogos2015 = pd.read_csv(path_base + str(2015) + "_partidas.csv", encoding="UTF-8", sep=',')
times2015 = pd.read_csv(path_base + str(2015) + "_clubes.csv", encoding="UTF-8", sep=',')
#jogos2015 = ""

p = jogos2015.groupby(['clube_casa_id']).mean()
max_casa = p[p["placar_oficial_mandante"] == p["placar_oficial_mandante"].max()]
min_casa = p[p["placar_oficial_mandante"] == p["placar_oficial_mandante"].min()]
print(max_casa["placar_oficial_mandante"])
print(min_casa["placar_oficial_mandante"])
print(times2015)
times = times2015.loc[(times2015['id'] == 264) | (times2015['id'] == 317)]
#placar_oficial_mandante
#placar_oficial_visitante
#info = pd.merge(estat,times,left_on='clube_id',right_on='id')
jogos = jogos2015.loc[(jogos2015['clube_casa_id'] == 264) | (jogos2015['clube_visitante_id'] == 317) | (jogos2015['clube_casa_id'] == 317) | (jogos2015['clube_visitante_id'] == 264)]

jogosVisCor = jogos.loc[(jogos2015['clube_visitante_id'] == 264)]
jogosManCor = jogos.loc[(jogos2015['clube_casa_id'] == 264)]
jogosManAGO = jogos.loc[(jogos2015['clube_casa_id'] == 317)]
jogosVisAGO = jogos.loc[(jogos2015['clube_visitante_id'] == 317)]

golsVisCor = pd.DataFrame(jogosVisCor,columns=['placar_oficial_visitante'])
golsVisCor['gols'] = golsVisCor['placar_oficial_visitante']
golsManCor = pd.DataFrame(jogosManCor,columns=['placar_oficial_mandante'])
golsManCor['gols'] = golsManCor['placar_oficial_mandante']

golsManAGO = pd.DataFrame(jogosManAGO,columns=['placar_oficial_mandante'])
golsManAGO['gols'] = golsManAGO['placar_oficial_mandante']
golsVisAGO = pd.DataFrame(jogosVisAGO,columns=['placar_oficial_visitante'])
golsVisAGO['gols'] = golsVisAGO['placar_oficial_visitante']

golsCor = golsManCor.append(golsVisCor,ignore_index=True)
golsAGO = golsManAGO.append(golsVisAGO,ignore_index=True)
#print(golsCor)

print(golsCor.head(5))
print(golsAGO.head(5))
ttest,pval = ttest_rel(golsCor['gols'],golsAGO['gols'])
print(pval)
if pval <0.05:
  print("we reject null hypothesis")
else:
  print("we accept null hypothesis")

sns.set(style="whitegrid")
ax = sns.boxplot(x=golsCor["gols"])
ax.set_title("Gols do Corinthians - 2015")
plt.plot()
plt.show()


sns.set(style="whitegrid")
ax = sns.boxplot(x=golsAGO["gols"])
ax.set_title("Gols do Joinvile - 2015")
plt.plot()
plt.show()
