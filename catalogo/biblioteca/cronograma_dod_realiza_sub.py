# cronograma_dod_realiza_sub
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_realiza_sub
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_realiza_sub(ID_OCORRENCIA, FASE, ITERACAO, ESFORCO_REAL):
    
    qry = " UPDATE CRONOGRAMA_DOD SET DATA_FIM_REAL = to_date(to_char(sysdate, 'DD/MM/YYYY hh24:mi:ss'), 'DD/MM/YYYY hh24:mi:ss') , ESFORCO_REAL = " + ESFORCO_REAL.ToString() + " WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_realizado - " + qry  , False) 

    DB.ExecuteNonQuery(qry)
    
    persistencia = "commit"
    
    DB.ExecuteNonQuery(persistencia)
