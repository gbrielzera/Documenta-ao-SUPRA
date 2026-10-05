# isVisible_novo
# Caminho: Catálogo > Biblioteca de scripts > isVisible_novo
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

def isVisible_novo(field): 
    if field == None or field == DBNull.Value:
        return False
    elif field == '' or String.IsNullOrEmpty(field):
        return False
    else:
        return True
