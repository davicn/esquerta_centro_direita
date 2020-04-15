import numpy as np
import pandas as pd
import os
import dask.dataframe as dd
import dask as dk
from numba import njit


@njit
def cont(x):
    return np.unique(x)


path = os.getcwd()
files = pd.read_csv(path+'/data/lista.txt', header=None).to_numpy()[:, 0]

use = ['SIGLA DO PARTIDO', 'NOME DO PARTIDO', 'UF',
       'CODIGO DO MUNICIPIO', 'NOME DO MUNICIPIO']

frames = []

for i in range(len(files)):
    d = pd.read_csv(path+'/data/'+files[i], sep=';', encoding='ISO-8859-1')
    d = d[d['SITUACAO DO REGISTRO'] == 'REGULAR']
    conta = d['NOME DO MUNICIPIO'].value_counts().to_numpy()
    d = d.loc[:, use].drop_duplicates()
    d['NUM FILIADOS'] = conta
    frames.append(d)
    print(d)

result = pd.concat(frames)

result.to_csv('result_data.csv', index=False)


# frames.append(d)
# print(d['NOME DO MUNICIPIO'].value_counts().to_numpy())
# result = pd.concat(frames)
# print(result.head(len(result)-1))

# print(result.columns)
# with open(path+'/data/'+files[0], 'rb') as f:
#    contents = f.read()

# print(type(contents))
# print(np.unique(pts),len(np.unique(pts)))

# pts_d = dd.from_pandas(pts,npartitions=2)


# itens,cont = np.unique(pts.to_numpy(),return_counts=True)

# print(len(itens))
# for i in range(len(itens)):
# print(itens[i],cont[i])
# print(np.unique(pts.to_numpy(),return_counts=True))
