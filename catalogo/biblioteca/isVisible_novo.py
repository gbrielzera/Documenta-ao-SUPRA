# isVisible_novo
# Caminho: Catálogo > Biblioteca de scripts > isVisible_novo
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

def isVisible_novo(field): 
    if field == None or field == DBNull.Value:
        return False
    elif field == '' or String.IsNullOrEmpty(field):
        return False
    else:
        return True
