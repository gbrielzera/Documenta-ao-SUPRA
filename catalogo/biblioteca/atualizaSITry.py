# atualizaSITry
# Caminho: Catálogo > Biblioteca de scripts > atualizaSITry
# Fonte: Gestão_de_Pessoas_-_Benefícios_Versão_90_Reembolso.xml (2 variantes entre os XMLs; esta é a mais recente)

def trySi(tabela, usuarioRede, dtAgi, numeroOS):
    #calcula segundos do dt_evt
    qryU = " "
    qryI = " "
    # acrescentado 10800 para compensar bug no SI
    
    qry = "SELECT EXTRACT(DAY FROM dt)*24*60*60 + EXTRACT(hour FROM dt)*60*60 + EXTRACT(minute FROM dt)*60 + EXTRACT(second FROM dt) + 10800 S FROM (SELECT TO_TIMESTAMP( SYSDATE ,'DD/MM/RR HH24:MI:SSXFF') - TO_TIMESTAMP( '01/01/1970','DD/MM/RR HH24:MI:SSXFF') DT FROM DUAL)"
    #lst = DB.ExecuteDataTable(qry)
        
    dtEvt = ""
    for l in lst.Rows:
        dtEvt = l["S"].ToString()
    
    if tabela != "tid":
        qry = "SELECT NVL(MAX(dt_evt),0) DT FROM " + tabela + " WHERE ativo = 'S' and autorizado = 'S' and id = '" + usuarioRede + "'"
        lista = Utils.ExecuteDataTable(qry)
        for linha in lista.Rows:
            # desativa o registro mais atual
            qryU = "UPDATE " + tabela + " SET ATIVO = 'N' WHERE dt_evt = (SELECT NVL(MAX(dt_evt),0) FROM " + tabela + " WHERE ativo = 'S' and autorizado = 'S' and id = '" + usuarioRede + "') and id = '" + usuarioRede + "'"
            #Utils.LogInformation(qryU.ToString(),"Script")
            #DB.ExecuteNonQuery(qryU)
            
            try:
                DB.ExecuteNonQuery(qryU)
            except Exception as erro:
                #Utils.SendMail("ivo.araujo@bbtecno.com.br", "ivo.araujo@bbtecno.com.br", "Erro qryU", qryU.ToString())
                #Utils.LogError("Erro : "+ erro.Message, "Erro")
            
            # cria novo registro ativo
            #qry = "INSERT INTO " + tabela + " (id, matricula, autorizado, tipo, ativo, dt_evt, dt_agi, dt_agf, usuario) SELECT id, matricula, 'S' autorizado, tipo, 'S' ativo, TRUNC((SYSDATE - DATE '1970-01-01')*24*60*60) dt_evt, TRUNC((DATE '" + data_retorno + "' - DATE '1970-01-01')*24*60*60) dt_agi, dt_agf, 'supravizio' usuario FROM " + tabela + " WHERE id = '" + usuarioRede + "' and dt_evt = (SELECT NVL(MAX(dt_evt),0) FROM " + tabela + " WHERE id = '" + usuarioRede + "' )"
            
            qryI = "INSERT INTO " + tabela + " (id, matricula, autorizado, tipo, ativo, dt_evt, dt_agi, dt_agf, usuario) SELECT id, matricula, 'S' autorizado, tipo, 'S' ativo, " + dtEvt.ToString() + " dt_evt, " + dtAgi.ToString()  + " dt_agi, dt_agf, 'supravizio' usuario FROM " + tabela + " WHERE id = '" + usuarioRede + "' and dt_evt = (SELECT NVL(MAX(dt_evt),0) FROM " + tabela + " WHERE id = '" + usuarioRede + "' )"
            
            DB.ExecuteNonQuery(qryI)
    else:
        # Pegar conteudo do campo acao para concatenar posteriormente
        qry = "select acao from (SELECT NVL(MAX(dt_evt),0) dt, ACAO FROM tid WHERE id = '" + usuarioRede + "' group by acao order by dt desc) where rownum = 1"
        lista = Utils.ExecuteDataTable(qry)
        acao = " - "
        for linha in lista.Rows:
            acao = linha["ACAO"]
        # atualiza tid
        # 1 - UPDATE
        # desativa o registro mais atual
        qryU = "UPDATE tid t SET ATIVO = 'N' WHERE dt_evt = (SELECT NVL(MAX(dt_evt),0) FROM tid WHERE id = '" + usuarioRede + "') and id = '" + usuarioRede + "'"
        DB.ExecuteNonQuery(qryU)
        
        # 2 - insert na tid para colocar ACAO = 'OS-999999 - Bloqueio de ferias', ATIVO = 'S' AUTORIZADO = 'N' e DT_EVT = TRUNC((SYSDATE - DATE '1970-01-01')*24*60*60)
        # cria novo registro ativo
        acao = " OS-" + numeroOS.ToString() + " - Bloqueio Automático de Férias. " + acao
        qryI = "INSERT INTO tid (id, matricula, pendente, acao, status, ativo, dt_evt, usuario) SELECT id, matricula, pendente, '" + acao + "' acao, status, 'S' ativo, " + dtEvt.ToString() + " dt_evt, 'supravizio' usuario FROM tid WHERE id = '" + usuarioRede + "' and dt_evt = (SELECT NVL(MAX(dt_evt),0) FROM tid WHERE id = '" + usuarioRede + "') "
                
        DB.ExecuteNonQuery(qryI)
 
    return "ok" #qry + " --- " + qryU + " --- " + qryI
