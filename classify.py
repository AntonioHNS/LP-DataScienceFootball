import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from lib.functions import GenerateGameTable

jogos = GenerateGameTable()
data = jogos.drop(columns=["awayScore","homeScore",'MatchId', "year", "winner"])
result = jogos["winner"]

X_train, X_test, y_train, y_test = train_test_split(data, result, test_size = 0.20)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))