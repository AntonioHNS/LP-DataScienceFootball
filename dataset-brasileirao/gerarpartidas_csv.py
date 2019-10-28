import numpy as np
import pandas as pd


path_base = "/Users/ulyssesbarros/Desktop/"
campeonato = "-Match-SerieA"
    
    
def partidas(data):    
    partidas = data[['MatchId', 'teamId','nameTeam', 'venue', 'score', 'attendance']]  
    return partidas

def idToInteger(data):
    id = int(data, 16)    
    return id 

def MandanteId(data):
    home = data.loc[data['venue'] == 'home']
    y = map(idToInteger, home.teamId)
    return list(y)

def VisitanteId(data):
    home = data.loc[data['venue'] == 'away']
    y = map(idToInteger, home.teamId)
    return list(y)

def PlacarMandante(data):
    home = data.loc[data['venue'] == 'home']    
    return home.score

def PlacarVisitante(data):
    away = data.loc[data['venue'] == 'away']    
    return away.score

def idVencedor(data):
    
    return x 


data = pd.read_csv(path_base + str(2017) + campeonato + ".csv", encoding="UTF-8", sep='\t')


partidas = map(idToInteger, data.MatchId.unique())
partidas = pd.Series(partidas, name='partidaId')
partidas = partidas.to_frame()

mandanteId = MandanteId(data)
visitanteId = VisitanteId(data)

df = { 'mandanteId': mandanteId }
df1 = { 'visitanteId': visitanteId }

df = pd.DataFrame(df)
df = df.reset_index(drop=True)

df1 = pd.DataFrame(df1)
df1 = df1.reset_index(drop=True)

partidas['mandanteId'] = df
partidas['visitanteId'] = df1

x = PlacarMandante(data)
y = PlacarVisitante(data)

frame1 = { 'placarMandante': x}
frame2 = { 'placarVisitante': y }

result1 = pd.DataFrame(frame1)
result1 = result1.reset_index(drop=True)

result2 = pd.DataFrame(frame2)
result2 = result2.reset_index(drop=True)

partidas['placarMandante'] = result1
partidas['placarVisitante'] = result2


publico = data.loc[data['venue'] == 'home']
publico = publico.attendance
publico = { 'publico': publico }
publico = pd.DataFrame(publico)
publico = publico.reset_index(drop=True)

partidas['publico'] = publico


b = PlacarMandante(data)
b = b.reset_index(drop=True)
f = PlacarVisitante(data)
f = f.reset_index(drop=True)


teste = np.select([b < f, b > f], [-1,1], 0)
partidas['vencedor'] = teste


rodada = data.loc[data['venue'] == 'home']
rodada = rodada.matchWeek

rodada = { 'rodada': rodada }
rodada = pd.DataFrame(rodada)
rodada = rodada.reset_index(drop=True)

partidas['rodada'] = rodada

print(partidas)

partidas.to_csv(r'/Users/ulyssesbarros/Desktop/partidas.csv')

