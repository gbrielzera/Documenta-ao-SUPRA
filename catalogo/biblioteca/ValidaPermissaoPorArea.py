# ValidaPermissaoPorArea
# Caminho: Catálogo > Biblioteca de scripts > ValidaPermissaoPorArea
# Fonte: Reembolsos__I.A_Versão_1_Reembolso_-_Iniciativa_IA.xml

def ValidaPermissaoPorArea(codAreaCliente, codAreaValida):

    resultado = 'Erro'

    if OrdemServico.Cliente.Orgao.Sigla == codAreaValida:
        resultado = 'Ok'
    else:
        areas = OrdemServico.Cliente.Orgao.ObtemSubOrgaos(True)
        
        for area in areas:
            if area.Ativo == True:
                if (area.Sigla == codAreaValida):
                    resultado = 'Ok'
        
        if resultado == 'Erro':
            areasPai = OrdemServico.Cliente.Orgao.ObtemOrgaosPais()

            for areaPai in areasPai:
                if areaPai.Ativo == True:
                    if (areaPai.Sigla == codAreaValida):
                        resultado = 'Ok'
            
    return resultado
