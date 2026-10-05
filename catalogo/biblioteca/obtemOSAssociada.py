# obtemOSAssociada
# Caminho: Catálogo > Biblioteca de scripts > obtemOSAssociada
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def obtemOSAssociada(numero):
# recebe como parâmetro o numero da OS Alvo 
# retorna numero da OS Fonte
    os = ""
    lista = Utils.ExecuteDataTable("SELECT OO.NUMERO OSASSOCIADA FROM OCORRENCIA O INNER JOIN ASSOCIACAO_OCORR AO ON AO.ID_OCORR_ALVO = O.ID_OCORRENCIA INNER JOIN OCORRENCIA OO ON OO.ID_OCORRENCIA = AO.ID_OCORR_FONTE WHERE O.NUMERO = '" + numero + "'")
    for linha in lista.Rows:
        os = linha["OSASSOCIADA"]
    
    return os
