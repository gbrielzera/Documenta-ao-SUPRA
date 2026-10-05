# cronograma_dod_aloc_sub
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_aloc_sub
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_aloc_sub(ID_OCORRENCIA, FASE, ITERACAO ):
 
    qry = " UPDATE CRONOGRAMA_DOD SET DATA_INICIO_REAL = to_date(to_char(sysdate, 'DD/MM/YYYY hh24:mi:ss'), 'DD/MM/YYYY hh24:mi:ss') WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_aloc_sub - " + qry  , False)
    
    DB.ExecuteNonQuery(qry)
    
    presistencia = "commit"
    
    DB.ExecuteNonQuery(presistencia)
