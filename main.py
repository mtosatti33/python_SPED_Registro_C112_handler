import arquivos
import Blocos.registros as registros

arquivos.ApagarArquivosCSV()
if __name__ == "__main__":
    for x in arquivos.ListarArquivos():
        registros.GerarRegistros(arquivo=x)