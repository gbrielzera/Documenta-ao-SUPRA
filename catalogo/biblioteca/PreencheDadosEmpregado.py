# PreencheDadosEmpregado
# Caminho: Catálogo > Biblioteca de scripts > PreencheDadosEmpregado
# Fonte: Utilização_de_veículo_locado_Versão_10_Indenização_por_Guarda_e_zelo_do_veículo_da_frota_(Lote).xml

def PreencheDadosEmpregado():
    for campo in ["TE_MATRICULA", "TE_CARGO", "TE_FUNCAO", "TE_UOR"]:
        Formulario[campo].Visivel = True
        Formulario[campo].Habilitado = False
        Formulario[campo].Valor = None

    lista = Utils.ExecuteDataTable("SELECT CASE WHEN P.CARGO IS NOT NULL THEN P.CARGO ELSE CAST(SUBSTR(C.CARGO,INSTR(C.CARGO,'|')+1,LENGTH(C.CARGO)) AS NVARCHAR2(50)) END CARGO, CASE WHEN CP.FUNCAO_GRATIFICADA IS NOT NULL THEN CP.FUNCAO_GRATIFICADA ELSE CAST(C.FUNCAO_GRATIFICADA AS NVARCHAR2(50)) END FUNCAO_GRATIFICADA, C.FIM_DATA_FUNCAO, CP.MATRICULA, O.DESCRICAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON P.ID_PESSOA = CP.ID_PESSOA INNER JOIN ORGAO O ON O.ID_ORGAO = P.ID_ORGAO LEFT JOIN CAD_FUNCIONARIO_V C ON C.MATRICULA = CP.MATRICULA AND C.DATA_DE_DEMISSAO IS NULL WHERE P.ID_PESSOA = '" + str(int(Formulario["FAVORECIDO_COBRA"].Valor or 0)) + "'")

    for linha in lista.Rows:
        Formulario["TE_CARGO"].Valor = linha["CARGO"].ToString()
        Formulario["TE_MATRICULA"].Valor = linha["MATRICULA"].ToString()
        Formulario["TE_UOR"].Valor = linha["DESCRICAO"].ToString()
        if linha["FIM_DATA_FUNCAO"].ToString() == "":
            Formulario["TE_FUNCAO"].Valor = linha["FUNCAO_GRATIFICADA"].ToString()
