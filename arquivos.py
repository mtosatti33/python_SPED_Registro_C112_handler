import pandas as pd
import os
import glob

csvfile = None

def ApagarArquivosCSV():
    path = "CSV\\"
    for arquivo in os.listdir(path):
        os.remove(path + arquivo)

def SalvarParaCSV(lista, reg):
    df = pd.json_normalize(lista, errors='ignore')
    #print(df)

    if os.name == "nt":
        #Windows
        df.to_csv('CSV\\Reg{}.csv'.format(reg), sep=';', encoding='utf-8', index=False)
    else:
        #Linux
        df.to_csv('CSV/Reg{}.csv'.format(reg), sep=';', encoding='utf-8', index=False)

def ArquivoExiste(arquivo):
    return os.path.exists(arquivo)

def ListarArquivos():
    return glob.glob('C:\\Users\\Marcelo\Dropbox\\SPED\\Arquivos SPED\\**\\**\\*.txt', recursive=False)