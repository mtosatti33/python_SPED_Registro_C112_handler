
def createTableQuery(registro):
    if registro == '0000':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4), 
                COD_VER int, 
                COD_FIN int, 
                DT_INI varchar(8), 
                DT_FIN varchar(8), 
                NOME varchar(100), 
                CNPJ varchar(14), 
                CPF varchar(11), 
                UF varchar(2), 
                IE varchar(14), 
                COD_MUN varchar(7), 
                IM varchar(15), 
                SUFRAMA varchar(9), 
                IND_PERFIL varchar(1), 
                IND_ATIV int);'''.format(registro)
    
    elif registro == '0100':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                NOME varchar(100),
                CPF varchar(11),
                CRC varchar(15),
                CNPJ varchar(14),
                CEP varchar(8),
                END varchar(60),
                NUM varchar(10),
                COMPL varchar(60),
                BAIRRO varchar(60),
                FONE varchar(11),
                FAX varchar(11),
                EMAIL varchar(255),
                COD_MUN varchar(7));'''.format(registro)
    
    elif registro == '0150':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                COD_PART varchar(60),
                NOME varchar(100),
                COD_PAIS varchar(5),
                CNPJ varchar(14),
                CPF varchar(11),
                IE varchar(14),
                COD_MUN varchar(7),
                SUFRAMA varchar(9),
                END varchar(60),
                NUM varchar(10),
                COMPL varchar(60),
                BAIRRO varchar(60));'''.format(registro)
    
    elif registro =='0175':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                DT_ALT varchar(8),
                NR_CAMPO varchar(2),
                CONT_ANT varchar(100),
                ID_PAI varchar(60));'''.format(registro)
    
    elif registro == '0190':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                UNID varchar(6),
                DESCR varchar(255));'''.format(registro)

    elif registro == '0200':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                COD_ITEM varchar(60),
                DESCR_ITEM varchar(100),
                COD_BARRA varchar(14),
                COD_ANT_ITEM varchar(60),
                UNID_INV varchar(6),
                TIPO_ITEM varchar(2),
                COD_NCM varchar(8),
                EX_IPI varchar(3),
                COD_GEN varchar(2),
                COD_LST varchar(5),
                ALIQ_ICMS numeric(3,2),
                CEST varchar(7));'''.format(registro)
    
    elif registro == '0205':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                DESCR_ANT_ITEM varchar(255),
                DT_INI varchar(8),
                DT_FIM varchar(8),
                COD_ANT_ITEM varchar(60),
                ID_PAI varchar(60));'''.format(registro)
    
    elif registro == '0220':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                UNID_CONV varchar(6),
                FAT_CONV numeric(3,10),
                COD_BARRA varchar(14),
                ID_PAI varchar(60));'''.format(registro)
    
    elif registro == '0400':
        return '''create table if not exists Reg{}(
                NLINHA int,
                REG varchar(4),
                COD_NAT varchar(10),
                DESCR_NAT varchar(255));'''.format(registro)
    
    elif registro == 'C100':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                IND_OPER varchar(1), 
                IND_EMIT varchar(1), 
                COD_PART varchar(60), 
                COD_MOD varchar(2), 
                COD_SIT varchar(2), 
                SER varchar(3), 
                NUM_DOC varchar(9), 
                CHV_NFE varchar(44), 
                DT_DOC varchar(8), 
                DT_E_S varchar(8), 
                VL_DOC numeric(7,2), 
                IND_PGTO varchar(1), 
                VL_DESC numeric(5,2), 
                VL_ABAT_NT numeric(5,2), 
                VL_MERC numeric(7,2), 
                IND_FRT varchar(1), 
                VL_FRT numeric(7,2), 
                VL_SEG numeric(7,2), 
                VL_OUT_DA numeric(7,2), 
                VL_BC_ICMS numeric(7,2), 
                VL_ICMS numeric(7,2), 
                VL_BC_ICMS_ST numeric(7,2), 
                VL_ICMS_ST numeric(7,2), 
                VL_IPI numeric(7,2), 
                VL_PIS numeric(7,2), 
                VL_COFINS numeric(7,2), 
                VL_PIS_ST numeric(7,2), 
                VL_COFINS_ST numeric(7,2)
                );'''.format(registro)
    
    elif registro == 'C112':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                COD_DA varchar(1), 
                UF varchar(2), 
                NUM_DA varchar(255), 
                COD_AUT varchar(255), 
                VL_DA numeric(5,2), 
                DT_VCTO varchar(8), 
                DT_PGTO varchar(8), 
                ID_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'C113':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                IND_OPER varchar(1), 
                IND_EMIT varchar(1), 
                COD_PART varchar(60), 
                COD_MOD varchar(2), 
                SER varchar(4), 
                SUB varchar(3), 
                NUM_DOC varchar(9), 
                DT_DOC varchar(8), 
                CHV_DOCe varchar(44), 
                ID_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'C170':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                NUM_ITEM varchar(3), 
                COD_ITEM varchar(60), 
                DESCR_COMPL varchar(255), 
                QTD varchar(7,5), 
                UNID varchar(6), 
                VL_ITEM numeric(8,2), 
                VL_DESC numeric(8,2), 
                IND_MOV varchar(1), 
                CST_ICMS varchar(3), 
                CFOP varchar(4), 
                COD_NAT varchar(10), 
                VL_BC_ICMS numeric(8,2), 
                ALIQ_ICMS numeric(8,2), 
                VL_ICMS numeric(8,2), 
                VL_BC_ICMS_ST numeric(8,2), 
                ALIQ_ST numeric(8,2), 
                VL_ICMS_ST numeric(8,2), 
                IND_APUR varchar(1), 
                CST_IPI varchar(2), 
                COD_ENQ varchar(3), 
                VL_BC_IPI numeric(8,2), 
                ALIQ_IPI numeric(8,2), 
                VL_IPI numeric(8,2), 
                CST_PIS numeric(8,2), 
                VL_BC_PIS numeric(8,2), 
                ALIQ_PIS_PCT numeric(8,2), 
                QUANT_BC_PIS numeric(8,2), 
                ALIQ_PIS_RS numeric(8,2), 
                VL_PIS numeric(8,2), 
                CST_COFINS numeric(8,2), 
                VL_BC_COFINS numeric(8,2), 
                ALIQ_COFINS_PCT numeric(8,2), 
                QUANT_BC_COFINS numeric(8,2), 
                ALIQ_COFINS_RS numeric(8,2), 
                VL_COFINS numeric(8,2), 
                COD_CTA numeric(8,2), 
                VL_ABAT_NT numeric(8,2), 
                ID_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'C180':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                COD_RESP_RET varchar(1), 
                QUANT_CONV numeric(6,6), 
                UNID varchar(6), 
                VL_UNIT_CONV numeric(6,6), 
                VL_UNIT_ICMS_OP_CONV numeric(6,6), 
                VL_UNIT_BC_ICMS_ST_CONV numeric(6,6), 
                VL_UNIT_ICMS_ST_CONV numeric(6,6), 
                VL_UNIT_FCP_ST_CONV numeric(6,6), 
                COD_DA varchar(1), 
                NUM_DA varchar(255), 
                ID_PAI varchar(60), 
                PRODUTO_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'C181':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                COD_MOT_REST_COMPL varchar(5), 
                QUANT_CONV numeric(6,6), 
                UNID varchar(6), 
                COD_MOD_SAIDA varchar(2), 
                SERIE_SAIDA varchar(3), 
                ECF_FAB_SAIDA varchar(21), 
                NUM_DOC_SAIDA varchar(8), 
                CHV_DFE_SAIDA varchar(44), 
                DT_DOC_SAIDA varchar(8), 
                NUM_ITEM_SAIDA varchar(3), 
                VL_UNIT_CONV_SAIDA numeric(6,6), 
                VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA numeric(6,6), 
                VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA numeric(6,6), 
                VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA numeric(6,6), 
                VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA numeric(6,6), 
                VL_UNIT_ICMS_OP_CONV_SAIDA numeric(6,6), 
                VL_UNIT_ICMS_ST_CONV_REST numeric(6,6), 
                VL_UNIT_FCP_ST_CONV_REST numeric(6,6), 
                VL_UNIT_ICMS_ST_CONV_COMPL numeric(6,6), 
                VL_UNIT_FCP_ST_CONV_COMPL numeric(6,6), 
                ID_PAI varchar(60), 
                PRODUTO_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'C185':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                NUM_ITEM varchar(3), 
                COD_ITEM varchar(60), 
                CST_ICMS varchar(3), 
                CFOP varchar(4), 
                COD_MOT_REST_COMPL varchar(5), 
                QUANT_CONV numeric(6,6), 
                UNID varchar(6), 
                VL_UNIT_CONV numeric(6,6), 
                VL_UNIT_ICMS_NA_OPERACAO_CONV numeric(6,6), 
                VL_UNIT_ICMS_OP_ESTOQUE_CONV numeric(6,6), 
                VL_UNIT_ICMS_ST_ESTOQUE_CONV numeric(6,6), 
                VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV numeric(6,6), 
                VL_UNIT_ICMS_ST_CONV_REST numeric(6,6), 
                VL_UNIT_FCP_ST_CONV_REST numeric(6,6), 
                VL_UNIT_ICMS_ST_CONV_COMPL numeric(6,6), 
                VL_UNIT_FCP_ST_CONV_ numeric(6,6), 
                ID_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'C186':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                NUM_ITEM varchar(3), 
                COD_ITEM varchar(60), 
                CST_ICMS varchar(3), 
                CFOP varchar(4), 
                COD_MOT_REST_COMPL varchar(5), 
                QUANT_CONV numeric(6,6), 
                UNID varchar(6), 
                COD_MOD_ENTRADA varchar(2), 
                SERIE_ENTRADA varchar(3), 
                NUM_DOC_ENTRADA varchar(9), 
                CHV_DFE_ENTRADA varchar(44), 
                DT_DOC_ENTRADA varchar(8), 
                NUM_ITEM_ENTRADA varchar(3), 
                VL_UNIT_CONV_ENTRADA numeric(6,6), 
                VL_UNIT_ICMS_OP_CONV_ numeric(6,6), 
                VL_UNIT_BC_ICMS_ST numeric(6,6), 
                VL_UNIT_ICMS_ST_CONV_ENTRADA numeric(6,6), 
                VL_UNIT_FCP_ST_CONV_ENTRADA numeric(6,6), 
                ID_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'C190':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                CST_ICMS varchar(3), 
                CFOP varchar(4), 
                ALIQ_ICMS numeric(6,2), 
                VL_OPR numeric(6,2), 
                VL_BC_ICMS numeric(6,2), 
                VL_ICMS numeric(6,2), 
                VL_BC_ICMS_ numeric(6,2), 
                VL_ICMS_ST numeric(6,2), 
                VL_RED_BC numeric(6,2), 
                VL_IPI numeric(6,2), 
                COD_OBS varchar(6), 
                ID_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == 'E110':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                VL_TOT_DEBITOS numeric(7,2),
                VL_AJ_DEBITOS numeric(7,2),
                VL_TOT_AJ_DEBITOS numeric(7,2),
                VL_ESTORNOS_CRED numeric(7,2),
                VL_TOT_CREDITOS numeric(7,2),
                VL_AJ_CREDITOS numeric(7,2),
                VL_TOT_AJ_CREDITOS numeric(7,2),
                VL_ESTORNOS_DEB numeric(7,2),
                VL_SLD_CREDOR_ANT numeric(7,2),
                VL_SLD_APURADO numeric(7,2),
                VL_TOT_DED numeric(7,2),
                VL_ICMS_RECOLHER numeric(7,2),
                VL_SLD_CREDOR_TRANSPORTAR numeric(7,2),
                DEB_ESP numeric(7,2)
                );'''.format(registro)
    
    elif registro == 'E115':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                COD_INF_ADIC varchar(8),
                VL_INF_ADIC numeric(7,2),
                DESCR_COMPL_AJ varchar(4)
                );'''.format(registro)
    
    elif registro == 'E210':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                IND_MOV_ST varchar(1),
                VL_SLD_CRED_ANT_ST numeric(7,2),
                VL_DEVOL_ST numeric(7,2),
                VL_RESSARC_ST numeric(7,2),
                VL_OUT_CRED_ST numeric(7,2),
                VL_AJ_CREDITOS_ST numeric(7,2),
                VL_RETENCAO_ST numeric(7,2),
                VL_OUT_DEB_ST numeric(7,2),
                VL_AJ_DEBITOS_ST numeric(7,2),
                VL_SLD_DEV_ANT_ST numeric(7,2),
                VL_DEDUCOES_ST numeric(7,2),
                VL_ICMS_RECOL_ST numeric(7,2),
                VL_SLD_CRED_ST_TRANSPORTAR numeric(7,2),
                DEB_ESP_ST numeric(7,2)
                );'''.format(registro)
    
    elif registro == 'H010':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                COD_ITEM varchar(60), 
                UNID varchar(6), 
                QTD numeric(5,3), 
                VL_UNIT numeric(5,6), 
                VL_ITEM numeric(5,2), 
                IND_PROP varchar(1), 
                COD_PART varchar(60), 
                TXT_COMPL varchar(15), 
                COD_CTA varchar(15), 
                VL_ITEM_IR numeric(5,2)
                );'''.format(registro)
    
    elif registro == 'H030':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4), 
                VL_ICMS_OP numeric(5,6), 
                VL_BC_ICMS_ST numeric(5,6), 
                VL_ICMS_ST numeric(5,6), 
                VL_FCP numeric(5,6), 
                ID_PAI varchar(60)
                );'''.format(registro)
    
    elif registro == '1250':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                VL_CREDITO_ICMS_OP numeric(7,2),
                VL_ICMS_ST_REST numeric(7,2),
                VL_FCP_ST_REST numeric(7,2),
                VL_ICMS_ST_COMPL numeric(7,2),
                VL_FCP_ST_COMPL numeric(7,2)
                );'''.format(registro)
    
    elif registro == '1255':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                COD_MOT_REST_COMPL varchar(5),
                VL_CREDITO_ICMS_OP_MOT numeric(7,2),
                VL_ICMS_ST_REST_MOT numeric(7,2),
                VL_FCP_ST_REST_MOT numeric(7,2),
                VL_ICMS_ST_COMPL_MOT numeric(7,2),
                VL_FCP_ST_COMPL_MOT numeric(7,2)
                );'''.format(registro)
    
    elif registro == '1601':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                COD_PART_IP varchar(60),
                COD_PART_IT varchar(60),
                TOT_VS numeric(7,2),
                TOT_ISS numeric(7,2),
                TOT_OUTROS numeric(7,2)
                );'''.format(registro)
    
    elif registro == 'D100':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                IND_OPER varchar(1),
                IND_EMIT varchar(1),
                COD_PART varchar(60),
                COD_MOD varchar(2),
                COD_SIT varchar(2),
                SER varchar(4),
                SUB varchar(3),
                NUM_DOC varchar(9),
                CHV_CTE varchar(44),
                DT_DOC varchar(8),
                DT_A_P varchar(8),
                TP_CTE varchar(1),
                CHV_CTE_REF varchar(44),
                VL_DOC numeric(6,2),
                VL_DESC numeric(6,2),
                IND_FRT varchar(1),
                VL_SERV numeric(6,2),
                VL_BC_ICMS numeric(6,2),
                VL_ICMS numeric(6,2),
                VL_NT numeric(6,2),
                COD_INF varchar(6),
                COD_CTA varchar(10),
                COD_MUN_ORIG varchar(7),
                COD_MUN_DEST varchar(7)
                );'''.format(registro)

    elif registro == 'D190':
        return '''create table if not exists Reg{}(
                NLINHA int, 
                REG varchar(4),
                CST_ICMS varchar(3),
                CFOP varchar(4),
                ALIQ_ICMS numeric(6,2),
                VL_OPR numeric(6,2),
                VL_BC_ICMS numeric(6,2),
                VL_ICMS numeric(6,2),
                VL_RED_BC numeric(6,2),
                COD_OBS varchar(6),
                ID_PAI numeric(6,2)
                );'''.format(registro)
    
def dropTableQuery(registro):
    return '''drop table if exists Reg{};'''.format(registro)