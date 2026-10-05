# obtemSiglaDaOS
# Caminho: Catálogo > Biblioteca de scripts > obtemSiglaDaOS
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def obtemSiglaDaOS(numero):
# recebe como parâmetro o numero da OS 
# retorna sigla da os
    sigla = ""
    lista = Utils.ExecuteDataTable("SELECT CS.SIGLA SIGLAOS FROM OCORRENCIA O INNER JOIN CLASSE_SUB_PROCESSO CS ON CS.ID_CLASSE_SUB_PROCESSO = O.ID_CLASSE_SUB_PROC WHERE O.NUMERO = '" + numero + "'")
    for linha in lista.Rows:
        sigla = linha["SIGLAOS"]
    
    return sigla
