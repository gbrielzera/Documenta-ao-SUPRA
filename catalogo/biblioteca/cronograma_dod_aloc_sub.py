# cronograma_dod_aloc_sub
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_aloc_sub
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_aloc_sub(ID_OCORRENCIA, FASE, ITERACAO ):
 
    qry = " UPDATE CRONOGRAMA_DOD SET DATA_INICIO_REAL = to_date(to_char(sysdate, 'DD/MM/YYYY hh24:mi:ss'), 'DD/MM/YYYY hh24:mi:ss') WHERE ID_OCORRENCIA = "  + ID_OCORRENCIA.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + ""
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_aloc_sub - " + qry  , False)
    
    DB.ExecuteNonQuery(qry)
    
    presistencia = "commit"
    
    DB.ExecuteNonQuery(presistencia)
