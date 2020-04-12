import numpy as np
import pandas as pd
import os

path = os.getcwd()
files = pd.read_csv(path+'/data/lista.txt', header=None).to_numpy()
files = files.reshape(len(files))

# SIGLA DO PARTIDO, UF, NOME DO MUNICIPIO
dados = []
for i in range(len(files)):
    data = pd.read_csv(path+'/data/'+files[i], encoding="ISO-8859-1", sep=';')
    aux = data[data['SITUACAO DO REGISTRO'] == 'REGULAR'].iloc[:, [4, 6, 8]].to_numpy()
    for ii in aux:
        print(ii)
        dados.append(ii)

pd.DataFrame(data=dados,columns=['sigla','uf','municipio']).to_csv('dados_partidos.csv',index=False)
