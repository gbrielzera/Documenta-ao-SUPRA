# ValidaItensAssTec
# Caminho: Catálogo > Biblioteca de scripts > ValidaItensAssTec
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def ValidaItensAssTec():
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Cadastrar":
        if String.IsNullOrEmpty(OrdemServico["PRJ_DESC_LONGA"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição do Item'")
        if String.IsNullOrEmpty(OrdemServico["PRJ_DESC_CURTA"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição Curta do Item'")
        if String.IsNullOrEmpty(OrdemServico["PRJ_TIPO_ITEM"]):
            Criticas.AdicionaPendencia("É obrigatório informar o 'Tipo do Item'")
        if String.IsNullOrEmpty(OrdemServico["PRJ_UNI_MEDIDA"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Unidade de Medida'")
        if String.IsNullOrEmpty(OrdemServico["PRJ_CLASSE"]):
            Criticas.AdicionaPendencia("É obrigatório informar se o item a 'Classe'")
        if String.IsNullOrEmpty(OrdemServico["PRJ_ORIGEM_ITEM"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Origem do Item'")
        if String.IsNullOrEmpty(OrdemServico["PRJ_CATEGORIA_NCM"]):
            Criticas.AdicionaPendencia("É obrigatório informar a 'Categoria NCM'")
        if String.IsNullOrEmpty(OrdemServico["PRJ_PLANEJADOR"]):
            Criticas.AdicionaPendencia("É obrigatório informar o 'Planejador'")
        if OrdemServico["PRJ_FABRICANTE"].Rows.Count == 0:
            Criticas.AdicionaPendencia("É obrigatório informar pelo menos um registro de 'Fabricante'")
        if OrdemServico["PRJ_FABRICANTE"].Rows.Count > 0:
            fabricantes = OrdemServico["PRJ_FABRICANTE"]
            posicao = 1
            for linha in fabricantes.Rows:
                if linha["FORNEC_FABRIC"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Fabricante' linha: "+posicao.ToString()+" - É obrigatório informar o 'Fornecedor ou Fabricante'")
                if linha["PART_NUMBER"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Fabricante' linha: "+posicao.ToString()+" - É obrigatório informar o 'Part Number'")
                if linha["PART_NUM_COM"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Fabricante' linha: "+posicao.ToString()+" - É obrigatório informar o 'Part Number é comercial?'")  
                posicao += posicao
        #Itens alternativos
        if OrdemServico["PRJ_ITENS_ALT"].Rows.Count > 0:
            itens = OrdemServico["PRJ_ITENS_ALT"]
            posicao = 1
            for linha in itens.Rows:
                if linha["ACAO"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Tipos de Itens Alternativos' linha: "+posicao.ToString()+" - É obrigatório informar a 'Ação'")
                if linha["COD_ITEM"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Tipos de Itens Alternativos' linha: "+posicao.ToString()+" - É obrigatório informar o 'Código do Item'")
                if linha["RECIPROCO"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Tipos de Itens Alternativos' linha: "+posicao.ToString()+" - É obrigatório informar o campo 'Reciproco?'") 
                posicao += posicao
        #Perifericos
        if OrdemServico["PRJ_COD_EQUI_PERIF"].Rows.Count > 0:
            itens = OrdemServico["PRJ_COD_EQUI_PERIF"]
            posicao = 1
            for linha in itens.Rows:
                if linha["ACAO"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Códigos de Equipamentos e/ou Periféricos' linha: "+posicao.ToString()+" - É obrigatório informar a 'Ação'")
                if linha["CODIGO_ITEM"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Códigos de Equipamentos e/ou Periféricos' linha: "+posicao.ToString()+" - É obrigatório informar o 'Código do Item'")
                if linha["QTDE"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Códigos de Equipamentos e/ou Periféricos' linha: "+posicao.ToString()+" - É obrigatório informar o campo 'Quantidade'")
                posicao += posicao
    #Validação para tipo Alterar
    if OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Alterar":
        if String.IsNullOrEmpty(OrdemServico["PRJ_CODIGO_ITEM"]):
            Criticas.AdicionaPendencia("É obrigatório informar o 'Código do Item'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_DESC_ITEM"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição do Item'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_DESC_CURTA"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar a 'Descrição Curta do Item'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_TIPO_ITEM"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar o 'Tipo do Item'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_ORIGEM_ITEM"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar a 'Origem do Item'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_CATEGORIA_NCM"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar a 'Categoria NCM'")
        #if String.IsNullOrEmpty(OrdemServico["PRJ_PLANEJADOR"]):
        #    Criticas.AdicionaPendencia("É obrigatório informar o 'Planejador'")
    if OrdemServico["PRJ_FABRICANTE"].Rows.Count > 0:
            fabricantes = OrdemServico["PRJ_FABRICANTE"]
            posicao = 1
            for linha in fabricantes.Rows:
                if linha["FORNEC_FABRIC"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Fabricante' linha: "+posicao.ToString()+" - É obrigatório informar o 'Fornecedor ou Fabricante'")
                if linha["PART_NUMBER"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Fabricante' linha: "+posicao.ToString()+" - É obrigatório informar o 'Part Number'")
                if linha["PART_NUM_COM"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Fabricante' linha: "+posicao.ToString()+" - É obrigatório informar o 'Part Number é comercial?'")  
                posicao += posicao
     #Itens alternativos
    if OrdemServico["PRJ_ITENS_ALT"].Rows.Count > 0:
            itens = OrdemServico["PRJ_ITENS_ALT"]
            posicao = 1
            for linha in itens.Rows:
                if linha["ACAO"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Tipos de Itens Alternativos' linha: "+posicao.ToString()+" - É obrigatório informar a 'Ação'")
                if linha["COD_ITEM"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Tipos de Itens Alternativos' linha: "+posicao.ToString()+" - É obrigatório informar o 'Código do Item'")
                if linha["RECIPROCO"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Tipos de Itens Alternativos' linha: "+posicao.ToString()+" - É obrigatório informar o campo 'Reciproco?'") 
                posicao += posicao   
     #Perifericos
    if OrdemServico["PRJ_COD_EQUI_PERIF"].Rows.Count > 0:
            itens = OrdemServico["PRJ_COD_EQUI_PERIF"]
            posicao = 1
            for linha in itens.Rows:
                if linha["ACAO"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Códigos de Equipamentos e/ou Periféricos' linha: "+posicao.ToString()+" - É obrigatório informar a 'Ação'")
                if linha["CODIGO_ITEM"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Códigos de Equipamentos e/ou Periféricos' linha: "+posicao.ToString()+" - É obrigatório informar o 'Código do Item'")
                if linha["QTDE"] == DBNull.Value:
                    Criticas.AdicionaPendencia("Campo 'Códigos de Equipamentos e/ou Periféricos' linha: "+posicao.ToString()+" - É obrigatório informar o campo 'Quantidade'")
                posicao += posicao       
     #Validação para tipo Inativar e Reativar   
    if (OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Inativar" or OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Reativar") and OrdemServico["PRJ_CODIGO_ITENS"].Rows.Count == 0:
        Criticas.AdicionaPendencia("É obrigatório informar pelo menos um 'Cógido do Item'")
            
    if (OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Inativar" or OrdemServico["PRJ_TIPO_SOLICITACAO"] == "Reativar") and String.IsNullOrEmpty(OrdemServico.Justificativa):
        Criticas.AdicionaPendencia("É obrigatório informar a 'Justificativa'")
