import pandas as pd

'''
# def calc_horas(coluna_tempo_voo):
#    return coluna_transformada_hora

def calc_horas(coluna_tempo_voo):
    return coluna_tempo_voo * 60


# Aplicando a função na coluna
df['tempo_voo_minutos'] = calc_horas(df['tempo_voo'])




# def classifica_turno(coluna_data_hora):
    
#     Regra de classificação:
#     06:00 - 12:00 : MANHÃ
#     12:00 - 18:00 : TARDE
#     18:00 - 00:00 : NOITE
#     00:00 - 06:00 : MADRUGADA

#     return coluna_turno
# '''


def calc_horas(coluna_tempo_voo):
    return coluna_tempo_voo * 60


# Aplicando a função na coluna
# df['tempo_voo_minutos'] = calc_horas(df['tempo_voo'])


def classifica_turno(coluna_data_hora):
    hora = coluna_data_hora.hour  # Extrai a hora da coluna datetime
    
    # Classificação com base nas faixas horárias
    if 6 <= hora < 12:
        return "MANHÃ"
    elif 12 <= hora < 18:
        return "TARDE"
    elif 18 <= hora < 24:
        return "NOITE"
    else:
        return "MADRUGADA"
    

# df['turno'] = df['data_hora'].apply(classifica_turno)
