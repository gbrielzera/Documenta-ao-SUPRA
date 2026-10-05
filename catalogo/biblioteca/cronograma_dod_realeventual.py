# cronograma_dod_realeventual
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_realeventual
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_realeventual(NUMERO_OC, FASE, ITERACAO, ESFORCO_REAL, DATA_FIM_REAL):

    qry = " UPDATE CRONOGRAMA_DOD SET DATA_FIM_REAL = to_date('"+DATA_FIM_REAL.ToString()+"','DD/MM/YYYY hh24:mi:ss') , ESFORCO_REAL = " + ESFORCO_REAL.ToString() + " WHERE NUMERO_OC = "  + NUMERO_OC.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_realizado - " + qry  , False) 

    DB.ExecuteNonQuery(qry)
    
    persistencia = "commit"
    
    DB.ExecuteNonQuery(persistencia)
