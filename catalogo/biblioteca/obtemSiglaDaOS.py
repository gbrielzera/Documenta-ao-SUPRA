# obtemSiglaDaOS
# Caminho: Catálogo > Biblioteca de scripts > obtemSiglaDaOS
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

def obtemSiglaDaOS(numero):
# recebe como parâmetro o numero da OS 
# retorna sigla da os
    sigla = ""
    lista = Utils.ExecuteDataTable("SELECT CS.SIGLA SIGLAOS FROM OCORRENCIA O INNER JOIN CLASSE_SUB_PROCESSO CS ON CS.ID_CLASSE_SUB_PROCESSO = O.ID_CLASSE_SUB_PROC WHERE O.NUMERO = '" + numero + "'")
    for linha in lista.Rows:
        sigla = linha["SIGLAOS"]
    
    return sigla
