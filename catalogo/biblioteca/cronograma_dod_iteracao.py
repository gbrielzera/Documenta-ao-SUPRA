# cronograma_dod_iteracao
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_iteracao
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_iteracao(NUMERO_OC, FASE):

    qry = " SELECT nvl(MAX(ITERACAO),0) ITERACAO FROM CRONOGRAMA_DOD WHERE NUMERO_OC = "  + NUMERO_OC.ToString() + " AND FASE = " + FASE.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_iteracao - " + qry  , False) 

    lista = DB.ExecuteDataTable(qry)

    for linha in lista.Rows:
        return linha["ITERACAO"]
