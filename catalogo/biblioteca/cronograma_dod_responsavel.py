# cronograma_dod_responsavel
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_responsavel
# Fonte: Reembolsos__I.A_Versão_1_Reembolso_-_Iniciativa_IA.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_responsavel(ID_OCORRENCIA, FASE, ITERACAO ):
    
    qry = " UPDATE CRONOGRAMA_DOD SET ID_RESPONSAVEL = " + OrdemServico.ResponsavelId.ToString() + " WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_responsavel - " + qry  , False) 
    
    DB.ExecuteNonQuery(qry)
    
    presistencia = "commit"
    
    DB.ExecuteNonQuery(presistencia)
