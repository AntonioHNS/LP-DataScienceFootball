from sklearn.preprocessing import StandardScaler
from lib.functions import GenerateGameTable, getLastFiveRounds

jogos = GenerateGameTable()

#Para pegar o id dos times e testar
print(jogos.homeTeamId.unique())

rodadaDataFrame = getLastFiveRounds(jogos, 2019, 1596141233, 95417625, 12, 35)

print(rodadaDataFrame)

