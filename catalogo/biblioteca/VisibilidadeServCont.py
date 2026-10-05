# VisibilidadeServCont
# Caminho: Catálogo > Biblioteca de scripts > VisibilidadeServCont
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def VisibilidadeServCont():
    if Controle.Valor == "Cadastrar":
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = True
        Formulario["PRJ_UNI_MEDIDA"].Visivel = True
        Formulario["PRJ_PATRIMONIADO"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = False
        Formulario["LABEL1"].Visivel = False
    elif Controle.Valor == "Alterar":
        Formulario["PRJ_CODIGO_ITEM"].Visivel = True
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = True
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_PATRIMONIADO"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = False
        Formulario["LABEL1"].Visivel = True
    elif Controle.Valor == "Inativar" or Controle.Valor == "Reativar":
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = True
        Formulario["PRJ_DESC_ITEM"].Visivel = False
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_PATRIMONIADO"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = False
        Formulario["Justificativa"].Visivel = True
        Formulario["PRJ_AVISO"].Visivel = False
        Formulario["LABEL1"].Visivel = False
    else:
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = False
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_PATRIMONIADO"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = False
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = False
        Formulario["LABEL1"].Visivel = False
