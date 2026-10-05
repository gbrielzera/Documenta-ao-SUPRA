# VisibilidadeItensAssTec
# Caminho: Catálogo > Biblioteca de scripts > VisibilidadeItensAssTec
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def VisibilidadeItensAssTec():
    if Controle.Valor == "Cadastrar":
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_TIPO_ITEM"].Visivel = True
        Formulario["PRJ_DESC_CURTA"].Visivel = True
        Formulario["PRJ_DESC_LONGA"].Visivel = True
        Formulario["PRJ_UNI_MEDIDA"].Visivel = True
        Formulario["PRJ_CLASSE"].Visivel = True
        Formulario["PRJ_CONF_BEM"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = True
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
        Formulario["PRJ_PLANEJADOR"].Visivel = True
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = True
        Formulario["PRJ_FABRICANTE"].Visivel = True
        Formulario["PRJ_COD_EQUI_PERIF"].Visivel = True
        Formulario["PRJ_ITENS_ALT"].Visivel = True
        Formulario["LABEL1"].Visivel = False
        
    elif Controle.Valor == "Alterar":
        Formulario["PRJ_CODIGO_ITEM"].Visivel = True
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_TIPO_ITEM"].Visivel = True
        Formulario["PRJ_DESC_CURTA"].Visivel = True
        Formulario["PRJ_DESC_LONGA"].Visivel = True
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_CLASSE"].Visivel = False
        Formulario["PRJ_CONF_BEM"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = True
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
        Formulario["PRJ_PLANEJADOR"].Visivel = True
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = True
        Formulario["PRJ_FABRICANTE"].Visivel = True
        Formulario["PRJ_COD_EQUI_PERIF"].Visivel = True
        Formulario["PRJ_ITENS_ALT"].Visivel = True
        Formulario["LABEL1"].Visivel = True
        
    elif Controle.Valor == "Inativar" or Controle.Valor == "Reativar":
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = True
        Formulario["PRJ_TIPO_ITEM"].Visivel = False
        Formulario["PRJ_DESC_CURTA"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = False
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_CLASSE"].Visivel = False
        Formulario["PRJ_CONF_BEM"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = False
        Formulario["PRJ_PLANEJADOR"].Visivel = False
        Formulario["Justificativa"].Visivel = True
        Formulario["PRJ_AVISO"].Visivel = False
        Formulario["PRJ_FABRICANTE"].Visivel = False
        Formulario["PRJ_COD_EQUI_PERIF"].Visivel = False
        Formulario["PRJ_ITENS_ALT"].Visivel = False
        Formulario["LABEL1"].Visivel = False
    else:
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_TIPO_ITEM"].Visivel = False
        Formulario["PRJ_DESC_CURTA"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = False
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_CLASSE"].Visivel = False
        Formulario["PRJ_CONF_BEM"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = False
        Formulario["PRJ_PLANEJADOR"].Visivel = False
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = False
        Formulario["PRJ_FABRICANTE"].Visivel = False
        Formulario["PRJ_COD_EQUI_PERIF"].Visivel = False
        Formulario["PRJ_ITENS_ALT"].Visivel = False
        Formulario["LABEL1"].Visivel = False
