# coding: utf-8
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize
from scipy.stats import ttest_rel

#Region Atributos
path_base = "../LP-files/Datasets/Dataset-Brasileirão/"
partidas = pd.read_csv(path_base + "2017_partidas.csv", "index")
scouts = pd.read_csv(path_base + "2017_scouts.csv", "index")
clubes = pd.read_csv(path_base + "2017_clubes.csv", "index")
print(partidas)
