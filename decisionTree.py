from sklearn.datasets import load_iris
from sklearn import tree
from lib.functions import GetTrainTest
from sklearn.metrics import classification_report, confusion_matrix


trainTest, columnsArray = GetTrainTest()
attribute_train, attribute_test, result_train, result_test = trainTest[0], trainTest[1], trainTest[2], trainTest[3]

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(attribute_train,result_train)
forecast = clf.predict(attribute_test)


confusionMatrix = confusion_matrix(result_test, forecast)
classificationReport = classification_report(result_test, forecast)

print(confusionMatrix, classificationReport)
