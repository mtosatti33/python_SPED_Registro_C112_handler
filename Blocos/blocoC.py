from csv import DictWriter
import DB.headers as headers
import config as cfg

"""Bloco C: Notas Fiscais de Mercadorias"""
class BlocoC():
    def __init__(self) -> None:
        pass
        
    def regC100(self, nlinha, linha, registro):
        """Registro de Notas Fiscais de Mercadorias"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['IND_OPER'] = linha[2]
            reg['IND_EMIT'] = linha[3]
            reg['COD_PART'] = linha[4]
            reg['COD_MOD'] = linha[5]
            reg['COD_SIT'] = linha[6]
            reg['SER'] = linha[7]
            reg['NUM_DOC'] = linha[8]
            reg['CHV_NFE'] = linha[9]
            reg['DT_DOC'] = linha[10]
            reg['DT_E_S'] = linha[11]
            reg['VL_DOC'] = linha[12]
            reg['IND_PGTO'] = linha[13]
            reg['VL_DESC'] = linha[14]
            reg['VL_ABAT_NT'] = linha[15]
            reg['VL_MERC'] = linha[16]
            reg['IND_FRT'] = linha[17]
            reg['VL_FRT'] = linha[18]
            reg['VL_SEG'] = linha[19]
            reg['VL_OUT_DA'] = linha[20]
            reg['VL_BC_ICMS'] = linha[21]
            reg['VL_ICMS'] = linha[22]
            reg['VL_BC_ICMS_ST'] = linha[23]
            reg['VL_ICMS_ST'] = linha[24]
            reg['VL_IPI'] = linha[25]
            reg['VL_PIS'] = linha[26]
            reg['VL_COFINS'] = linha[27]
            reg['VL_PIS_ST'] = linha[28]
            reg['VL_COFINS_ST'] = linha[29]
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def regC112(self, nlinha, linha, registro, idPai, participante, cnpj):
        """Documento de Arrecadação (GNRE, GA)"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['COD_DA'] = linha[2]
            reg['UF'] = linha[3]
            reg['NUM_DA'] = linha[4]
            reg['COD_AUT'] = linha[5]
            reg['VL_DA'] = linha[6]
            reg['DT_VCTO'] = linha[7]
            reg['DT_PGTO'] = linha[8]
            reg['ID_PAI'] = idPai
            reg['PARTICIPANTE'] = participante
            reg['CNPJ'] = cnpj
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)