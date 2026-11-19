# isVisible_novo
# Caminho: Catálogo > Biblioteca de scripts > isVisible_novo
# Fonte: Reembolsos__I.A_Versão_1_Reembolso_-_Iniciativa_IA.xml

def isVisible_novo(field): 
    if field == None or field == DBNull.Value:
        return False
    elif field == '' or String.IsNullOrEmpty(field):
        return False
    else:
        return True
