# cronograma_dod_incluir
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_incluir
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_incluir(ID_OCORRENCIA, NUMERO_OC, FASE, DESC_FASE, ITERACAO):

    qry = " INSERT INTO CRONOGRAMA_DOD (ID_OCORRENCIA, NUMERO_OC , FASE, DESC_FASE, ITERACAO, DATA_CRIACAO) VALUES ("+ ID_OCORRENCIA.ToString() + ", " + NUMERO_OC.ToString() + ", " + FASE.ToString() + ", '" + DESC_FASE.ToString() + "', " + ITERACAO.ToString() +  ", to_date(to_char(sysdate, 'DD/MM/YYYY hh24:mi:ss'), 'DD/MM/YYYY hh24:mi:ss')" + " )"
    
    #OrdemServico.AdicionaComentario(" cronograma_dod_incluir - " + qry  , False)
     
    DB.ExecuteNonQuery(qry)
    
    persistencia = "commit"
    
    DB.ExecuteNonQuery(persistencia)
