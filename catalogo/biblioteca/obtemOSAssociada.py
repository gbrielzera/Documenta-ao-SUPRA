# obtemOSAssociada
# Caminho: Catálogo > Biblioteca de scripts > obtemOSAssociada
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

def obtemOSAssociada(numero):
# recebe como parâmetro o numero da OS Alvo 
# retorna numero da OS Fonte
    os = ""
    lista = Utils.ExecuteDataTable("SELECT OO.NUMERO OSASSOCIADA FROM OCORRENCIA O INNER JOIN ASSOCIACAO_OCORR AO ON AO.ID_OCORR_ALVO = O.ID_OCORRENCIA INNER JOIN OCORRENCIA OO ON OO.ID_OCORRENCIA = AO.ID_OCORR_FONTE WHERE O.NUMERO = '" + numero + "'")
    for linha in lista.Rows:
        os = linha["OSASSOCIADA"]
    
    return os
