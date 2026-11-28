# PrecifObtemCronogramaAtividade
# Caminho: Catálogo > Biblioteca de scripts > PrecifObtemCronogramaAtividade
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml (2 variantes entre os XMLs; esta é a mais recente)

def PrecifObtemCronogramaAtividade(ID_OCORRENCIA, CODIGO_ATIVIDADE):
    qry = " SELECT ID_OCORRENCIA, CODIGO_ATIVIDADE, RESPONSAVEL_ATIVIDADE, DATA_INICIO_ATIVIDADE, DATA_FIM_ATIVIDADE, DIAS_ATIVIDADE FROM Z_00143_PRECIF_CRONOGRAMA WHERE ID_OCORRENCIA = " + ID_OCORRENCIA.ToString() + " AND CODIGO_ATIVIDADE = '" + CODIGO_ATIVIDADE.ToString() + "'"

    lista = DB.ExecuteDataTable(qry)

    for linha in lista.Rows:
        return linha
