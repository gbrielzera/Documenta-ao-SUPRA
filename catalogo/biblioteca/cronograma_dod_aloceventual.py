# cronograma_dod_aloceventual
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_aloceventual
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_aloceventual(NUMERO_OC, FASE, ITERACAO, DATA_INICIO_REAL):

    #OrdemServico.AdicionaComentario("teste" + DATA_INICIO_REAL.ToString() , False) 
    
    qry = "UPDATE CRONOGRAMA_DOD SET DATA_INICIO_REAL = to_date('"+DATA_INICIO_REAL.ToString()+"','DD/MM/YYYY hh24:mi:ss') WHERE NUMERO_OC = "+NUMERO_OC.ToString()+" AND FASE = "+FASE.ToString()+" AND ITERACAO = "+ITERACAO.ToString()+ ""
    
    DB.ExecuteNonQuery(qry)
    
    presistencia = "commit"
    
    DB.ExecuteNonQuery(presistencia)
