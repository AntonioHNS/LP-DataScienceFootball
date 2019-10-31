from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from lib.functions import GetTrainTest

trainTest, columnsArray = GetTrainTest()
attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]

clf = MLPClassifier(solver='sgd', alpha=0.0001, hidden_layer_sizes=(15,), random_state=1, learning_rate="invscaling")
clf.fit(attribute_train, result_train)
forecast = clf.predict(attribute_test)

confusionMatrix = confusion_matrix(result_test, forecast)
classificationReport = classification_report(result_test, forecast)

print(classificationReport)