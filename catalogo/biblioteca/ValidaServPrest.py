# ValidaServPrest
# Caminho: Catálogo > Biblioteca de scripts > ValidaServPrest
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def ValidaServPrest():
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Cadastrar":
        if String.IsNullOrEmpty(OrdemServico["PRJ_DESC_ITEM"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição do Item'")

        if String.IsNullOrEmpty(OrdemServico["PRJ_UNI_MEDIDA"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Unidade de Medida'")
        
        if String.IsNullOrEmpty(OrdemServico["PRJ_CATEGORIA_NCM"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Categoria NCM'")
        
    #Validação para tipo Alterar
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Alterar":
        if String.IsNullOrEmpty(OrdemServico["PRJ_CODIGO_ITEM"]):
            Criticas.AdicionaPendencia("É obrigatório informar o 'Cógido do Item'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_DESC_ITEM"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição do Item'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_CATEGORIA_NCM"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar a 'Categoria NCM'")            
        if OrdemServico["PRJ_ALIQUOTA"].Rows.Count > 0:
            alicotas = OrdemServico["PRJ_ALIQUOTA"]
            posicao = 1
            for linha in alicotas.Rows:
                if linha["ACAO"] == DBNull.Value or linha["ACAO"] == "Não se aplica":
                    Criticas.AdicionaPendencia("Campo 'Alíquota' linha: "+posicao.ToString()+" - É obrigatório informar a 'Ação'")  
                posicao += posicao
        
     #Validação para tipo Inativar e Reativar   
    if (OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Inativar" or OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Reativar") and OrdemServico["PRJ_CODIGO_ITENS"].Rows.Count == 0:
        Criticas.AdicionaPendencia("É obrigatório informar pelo menos um 'Cógido do Item'")
        
    if (OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Inativar" or OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Reativar") and String.IsNullOrEmpty(OrdemServico.Justificativa):
        Criticas.AdicionaPendencia("É obrigatório informar a 'Justificativa'")
