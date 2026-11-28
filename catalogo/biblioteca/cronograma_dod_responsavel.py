# cronograma_dod_responsavel
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_responsavel
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_responsavel(ID_OCORRENCIA, FASE, ITERACAO ):
    
    qry = " UPDATE CRONOGRAMA_DOD SET ID_RESPONSAVEL = " + OrdemServico.ResponsavelId.ToString() + " WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_responsavel - " + qry  , False) 
    
    DB.ExecuteNonQuery(qry)
    
    presistencia = "commit"
    
    DB.ExecuteNonQuery(presistencia)
