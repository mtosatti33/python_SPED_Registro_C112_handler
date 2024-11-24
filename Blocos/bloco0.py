from csv import DictWriter
import DB.headers as headers
import config as cfg

"""Bloco 0: Cadastros"""
class Bloco0():
    def __init__(self) -> None:
        pass

        
    def reg0000(self, nlinha, linha, registro):
        """Registro da Empresa"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['COD_VER'] = linha[2]
            reg['COD_FIN'] = linha[3]
            reg['DT_INI'] = linha[4]
            reg['DT_FIN'] = linha[5]
            reg['NOME'] = linha[6]
            reg['CNPJ'] = linha[7]
            reg['CPF'] = linha[8]
            reg['UF'] = linha[9]
            reg['IE'] = linha[10]
            reg['COD_MUN'] = linha[11]
            reg['IM'] = linha[12]
            reg['SUFRAMA'] = linha[13]
            reg['IND_PERFIL'] = linha[14]
            reg['IND_ATIV'] = linha[15]
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0100(self, nlinha, linha, registro):
        """Registro do Contabilista"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['NOME'] = linha[2]
            reg['CPF'] = linha[3]
            reg['CRC'] = linha[4]
            reg['CNPJ'] = linha[5]
            reg['CEP'] = linha[6]
            reg['END'] = linha[7]
            reg['NUM'] = linha[8]
            reg['COMPL'] = linha[9]
            reg['BAIRRO'] = linha[10]
            reg['FONE'] = linha[11]
            reg['FAX'] = linha[12]
            reg['EMAIL'] = linha[13]
            reg['COD_MUN'] = linha[14]
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0150(self, nlinha, linha, registro):
        """Registro dos Participantes"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['COD_PART'] =  linha[2]
            reg['NOME'] = linha[3]
            reg['COD_PAIS'] = linha[4]
            reg['CNPJ'] = linha[5]
            reg['CPF'] = linha[6]
            reg['IE'] = linha[7]
            reg['COD_MUN'] = linha[8]
            reg['SUFRAMA'] = linha[9]
            reg['END'] = linha[10]
            reg['NUM'] = linha[11]
            reg['COMPL'] = linha[12]
            reg['BAIRRO'] = linha[13]
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0175(self, nlinha, linha, registro, idPai):
        """Alteração do Registro 0150"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['DT_ALT'] = linha[2]
            reg['NR_CAMPO'] = linha[3]
            reg['CONT_ANT'] =  linha[4]
            reg['ID_PAI'] = idPai
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0190(self, nlinha, linha, registro):
        """Registro Das Unidades de Conversão"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['UNID'] = linha[2]
            reg['DESCR'] = linha[3]
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0200(self, nlinha, linha, registro):
        """Registro de Produtos e Serviços"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['COD_ITEM'] = linha[2]
            reg['DESCR_ITEM'] = linha[3]
            reg['COD_BARRA'] = linha[4]
            reg['COD_ANT_ITEM'] = linha[5]
            reg['UNID_INV'] = linha[6]
            reg['TIPO_ITEM'] = linha[7]
            reg['COD_NCM'] = linha[8]
            reg['EX_IPI'] = linha[9]
            reg['COD_GEN'] = linha[10]
            reg['COD_LST'] = linha[11]
            reg['ALIQ_ICMS'] = linha[12]
            reg['CEST'] = linha[13]
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0205(self, nlinha, linha, registro, idPai):
        """Alteração do Registro 0200"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['DESCR_ANT_ITEM'] = linha[2]
            reg['DT_INI'] = linha[3]
            reg['DT_FIM'] =  linha[4]
            reg['COD_ANT_ITEM'] = linha[5]
            reg['ID_PAI'] = idPai
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0220(self, nlinha, linha, registro, idPai):
        """Fator de Conversão do Registro 0200"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['UNID_CONV'] = linha[2]
            reg['FAT_CONV'] = linha[3]
            reg['COD_BARRA'] =  linha[4]
            reg['ID_PAI'] = idPai
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)

    def reg0400(self, nlinha, linha, registro):
        """Registro de Naturezas de Operação"""
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg['NLINHA'] = nlinha
            reg['REG'] = linha[1]
            reg['COD_NAT'] = linha[2]
            reg['DESCR_NAT'] = linha[3]
        
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)
