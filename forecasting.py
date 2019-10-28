from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

X, y = make_blobs(n_samples=10000, n_features=10, centers=100, random_state=0)
print("XXXXXXXXXXXXXXXXXXXXX")
print(len(X))
print("YYYYYYYYYYYYYYYYYYYYY")
print(len(y))
print("Dados")
clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=0)
scores = cross_val_score(clf, X, y, cv=5)
print(scores)
print(scores.mean())
