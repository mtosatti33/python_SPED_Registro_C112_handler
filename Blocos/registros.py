import re
from Blocos.blocoC import BlocoC
from Blocos.bloco0 import Bloco0
import config as cfg

bloco0 = Bloco0()
blocoC = BlocoC()

def GerarRegistros(arquivo):

    f = open(arquivo, "r", encoding=cfg.ENCODING_ISO)
    idPai = ''
    participante = ''
    nlinha = 1
    cnpj = ''
    for i in f:
        x = re.split("\|", i)
        if x[1] == "0000":
            cnpj = x[7]
            bloco0.reg0000(nlinha, x, x[1])
        if x[1] == "C100" and x[2] == "0" and x[3] == "1":
            idPai = x[8]                            #Necessário pra preencher os registros filhos
            participante = x[4]
            blocoC.regC100(nlinha, x, x[1])
        elif x[1] == "C112":
            blocoC.regC112(nlinha, x, x[1], idPai, participante, cnpj)

        """elif x[1] == "C113":
            break"""

        nlinha += 1