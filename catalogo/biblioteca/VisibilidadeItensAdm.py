# VisibilidadeItensAdm
# Caminho: Catálogo > Biblioteca de scripts > VisibilidadeItensAdm
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

def VisibilidadeItensAdm():
    if Controle.Valor == "Cadastrar":
        Formulario["LABEL1"].Visivel = False
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = True
        Formulario["PRJ_UNI_MEDIDA"].Visivel = True
        Formulario["PRJ_PATRIMONIADO"].Visivel = True
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = True
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = True
    elif Controle.Valor == "Alterar":
        Formulario["PRJ_CODIGO_ITEM"].Visivel = True
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = True
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_PATRIMONIADO"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = True
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = True
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = True
        Formulario["LABEL1"].Visivel = True
    elif Controle.Valor == "Inativar" or Controle.Valor == "Reativar":
        Formulario["LABEL1"].Visivel = False
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = True
        Formulario["PRJ_DESC_ITEM"].Visivel = False
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_PATRIMONIADO"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = False
        Formulario["Justificativa"].Visivel = True
        Formulario["PRJ_AVISO"].Visivel = False
    else:
        Formulario["LABEL1"].Visivel = False
        Formulario["PRJ_CODIGO_ITEM"].Visivel = False
        Formulario["PRJ_CODIGO_ITENS"].Visivel = False
        Formulario["PRJ_DESC_ITEM"].Visivel = False
        Formulario["PRJ_UNI_MEDIDA"].Visivel = False
        Formulario["PRJ_PATRIMONIADO"].Visivel = False
        Formulario["PRJ_ORIGEM_ITEM"].Visivel = False
        Formulario["PRJ_CATEGORIA_NCM"].Visivel = False
        Formulario["Justificativa"].Visivel = False
        Formulario["PRJ_AVISO"].Visivel = False
