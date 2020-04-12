import os 
import pandas as pd 

PATH = os.getcwd()
file = PATH + '/data/folders.txt'
print(file)
f = pd.read_csv(file,header=None)
f = f[0].to_numpy()

for i in range(len(f)):
    os.system("unzip -o "+file.replace('folders.txt','')+f[i])