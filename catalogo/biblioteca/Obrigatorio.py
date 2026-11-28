# Obrigatorio
# Caminho: Catálogo > Biblioteca de scripts > Obrigatorio
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

def Obrigatorio(campo):
    lista = Utils.ExecuteDataTable("SELECT TEXT, TYPE FROM SV_CUSTOM_PROPERTY WHERE NAME = '" + campo + "'")
    label = ""
    tipo = ""
    for cpo in lista.Rows:
        label = cpo["TEXT"]
        tipo = cpo["TYPE"]
        eNulo = False
        if tipo == "Boolean":
             if (OrdemServico.GetCustom(campo) == None):
                eNulo = True        
        if tipo == "DateTime":
             if (OrdemServico.GetCustom(campo) == None):
                eNulo = True
        if tipo == "String":
            if String.IsNullOrEmpty(OrdemServico.GetCustom(campo)) == True:
                eNulo = True
        if eNulo:
            Criticas.AdicionaPendencia("O campo '" + label + "' não foi preenchido.")
