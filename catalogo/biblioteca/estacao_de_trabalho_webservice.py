# estacao_de_trabalho_webservice
# Caminho: Catálogo > Biblioteca de scripts > estacao_de_trabalho_webservice
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def listaDeAgendamentos():
    
    try:
    
        dados = DB.ExecuteDataTable("SELECT * FROM Z_00143_LISTA_AGEND_ESTACAO_TRABALHO")
        
        if dados.Rows.Count > 0:
            return "Sucesso"
        
    except Exception, e:
        return "Erro na solicitação. "
