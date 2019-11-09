from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from lib.functions import GetTrainTest, getMeanMedianAccuracyPredict
import pandas as pd
attribute_train, attribute_test, result_train, result_test, columnsArray = GetTrainTest()

clf = MLPClassifier(
    hidden_layer_sizes=(30, 17, 9, 3), 
    solver="adam", learning_rate="adaptive", alpha=0.000015, learning_rate_init=0.001)
#, learning_rate="invscaling" solver='sgd', alpha=0.0001, , random_state=1
clf.fit(attribute_train, result_train)
forecast = clf.predict(attribute_test)

confusionMatrix = confusion_matrix(result_test, forecast)
classificationReport = classification_report(result_test, forecast)
accuracy = accuracy_score(result_test, forecast)

print(classificationReport)
print(accuracy)

df = pd.DataFrame()

# mean, median = getMeanMedianAccuracyPredict(0, 10, [], clf, attribute_train, attribute_test, result_train, result_test)
# print("Median Accuracy: " + str(median))
# print("Mean Accuracy: " + str(mean))