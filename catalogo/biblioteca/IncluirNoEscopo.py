# IncluirNoEscopo
# Caminho: Catálogo > Biblioteca de scripts > IncluirNoEscopo
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml

# Observação: ainda não foi utilizado em produção. Falta verificar se existe permissão para gravar na tabela 'SV_CUSTOM_PROPERTY_SCOPE'
# ATENÇÃO: Este script deve ser chamado no "Script Início" do  "evento inicial" para cadastrar todos os escopos utilizados no fluxo
# ex: campo = 'NUMERO_SERIE' <- campo a ser colocado o escopo e sigla = 'DEVAPAR' <- sigla do servico a ser colocado no escopo
# Exemplo de chamada deste método:
# campo = "NUMERO_SERIE" <- campo onder será incluido o escopo
# sigla = "DEVAPAR" <- sigla do servico que será colocado no escopo
# IncluirNoEscopo(campo, sigla) <- chamada do método de inclusão no escopo
def IncluirNoEscopo(campo, sigla):
    if campo != "" and sigla != "":
        #PEGA ID_SERVICO
        qry = "SELECT ID_SERVICO FROM SERVICO WHERE SIGLA = '" + sigla + "'"
        lista = DB.ExecuteDataTable(qry)
        for linha in lista.Rows:
            idServico = linha["ID_SERVICO"].ToString()
            if idServico != "":
#               # PEGA ESCOPO DO CAMPO
                qry = "SELECT CPS.ID_CUSTOM_PROPERTY, CPS.ID_PROPERTY, CP.NAME CAMPO, CPS.VALUE_SCOPE ESCOPO FROM SV_CUSTOM_PROPERTY CP INNER JOIN SV_CUSTOM_PROPERTY_SCOPE CPS ON CPS.ID_CUSTOM_PROPERTY = CP.ID_CUSTOM_PROPERTY WHERE CP.NAME = '" + campo.ToString() + "'"
                #Utils.LogInformation(qry.ToString(),"qry")
                lista = DB.ExecuteDataTable(qry)
                inclui = False
                for linha in lista.Rows:
                    inclui = True
                    cpo = linha["CAMPO"].ToString()
                    idCustomProperty = linha["ID_CUSTOM_PROPERTY"].ToString()
                    idProperty = linha["ID_PROPERTY"].ToString()
                    arr = linha["ESCOPO"].split(",")
                    # verifica se servico está no escopo
                    for id in arr:
                        if id == idServico:
                            # ja existe, não incluir no escopo
                            inclui = False
                if inclui == True :                
                    escopo = linha["ESCOPO"] + "," + idServico.ToString()
                    qry = "UPDATE SV_CUSTOM_PROPERTY_SCOPE SET VALUE_SCOPE = '" + escopo + "' WHERE ID_CUSTOM_PROPERTY = " + idCustomProperty.ToString() + " AND ID_PROPERTY = " + idProperty.ToString()
                    DB.ExecuteNonQuery(qry)
                    #Utils.LogInformation(message, category)Utils.LogInformation(message, category)
                    #Utils.LogWarning(message, category)Utils.LogInformation(message, category)
                    #Utils.LogWarning(message, category)Utils.NewSequenceValue(sequenceName)Utils.LogInformation(message, category)
