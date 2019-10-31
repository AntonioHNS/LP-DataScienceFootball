import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from lib.functions import GetTrainTest
# from positionFunction import ReturnTableMatchWithPosition

attribute_train, attribute_test, result_train, result_test  = GetTrainTest()
classificador = RandomForestClassifier(n_jobs=2, random_state = 0)
classificador.fit(attribute_train,result_train)
forecast = classificador.predict(attribute_test)

print(confusion_matrix(result_test, forecast))
print(classification_report(result_test, forecast))
