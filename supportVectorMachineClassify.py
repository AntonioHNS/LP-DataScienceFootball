from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from lib.functions import GetTrainTest

trainTest, columnsArray = GetTrainTest()
attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]

svclassifier = SVC(kernel="rdb", degree=10)
svclassifier.fit(attribute_train, result_train)
forecast = svclassifier.predict(attribute_test)

confusionMatrix = confusion_matrix(result_test, forecast)
classificationReport = classification_report(result_test, forecast)

print(classificationReport)