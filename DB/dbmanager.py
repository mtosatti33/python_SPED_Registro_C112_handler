from pathlib import Path
import os
import sqlite3
import csv
from arquivos import ArquivoExiste
import DB.queries as db
import config as cfg

def criabanco():
    if not ArquivoExiste(arquivo=cfg.ARQUIVO):
        Path(cfg.ARQUIVO).touch()

def insereDados():
    Reg0000()
    Reg0100()
    Reg0150()
    Reg0175()
    Reg0190()
    Reg0200()
    Reg0205()
    Reg0220()
    Reg0400()
    RegC100()
    RegC112()
    RegC113()
    RegC170()
    RegC180()
    RegC181()
    RegC185()
    RegC186()
    RegC190()
    RegD100()
    RegD190()
    RegE110()
    RegE115()
    RegE210()
    RegH010()
    RegH030()
    Reg1250()
    Reg1255()
    Reg1601()
    
def Reg0000():
    registro = '0000'
    criabanco()
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}
        
        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
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

            insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'],
                reg['REG'], 
                reg['COD_VER'], 
                reg['COD_FIN'], 
                reg['DT_INI'], 
                reg['DT_FIN'], 
                reg['NOME'], 
                reg['CNPJ'], 
                reg['CPF'], 
                reg['UF'], 
                reg['IE'], 
                reg['COD_MUN'], 
                reg['IM'], 
                reg['SUFRAMA'], 
                reg['IND_PERFIL'], 
                reg['IND_ATIV']
            )
            cursor.execute(insert)

        connection.commit()
        connection.close()

def Reg0100():
    registro = '0100'
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}

        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
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

            insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'],
                reg['REG'],
                reg['NOME'],
                reg['CPF'],
                reg['CRC'],
                reg['CNPJ'],
                reg['CEP'],
                reg['END'],
                reg['NUM'],
                reg['COMPL'],
                reg['BAIRRO'],
                reg['FONE'],
                reg['FAX'],
                reg['EMAIL'],
                reg['COD_MUN']
            )

            cursor.execute(insert)

        connection.commit()
        connection.close()

def Reg0150():
    registro = '0150'
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}
        
        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
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

            insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'],
                reg['REG'],
                reg['COD_PART'],
                reg['NOME'],
                reg['COD_PAIS'],
                reg['CNPJ'],
                reg['CPF'],
                reg['IE'],
                reg['COD_MUN'],
                reg['SUFRAMA'],
                reg['END'],
                reg['NUM'],
                reg['COMPL'],
                reg['BAIRRO']
                )
            
            cursor.execute(insert)

        connection.commit()
        connection.close()

def Reg0175():
    registro = '0175'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}
            
            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['DT_ALT'] = linha[2]
                    reg['NR_CAMPO'] = linha[3]
                    reg['CONT_ANT'] =  linha[4]
                    reg['ID_PAI'] = linha[5]

                
                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'], 
                    reg['DT_ALT'], 
                    reg['NR_CAMPO'], 
                    reg['CONT_ANT'], 
                    reg['ID_PAI']
                    )
                cursor.execute(insert)

            connection.commit()
            connection.close()

def Reg0190():
    registro = '0190'
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}

        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
                reg['REG'] = linha[1]
                reg['UNID'] = linha[2]
                reg['DESCR'] = linha[3]

            insert =  "insert into Reg{} values ('{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'],
                reg['REG'],
                reg['UNID'],
                reg['DESCR']
            )

            cursor.execute(insert)

        connection.commit()
        connection.close()

def Reg0200():
    registro = '0200'
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}

        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
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

            insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'],
                reg['REG'],
                reg['COD_ITEM'],
                reg['DESCR_ITEM'],
                reg['COD_BARRA'],
                reg['COD_ANT_ITEM'],
                reg['UNID_INV'],
                reg['TIPO_ITEM'],
                reg['COD_NCM'],
                reg['EX_IPI'],
                reg['COD_GEN'],
                reg['COD_LST'],
                reg['ALIQ_ICMS'],
                reg['CEST']
            )

            cursor.execute(insert)

            update_ALIQ_ICMS = "update Reg{} set ALIQ_ICMS = REPLACE(ALIQ_ICMS, ',', '.')".format(registro)

            cursor.execute(update_ALIQ_ICMS)

        connection.commit()
        connection.close()

def Reg0205():
    registro = '0205'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['DESCR_ANT_ITEM'] = linha[2]
                    reg['DT_INI'] = linha[3]
                    reg['DT_FIM'] =  linha[4]
                    reg['COD_ANT_ITEM'] = linha[5]
                    reg['ID_PAI'] = linha[6]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['DESCR_ANT_ITEM'],
                    reg['DT_INI'],
                    reg['DT_FIM'],
                    reg['COD_ANT_ITEM'],
                    reg['ID_PAI']
                )
                cursor.execute(insert)

            connection.commit()
            connection.close()

def Reg0220():
    registro = '0220'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['UNID_CONV'] = linha[2]
                    reg['FAT_CONV'] = linha[3]
                    reg['COD_BARRA'] =  linha[4]
                    reg['ID_PAI'] = linha[5]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['UNID_CONV'],
                    reg['FAT_CONV'],
                    reg['COD_BARRA'],
                    reg['ID_PAI']
                )
                cursor.execute(insert)

                update_FAT_CONV = "update Reg{} set FAT_CONV = REPLACE(FAT_CONV, ',', '.')".format(registro)
                cursor.execute(update_FAT_CONV)

            connection.commit()
            connection.close()

def Reg0400():
    registro = '0400'
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}

        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
                reg['REG'] = linha[1]
                reg['COD_NAT'] = linha[2]
                reg['DESCR_NAT'] = linha[3]

            insert =  "insert into Reg{} values ('{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'],
                reg['REG'],
                reg['COD_NAT'],
                reg['DESCR_NAT']
            )

            cursor.execute(insert)

        connection.commit()
        connection.close()

def RegC100():
    registro = 'C100'
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}

        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
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

            insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'],
                reg['REG'],
                reg['IND_OPER'],
                reg['IND_EMIT'],
                reg['COD_PART'],
                reg['COD_MOD'],
                reg['COD_SIT'],
                reg['SER'],
                reg['NUM_DOC'],
                reg['CHV_NFE'],
                reg['DT_DOC'],
                reg['DT_E_S'],
                reg['VL_DOC'],
                reg['IND_PGTO'],
                reg['VL_DESC'],
                reg['VL_ABAT_NT'],
                reg['VL_MERC'],
                reg['IND_FRT'],
                reg['VL_FRT'],
                reg['VL_SEG'],
                reg['VL_OUT_DA'],
                reg['VL_BC_ICMS'],
                reg['VL_ICMS'],
                reg['VL_BC_ICMS_ST'],
                reg['VL_ICMS_ST'],
                reg['VL_IPI'],
                reg['VL_PIS'],
                reg['VL_COFINS'],
                reg['VL_PIS_ST'],
                reg['VL_COFINS_ST']
            )

            cursor.execute(insert)

        connection.commit()
        connection.close()
def RegC112():
    registro = 'C112'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['COD_DA'] = linha[2]
                    reg['UF'] = linha[3]
                    reg['NUM_DA'] = linha[4]
                    reg['COD_AUT'] = linha[5]
                    reg['VL_DA'] = linha[6]
                    reg['DT_VCTO'] = linha[7]
                    reg['DT_PGTO'] = linha[8]
                    reg['ID_PAI'] = linha[9]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['COD_DA'],
                    reg['UF'],
                    reg['NUM_DA'],
                    reg['COD_AUT'],
                    reg['VL_DA'],
                    reg['DT_VCTO'],
                    reg['DT_PGTO'],
                    reg['ID_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

        
def RegC113():
    registro = 'C113'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['IND_OPER'] = linha[2]
                    reg['IND_EMIT'] = linha[3]
                    reg['COD_PART'] = linha[4]
                    reg['COD_MOD'] = linha[5]
                    reg['SER'] = linha[6]
                    reg['SUB'] = linha[7]
                    reg['NUM_DOC'] = linha[8]
                    reg['DT_DOC'] = linha[9]
                    reg['CHV_DOCe'] = linha[10]
                    reg['ID_PAI'] = linha[11]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['IND_OPER'], 
                    reg['IND_EMIT'], 
                    reg['COD_PART'], 
                    reg['COD_MOD'], 
                    reg['SER'], 
                    reg['SUB'], 
                    reg['NUM_DOC'], 
                    reg['DT_DOC'], 
                    reg['CHV_DOCe'], 
                    reg['ID_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()
def RegC170():
    registro = 'C170'
    with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
        # skip the header 
        next(csv_file_reader,None)

        reg = {}

        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()

        cursor.execute(db.dropTableQuery(registro))
        cursor.execute(db.createTableQuery(registro))

        for linha in csv_file_reader:

            for i in range(len(linha)):
                reg['NLINHA'] = linha[0]
                reg['REG'] = linha[1]
                reg['NUM_ITEM'] = linha[2]
                reg['COD_ITEM'] = linha[3]
                reg['DESCR_COMPL'] = linha[4]
                reg['QTD'] = linha[5]
                reg['UNID'] = linha[6]
                reg['VL_ITEM'] = linha[7]
                reg['VL_DESC'] = linha[8]
                reg['IND_MOV'] = linha[9]
                reg['CST_ICMS'] = linha[10]
                reg['CFOP'] = linha[11]
                reg['COD_NAT'] = linha[12]
                reg['VL_BC_ICMS'] = linha[13]
                reg['ALIQ_ICMS'] = linha[14]
                reg['VL_ICMS'] = linha[15]
                reg['VL_BC_ICMS_ST'] = linha[16] 
                reg['ALIQ_ST'] = linha[17]
                reg['VL_ICMS_ST'] = linha[18]
                reg['IND_APUR'] = linha[19]
                reg['CST_IPI'] = linha[20]
                reg['COD_ENQ'] = linha[21]
                reg['VL_BC_IPI'] = linha[22]
                reg['ALIQ_IPI'] = linha[23]
                reg['VL_IPI'] = linha[24]
                reg['CST_PIS'] = linha[25]
                reg['VL_BC_PIS'] = linha[26]
                reg['ALIQ_PIS'] = linha[27]
                reg['QUANT_BC_PIS'] = linha[28] 
                reg['ALIQ_PIS'] = linha[29]
                reg['VL_PIS'] = linha[30]
                reg['CST_COFINS'] = linha[31]
                reg['VL_BC_COFINS'] = linha[32]
                reg['ALIQ_COFINS'] = linha[33]
                reg['QUANT_BC_COFINS'] = linha[34]
                reg['ALIQ_COFINS'] = linha[35]
                reg['VL_COFINS'] = linha[36]
                reg['COD_CTA'] = linha[37]
                reg['VL_ABAT_NT'] = linha[38]
                reg['ID_PAI'] = linha[39]

            insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['NLINHA'], 
                reg['REG'], 
                reg['NUM_ITEM'], 
                reg['COD_ITEM'], 
                reg['DESCR_COMPL'], 
                reg['QTD'], 
                reg['UNID'], 
                reg['VL_ITEM'], 
                reg['VL_DESC'], 
                reg['IND_MOV'], 
                reg['CST_ICMS'], 
                reg['CFOP'], 
                reg['COD_NAT'], 
                reg['VL_BC_ICMS'], 
                reg['ALIQ_ICMS'], 
                reg['VL_ICMS'], 
                reg['VL_BC_ICMS_ST'], 
                reg['ALIQ_ST'], 
                reg['VL_ICMS_ST'], 
                reg['IND_APUR'], 
                reg['CST_IPI'], 
                reg['COD_ENQ'], 
                reg['VL_BC_IPI'], 
                reg['ALIQ_IPI'], 
                reg['VL_IPI'], 
                reg['CST_PIS'], 
                reg['VL_BC_PIS'], 
                reg['ALIQ_PIS'], 
                reg['QUANT_BC_PIS'], 
                reg['ALIQ_PIS'], 
                reg['VL_PIS'], 
                reg['CST_COFINS'], 
                reg['VL_BC_COFINS'], 
                reg['ALIQ_COFINS'], 
                reg['QUANT_BC_COFINS'], 
                reg['ALIQ_COFINS'], 
                reg['VL_COFINS'], 
                reg['COD_CTA'], 
                reg['VL_ABAT_NT'], 
                reg['ID_PAI']
            )

            cursor.execute(insert)

        connection.commit()
        connection.close()
def RegC180():
    registro = 'C180'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['COD_RESP_RET'] = linha[2]
                    reg['QUANT_CONV'] = linha[3]
                    reg['UNID'] = linha[4]
                    reg['VL_UNIT_CONV'] = linha[5]
                    reg['VL_UNIT_ICMS_OP_CONV'] = linha[6]
                    reg['VL_UNIT_BC_ICMS_ST_CONV'] = linha[7]
                    reg['VL_UNIT_ICMS_ST_CONV'] = linha[8]
                    reg['VL_UNIT_FCP_ST_CONV'] = linha[9]
                    reg['COD_DA'] = linha[10]
                    reg['NUM_DA'] = linha[11]
                    reg['ID_PAI'] = linha[12]
                    reg['PRODUTO_PAI'] = linha[13]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['COD_RESP_RET'], 
                    reg['QUANT_CONV'], 
                    reg['UNID'], 
                    reg['VL_UNIT_CONV'], 
                    reg['VL_UNIT_ICMS_OP_CONV'], 
                    reg['VL_UNIT_BC_ICMS_ST_CONV'], 
                    reg['VL_UNIT_ICMS_ST_CONV'], 
                    reg['VL_UNIT_FCP_ST_CONV'], 
                    reg['COD_DA'], 
                    reg['NUM_DA'], 
                    reg['ID_PAI'], 
                    reg['PRODUTO_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegC181():
    registro = 'C181'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['COD_MOT_REST_COMPL'] = linha[2]
                    reg['QUANT_CONV'] = linha[3]
                    reg['UNID'] = linha[4]
                    reg['COD_MOD_SAIDA'] = linha[5]
                    reg['SERIE_SAIDA'] = linha[6]
                    reg['ECF_FAB_SAIDA'] = linha[7]
                    reg['NUM_DOC_SAIDA'] = linha[8]
                    reg['CHV_DFE_SAIDA'] = linha[9]
                    reg['DT_DOC_SAIDA'] = linha[10]
                    reg['NUM_ITEM_SAIDA'] = linha[11]
                    reg['VL_UNIT_CONV_SAIDA'] = linha[12]
                    reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA'] = linha[13]
                    reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA'] = linha[14]
                    reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA'] = linha[15]
                    reg['VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA'] = linha[16]
                    reg['VL_UNIT_ICMS_OP_CONV_SAIDA'] = linha[17]
                    reg['VL_UNIT_ICMS_ST_CONV_REST'] = linha[18]
                    reg['VL_UNIT_FCP_ST_CONV_REST'] = linha[19]
                    reg['VL_UNIT_ICMS_ST_CONV_COMPL'] = linha[20]
                    reg['VL_UNIT_FCP_ST_CONV_COMPL'] = linha[21]
                    reg['ID_PAI'] = linha[22]
                    reg['PRODUTO_PAI'] = linha[23]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['COD_MOT_REST_COMPL'],
                    reg['QUANT_CONV'],
                    reg['UNID'],
                    reg['COD_MOD_SAIDA'],
                    reg['SERIE_SAIDA'],
                    reg['ECF_FAB_SAIDA'],
                    reg['NUM_DOC_SAIDA'],
                    reg['CHV_DFE_SAIDA'],
                    reg['DT_DOC_SAIDA'],
                    reg['NUM_ITEM_SAIDA'],
                    reg['VL_UNIT_CONV_SAIDA'],
                    reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA'],
                    reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA'],
                    reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA'],
                    reg['VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA'],
                    reg['VL_UNIT_ICMS_OP_CONV_SAIDA'],
                    reg['VL_UNIT_ICMS_ST_CONV_REST'],
                    reg['VL_UNIT_FCP_ST_CONV_REST'],
                    reg['VL_UNIT_ICMS_ST_CONV_COMPL'],
                    reg['VL_UNIT_FCP_ST_CONV_COMPL'],
                    reg['ID_PAI'],
                    reg['PRODUTO_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegC185():
    registro = 'C185'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['NUM_ITEM'] = linha[2]
                    reg['COD_ITEM'] = linha[3]
                    reg['CST_ICMS'] = linha[4]
                    reg['CFOP'] = linha[5]
                    reg['COD_MOT_REST_COMPL'] = linha[6]
                    reg['QUANT_CONV'] = linha[7]
                    reg['UNID'] = linha[8]
                    reg['VL_UNIT_CONV'] = linha[9]
                    reg['VL_UNIT_ICMS_NA_OPERACAO_CONV'] = linha[10] 
                    reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV'] = linha[11]
                    reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV'] = linha[12]
                    reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV'] = linha[13]
                    reg['VL_UNIT_ICMS_ST_CONV_REST'] = linha[14] 
                    reg['VL_UNIT_FCP_ST_CONV_REST'] = linha[15]
                    reg['VL_UNIT_ICMS_ST_CONV_COMPL'] = linha[16]
                    reg['VL_UNIT_FCP_ST_CONV_'] = linha[17]
                    reg['ID_PAI'] = linha[18]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['NUM_ITEM'], 
                    reg['COD_ITEM'], 
                    reg['CST_ICMS'], 
                    reg['CFOP'], 
                    reg['COD_MOT_REST_COMPL'], 
                    reg['QUANT_CONV'], 
                    reg['UNID'], 
                    reg['VL_UNIT_CONV'], 
                    reg['VL_UNIT_ICMS_NA_OPERACAO_CONV'], 
                    reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV'], 
                    reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV'], 
                    reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV'], 
                    reg['VL_UNIT_ICMS_ST_CONV_REST'], 
                    reg['VL_UNIT_FCP_ST_CONV_REST'], 
                    reg['VL_UNIT_ICMS_ST_CONV_COMPL'], 
                    reg['VL_UNIT_FCP_ST_CONV_'], 
                    reg['ID_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegC186():
    registro = 'C186'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1] 
                    reg['NUM_ITEM'] = linha[2] 
                    reg['COD_ITEM'] = linha[3]
                    reg['CST_ICMS'] = linha[4]
                    reg['CFOP'] = linha[5]
                    reg['COD_MOT_REST_COMPL'] = linha[6]
                    reg['QUANT_CONV'] = linha[7]
                    reg['UNID'] = linha[8]
                    reg['COD_MOD_ENTRADA'] = linha[9]
                    reg['SERIE_ENTRADA'] = linha[10]
                    reg['NUM_DOC_ENTRADA'] = linha[11]
                    reg['CHV_DFE_ENTRADA'] = linha[12]
                    reg['DT_DOC_ENTRADA'] = linha[13]
                    reg['NUM_ITEM_ENTRADA'] = linha[14]
                    reg['VL_UNIT_CONV_ENTRADA'] = linha[15] 
                    reg['VL_UNIT_ICMS_OP_CONV_'] = linha[16] 
                    reg['VL_UNIT_BC_ICMS_ST'] = linha[17]
                    reg['VL_UNIT_ICMS_ST_CONV_ENTRADA'] = linha[18]
                    reg['VL_UNIT_FCP_ST_CONV_ENTRADA'] = linha[19]
                    reg['ID_PAI'] = linha[20]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['NUM_ITEM'], 
                    reg['COD_ITEM'], 
                    reg['CST_ICMS'], 
                    reg['CFOP'], 
                    reg['COD_MOT_REST_COMPL'], 
                    reg['QUANT_CONV'], 
                    reg['UNID'], 
                    reg['COD_MOD_ENTRADA'], 
                    reg['SERIE_ENTRADA'], 
                    reg['NUM_DOC_ENTRADA'], 
                    reg['CHV_DFE_ENTRADA'], 
                    reg['DT_DOC_ENTRADA'], 
                    reg['NUM_ITEM_ENTRADA'], 
                    reg['VL_UNIT_CONV_ENTRADA'], 
                    reg['VL_UNIT_ICMS_OP_CONV_'], 
                    reg['VL_UNIT_BC_ICMS_ST'], 
                    reg['VL_UNIT_ICMS_ST_CONV_ENTRADA'], 
                    reg['VL_UNIT_FCP_ST_CONV_ENTRADA'], 
                    reg['ID_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegC190():
    registro = 'C190'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['CST_ICMS'] = linha[2]
                    reg['CFOP'] = linha[3]
                    reg['ALIQ_ICMS'] = linha[4]
                    reg['VL_OPR'] = linha[5]
                    reg['VL_BC_ICMS'] = linha[6]
                    reg['VL_ICMS'] = linha[7]
                    reg['VL_BC_ICMS_'] = linha[8]
                    reg['VL_ICMS_ST'] = linha[9]
                    reg['VL_RED_BC'] = linha[10]
                    reg['VL_IPI'] = linha[11]
                    reg['COD_OBS'] = linha[12]
                    reg['ID_PAI'] = linha[13]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['CST_ICMS'], 
                    reg['CFOP'], 
                    reg['ALIQ_ICMS'], 
                    reg['VL_OPR'], 
                    reg['VL_BC_ICMS'], 
                    reg['VL_ICMS'], 
                    reg['VL_BC_ICMS_'], 
                    reg['VL_ICMS_ST'], 
                    reg['VL_RED_BC'], 
                    reg['VL_IPI'], 
                    reg['COD_OBS'], 
                    reg['ID_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegE110():
    registro = 'E110'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['VL_TOT_DEBITOS'] = linha[2]
                    reg['VL_AJ_DEBITOS'] = linha[3]
                    reg['VL_TOT_AJ_DEBITOS'] = linha[4]
                    reg['VL_ESTORNOS_CRED'] = linha[5]
                    reg['VL_TOT_CREDITOS'] = linha[6]
                    reg['VL_AJ_CREDITOS'] = linha[7]
                    reg['VL_TOT_AJ_CREDITOS'] = linha[8]
                    reg['VL_ESTORNOS_DEB'] = linha[9]
                    reg['VL_SLD_CREDOR_ANT'] = linha[10]
                    reg['VL_SLD_APURADO'] = linha[11]
                    reg['VL_TOT_DED'] = linha[12]
                    reg['VL_ICMS_RECOLHER'] = linha[13]
                    reg['VL_SLD_CREDOR_TRANSPORTAR'] = linha[14]
                    reg['DEB_ESP'] = linha[15]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['VL_TOT_DEBITOS'], 
                    reg['VL_AJ_DEBITOS'], 
                    reg['VL_TOT_AJ_DEBITOS'], 
                    reg['VL_ESTORNOS_CRED'], 
                    reg['VL_TOT_CREDITOS'], 
                    reg['VL_AJ_CREDITOS'], 
                    reg['VL_TOT_AJ_CREDITOS'], 
                    reg['VL_ESTORNOS_DEB'], 
                    reg['VL_SLD_CREDOR_ANT'], 
                    reg['VL_SLD_APURADO'], 
                    reg['VL_TOT_DED'], 
                    reg['VL_ICMS_RECOLHER'], 
                    reg['VL_SLD_CREDOR_TRANSPORTAR'], 
                    reg['DEB_ESP']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegE115():
    registro = 'E115'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['COD_INF_ADIC'] = linha[2]
                    reg['VL_INF_ADIC'] = linha[3]
                    reg['DESCR_COMPL_AJ'] = linha[4]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['COD_INF_ADIC'], 
                    reg['VL_INF_ADIC'], 
                    reg['DESCR_COMPL_AJ']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegE210():
    registro = 'E210'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['IND_MOV_ST'] = linha[2]
                    reg['VL_SLD_CRED_ANT_ST'] = linha[3]
                    reg['VL_DEVOL_ST'] = linha[4]
                    reg['VL_RESSARC_ST'] = linha[5]
                    reg['VL_OUT_CRED_ST'] = linha[6]
                    reg['VL_AJ_CREDITOS_ST'] = linha[7]
                    reg['VL_RETENCAO_ST'] = linha[8]
                    reg['VL_OUT_DEB_ST'] = linha[9]
                    reg['VL_AJ_DEBITOS_ST'] = linha[10]
                    reg['VL_SLD_DEV_ANT_ST'] = linha[11]
                    reg['VL_DEDUCOES_ST'] = linha[12]
                    reg['VL_ICMS_RECOL_ST'] = linha[13]
                    reg['VL_SLD_CRED_ST_TRANSPORTAR'] = linha[14]
                    reg['DEB_ESP_ST'] = linha[15]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['IND_MOV_ST'], 
                    reg['VL_SLD_CRED_ANT_ST'], 
                    reg['VL_DEVOL_ST'], 
                    reg['VL_RESSARC_ST'], 
                    reg['VL_OUT_CRED_ST'], 
                    reg['VL_AJ_CREDITOS_ST'], 
                    reg['VL_RETENCAO_ST'], 
                    reg['VL_OUT_DEB_ST'], 
                    reg['VL_AJ_DEBITOS_ST'], 
                    reg['VL_SLD_DEV_ANT_ST'], 
                    reg['VL_DEDUCOES_ST'], 
                    reg['VL_ICMS_RECOL_ST'], 
                    reg['VL_SLD_CRED_ST_TRANSPORTAR'], 
                    reg['DEB_ESP_ST']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegH010():
    registro = 'H010'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['COD_ITEM'] = linha[2]
                    reg['UNID'] = linha[3]
                    reg['QTD'] = linha[4]
                    reg['VL_UNIT'] = linha[5]
                    reg['VL_ITEM'] = linha[6]
                    reg['IND_PROP'] = linha[7]
                    reg['COD_PART'] = linha[8]
                    reg['TXT_COMPL'] = linha[9]
                    reg['COD_CTA'] = linha[10]
                    reg['VL_ITEM_IR'] = linha[11]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['COD_ITEM'], 
                    reg['UNID'], 
                    reg['QTD'], 
                    reg['VL_UNIT'], 
                    reg['VL_ITEM'], 
                    reg['IND_PROP'], 
                    reg['COD_PART'], 
                    reg['TXT_COMPL'], 
                    reg['COD_CTA'], 
                    reg['VL_ITEM_IR'] 
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegH030():
    registro = 'H030'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['VL_ICMS_OP'] = linha[2]
                    reg['VL_BC_ICMS_ST'] = linha[3]
                    reg['VL_ICMS_ST'] = linha[4]
                    reg['VL_FCP'] = linha[5]
                    reg['ID_PAI'] = linha[6]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'], 
                    reg['REG'], 
                    reg['VL_ICMS_OP'], 
                    reg['VL_BC_ICMS_ST'], 
                    reg['VL_ICMS_ST'], 
                    reg['VL_FCP'], 
                    reg['ID_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def Reg1250():
    registro = '1250'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['VL_CREDITO_ICMS_OP'] = linha[2]
                    reg['VL_ICMS_ST_REST'] = linha[3]
                    reg['VL_FCP_ST_REST'] = linha[4]
                    reg['VL_ICMS_ST_COMPL'] = linha[5]
                    reg['VL_FCP_ST_COMPL'] = linha[6]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['VL_CREDITO_ICMS_OP'],
                    reg['VL_ICMS_ST_REST'],
                    reg['VL_FCP_ST_REST'],
                    reg['VL_ICMS_ST_COMPL'],
                    reg['VL_FCP_ST_COMPL']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def Reg1255():
    registro = '1255'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['COD_MOT_REST_COMPL'] = linha[2]
                    reg['VL_CREDITO_ICMS_OP_MOT'] = linha[3]
                    reg['VL_ICMS_ST_REST_MOT'] = linha[4]
                    reg['VL_FCP_ST_REST_MOT'] = linha[5]
                    reg['VL_ICMS_ST_COMPL_MOT'] = linha[6]
                    reg['VL_FCP_ST_COMPL_MOT'] = linha[7]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['COD_MOT_REST_COMPL'],
                    reg['VL_CREDITO_ICMS_OP_MOT'],
                    reg['VL_ICMS_ST_REST_MOT'],
                    reg['VL_FCP_ST_REST_MOT'],
                    reg['VL_ICMS_ST_COMPL_MOT'],
                    reg['VL_FCP_ST_COMPL_MOT']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def Reg1601():
    registro = '1601'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['COD_PART_IP'] = linha[2]
                    reg['COD_PART_IT'] = linha[3]
                    reg['TOT_VS'] = linha[4]
                    reg['TOT_ISS'] = linha[5]
                    reg['TOT_OUTROS'] = linha[6]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['COD_PART_IP'],
                    reg['COD_PART_IT'],
                    reg['TOT_VS'],
                    reg['TOT_ISS'],
                    reg['TOT_OUTROS']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()

def RegD100():
    registro = 'D100'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['IND_OPER'] = linha[2]
                    reg['IND_EMIT'] = linha[3]
                    reg['COD_PART'] = linha[4]
                    reg['COD_MOD'] = linha[5]
                    reg['COD_SIT'] = linha[6]
                    reg['SER'] = linha[7]
                    reg['SUB'] = linha[8]
                    reg['NUM_DOC'] = linha[9]
                    reg['CHV_CTE'] = linha[10]
                    reg['DT_DOC'] = linha[11]
                    reg['DT_A_P'] = linha[12]
                    reg['TP_CTE'] = linha[13]
                    reg['CHV_CTE_REF'] = linha[14]
                    reg['VL_DOC'] = linha[15]
                    reg['VL_DESC'] = linha[16]
                    reg['IND_FRT'] = linha[17]
                    reg['VL_SERV'] = linha[18]
                    reg['VL_BC_ICMS'] = linha[19]
                    reg['VL_ICMS'] = linha[20]
                    reg['VL_NT'] = linha[21]
                    reg['COD_INF'] = linha[22]
                    reg['COD_CTA'] = linha[23]
                    reg['COD_MUN_ORIG'] = linha[24]
                    reg['COD_MUN_DEST'] = linha[25]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['IND_OPER'],
                    reg['IND_EMIT'],
                    reg['COD_PART'],
                    reg['COD_MOD'],
                    reg['COD_SIT'],
                    reg['SER'],
                    reg['SUB'],
                    reg['NUM_DOC'],
                    reg['CHV_CTE'],
                    reg['DT_DOC'],
                    reg['DT_A_P'],
                    reg['TP_CTE'],
                    reg['CHV_CTE_REF'],
                    reg['VL_DOC'],
                    reg['VL_DESC'],
                    reg['IND_FRT'],
                    reg['VL_SERV'],
                    reg['VL_BC_ICMS'],
                    reg['VL_ICMS'],
                    reg['VL_NT'],
                    reg['COD_INF'],
                    reg['COD_CTA'],
                    reg['COD_MUN_ORIG'],
                    reg['COD_MUN_DEST']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()


def RegD190():
    registro = 'D190'

    if ArquivoExiste(cfg.TEMPLATE.format(registro)):
        with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
            # create the object of csv.reader()
            csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
            # skip the header 
            next(csv_file_reader,None)

            reg = {}

            connection = sqlite3.connect(cfg.ARQUIVO)
            cursor = connection.cursor()

            cursor.execute(db.dropTableQuery(registro))
            cursor.execute(db.createTableQuery(registro))

            for linha in csv_file_reader:

                for i in range(len(linha)):
                    reg['NLINHA'] = linha[0]
                    reg['REG'] = linha[1]
                    reg['CST_ICMS'] = linha[2]
                    reg['CFOP'] = linha[3]
                    reg['ALIQ_ICMS'] = linha[4]
                    reg['VL_OPR'] = linha[5]
                    reg['VL_BC_ICMS'] = linha[6]
                    reg['VL_ICMS'] = linha[7]
                    reg['VL_RED_BC'] = linha[8]
                    reg['COD_OBS'] = linha[9]
                    reg['ID_PAI'] = linha[10]

                insert =  "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    registro,
                    reg['NLINHA'],
                    reg['REG'],
                    reg['CST_ICMS'],
                    reg['CFOP'],
                    reg['ALIQ_ICMS'],
                    reg['VL_OPR'],
                    reg['VL_BC_ICMS'],
                    reg['VL_ICMS'],
                    reg['VL_RED_BC'],
                    reg['COD_OBS'],
                    reg['ID_PAI']
                )

                cursor.execute(insert)

            connection.commit()
            connection.close()