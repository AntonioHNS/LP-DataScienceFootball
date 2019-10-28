import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR

from matplotlib import pyplot
from pandas.plotting import lag_plot

path = "./dataset-brasileirao/2017-Match-SerieA.csv"

df1 = pd.read_csv(path, encoding="UTF-8", sep='\t')

atl = df1.loc[(df1['nameTeam'] == "Atlético Mineiro")]
gre = df1.loc[(df1['nameTeam'] == "Grêmio")]

gre = gre["score"]
atl = atl["score"]

gre = gre.tolist()
del gre[-1]
atl = atl.tolist()
del atl[-1]
data = np.column_stack((gre, atl))

model = VAR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.forecast(model_fit.endog, steps=1)
print(yhat)
