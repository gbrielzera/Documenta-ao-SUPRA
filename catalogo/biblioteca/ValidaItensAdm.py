# ValidaItensAdm
# Caminho: Catálogo > Biblioteca de scripts > ValidaItensAdm
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def ValidaItensAdm():
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Cadastrar" and String.IsNullOrEmpty(OrdemServico["PRJ_DESC_ITEM"]):
        Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição do Item'")
        
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Cadastrar" and String.IsNullOrEmpty(OrdemServico["PRJ_UNI_MEDIDA"]):
        Criticas.AdicionaPendencia("É obrigatório informar a 'Unidade de Medida'")
        
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Cadastrar" and String.IsNullOrEmpty(OrdemServico["PRJ_PATRIMONIADO"]):
        Criticas.AdicionaPendencia("É obrigatório informar se o item é 'Patrimoniado'")
        
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Cadastrar" and String.IsNullOrEmpty(OrdemServico["PRJ_ORIGEM_ITEM"]):
        Criticas.AdicionaPendencia("É obrigatório informar a 'Origem do Item'")
        
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Cadastrar" and String.IsNullOrEmpty(OrdemServico["PRJ_CATEGORIA_NCM"]):
        Criticas.AdicionaPendencia("É obrigatório informar a 'Categoria NCM'")
    #Validação para tipo Alterar
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Alterar" and String.IsNullOrEmpty(OrdemServico["PRJ_CODIGO_ITEM"]):
        Criticas.AdicionaPendencia("É obrigatório informar o 'Cógido do Item'")
    #if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Alterar" and String.IsNullOrEmpty(OrdemServico["PRJ_DESC_ITEM"]):
    #    Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição do Item'")
    #if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Alterar" and String.IsNullOrEmpty(OrdemServico["PRJ_ORIGEM_ITEM"]):
    #    Criticas.AdicionaPendencia("É obrigatório informar a 'Origem do Item'")
    #if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Alterar" and String.IsNullOrEmpty(OrdemServico["PRJ_CATEGORIA_NCM"]):
    #    Criticas.AdicionaPendencia("É obrigatório informar a 'Categoria NCM'")        
        
        
     #Validação para tipo Inativar e Reativar   
    if (OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Inativar" or OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Reativar") and OrdemServico["PRJ_CODIGO_ITENS"].Rows.Count == 0:
        Criticas.AdicionaPendencia("É obrigatório informar pelo menos um 'Cógido do Item'")
        
    if (OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Inativar" or OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Reativar") and String.IsNullOrEmpty(OrdemServico.Justificativa):
        Criticas.AdicionaPendencia("É obrigatório informar a 'Justificativa'")
