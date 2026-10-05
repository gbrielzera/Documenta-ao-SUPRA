# cronograma_dod_previseventual
# Caminho: Catálogo > Biblioteca de scripts > cronograma_dod_previseventual
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def cronograma_dod_previseventual(NUMERO_OC, FASE, ITERACAO, DATA_PREVISTA_INICIO, DATA_PREVISTA_FIM, ESFORCO_PREVISTO_INICIO):
 
    qry = " UPDATE CRONOGRAMA_DOD SET DATA_PREVISTA_INICIO = to_date('"+ DATA_PREVISTA_INICIO.ToString("dd/MM/yyyy") + "','dd-mm-yyyy') , DATA_PREVISTA_FIM = to_date('" + DATA_PREVISTA_FIM.ToString("dd/MM/yyyy") + "','dd-mm-yyyy') , ESFORCO_PREVISTO_INICIO = " + ESFORCO_PREVISTO_INICIO.ToString() + " WHERE NUMERO_OC = "  + NUMERO_OC.ToString() + " AND FASE = " + FASE.ToString() + " AND ITERACAO = " + ITERACAO.ToString() + " "
    
    DB.ExecuteNonQuery(qry)
    
    persistencia = "commit"
    
    DB.ExecuteNonQuery(persistencia)
