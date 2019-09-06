# Se remover o 'len' das varáveis, temos os jogadores por posição
# Do contrário temos o número de jogadores por posição
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

df = pd.read_csv('2014_atletas.csv', encoding = 'UTF-8', sep = ',')
goleiros = len(df.loc[df['posicao_id'] == 1])
laterais = len(df.loc[df['posicao_id'] == 2])
zagueiros = len(df.loc[df['posicao_id'] == 3])
meias = len(df.loc[df['posicao_id'] == 4])
atacantes = len(df.loc[df['posicao_id'] == 5])
tecnicos = len(df.loc[df['posicao_id'] == 6])

dtframe = pd.DataFrame({'total': [goleiros, laterais,
                                    zagueiros, meias,
                                    atacantes, tecnicos]},
                       index = ['goleiro', 'lateral',
                                        'zagueiro', 'meia',
                                        'atacante', 'tecnico'])

plot = dtframe.plot.pie(y='total', figsize=(5,5), autopct='%1.1f%%')
plt.show()

ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, dtframe, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(14)

plt.show()

