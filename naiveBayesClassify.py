from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
from lib.functions import GetTrainTest

trainTest, columnsArray = GetTrainTest()
attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]
gnb = GaussianNB()
forecast = gnb.fit(attribute_train, result_train).predict(attribute_test)

confusionMatrix = confusion_matrix(result_test, forecast)
classificationReport = classification_report(result_test, forecast)

print(classificationReport)