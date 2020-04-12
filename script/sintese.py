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
pts = pd.read_csv(path+'/data/dados_partidos.csv')
print(np.unique(pts),len(np.unique(pts)))

# pts_d = dd.from_pandas(pts,npartitions=2)


# itens,cont = np.unique(pts.to_numpy(),return_counts=True)

# print(len(itens))
# for i in range(len(itens)):
    # print(itens[i],cont[i])
# print(np.unique(pts.to_numpy(),return_counts=True))