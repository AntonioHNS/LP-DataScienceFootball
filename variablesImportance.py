from sklearn.ensemble import RandomForestClassifier
from lib.functions import GetTrainTest, GetImportanceList
import matplotlib.pyplot as plt

trainTest, columnsArray = GetTrainTest()

attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]
clf = RandomForestClassifier(n_jobs=2, random_state = 0)
clf.fit(attribute_train, result_train)
forecast = clf.predict(attribute_test)

df, listaImportancia = GetImportanceList(forecast, clf)

print("Total: " +  str(sum(listaImportancia)))

df.plot.barh(x="stats", y= "importancia")
plt.show()


# '''TRATAMENTO DO DATAFRAME'''

# jogos = GenerateGameTable()
# jogos = jogos.drop(columns=["awayScore","homeScore",'MatchId', "awayAttendance"])
# jogos['winner'] = np.select([jogos.winner == 1,jogos.winner == -1],['vitoria mandante','vitoria visitante'],'empate')


# '''DEFININDO A FATIA DO TREINO E DE TESTE, O TREINO CORRESPONDE A CERCA DE 75%
# DO TAMANHO DO DATAFRAME E ELE SEPARA UNIFORME'''

# jogos['isTrain'] = np.random.uniform(0,1,len(jogos)) <= .75
# treino,teste = jogos[jogos['isTrain']==True], jogos[jogos['isTrain']==False]
# print('qtd treino: ' + str(len(treino)))
# print('qtd teste: ' + str(len(teste)))



# '''SEPARAÇÃO AS COLUNAS NECESSARIAS,
# AS COLUNAS CRIADAS ANTERIORMENTE FICAM EM STANDBY POR ENQUANTO'''

# colunas = jogos.columns[:47]
# print(colunas)


# ''' TRANSFORMA O RESULTADO EM NUMERICO (JÁ ERA ANTES MAS O TUTORIAL ELE FAZ ASSIM E EU N SABIA)
#  0 = vitoria visitante
#  1 = empate
#  2 = vitoria mandante

#     CRIAÇÃO DO CLASSIFICADOR, TREINO E REVISÃO
# '''

# resultados = pd.factorize(treino['winner'])[0]
# classificador = RandomForestClassifier(n_jobs=2,random_state = 0)
# classificador.fit(treino[colunas],resultados)
# previsao = classificador.predict(teste[colunas])

# '''LISTA COM RESULTADO DESCRITIVO PRA FACIL ENTENDIMENTO E DEPOIS
# UM FOR COMPARANDO O QUE FOI PREVISTO E O QUE REALMENTE ACONTECEU
# CONTANDO ERROS E ACERTOS'''

# results = []
# for i in previsao:
#     if i == 0:
#         results.append("vitoria visitante")
#     elif i == 1:
#         results.append("empate")
#     elif i == 2:
#         results.append("vitoria mandante")

# count = 0
# acertos = 0
# erros = 0
# for i in teste.iterrows():
#     if i[1]['winner'] == results[count]:
#         acertos = acertos+1
#     else:
#         erros = erros+1
#     count = count+1

# print(acertos)
# print(erros)


# '''lISTA DE COLUNAS E IMPORTANCIAS RESPECTIVAMENTE'''

# def returnPercentage(value):
#     return value*100
    
# listaImportancia = list(zip(treino[colunas],list(map(returnPercentage, classificador.feature_importances_))))

# for i in listaImportancia:
#     print(i)

