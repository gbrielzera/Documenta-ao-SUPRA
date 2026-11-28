# estacao_de_trabalho_webservice
# Caminho: Catálogo > Biblioteca de scripts > estacao_de_trabalho_webservice
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

def listaDeAgendamentos():
    
    try:
    
        dados = DB.ExecuteDataTable("SELECT * FROM Z_00143_LISTA_AGEND_ESTACAO_TRABALHO")
        
        if dados.Rows.Count > 0:
            return "Sucesso"
        
    except Exception, e:
        return "Erro na solicitação. "
