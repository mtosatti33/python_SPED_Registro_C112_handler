from pathlib import Path
import os
from csv import DictWriter

#bloco0
_0000 = ['NLINHA', 'REG', 'COD_VER', 'COD_FIN', 'DT_INI', 'DT_FIN', 'NOME', 'CNPJ', 'CPF', 'UF', 'IE', 'COD_MUN', 'IM', 'SUFRAMA', 'IND_PERFIL', 'IND_ATIV']
_0100 = ['NLINHA', 'REG', 'NOME', 'CPF', 'CRC', 'CNPJ', 'CEP', 'END', 'NUM', 'COMPL', 'BAIRRO', 'FONE', 'FAX', 'EMAIL', 'COD_MUN']
_0150 = ['NLINHA', 'REG', 'COD_PART', 'NOME', 'COD_PAIS', 'CNPJ', 'CPF', 'IE', 'COD_MUN', 'SUFRAMA', 'END', 'NUM', 'COMPL', 'BAIRRO']
_0175 = ['NLINHA', 'REG', 'DT_ALT', 'NR_CAMPO', 'CONT_ANT', 'ID_PAI']
_0190 = ['NLINHA', 'REG', 'UNID', 'DESCR']
_0200 = ['NLINHA', 'REG', 'COD_ITEM', 'DESCR_ITEM', 'COD_BARRA', 'COD_ANT_ITEM', 'UNID_INV', 'TIPO_ITEM', 'COD_NCM', 'EX_IPI', 'COD_GEN', 'COD_LST', 'ALIQ_ICMS', 'CEST']
_0205 = ['NLINHA', 'REG', 'DESCR_ANT_ITEM', 'DT_INI', 'DT_FIM', 'COD_ANT_ITEM', 'ID_PAI']
_0220 = ['NLINHA', 'REG', 'UNID_CONV', 'FAT_CONV', 'COD_BARRA', 'ID_PAI']
_0400 = ['NLINHA', 'REG', 'COD_NAT', 'DESCR_NAT']
#blocoC
_C100 = ['NLINHA', 'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'NUM_DOC', 'CHV_NFE', 'DT_DOC', 'DT_E_S', 'VL_DOC', 'IND_PGTO', 'VL_DESC', 'VL_ABAT_NT', 'VL_MERC', 'IND_FRT', 'VL_FRT', 'VL_SEG', 'VL_OUT_DA', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_IPI', 'VL_PIS', 'VL_COFINS', 'VL_PIS_ST', 'VL_COFINS_ST']
_C112 = ['NLINHA', 'REG', 'COD_DA', 'UF', 'NUM_DA', 'COD_AUT', 'VL_DA', 'DT_VCTO', 'DT_PGTO', 'ID_PAI', 'PARTICIPANTE', 'CNPJ']
_C113 = ['NLINHA', 'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'SER', 'SUB', 'NUM_DOC', 'DT_DOC', 'CHV_DOCe', 'ID_PAI']
_C170 = ['NLINHA', 'REG', 'NUM_ITEM', 'COD_ITEM', 'DESCR_COMPL', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'IND_MOV', 'CST_ICMS', 'CFOP', 'COD_NAT', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'ALIQ_ST', 'VL_ICMS_ST', 'IND_APUR', 'CST_IPI', 'COD_ENQ', 'VL_BC_IPI', 'ALIQ_IPI', 'VL_IPI', 'CST_PIS', 'VL_BC_PIS', 'ALIQ_PIS', 'QUANT_BC_PIS', 'ALIQ_PIS', 'VL_PIS', 'CST_COFINS', 'VL_BC_COFINS', 'ALIQ_COFINS', 'QUANT_BC_COFINS', 'ALIQ_COFINS', 'VL_COFINS', 'COD_CTA', 'VL_ABAT_NT', 'ID_PAI']
_C180 = ['NLINHA', 'REG', 'COD_RESP_RET', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_BC_ICMS_ST_CONV', 'VL_UNIT_ICMS_ST_CONV', 'VL_UNIT_FCP_ST_CONV', 'COD_DA', 'NUM_DA', 'ID_PAI', 'PRODUTO_PAI']
_C181 = ['NLINHA', 'REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'COD_MOD_SAIDA', 'SERIE_SAIDA', 'ECF_FAB_SAIDA', 'NUM_DOC_SAIDA', 'CHV_DFE_SAIDA', 'DT_DOC_SAIDA', 'NUM_ITEM_SAIDA', 'VL_UNIT_CONV_SAIDA', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA', 'VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA', 'VL_UNIT_ICMS_OP_CONV_SAIDA', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL', 'ID_PAI', 'PRODUTO_PAI']
_C185 = ['NLINHA', 'REG', 'NUM_ITEM', 'COD_ITEM', 'CST_ICMS', 'CFOP', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_', 'ID_PAI']
_C186 = ['NLINHA', 'REG', 'NUM_ITEM', 'COD_ITEM', 'CST_ICMS', 'CFOP', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'COD_MOD_ENTRADA', 'SERIE_ENTRADA', 'NUM_DOC_ENTRADA', 'CHV_DFE_ENTRADA', 'DT_DOC_ENTRADA', 'NUM_ITEM_ENTRADA', 'VL_UNIT_CONV_ENTRADA', 'VL_UNIT_ICMS_OP_CONV_', 'VL_UNIT_BC_ICMS_ST', 'VL_UNIT_ICMS_ST_CONV_ENTRADA', 'VL_UNIT_FCP_ST_CONV_ENTRADA', 'ID_PAI']
_C190 = ['NLINHA', 'REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_', 'VL_ICMS_ST', 'VL_RED_BC', 'VL_IPI', 'COD_OBS', 'ID_PAI']
#blocoD
_D100 = ['NLINHA', 'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'SUB', 'NUM_DOC', 'CHV_CTE', 'DT_DOC', 'DT_A_P', 'TP_CTE', 'CHV_CTE_REF', 'VL_DOC', 'VL_DESC', 'IND_FRT', 'VL_SERV', 'VL_BC_ICMS', 'VL_ICMS', 'VL_NT', 'COD_INF', 'COD_CTA', 'COD_MUN_ORIG', 'COD_MUN_DEST']
_D190 = ['NLINHA', 'REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_RED_BC', 'COD_OBS', 'ID_PAI']
#blocoE
_E110 = ['NLINHA', 'REG', 'VL_TOT_DEBITOS', 'VL_AJ_DEBITOS', 'VL_TOT_AJ_DEBITOS', 'VL_ESTORNOS_CRED', 'VL_TOT_CREDITOS', 'VL_AJ_CREDITOS', 'VL_TOT_AJ_CREDITOS', 'VL_ESTORNOS_DEB', 'VL_SLD_CREDOR_ANT', 'VL_SLD_APURADO', 'VL_TOT_DED', 'VL_ICMS_RECOLHER', 'VL_SLD_CREDOR_TRANSPORTAR', 'DEB_ESP']
_E115 = ['NLINHA', 'REG', 'COD_INF_ADIC', 'VL_INF_ADIC', 'DESCR_COMPL_AJ']
_E210 = ['NLINHA', 'REG', 'IND_MOV_ST', 'VL_SLD_CRED_ANT_ST', 'VL_DEVOL_ST', 'VL_RESSARC_ST', 'VL_OUT_CRED_ST', 'VL_AJ_CREDITOS_ST', 'VL_RETENCAO_ST', 'VL_OUT_DEB_ST', 'VL_AJ_DEBITOS_ST', 'VL_SLD_DEV_ANT_ST', 'VL_DEDUCOES_ST', 'VL_ICMS_RECOL_ST', 'VL_SLD_CRED_ST_TRANSPORTAR', 'DEB_ESP_ST']
#blocoH
_H010 = ['NLINHA', 'REG', 'COD_ITEM', 'UNID', 'QTD', 'VL_UNIT', 'VL_ITEM', 'IND_PROP', 'COD_PART', 'TXT_COMPL', 'COD_CTA', 'VL_ITEM_IR']
_H030 = ['NLINHA', 'REG', 'VL_ICMS_OP', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_FCP', 'ID_PAI']
#bloco1
_1250 = ['NLINHA', 'REG', 'VL_CREDITO_ICMS_OP', 'VL_ICMS_ST_REST', 'VL_FCP_ST_REST', 'VL_ICMS_ST_COMPL', 'VL_FCP_ST_COMPL']
_1255 = ['NLINHA', 'REG', 'COD_MOT_REST_COMPL', 'VL_CREDITO_ICMS_OP_MOT', 'VL_ICMS_ST_REST_MOT', 'VL_FCP_ST_REST_MOT', 'VL_ICMS_ST_COMPL_MOT', 'VL_FCP_ST_COMPL_MOT']
_1601 = ['NLINHA', 'REG', 'COD_PART_IP', 'COD_PART_IT', 'TOT_VS', 'TOT_ISS', 'TOT_OUTROS']

def defineCabecalho(registro):
        header = []
        if registro == '0000':
            header = _0000
        if registro == '0100':
            header = _0100
        if registro == '0150':
            header = _0150
        if registro == '0175':
            header = _0175
        if registro == '0190':
            header = _0190
        if registro == '0200':
            header = _0200
        if registro == '0205':
            header = _0205
        if registro == '0220':
            header = _0220
        if registro == '0400':
            header = _0400
        if registro == 'C100':
            header = _C100
        if registro == 'C112':
            header = _C112
        if registro == 'C113':
            header = _C113
        if registro == 'C170':
            header = _C170
        if registro == 'C180':
            header = _C180
        if registro == 'C181':
            header = _C181
        if registro == 'C185':
            header = _C185
        if registro == 'C186':
            header = _C186
        if registro == 'C190':
            header = _C190
        if registro == 'D100':
            header = _D100
        if registro == 'D190':
            header = _D190
        if registro == 'E110':
            header = _E110
        if registro == 'E115':
            header = _E115
        if registro == 'E210':
            header = _E210
        if registro == 'H010':
            header = _H010
        if registro == 'H030':
            header = _H030
        if registro == '1250':
            header = _1250
        if registro == '1255':
            header = _1255
        if registro == '1601':
            header = _1601

        return header

def GeraCabecalho(arquivo, header):
    if not os.path.exists(arquivo):
        Path(arquivo).touch()
        with open(arquivo, 'a+', newline='', encoding='utf-8') as f:
            dr = DictWriter(f, fieldnames=header)
            dr.writeheader()