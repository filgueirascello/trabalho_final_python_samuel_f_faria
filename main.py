import pandas as pd
from transform import classifica_turno, calc_horas
from data_clean import data_clean



# Gera o DataFrame a partir do clean.py
df = data_clean()



df['tempo_voo_minutos'] = calc_horas(df['tempo_voo'])



df['turno'] = df['data_hora'].apply(classifica_turno)


df.head()

print('finalizei')

df.to_csv("base_final.csv", index=False)
