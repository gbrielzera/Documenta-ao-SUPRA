# cronograma_dod_alocacao
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_alocacao
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_alocacao(NUMERO_OC, FASE, ITERACAO ):
 
    qry = " UPDATE CRONOGRAMA_DOD SET DATA_INICIO_REAL = to_date(to_char(sysdate, 'DD/MM/YYYY hh24:mi:ss'), 'DD/MM/YYYY hh24:mi:ss') WHERE NUMERO_OC = "  + NUMERO_OC.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_alocacao - " + qry  , False)
    
    DB.ExecuteNonQuery(qry)
    
    presistencia = "commit"
    
    DB.ExecuteNonQuery(presistencia)
