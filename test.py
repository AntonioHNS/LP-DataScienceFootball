from sklearn.preprocessing import StandardScaler
from lib.functions import GenerateGameTable, getLastFiveRounds

jogos = GenerateGameTable()

#639950ae = Flamengo
#Testando com um time
a = getLastFiveRounds(jogos, 2018, "639950ae")

print(a)

