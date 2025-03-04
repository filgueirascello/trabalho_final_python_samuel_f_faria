import pandas as pd
import sqlite3
from transform import classifica_turno, calc_horas
from data_clean import data_clean

# Conectando ao banco SQLite (o arquivo será criado se não existir)
conn = sqlite3.connect('trabalhofinal.db')


# Gera o DataFrame a partir do clean.py
df = data_clean()


df['tempo_voo_minutos'] = calc_horas(df['tempo_voo'])


df['turno'] = df['data_hora'].apply(classifica_turno)


# df.head()

# print('finalizei')

# df.to_csv("base_final.csv", index=False)


# Inserindo o DataFrame na tabela
df.to_sql('table_trabalho_final', conn, if_exists='replace', index=False)