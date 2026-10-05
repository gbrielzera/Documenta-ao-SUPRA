# cronograma_dod_prev_sub
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_prev_sub
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_prev_sub(ID_OCORRENCIA, FASE, ITERACAO, DATA_PREVISTA_INICIO, DATA_PREVISTA_FIM, ESFORCO_PREVISTO_INICIO):

    qry = " UPDATE CRONOGRAMA_DOD SET DATA_PREVISTA_INICIO = to_date('"+ DATA_PREVISTA_INICIO.ToString("dd/MM/yyyy") + "','dd-mm-yyyy') , DATA_PREVISTA_FIM = to_date('" + DATA_PREVISTA_FIM.ToString("dd/MM/yyyy") + "','dd-mm-yyyy') , ESFORCO_PREVISTO_INICIO = " + ESFORCO_PREVISTO_INICIO.ToString() + " WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + " "
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_previsto - " + qry  , False) 
    
    DB.ExecuteNonQuery(qry)
    
    persistencia = "commit"
    
    DB.ExecuteNonQuery(persistencia)
