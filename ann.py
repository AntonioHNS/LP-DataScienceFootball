from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from lib.functions import GetTrainTest, getMeanMedianAccuracyPredict, GetImportanceList

import keras
from keras.models import Sequential
from keras.layers import Dense

import numpy as np



X_train, X_test, y_train, y_test, columnsArray = GetTrainTest()


# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu', input_dim = 8))

# Adding the second hidden layer
#classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 3, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
#y_pred = (y_pred > 0.5)
y_pred = np.argmax(y_pred, axis=1)
y_test = np.argmax(y_test, axis=1)
# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print(cm)
