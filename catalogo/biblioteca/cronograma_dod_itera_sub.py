# cronograma_dod_itera_sub
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_itera_sub
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_itera_sub(ID_OCORRENCIA, FASE):

    qry = " SELECT nvl(MAX(ITERACAO),0) ITERACAO FROM CRONOGRAMA_DOD WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_iteracao - " + qry  , False) 

    lista = DB.ExecuteDataTable(qry)

    for linha in lista.Rows:
        return linha["ITERACAO"]
