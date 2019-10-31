from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from lib.functions import GetTrainTest

trainTest, columnsArray = GetTrainTest()

def returnPercentage(value):
    return value*100

def GetImportanceList():
    trainTest, columnsArray = GetTrainTest()
    attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]
    classificador = RandomForestClassifier(n_jobs=2, random_state = 0)
    classificador.fit(attribute_train,result_train)
    return list( zip( columnsArray, list( map( returnPercentage, classificador.feature_importances_ ) ) ) )

<<<<<<< HEAD
attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]
classificador = RandomForestClassifier(n_jobs=2, random_state = 0)
classificador.fit(attribute_train, result_train)
forecast = classificador.predict(attribute_test)

confusionMatrix = confusion_matrix(result_test, forecast)
classificationReport = classification_report(result_test, forecast)
print(classificationReport)
=======
listaImportancia = GetImportanceList()
importancia = list(list(zip(*listaImportancia))[1])
stats = list(list(zip(*listaImportancia))[0])
print(stats)
teste = pd.DataFrame({'importancia': importancia, 'stats': stats })
teste.plot.barh(x="stats", y= "importancia")
plt.show()
>>>>>>> 0712677af3010311279e2ccdd910ea7048e87841