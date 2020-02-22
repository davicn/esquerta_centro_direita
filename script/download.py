import os
import pandas as pd

PATH = os.getcwd()

partidos = pd.read_csv(PATH + '/docs/partidos.csv')
uf = pd.read_csv(PATH + '/docs/uf.csv')

# http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_PARTIDO_UF.zip
p = partidos['sigla'].to_numpy()
u = uf['uf'].to_numpy()

for i in range(len(p)):
    for ii in range(len(u)):
        os.system("wget http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_" +
              p[i].lower()+"_"+u[ii].lower()+".zip")

        # print(p[i].lower()+"_"+u[ii].lower())
        # print(str(partidos.iloc[i]).lower()+"_"+str(uf.iloc[i]).lower())
