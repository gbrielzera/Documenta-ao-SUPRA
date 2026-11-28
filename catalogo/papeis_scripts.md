# Scripts de papéis (Seleção de Atores) — homologação, 2026-11-27

[banco] 268 scripts distintos de papéis do tipo Script. Comentários, e-mails e identificadores de pessoas foram
removidos. São código do cliente, muitas vezes verboso: servem de prova de uso, não de modelo (valem as regras de script
mínimo). Variáveis usadas: `Atores`, `OrdemServico`, `DB`, `Utils`; classes importadas como `Pessoa`, `Orgao`, `Ator`.
Padrões: `Atores.Adiciona(pessoa, "motivo")`, `Pessoa.Carrega(id)`, `OrdemServico.Favorecido.ObtemChefia(True)`.

## Abertura processos TI
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.Favorecido.Id))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = gestor
i = 0
while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO":
    if i > 5:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(aprovador, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Abertura Solicitacao Uniformes
```python
tabela = DB.ExecuteDataTable("SELECT PESSOA.NOME AS PESSOAS FROM PESSOA INNER JOIN ORGAO ON PESSOA.ID_ORGAO = ORGAO.ID_ORGAO WHERE ORGAO.SIGLA IN ('2000004028', '2000004035', '2000004032', '2000004029', '2000004036', '2000004020', '2000007400', '1000004018', '1000004021')")
for dr in tabela.Rows:
    pessoa = Pessoa.Carrega(dr["PESSOAS"])
    Atores.Adiciona(pessoa)
```

## Alçada de Aprovação - Conforme Alçada da Abertura
```python
if OrdemServico.Servico.Sigla == "ALTERAPASSAAEREA":
    os = OrdemServico.Carrega("Numero", OrdemServico["CSC_NUMERO_OS"])
    favorecido = Pessoa.Carrega(Convert.ToInt32(os.FavorecidoId))
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
    Atores.Adiciona(aprovador, "Alçada de Aprovação do Favorecido")
```

## Alçada de Aprovação - Viagem e Hospedagem
```python
os = OrdemServico
if OrdemServico.Servico.Sigla == "ALTERAPASSAAEREA":
    os = OrdemServico.Carrega("Numero", OrdemServico["CSC_NUMERO_OS"])
favorecido = Pessoa.Carrega(Convert.ToInt32(os.FavorecidoId))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = gestor
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla
if os.Servico.Sigla == "CANCELPASSAGHOSPEDA":
    gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
    aprovador = gestor
else:
    if os["PAH_TIPO_SOLICITACAO"] == "Hospedagens":
       qry = "select trunc(to_date('" + os["PAH_DATA_ENTRADA"].ToString() + "', 'DD/MM/YYYY HH24:MI:SS')) - trunc(to_date('" + os.DataHoraSolicitacao.ToString() + "', 'DD/MM/YYYY HH24:MI:SS')) dias from dual"
       diasAntecedencia = DB.ExecuteScalar(qry)
    else:
       qry = "select (trunc(DATA_VOO) - trunc(to_date(data_hora_sol))) dias from (select z.DATA_VOO, oc.data_hora_sol from ocorrencia oc inner join z_00143_reserva_de_voo z on z.id_ocorrencia = oc.id_ocorrencia where z.id_ocorrencia = " + os.Id.ToString() + " order by z.DATA_VOO) where rownum = 1"
       diasAntecedencia = DB.ExecuteScalar(qry)
    if (orgaoFavorecido == "3000001330" or orgaoFavorecido == "3000009400" or orgaoFavorecido == "3000009220") and cargoFavorecido == "GERENTE EXECUTIVO" and diasAntecedencia < 14:
       div = Orgao.Carrega("Sigla", "4000009000")
       aprovador = div.Gestor
    elif os.Servico.Sigla != "CANCELPASSAGHOSPEDA":
        funcoes = ["GERENTE EXECUTIVO", "DIRETOR", "PRESIDENTE"]
        areas = ["3000001330", "3000001331", "3000001332", "3000009200", "3000009220", "3000009221", "3000009222", "3000009400", "3000009410", "3000009420", "3000001361", "3000001362", "3000009430"]
        cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
        orgaoFavorecido = favorecido.Orgao.Sigla
        aprovador = gestor
        estaFuncao = False
        for funcao in funcoes:
            if cargoFavorecido == funcao:
               estaFuncao = True
               break
        estaArea = False
        for area in areas:
            if orgaoFavorecido == area:
               estaArea = True
               break
        if (not estaFuncao) and (not estaArea):
           if diasAntecedencia > 14:
              if favorecido == aprovador:
                 aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
           elif diasAntecedencia > 1:
              i = 0
              while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO":
                 if i > 5:
                    break
                 i = i + 1
                 aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
           elif diasAntecedencia >= 0:
              i = 0
              while aprovador["CARGO_FUNCIONAL"] != "DIRETOR":
                 if i > 5:
                    break
                 i = i + 1
                 aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
        elif estaFuncao and os.Favorecido.Orgao.Sigla.ToString() == "4000001110":
           if diasAntecedencia > 14:
              div = Orgao.Carrega("Sigla", "4000001111")
              aprovador = div.Gestor
           elif diasAntecedencia >= 0:
              div = Orgao.Carrega("Sigla", "4000009000")
              aprovador = div.Gestor
        elif estaFuncao and os.Favorecido.Orgao.Sigla.ToString() == "3000001330":
           div = Orgao.Carrega("Sigla", "4000009000")
           aprovador = div.Gestor
        elif estaArea or estaFuncao:
           if diasAntecedencia > 14:
              if estaArea and not estaFuncao:
                 if favorecido == aprovador:
                    aprovador = aprovador.Orgao.OrgaoPai.Gestor
              elif cargoFavorecido == "DIRETOR" or cargoFavorecido == "PRESIDENTE":
                 div = Orgao.Carrega("Sigla", "3000009410")
                 aprovador = div.Gestor
           elif diasAntecedencia >= 0:
              if estaArea:
                 div = Orgao.Carrega("Sigla", "4000009000")
                 aprovador = div.Gestor
Atores.Adiciona(aprovador, "Alçada de Aprovação do Favorecido")
```

## Alçada de Aprovação por Posição Viagem e Hospedagem
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.FavorecidoId))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = gestor
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla
if OrdemServico.Servico.Sigla == "CANCELPASSAGHOSPEDA":
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.FavorecidoId))
    gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
    aprovador = gestor
else:
    if OrdemServico["PAH_TIPO_SOLICITACAO"] == "Hospedagens":
       qry = "select trunc(to_date('" + OrdemServico["PAH_DATA_ENTRADA"].ToString() + "', 'DD/MM/YYYY HH24:MI:SS')) - trunc(to_date('" + OrdemServico.DataHoraSolicitacao.ToString() + "', 'DD/MM/YYYY HH24:MI:SS')) dias from dual"
       diasAntecedencia = DB.ExecuteScalar(qry)
    else:
       qry = "select (trunc(DATA_VOO) - trunc(to_date(data_hora_sol))) dias from (select z.DATA_VOO, oc.data_hora_sol from ocorrencia oc inner join z_00143_reserva_de_voo z on z.id_ocorrencia = oc.id_ocorrencia where z.id_ocorrencia = " + OrdemServico.Id.ToString() + " order by z.DATA_VOO) where rownum = 1"
       diasAntecedencia = DB.ExecuteScalar(qry)
    if (orgaoFavorecido == "3000001330" or orgaoFavorecido == "3000009400" or orgaoFavorecido == "3000009220") and cargoFavorecido == "GERENTE EXECUTIVO" and diasAntecedencia < 14:
       div = Orgao.Carrega("Sigla", "4000009000")
       aprovador = div.Gestor
    elif OrdemServico.Servico.Sigla != "CANCELPASSAGHOSPEDA":
        funcoes = ["GERENTE EXECUTIVO", "DIRETOR", "PRESIDENTE"]
        areas = ["3000001330", "3000001331", "3000001332", "3000009200", "3000009220", "3000009221", "3000009222", "3000009400", "3000009410", "3000009420", "3000001361", "3000001362", "3000009430"]
        cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
        orgaoFavorecido = favorecido.Orgao.Sigla
        aprovador = gestor
        estaFuncao = False
        for funcao in funcoes:
            if cargoFavorecido == funcao:
               estaFuncao = True
               break
        estaArea = False
        for area in areas:
            if orgaoFavorecido == area:
               estaArea = True
               break
        if (not estaFuncao) and (not estaArea):
           if diasAntecedencia >= 14:
              if favorecido == aprovador:
                 aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
           elif diasAntecedencia > 1:
              i = 0
              while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO":
                 if i > 5:
                    break
                 i = i + 1
                 aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
           elif diasAntecedencia >= 0:
              i = 0
              while aprovador["CARGO_FUNCIONAL"] != "DIRETOR":
                 if i > 5:
                    break
                 i = i + 1
                 aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
        elif estaFuncao and OrdemServico.Favorecido.Orgao.Sigla.ToString() == "4000001110":
           if diasAntecedencia >= 14:
              div = Orgao.Carrega("Sigla", "4000001111")
              aprovador = div.Gestor
           elif diasAntecedencia >= 0:
              div = Orgao.Carrega("Sigla", "4000009000")
              aprovador = div.Gestor
        elif estaFuncao and OrdemServico.Favorecido.Orgao.Sigla.ToString() == "3000001330":
           div = Orgao.Carrega("Sigla", "4000009000")
           aprovador = div.Gestor
        elif estaArea or estaFuncao:
           if diasAntecedencia >= 14:
              if estaArea and not estaFuncao:
                 if favorecido == aprovador:
                    aprovador = aprovador.Orgao.OrgaoPai.Gestor
              elif cargoFavorecido == "DIRETOR" or cargoFavorecido == "PRESIDENTE":
                 div = Orgao.Carrega("Sigla", "3000009410")
                 aprovador = div.Gestor
           elif diasAntecedencia >= 0:
              if estaArea:
                 div = Orgao.Carrega("Sigla", "4000009000")
                 aprovador = div.Gestor
Atores.Adiciona(aprovador, "Alçada de Aprovação do Favorecido")
```

## Alçadas de Aprovação por Posição Viagem e Hospedagem - Conforme NI006v.50
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.FavorecidoId))
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla
diasAntecedencia = 0
diasH = 0
diasP = 0
gestorPosicao = ""
if cargoFavorecido == "PRESIDENTE":
   uor = Orgao.Carrega("Sigla", "3000003160")
   gestor = uor.Gestor
   gestorPosicao = gestor["MATRICULA"]
else:
   gestorPosicao = favorecido["GESTOR_POSICAO"].ToString()
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '" + gestorPosicao + "'")))
aprovador = gestor
if OrdemServico.Servico.Sigla == "CANCELPASSAGHOSPEDA" or OrdemServico["PAH_MOTIVO_SOL"] == "Atendimento técnico" :
    aprovador = gestor
Atores.Adiciona(aprovador, "Alçada de Aprovação do Favorecido")
```

## Alçadas de Aprovação por Posição Viagem e Hospedagem - Conforme NI006v.56
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.FavorecidoId))
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla
gestorPosicao = ""
if cargoFavorecido == "PRESIDENTE" or cargoFavorecido == "DIRETOR":
    uor = Orgao.Carrega("Sigla", "3000003150")
    gestor = uor.Gestor
    aprovador = gestor
else:
    if cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "4000001110":
        uor = Orgao.Carrega("Sigla", "4000001111")
        gestor = uor.Gestor
        aprovador = gestor
    else:
        gestorid = favorecido.Orgao.GestorId
        gestor = favorecido.Orgao.Gestor
        if gestorid == OrdemServico.FavorecidoId:
            gestor = favorecido.Orgao.OrgaoPai.Gestor
        aprovador = gestor
Atores.Adiciona(aprovador, "Alçada de Aprovação do Favorecido Conforme NI006v.56")
```

## Alçadas de Aprovação por Posição Viagem e Hospedagem - Conforme NI006v_56
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.FavorecidoId))
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla
gestorPosicao = ""
if cargoFavorecido == "PRESIDENTE" or cargoFavorecido == "DIRETOR":
    uor = Orgao.Carrega("Sigla", "3000009430")
    gestor = uor.Gestor
    aprovador = gestor
else:
    if cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "4000001110":
        uor = Orgao.Carrega("Sigla", "4000001111")
        gestor = uor.Gestor
        aprovador = gestor
    else:
        gestorid = favorecido.Orgao.GestorId
        gestor = favorecido.Orgao.Gestor
        if gestorid == OrdemServico.FavorecidoId:
            gestor = favorecido.Orgao.OrgaoPai.Gestor
        aprovador = gestor
Atores.Adiciona(aprovador, "Alçada de Aprovação do Favorecido Conforme NI006v.56")
```

## Analista de Suporte inicial
```python
if (OrdemServico.GetCustom("SISTEMA_OPERACIONAL") == "Windows"):
   pessoa = Pessoa.Carrega("Nome","<NOME>")
   Atores.Adiciona(pessoa)
if (OrdemServico.GetCustom("SISTEMA_OPERACIONAL") == "Linux"):
  pessoa = Pessoa.Carrega("Nome","<NOME>")
  Atores.Adiciona(pessoa)
if (OrdemServico.GetCustom("SISTEMA_OPERACIONAL") == "Solaris"):
  pessoa = Pessoa.Carrega("Nome","<NOME>")
  Atores.Adiciona(pessoa)
```

## Analista Responsável / Implantador de Acesso / Analista de Configuração / Responsável área negócio
```python
Atores.Adiciona(OrdemServico.Servico.ResponsavelTecnico, "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
```

## Analista Suplente
```python
analistaMatricula = str(OrdemServico.GetCustom('MATRICULA_ANA_SUP'))
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + analistaMatricula + "'")
idAnalista = 0
for row in lista.Rows:
    idAnalista = row['ID_PESSOA']
Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idAnalista)))
```

## Analista Titular
```python
analistaMatricula = str(OrdemServico.GetCustom('MATRICULA_ANA_TITU'))
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + analistaMatricula + "'")
idAnalista = 0
for row in lista.Rows:
    idAnalista = row['ID_PESSOA']
Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idAnalista)))
```

## Aprovador de uma movimentação
```python
idGestorRecurso = OrdemServico.GetCustom("FAVORECIDO_TODOS")
if idGestorRecurso != None:
    gestorRecurso = Pessoa.Carrega(Convert.ToInt32(idGestorRecurso))
    if gestorRecurso != None:
        Atores.Adiciona(gestorRecurso, "Gestor para aprovação")
```

## Aprovador Destino Orçamento
```python
db= DB.ExecuteDataTable('SELECT Z.AREA_DESTINO, Z.GLOSSARIO2, Z.AREA_DESTINO,Z.GLOSSARIO2  FROM OCORRENCIA O INNER JOIN Z_00143_ORCAMENTO Z ON Z.ID_OCORRENCIA = O.ID_OCORRENCIA where O.ID_OCORRENCIA = '+ OrdemServico.Id.ToString())
for rec in db.Rows:
    sql= ("select MATRICULA_APROV FROM xxbbtsgate.vw_bbts_remanejamento_aprov  WHERE CONTA = '"+rec["GLOSSARIO2"].ToString()+"' AND UOR = '" + rec["AREA_DESTINO"].ToString() + "'")
    matricula = DB.ExecuteScalar (sql)
    sqlusuario = ("SELECT P.USUARIO_REDE FROM PESSOA P INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA WHERE CP.MATRICULA ='"+matricula.ToString()+"'")
    usuario = DB.ExecuteScalar(sqlusuario)
    if usuario  != None:
        p = Pessoa.Carrega("UsuarioRede",usuario)
        Atores.Adiciona(p)
```

## Aprovador documento
```python
alcada = OrdemServico.GetCustom("NUM_VERSAO")
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join Z_00143_LISTA_APROVA_DOC aprova on oc.id_ocorrencia = aprova.id_ocorrencia inner join pessoa pe on aprova.APROVADOR = pe.id_pessoa WHERE oc.numero = '" + OrdemServico.Numero + "' AND aprova.ALCADA = '" + alcada.ToString() + "' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Aprovador Gerex 2 - Faturamento
```python
idGerex2 = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("GEREX_FAT")))
if idGerex2 != None:
    Atores.Adiciona(idGerex2, "Gerente Executivo Selecionado")
```

## Aprovador GESTOR_DO_COLABORADOR
```python
idGestor = OrdemServico["GESTOR_DO_COLABORADOR"]
pessoa = Pessoa.Carrega(idGestor)
Atores.Adiciona(pessoa)
```

## Aprovador Origem Orçamento
```python
db= DB.ExecuteDataTable('SELECT  Z.ARGESTORA, Z.GLOSSARIO  FROM OCORRENCIA O INNER JOIN Z_00143_ORCAMENTO Z ON Z.ID_OCORRENCIA = O.ID_OCORRENCIA where O.ID_OCORRENCIA = '+ OrdemServico.Id.ToString())
for rec in db.Rows:
    sql_conta= ("select  CONTA FROM xxbbtsgate.vw_bbts_remanejamento_aprov WHERE GLOSSARIO ='"+rec["GLOSSARIO"].ToString()+"' AND UOR = '" + rec["ARGESTORA"].ToString() + "'")
    sql= ("select MATRICULA_APROV FROM xxbbtsgate.vw_bbts_remanejamento_aprov  WHERE CONTA = '"+rec["GLOSSARIO"].ToString()+"' AND UOR = '" + rec["ARGESTORA"].ToString() + "'")
    matricula = DB.ExecuteScalar (sql)
    sqlusuario = ("SELECT P.USUARIO_REDE FROM PESSOA P INNER JOIN CP_PESSOA CP ON CP.ID_PESSOA = P.ID_PESSOA WHERE CP.MATRICULA ='"+matricula.ToString()+"'")
    usuario = DB.ExecuteScalar(sqlusuario)
    if usuario  != None:
        p = Pessoa.Carrega("UsuarioRede",usuario)
        Atores.Adiciona(p)
```

## Aprovador para Substituições
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_SUBST"))
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
    nomeFavorecido = favorecidoCustom.Nome
    orgaoFavorecido = favorecidoCustom.OrgaoId
else:
    nomeFavorecido = OrdemServico.Favorecido.Nome
    orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
orgao = Orgao.Carrega(orgaoFavorecido)
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
if gestor != None:
    if gestor == favorecidoCustom:
        gestor = gestor.Orgao.OrgaoPai.Gestor
        Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
    else:
        Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Aprovadores documentos TI
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join Z_00143_LISTA_INTERVENIENTES inter on oc.id_ocorrencia = inter.id_ocorrencia inner join pessoa pe on inter.interveniente = pe.id_pessoa where oc.id_ocorrencia = '"+ OrdemServico.Id.ToString() +"' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Aprovadores documentos TI - Gestor Pendente
```python
tabela = Utils.ExecuteDataTable(" SELECT Pea.Id_Pessoa, PEA.nome, Cppa.Matricula, Cppa.Gestor_Posicao FROM ocorrencia OC INNER JOIN ATIVIDADE AT ON (AT.id_atividade = oc.id_atividade) INNER JOIN OPERACAO_ATIVIDADE OA ON (AT.id_atividade = OA.id_atividade) INNER JOIN assunto_aprovacao ASS ON (oc.id_ocorrencia = ass.id_ocorrencia AND OA.ID_OPERACAO_ATIVIDADE = ASS.OPERACAO_ATIVIDADE) INNER JOIN aprovacao AP ON ass.id_assunto_aprovacao = ap.id_assunto_aprovacao INNER JOIN pessoa PEA ON ap.id_pessoa = pea.id_pessoa INNER JOIN CP_pessoa CPPA ON Pea.Id_Pessoa = Cppa.Id_Pessoa WHERE ap.versao = (SELECT MAX(ap.versao) FROM ocorrencia OC INNER JOIN assunto_aprovacao ASS ON (oc.id_ocorrencia = ass.id_ocorrencia) INNER JOIN aprovacao AP ON ass.id_assunto_aprovacao = ap.id_assunto_aprovacao AND oc.id_ocorrencia = '" + OrdemServico.Id.ToString() + "' ) AND Ap.Situacao = 'Pendente' AND oc.id_ocorrencia = '" + OrdemServico.Id.ToString() + "'")
for ator in tabela.Rows:
    gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '" + ator["GESTOR_POSICAO"].ToString() + "'")))
    if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
        gestor = OrdemServico.Cliente
    Atores.Adiciona(gestor, "Superior imediato de " + ator["ID_PESSOA"].ToString() + ' - ' + ator["NOME"].ToString())
```

## Aprovadores documentos TI - Pendente
```python
tabela = Utils.ExecuteDataTable(" SELECT Pea.Id_Pessoa FROM ocorrencia OC INNER JOIN ATIVIDADE AT ON (AT.id_atividade = oc.id_atividade) INNER JOIN OPERACAO_ATIVIDADE OA ON (AT.id_atividade = OA.id_atividade) INNER JOIN assunto_aprovacao ASS ON (oc.id_ocorrencia = ass.id_ocorrencia AND OA.ID_OPERACAO_ATIVIDADE = ASS.OPERACAO_ATIVIDADE) INNER JOIN aprovacao AP ON ass.id_assunto_aprovacao = ap.id_assunto_aprovacao INNER JOIN pessoa PEA ON ap.id_pessoa = pea.id_pessoa WHERE ap.versao = (SELECT max(ap.versao) FROM ocorrencia OC INNER JOIN assunto_aprovacao ASS ON (oc.id_ocorrencia = ass.id_ocorrencia) INNER JOIN aprovacao AP ON ass.id_assunto_aprovacao = ap.id_assunto_aprovacao AND oc.id_ocorrencia = '" + OrdemServico.Id.ToString() + "' ) and Ap.Situacao = 'Pendente' AND oc.id_ocorrencia = '" + OrdemServico.Id.ToString() + "' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Aprovadores pendentes
```python
pesquisaAprovadoresPendentes = DB.ExecuteDataTable("Select OCORRENCIA.NUMERO, OCORRENCIA.ID_OCORRENCIA, ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO, ASSUNTO_APROVACAO.DESCRICAO, VERSAO_APROVACAO.VERSAO,VERSAO_APROVACAO.DATA_HORA_CRIACAO, PESSOA.NOME, APROVACAO.MOTIVO, APROVACAO.SITUACAO From OCORRENCIA Inner Join ASSUNTO_APROVACAO On OCORRENCIA.ID_OCORRENCIA = ASSUNTO_APROVACAO.ID_OCORRENCIA Inner Join VERSAO_APROVACAO On ASSUNTO_APROVACAO.ID_ASSUNTO_APROVACAO = VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO Inner Join APROVACAO On VERSAO_APROVACAO.ID_ASSUNTO_APROVACAO = APROVACAO.ID_ASSUNTO_APROVACAO And VERSAO_APROVACAO.VERSAO = APROVACAO.VERSAO Inner Join PESSOA On APROVACAO.ID_PESSOA = PESSOA.ID_PESSOA WHERE OCORRENCIA.ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"' AND APROVACAO.SITUACAO = 'Pendente'")
for pessoa in pesquisaAprovadoresPendentes.Rows:
    aprovadorPendente = Pessoa.Carrega(pessoa["NOME"])
    Atores.Adiciona(aprovadorPendente)
```

## Aprovadores Projeto Básico
```python
tentativa = 0
while tentativa < 5:
    pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, APROVADORES FROM Z_00143_APROVADOR_PB WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
    tentativa = tentativa + 1
    for pessoa in pesquisa01.Rows:
        aprovadores = Pessoa.Carrega(Convert.ToInt32(pessoa["APROVADORES"]))
        Atores.Adiciona(aprovadores)
```

## Aprovadores requisitos
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join Z_00143_LISTA_INTERVENIENTES inter on oc.id_ocorrencia = inter.id_ocorrencia inner join pessoa pe on inter.interveniente = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Aprovação Viagem e Hospedagem - Conforme NI006v.87
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla
gestorPosicao = ""
if (cargoFavorecido == "PRESIDENTE" or cargoFavorecido == "DIRETOR" or cargoFavorecido == "ASSESSOR EXECUTIVO PRESIDENCIA" or cargoFavorecido == "<NOME>" or cargoFavorecido == "CONSELHEIRO DE ADMINISTRACAO" or cargoFavorecido == "CONSELHEIRO FISCAL") or (cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000009200" or orgaoFavorecido == "3000001330" or orgaoFavorecido == "3000009400" or orgaoFavorecido == "3000004052") or (cargoFavorecido == "GERENTE DE PROJETOS I" and orgaoFavorecido == "3000004051" or orgaoFavorecido == "3000004055"):
    uor = Orgao.Carrega("Sigla", "3000009430")
    gestor = uor.Gestor
    aprovador = gestor
else:
    if cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "4000001110":
        uor = Orgao.Carrega("Sigla", "4000001112")
        gestor = uor.Gestor
        aprovador = gestor
    else:
        gestorid = favorecido.Orgao.GestorId
        gestor = favorecido.Orgao.Gestor
        if gestorid == favorecido.Id:
            gestor = favorecido.Orgao.OrgaoPai.Gestor
        aprovador = gestor
Atores.Adiciona(aprovador, "Aprovação Viagem e Hospedagem - Conforme NI006v.87")
```

## Assessor Gesap / Gerente Divisão Gesap
```python
query = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL, ORGAO.SIGLA, PESSOA.ID_PESSOA From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Where CP_PESSOA.CARGO_FUNCIONAL Like '%DIVISAO' And ORGAO.SIGLA = '3000003154'")
for i in query.Rows:
    id = Convert.ToInt32(i['ID_PESSOA'])
    pessoa = Pessoa.Carrega(id)
    Atores.Adiciona(pessoa)
```

## Assessor Saúde Ocupacional
```python
tabela = Utils.ExecuteDataTable("SELECT pe.id_pessoa AS ID_PESSOA FROM cad_funcionario_v fu INNER JOIN cp_pessoa cpe ON fu.matricula = cpe.matricula INNER JOIN pessoa    pe ON ( pe.id_pessoa = cpe.id_pessoa ) INNER JOIN orgao    o ON ( pe.ID_ORGAO = o.ID_ORGAO ) WHERE o.sigla = '3000003204' and pe.ativo = 'Sim' and fu.cargo_funcional LIKE 'ASSESSOR%'")
for dr in tabela.Rows:
    pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## AssessoresGereg
```python
scr = OrdemServico.GetCustom("TE_UOR")
geregco =  ["1000007799", "1000007782", "1000007296", "1000007781", "1000007293"]
geregno =  ["1000007796", "1000007798", "1000007422", "1000007785", "1000007784"]
geregne =  ["1000007421", "1000007484", "1000007512", "1000007494", "1000007423", "1000007487"]
geregse =  ["1000007121", "1000007101", "1000007122", "1000007133", "1000007131", "1000007124"]
geregsp =  grupo_SP = ["1000007281 - CEN. ASSIST. TECN. S. PAULO","1000007283 - (não listado, precisa confirmar)","1000008122 - (não listado, precisa confirmar)","1000007295 - CENTRO DE ASSISTENCIA TECNICA BAURU","1000007282 - CEN. ASSIST. TECN. CAMPINAS","1000007290 - CEN. ASSIST. TECN. R. PRETO","1000007284 - CENTRO DE ASSISTENCIA TECNICA BARUERI"]
geregsul = ["1000007391", "1000007381", "1000007383", "1000007392", "1000007382", "1000007388", "1000007381"]
if scr in geregco:
    p1 = Pessoa.Carrega(12345)
    p2 = Pessoa.Carrega(67890)
    Atores.Adiciona(p1, "Assessores SuperGereg")
    Atores.Adiciona(p2, "Assessores SuperGereg")
elif scr in geregno:
    p1 = Pessoa.Carrega(11111)
    p2 = Pessoa.Carrega(22222)
    Atores.Adiciona(p1, "Assessores SuperGereg")
    Atores.Adiciona(p2, "Assessores SuperGereg")
elif scr in geregne:
    p1 = Pessoa.Carrega(33333)
    p2 = Pessoa.Carrega(44444)
    Atores.Adiciona(p1, "Assessores SuperGereg")
    Atores.Adiciona(p2, "Assessores SuperGereg")
elif scr in geregse:
    p1 = Pessoa.Carrega(55555)
    p2 = Pessoa.Carrega(66666)
    Atores.Adiciona(p1, "Assessores SuperGereg")
    Atores.Adiciona(p2, "Assessores SuperGereg")
elif scr in geregsp:
    p1 = Pessoa.Carrega(24307)
    p2 = Pessoa.Carrega(16155)
    Atores.Adiciona(p1, "Assessores SuperGereg")
    Atores.Adiciona(p2, "Assessores SuperGereg")
elif scr in geregsul:
    p1 = Pessoa.Carrega(99999)
    p2 = Pessoa.Carrega(15978)
    Atores.Adiciona(p1, "Assessores SuperGereg")
    Atores.Adiciona(p2, "Assessores SuperGereg")
else:
    Utils.LogError("SCR_TODOS_RH não mapeado: " + scr, "INFO")
```

## AssessoresSuper
```python
if not String.IsNullOrEmpty(OrdemServico['TE_UOR'].ToString()):
    num_uor = OrdemServico['TE_UOR'].split(' - ')[0]
else:
    num_uor = OrdemServico['SCR_TODOS_RH']
grupo_CO = ["1000007799","1000007782","1000007296","1000007781","1000007293"]
grupo_NO = ["1000007796","1000007798","1000007422","1000007785","1000007784"]
grupo_NE = ["1000007421","1000007484","1000007512","1000007494","1000007423","1000007487"]
grupo_SE = ["1000007121","1000007101","1000007122","1000007133","1000007131","1000007124"]
grupo_SP = ["1000007281","1000007283","1000008122","1000007295","1000007282","1000007290","1000007284"]
grupo_SUL = ["1000007391","1000007381","1000007383","1000007392","1000007382","1000007388"]
if num_uor in grupo_CO:
    for idPessoa in [24145, 4629, 25628]:
        p = Pessoa.Carrega(idPessoa)
        Atores.Adiciona(p, "Super CN Gereg CO")
elif num_uor in grupo_NO:
    for idPessoa in [24145, 4629, 25628]:
        p = Pessoa.Carrega(idPessoa)
        Atores.Adiciona(p, "Super CN Gereg NO")
elif num_uor in grupo_NE:
    for idPessoa in [24307, 16155]:
        p = Pessoa.Carrega(idPessoa)
        Atores.Adiciona(p, "Super NE Gereg NE")
elif num_uor in grupo_SE:
    for idPessoa in [24560, 25116, 28161]:
        p = Pessoa.Carrega(idPessoa)
        Atores.Adiciona(p, "Super SE Gereg SE")
elif num_uor in grupo_SP:
    for idPessoa in [23928,11444,13230]:
        p = Pessoa.Carrega(idPessoa)
        Atores.Adiciona(p, "Super SP Gereg SP")
elif num_uor in grupo_SUL:
    for idPessoa in [23495, 23224]:
        p = Pessoa.Carrega(idPessoa)
        Atores.Adiciona(p, "Super Sul Gereg Sul")
else:
    Utils.LogError("Não faz parte da Gered: " + num_uor, "INFO")
```

## Campo Responsável
```python
responsavel = Convert.ToInt32(OrdemServico.GetCustom("TEXT"))
favorecido = Pessoa.Carrega(responsavel)
if favorecido != None:
    Atores.Adiciona(favorecido, "Favorecido")
```

## Cipa - grupo resposta
```python
pessoa = Pessoa.Carrega(3210)
Atores.Adiciona(pessoa)
pessoa = Pessoa.Carrega(3208)
Atores.Adiciona(pessoa)
pessoa = Pessoa.Carrega(3278)
Atores.Adiciona(pessoa)
pessoa = Pessoa.Carrega(3122)
Atores.Adiciona(pessoa)
```

## CIPA Presidente e Vice
```python
idPresidente = OrdemServico.GetCustom("PRESIDENTE_CIPA")
idVicePresidente = OrdemServico.GetCustom("VICE_PRESIDENTE_CIPA")
presidente = Pessoa.Carrega(Convert.ToInt32(idPresidente))
vicePresidente = Pessoa.Carrega(Convert.ToInt32(idVicePresidente))
if presidente != None:
    Atores.Adiciona(presidente, "Presidente CIPA")
if vicePresidente != None:
    Atores.Adiciona(vicePresidente, "Vice Presidente CIPA")
```

## Cliente / Assessor Gepes
```python
Atores.Adiciona(OrdemServico.Cliente, "Pessoa informada como Cliente na Ordem de Serviço")
```

## Cliente processo compras
```python
tabela = Utils.ExecuteDataTable(" SELECT li.interveniente as ID_PESSOA FROM OCORRENCIA OC inner join Z_00143_LISTA_INTERVENIENTES li on oc.id_ocorrencia = li.id_ocorrencia where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
	pessoa = Pessoa.Carrega(Convert.ToInt32(ator["ID_PESSOA"]))
	Atores.Adiciona(pessoa)
```

## Colaborador DITEC
```python
colaborador = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DITEC"))
pessoa = Pessoa.Carrega(colaborador)
Atores.Adiciona(pessoa)
```

## Concursado
```python
pessoaId = DB.ExecuteNonQuery("SELECT ID_PESSOA FROM pessoa where USUARIO_REDE = '" + OrdemServico.GetCustom("CSC_USUARIO_REDE").ToString() + "' and ATIVO = 'Sim'")
OrdemServico.ResponsavelId = pessoaId
```

## Concursado Novo
```python
tabela = Utils.ExecuteDataTable("SELECT ID_PESSOA FROM pessoa where USUARIO_REDE = '" + OrdemServico.GetCustom("CSC_USUARIO_REDE").ToString() + "' and ATIVO = 'Sim')")
for dr in tabela.Rows:
    pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Condutor do Contrato
```python
import clr
clr.AddReference("Supravizio.Custom")
if OrdemServico.GetCustom("MATRICULA_CONDUT_TITU"):
    result_table = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA From CP_PESSOA Where CP_PESSOA.MATRICULA = '"+str(Convert.ToInt32(OrdemServico.GetCustom("MATRICULA_CONDUT_TITU")))+"'")
    OrdemServico.AdicionaComentario(str(result_table.Rows), True)
    for row in result_table.Rows:
        favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(row["ID_PESSOA"]))
        if favorecidoCobra != None:
            Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Condutor do Contrato Suplente
```python
import clr
clr.AddReference("Supravizio.Custom")
if OrdemServico.GetCustom("MATRICULA_CONDUT_SUP"):
    result_table = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA From CP_PESSOA Where CP_PESSOA.MATRICULA = '"+str(Convert.ToInt32(OrdemServico.GetCustom("MATRICULA_CONDUT_SUP")))+"'")
    OrdemServico.AdicionaComentario(str(result_table.Rows), True)
    for row in result_table.Rows:
        favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(row["ID_PESSOA"]))
        if favorecidoCobra != None:
            Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Controle de Licença
```python
pessoa = Pessoa.Carrega("Nome","<NOME>")
Atores.Adiciona(pessoa)
pessoa = Pessoa.Carrega("Nome","<NOME>")
Atores.Adiciona(pessoa)
pessoa = Pessoa.Carrega("Nome","<NOME>")
Atores.Adiciona(pessoa)
```

## Coordenador do Grupo de Trabalho
```python
tabela = Utils.ExecuteDataTable(" SELECT id_grupo_trabalho FROM grupo_trabalho WHERE descricao = '"+ OrdemServico.GetCustom("COMBOBOX").ToString() +"' ")
for grupo in tabela.Rows:
    idGrupoTrabalho = Convert.ToInt32(grupo["ID_GRUPO_TRABALHO"])
if idGrupoTrabalho != None:
    grupoTrabalho = GrupoTrabalho.Carrega(Convert.ToInt32(idGrupoTrabalho))
    idCorrdenador = grupoTrabalho.CoordenadorId
    coordenadorGrupoTrabalho = Pessoa.Carrega(idCorrdenador)
    if coordenadorGrupoTrabalho != None:
        Atores.Adiciona(coordenadorGrupoTrabalho, "Coordenador do Grupo de Trabalho para aprovação")
```

## Destinatário
```python
if OrdemServico.GetCustom("NOME_RECEBEDOR"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("NOME_RECEBEDOR")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```

## Destinatário do malote
```python
pessoa = Pessoa.Carrega(OrdemServico["PRJ_COLABORADOR_BBTS"])
Atores.Adiciona(pessoa)
```

## Diretor da UOR de Destino Aprova
```python
if OrdemServico.GetCustom("FAVORECIDO_TODOS"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Diretor da UOR de Origem
```python
uor = OrdemServico.GetCustom('UOR_ORIGEM')
DB.ExecuteDataTable('Select PESSOA.NOME, PESSOA.CARGO, ORGAO.DESCRICAO, ORGAO1.DESCRICAO, ORGAO2.DESCRICAO, ORGAO3.DESCRICAO, ORGAO4.DESCRICAO, ORGAO5.DESCRICAO, ORGAO6.DESCRICAO, ORGAO7.DESCRICAO From PESSOA Left Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Left Join ORGAO ORGAO1 On ORGAO1.ID_ORGAO = ORGAO.ID_ORGAO_PAI Left Join ORGAO ORGAO2 On ORGAO2.ID_ORGAO = ORGAO1.ID_ORGAO_PAI Left Join ORGAO ORGAO3 On ORGAO3.ID_ORGAO = ORGAO2.ID_ORGAO_PAI Left Join ORGAO ORGAO4 On ORGAO4.ID_ORGAO = ORGAO3.ID_ORGAO_PAI Left Join ORGAO ORGAO5 On ORGAO5.ID_ORGAO = ORGAO4.ID_ORGAO_PAI Left Join ORGAO ORGAO6 On ORGAO6.ID_ORGAO = ORGAO5.ID_ORGAO_PAI Left Join ORGAO ORGAO7 On ORGAO7.ID_ORGAO = ORGAO6.ID_ORGAO_PAI ')
```

## Diretor da UOR de Origem Aprova / Favorecido Cobra 2
```python
if OrdemServico.GetCustom("FAVORECIDO_COBRA2"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA2")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Diretor de Destino
```python
scrOrgao = OrdemServico.GetCustom("SCR_TODOS_DESTINO").ToString()
lista = Utils.ExecuteDataTable(" SELECT id_orgao FROM orgao where sigla = '"+ scrOrgao +"' ")
for linha in lista.Rows:
    idOrgao = Convert.ToInt32(linha["ID_ORGAO"])
presi = 934
orgao = Orgao.Carrega(idOrgao)
perfil = ""
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (perfil != "Diretoria"):
        orgao = Orgao.Carrega(presi)
        gestor = gestor.Orgao.Gestor
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Atores.Adiciona(gestor, "Diretor de" + OrdemServico.Cliente.ToString())
```

## Diretor de Origem
```python
scrOrgao = OrdemServico.GetCustom("SCR_TODOS_RH").ToString()
lista = Utils.ExecuteDataTable(" SELECT id_orgao FROM orgao where sigla = '"+ scrOrgao +"' ")
for linha in lista.Rows:
    idOrgao = Convert.ToInt32(linha["ID_ORGAO"])
presi = 934
orgao = Orgao.Carrega(idOrgao)
perfil = ""
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        Utils.LogInformation(gestor.ToString(), "gestor")
        countLoop = countLoop + 1
    if (perfil != "Diretoria"):
        orgao = Orgao.Carrega(presi)
        gestor = gestor.Orgao.Gestor
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Atores.Adiciona(gestor, "Diretor de" + OrdemServico.Cliente.ToString())
```

## Diretor do Cliente
```python
gestor = OrdemServico.Cliente.Orgao.Gestor
countLoop = 0;
while (((gestor.Orgao.OrgaoPai.Descricao != "4000001300- PRESIDENCIA.") and (gestor.Orgao.OrgaoPai.Descricao != "4000001100- CONSELHO DE ADMINISTRACAO")) and countLoop < 6):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    countLoop = countLoop + 1
if (countLoop >= 6):
    Utils.LogError("SAIDA DO LOOP - PAPEL DIRETOR", "ERROR")
Atores.Adiciona(gestor, "Diretor de " + OrdemServico.Cliente.ToString())
```

## Diretor do Favorecido
```python
gestor = OrdemServico.Favorecido.Orgao.Gestor
gestorAreaPai = OrdemServico.Favorecido.Orgao.OrgaoPai.Sigla
countLoop = 0;
while (((gestor.Orgao.OrgaoPai.Sigla != "4000001300") and (gestor.Orgao.OrgaoPai.Sigla != "4000001100")) and countLoop < 6):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    countLoop = countLoop + 1
if (countLoop >= 6):
    Utils.LogError("SAIDA DO LOOP - PAPEL DIRETOR", "ERROR")
if gestorAreaPai == "4000001300":
    gestor = Pessoa.Carrega(27818)
Atores.Adiciona(gestor, "Diretor de " + OrdemServico.Cliente.ToString())
```

## Diretor Lista SCR
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join z_00143_lista_scr li on oc.id_ocorrencia = li.id_ocorrencia inner join orgao o on li.scr = o.id_orgao inner join pessoa pe on o.id_gestor = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
    gestor = Pessoa.Carrega(ator["ID_PESSOA"])
    countLoop = 0
    presi = 934
    perfil = ''
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
        if (perfil != "Diretoria"):
            orgao = Orgao.Carrega(presi)
            gestor = gestor.Orgao.Gestor
        if (countLoop >= 6):
            Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        Atores.Adiciona(gestor)
```

## Diretor para aprovação / Diretor Financeiro
```python
orgao = Orgao.Carrega("Id", OrdemServico.GetCustom("DIRETORES"));
if (orgao != None):
	diretor = orgao.Gestor;
	if (diretor != None):
		Atores.Adiciona(diretor , "Diretor Selecionado");
```

## E-mail Destinatários
```python
OrdemServico["EMAIL_CAIXA"]
```

## Especialista
```python
uor=OrdemServico.Servico.ResponsavelTecnico.Orgao.Sigla.ToString()
if (uor == '3000008020' or uor == '3000008023'):
    if (OrdemServico.ClasseSubProcesso.Sigla == 'INCISISTE'):
        Atores.Adiciona(Pessoa.Carrega(26612), "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
    elif (OrdemServico.ClasseSubProcesso.Sigla == 'DEMANDA'):
        Atores.Adiciona(Pessoa.Carrega(26613), "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
    elif (OrdemServico.ClasseSubProcesso.Sigla == 'MANUTAPOIO'):
        Atores.Adiciona(Pessoa.Carrega(26614), "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
    else:
        Atores.Adiciona(OrdemServico.Servico.ResponsavelTecnico, "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
else:
    Atores.Adiciona(OrdemServico.Servico.ResponsavelTecnico, "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
```

## Executivo LISTA_INTER
```python
tabela = Utils.ExecuteDataTable(" SELECT o.id_orgao_pai FROM OCORRENCIA OC INNER JOIN Z_00143_LISTA_INTER li ON oc.id_ocorrencia = li.id_ocorrencia INNER JOIN orgao o ON li.SCR_INTER = o.descricao INNER JOIN pessoa pe ON o.id_gestor  = pe.id_pessoa WHERE oc.numero = '"+ OrdemServico.Numero.ToString() +"'")
for ator in tabela.Rows:
	scr = Orgao.Carrega(ator["ID_ORGAO_PAI"])
	pessoa = scr.Gestor
	Atores.Adiciona(pessoa)
```

## Executivo NN_LISTA_SCR
```python
tabela = Utils.ExecuteDataTable(" SELECT o.id_orgao FROM OCORRENCIA OC inner join z_00143_nn_lista_scr li on oc.id_ocorrencia = li.id_ocorrencia inner join orgao o on li.scr = o.descricao inner join pessoa pe on o.id_gestor = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for scr in tabela.Rows:
    orgao = Orgao.Carrega(scr["ID_ORGAO"])
    if orgao != None:
        gestor = orgao.Gestor
        countLoop = 0;
        while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao == "Gerência Executiva")) and countLoop < 6):
            gestor = gestor.Orgao.OrgaoPai.Gestor
            countLoop = countLoop + 1
        if (countLoop >= 6):
            Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        Atores.Adiciona(gestor)
```

## Executivo Posição NN_LISTA_SCR
```python
tabela = Utils.ExecuteDataTable(" SELECT o.id_orgao FROM OCORRENCIA OC inner join z_00143_nn_lista_scr li on oc.id_ocorrencia = li.id_ocorrencia inner join orgao o on li.scr = o.descricao inner join pessoa pe on o.id_gestor = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
if tabela.Rows.Count == 0 :
    Atores.Adiciona(Pessoa.Carrega(OrdemServico.ResponsavelId), "Aprovação do responsável pelo chamado")
else:
    for scr in tabela.Rows:
        orgao = Orgao.Carrega(scr["ID_ORGAO"])
        if orgao != None:
            idScr=Convert.ToInt32(scr["ID_ORGAO"])
            contapessoascr= DB.ExecuteScalar("select count(cpp.ID_PESSOA) as QTD from GRUPO_TRABALHO gt inner join tecnico te on te.id_grupo_trabalho = gt.id_grupo_trabalho inner join pessoa pe on pe.id_pessoa = te.id_pessoa inner join cp_pessoa cpp on cpp.id_pessoa = te.id_pessoa inner join orgao org on org.id_orgao = pe.id_orgao where te.ativo = 'Sim' and pe.ativo = 'Sim' and org.ID_ORGAO='"+idScr.ToString()+"'")
            listapessoascr = DB.ExecuteDataTable("select cpp.ID_PESSOA, cpp.CARGO_FUNCIONAL, cpp.GESTOR_POSICAO from GRUPO_TRABALHO gt inner join tecnico te on te.id_grupo_trabalho = gt.id_grupo_trabalho inner join pessoa pe on pe.id_pessoa = te.id_pessoa inner join cp_pessoa cpp on cpp.id_pessoa = te.id_pessoa inner join orgao org on org.id_orgao = pe.id_orgao where te.ativo = 'Sim' and pe.ativo = 'Sim' and org.ID_ORGAO='"+idScr.ToString()+"'")
            if contapessoascr >= 1:
                edivisao=0
                for pessoascr in listapessoascr.Rows:
                    cargofuncao = pessoascr["CARGO_FUNCIONAL"].ToString()
                    idpessoa=pessoascr["ID_PESSOA"].ToString()
                    if cargofuncao == 'GERENTE EXECUTIVO':
                        edivisao=1
                        Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idpessoa)))
                if edivisao==0 :
                    cargofuncao = pessoascr["CARGO_FUNCIONAL"].ToString()
                    idpessoa=pessoascr["ID_PESSOA"].ToString()
                    matriculagestor=pessoascr["GESTOR_POSICAO"].ToString()
                    cargogestor=''
                    i=0
                    while cargogestor.ToString() != "DIRETOR" or cargogestor.ToString() != "PRESIDENTE":
                        if matriculagestor.ToString() == '' or i > 5:
                            break
                        i = i + 1
                        cargogestor = DB.ExecuteScalar("select CARGO_FUNCIONAL FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor+"'")
                        if cargogestor.ToString() == "DIRETOR" or cargogestor.ToString() == "PRESIDENTE":
                            Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idpessoa)))
                        else:
                            idpessoa=DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor.ToString()+"'")
                            matriculagestor=DB.ExecuteScalar("select GESTOR_POSICAO FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor.ToString()+"'")
            else:
                gestor = orgao.Gestor
                countLoop = 0;
                while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao == "Gerência Executiva")) and countLoop < 6):
                    gestor = gestor.Orgao.OrgaoPai.Gestor
                    countLoop = countLoop + 1
                if (countLoop >= 6):
                    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
                Atores.Adiciona(gestor)
```

## Favorecido
```python
Atores.Adiciona(OrdemServico.Favorecido)
```

## Favorecido Alimentação
```python
favorecidoAlimentacao = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_ALIMENTACAO")))
if favorecidoAlimentacao != None:
	Atores.Adiciona(favorecidoAlimentacao, "Favorecido")
```

## Favorecido All
```python
if OrdemServico.GetCustom("FAVORECIDO_ALL"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_ALL")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido BBTS / Gerente Executivo da Geemp
```python
if OrdemServico.GetCustom("FAVORECIDO_BBTS"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_BBTS")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Cobra / Favorecido Cobra 1 / Favorecido Cobra 3
```python
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Cobra e Favorecido Cobra1
```python
if OrdemServico.GetCustom("FAVORECIDO_COBRA") and OrdemServico.GetCustom("FAVORECIDO_COBRA1"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
    favorecidoCobra1 = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA1")))
    if favorecidoCobra and favorecidoCobra1 != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
        Atores.Adiciona(favorecidoCobra1, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Cobra e Gerente
```python
if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
gestorMatricula = str(OrdemServico.GetCustom('MATRICULA'))
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + gestorMatricula + "'")
idAnalista = 0
for row in lista.Rows:
    idAnalista = row['ID_PESSOA']
try:
    if OrdemServico.GetCustom("FAVORECIDO_COBRA"):
        idFavorecido = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA"))
    else:
        idFavorecido = OrdemServico.Cliente.Id
    gerenteGrupo = DB.ExecuteDataTable("Select ORGAO.ID_GESTOR From PESSOA Inner Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Where PESSOA.ID_PESSOA = '" + str(idFavorecido) + "'")
    for linha in gerenteGrupo.Rows:
        if linha["ID_GESTOR"] is not None and linha["ID_GESTOR"] is not DBNull.Value:
            idGerenteGrupo = Convert.ToInt32(linha["ID_GESTOR"])
            if idGerenteGrupo != idFavorecido:
                Atores.Adiciona(Pessoa.Carrega(idGerenteGrupo), "Gerente de grupo")
except:
    pass
```

## FAVORECIDO COBRA1 / Ger. Executivo da UOR de Origem
```python
if OrdemServico.GetCustom("FAVORECIDO_COBRA1"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA1")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Cobra5
```python
if OrdemServico.GetCustom("FAVORECIDO_COBRA5"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA5")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Cultura
```python
favorecidoCultura = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_CULTURA")))
if favorecidoCultura != None:
	Atores.Adiciona(favorecidoCultura, "Favorecido")
```

## Favorecido Custom
```python
idFavorecidoCustom = OrdemServico.GetCustom("FAVORECIDO_CUSTOM")
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
	Atores.Adiciona(favorecidoCustom, "Favorecido")
```

## Favorecido Deslocamento
```python
if OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido DITEC
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DITEC")))
if favorecido != None:
    Atores.Adiciona(favorecido, "Favorecido")
```

## Favorecido do Gestor Contrato
```python
if OrdemServico.GetCustom("CSC_FAVORECIDO"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("CSC_FAVORECIDO")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Funcio
```python
favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_FUNCIO")))
if favorecidoCobra != None:
    Atores.Adiciona(favorecidoCobra, "Favorecido")
```

## Favorecido Gestor
```python
import clr
clr.AddReference("Supravizio.Custom")
if OrdemServico.GetCustom("MATRICULA_GESTOR"):
    result_table = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA From CP_PESSOA Where CP_PESSOA.MATRICULA = '"+str(Convert.ToInt32(OrdemServico.GetCustom("MATRICULA_GESTOR")))+"'")
    OrdemServico.AdicionaComentario(str(result_table.Rows), True)
    for row in result_table.Rows:
        favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(row["ID_PESSOA"]))
        if favorecidoCobra != None:
            Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Gratificado
```python
favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_GRATIF")))
if favorecidoCobra != None:
    Atores.Adiciona(favorecidoCobra, "Favorecido")
```

## Favorecido Nome
```python
if OrdemServico.GetCustom("FAVORECIDO_NOME"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_NOME")))
    idFav = 0
    lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, PESSOA.NOME From PESSOA Where PESSOA.NOME = '" + favorecidoCobra + "'")
    for linha in lista.Rows:
        idFav = linha["ID_PESSOA"]
    if favorecidoCobra != None:
        Atores.Adiciona(idFav, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Time Dev Gesap
```python
if OrdemServico.GetCustom("<NOME>"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("<NOME>")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Favorecido Todos
```python
if OrdemServico.GetCustom("FAVORECIDO_TODOS"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```

## Favorecido Todos 2
```python
if OrdemServico.GetCustom("FAVORECIDO_TODOS_2"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS_2")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Aprovador")
```

## Favorecido Todos Papel
```python
if OrdemServico("FAVORECIDO_TODOS"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico("FAVORECIDO_TODOS")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```

## Favorecido Verba
```python
fav = OrdemServico.GetCustom("FAVORECIDO_COBRA")
if fav != None and fav != "":
    p = Pessoa.Carrega(Convert.ToInt32(fav))
    if p != None:
        Atores.Adiciona(p, "Favorecido da verba")
```

## Fila CSC - Benefícios
```python
pessoa = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
atores = OrdemServico.ObtemAtoresProcesso('Fila CSC - Benefícios')
for ator in atores:
    if ator != pessoa:
        Atores.Adiciona(ator)
```

## Fiscais de Encerramento 01
```python
fiscalAdm = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_ADM_DO_CONTRATO")))
Atores.Adiciona(fiscalAdm)
GestorContr = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("GESTOR_DO_CONTRATO")))
Atores.Adiciona(GestorContr)
```

## Fiscais do Contrato
```python
pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_SERVICO, FISCAL_SUPLENTE FROM Z_00143_FISCAL_SER WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa01.Rows:
    fiscalServico = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SERVICO"]))
    fiscalSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SUPLENTE"]))
    Atores.Adiciona(fiscalServico)
    Atores.Adiciona(fiscalSuplente)
pesquisa02 = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_ADM, FISCAL_ADM_SUPLENTE FROM Z_00143_FISCAL_ADMINISTRATIVO WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa02.Rows:
    fiscalAdm = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_ADM"]))
    fiscalAdmSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_ADM_SUPLENTE"]))
    Atores.Adiciona(fiscalAdm)
    Atores.Adiciona(fiscalAdmSuplente)
pesquisa03 = DB.ExecuteDataTable("select ID_OCORRENCIA, GESTOR_CONTRATO, GESTOR_CONTRATO_SUPLENTE FROM Z_00143_GESTOR_CONTRATO WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa03.Rows:
    gestorContrato = Pessoa.Carrega(Convert.ToInt32(pessoa["GESTOR_CONTRATO"]))
    gestorContratoSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["GESTOR_CONTRATO_SUPLENTE"]))
    Atores.Adiciona(gestorContrato)
    Atores.Adiciona(gestorContratoSuplente)
pesquisa04 = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_MASTER, FISCAL_MASTER_SUPLENTE FROM Z_00143_FISCAL_MASTER WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa04.Rows:
    fiscalMaster = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_MASTER"]))
    fiscalMasterSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_MASTER_SUPLENTE"]))
    Atores.Adiciona(fiscalMaster)
    Atores.Adiciona(fiscalMasterSuplente)
```

## Fiscais e gestores do contrato
```python
pesquisaFiscalDeServico = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_DE_SERVICO FROM CPE_CSC WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisaFiscalDeServico.Rows:
    if pessoa["FISCAL_DE_SERVICO"] != DBNull.Value:
        fiscalServico = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_DE_SERVICO"]))
        Atores.Adiciona(fiscalServico)
pesquisaGestorDoContrato = DB.ExecuteDataTable("select ID_OCORRENCIA, GESTOR_DO_CONTRATO FROM CPE_CSC WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisaGestorDoContrato.Rows:
        gestor = Pessoa.Carrega(Convert.ToInt32(pessoa["GESTOR_DO_CONTRATO"]))
        Atores.Adiciona(gestor)
pesquisaFiscalAdministrativo = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_ADM_DO_CONTRATO FROM CPE_CSC WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisaFiscalAdministrativo.Rows:
    if pessoa["FISCAL_ADM_DO_CONTRATO"] != DBNull.Value:
        fiscalAdministrativo = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_ADM_DO_CONTRATO"]))
        Atores.Adiciona(fiscalAdministrativo)
```

## Fiscais encerramento
```python
fiscalAdm = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_ADM_DO_CONTRATO")))
Atores.Adiciona(fiscalAdm)
fiscalServ = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_DE_SERVICO")))
Atores.Adiciona(fiscalServ)
GestorContr = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("GESTOR_DO_CONTRATO")))
Atores.Adiciona(GestorContr)
```

## Fiscal Administrativo
```python
pesquisa02 = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_ADM, FISCAL_ADM_SUPLENTE FROM Z_00143_FISCAL_ADMINISTRATIVO WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa02.Rows:
    fiscalAdm = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_ADM"]))
    fiscalAdmSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_ADM_SUPLENTE"]))
    Atores.Adiciona(fiscalAdm)
    Atores.Adiciona(fiscalAdmSuplente)
```

## Fiscal Administrativo de Contratos
```python
fiscalAdministrativo = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_ADM_DO_CONTRATO")))
if fiscalAdministrativo != None:
    Atores.Adiciona(fiscalAdministrativo, "Fiscal Administrativo")
```

## Fiscal Administrativo Papel
```python
fiscalAdministrativo = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_ADM_SGPS")))
if fiscalAdministrativo != None:
    Atores.Adiciona(fiscalAdministrativo, "Fiscal Administrativo")
```

## Fiscal Avaliador
```python
import clr
clr.AddReference("Supravizio.Custom")
if OrdemServico.GetCustom("CSC_MATRICULA"):
    result_table = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA From CP_PESSOA Where CP_PESSOA.MATRICULA = '"+str(Convert.ToInt32(OrdemServico.GetCustom("CSC_MATRICULA")))+"'")
    OrdemServico.AdicionaComentario(str(result_table.Rows), True)
    for row in result_table.Rows:
        favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(row["ID_PESSOA"]))
        if favorecidoCobra != None:
            Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Fiscal de Serviço / Gestor de Contrato
```python
idPessoa = OrdemServico["FAVORECIDO_TODOS"]
if idPessoa!= None:
    p = Pessoa.Carrega("Id",idPessoa )
    Atores.Adiciona(p);
```

## Fiscal de Serviço de Contratos
```python
fiscalServ = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_DE_SERVICO")))
Atores.Adiciona(fiscalServ)
```

## Fiscal de Serviço Papel
```python
fiscalServico = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_SERVI_SGPS")))
if fiscalServico != None:
    Atores.Adiciona(fiscalServico, "Fiscal de Serviço")
```

## Fiscal do Serviço
```python
if OrdemServico.SubProcesso.ClasseSubProcesso.Sigla =='AVALFORNECEDOR':
    if OrdemServico.GetCustom("COMBOBOX") != 'Fiscalização Administrativa':
        sql_fs="select to_char(cpp.id_pessoa) as FISCAL_SERVICO, f.nome as NOME from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular or f.id = d.id_suplente LEFT OUTER join pessoa cpp on upper(cpp.usuario_rede) = replace(replace(replace(f.email, 'MODIF_',''),'@BBTS.COM.BR',''),'@BBTECNO.COM.BR','') where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+OrdemServico.GetCustom('CSC_DGCO').ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_SERVICO'"
    else:
        sql_fs="select to_char(cpp.id_pessoa) as FISCAL_SERVICO, f.nome as NOME from bbts_gescon_designacao d inner join bbts_gescon_contrato c on c.id = d.ID_CONTRATO LEFT OUTER join bbts_gescon_funcionario f on f.id = d.id_titular or f.id = d.id_suplente LEFT OUTER join pessoa cpp on upper(cpp.usuario_rede) = replace(replace(replace(f.email, 'MODIF_',''),'@BBTS.COM.BR',''),'@BBTECNO.COM.BR','') where d.status = 'VIGENTE' and replace(replace(replace(c.dgco,'.',''),'/',''),'-','') = replace(replace(replace('"+OrdemServico.GetCustom('CSC_DGCO').ToString()+"','.',''),'/',''),'-','') and d.tipo_designacao = 'FISCALIZACAO_ADMINISTRATIVA'"
    pesquisa01 = DB.ExecuteDataTable(sql_fs)
    for pessoa in pesquisa01.Rows:
        fiscalServico = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SERVICO"]))
        Atores.Adiciona(fiscalServico)
else:
    pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_SERVICO, FISCAL_SUPLENTE FROM Z_00143_FISCAL_SER WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
    for pessoa in pesquisa01.Rows:
        fiscalServico = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SERVICO"]))
        fiscalSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_SUPLENTE"]))
        Atores.Adiciona(fiscalServico)
        Atores.Adiciona(fiscalSuplente)
```

## Fiscal do Serviço Master
```python
pesquisa04 = DB.ExecuteDataTable("select ID_OCORRENCIA, FISCAL_MASTER, FISCAL_MASTER_SUPLENTE FROM Z_00143_FISCAL_MASTER WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa04.Rows:
    fiscalMaster = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_MASTER"]))
    fiscalMasterSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["FISCAL_MASTER_SUPLENTE"]))
    Atores.Adiciona(fiscalMaster)
    Atores.Adiciona(fiscalMasterSuplente)
```

## Ger. Executivo da UOR de Destino
```python
if OrdemServico.GetCustom("FAVORECIDO_COBRA3"):
    favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA3")))
    if favorecidoCobra != None:
        Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Gerende de Divisão GERIC
```python
gestor = OrdemServico.Responsavel.Orgao.Gestor
Atores.Adiciona(gestor, "Gerente de Divisão" + OrdemServico.Responsavel.ToString())
```

## Gerente - PPGEREX_NEGOCIO
```python
ator = DB.ExecuteScalar("SELECT CPO.PPGEREX_NEGOCIO FROM CP_ORDEM_SERVICO CPO WHERE CPO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"' ")
if ator != DBNull.Value:
    if ator != None and ator != '' :
        gerente = Convert.ToInt32(ator)
        Atores.Adiciona(Pessoa.Carrega("Id", gerente))
else:
    Atores.Adiciona(Pessoa.Carrega("Id", 3))
```

## Gerente da Pessoa
```python
if OrdemServico.Servico.Sigla.ToString() == 'LIBERACAORI' or OrdemServico.Servico.Sigla.ToString() == 'REVERSAORI':
    favorecido=Pessoa.Carrega(Convert.ToInt32(OrdemServico["CSC_FAVORECIDO"]))
    gestor = favorecido.ObtemChefia(False)
else:
    gestor = OrdemServico.Cliente.ObtemChefia(False)
if (gestor == OrdemServico.Cliente):
    gestor = OrdemServico.Cliente.Orgao.OrgaoPai.Gestor
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = OrdemServico.Cliente
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())
```

## Gerente DAPN
```python
tabela = Utils.ExecuteDataTable("Select Distinct ID_PESSOA, PESSOA.NOME, ORGAO.DESCRICAO From PESSOA Inner Join ORGAO On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Where PESSOA.CARGO Like '%GER%' And ORGAO.DESCRICAO Like '%7002%' And PESSOA.ATIVO Like 'Sim')")
for dr in tabela.Rows:
	pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
	Atores.Adiciona(pessoa)
gestores = Orgao.ObtemTodosGestores()
for gestor in gestores:
    if gestor.Ativo:
        Atores.Adiciona(gestor)
```

## Gerente de Centro do favorecido
```python
subordinado = OrdemServico.GetCustom("FAVORECIDO_COBRA")
gestor = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL As CargoPessoa, PESSOA1.NOME As NomeGestor, CP_PESSOA1.CARGO_FUNCIONAL As CargoGestor, PESSOA2.NOME As NomeGestorDoGestor, CP_PESSOA2.CARGO_FUNCIONAL As CargoGestorDoGestor, SUBORDINADO.NOME As NomeSubordinado, CP_SUBORDINADO.CARGO_FUNCIONAL As CargoSubordinado, PESSOA1.ID_PESSOA From PESSOA Left Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Left Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Left Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = ORGAO.ID_GESTOR Left Join CP_PESSOA CP_PESSOA1 On CP_PESSOA1.ID_PESSOA = PESSOA1.ID_PESSOA Left Join ORGAO ORGAO1 On ORGAO1.ID_ORGAO = PESSOA1.ID_ORGAO Left Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = ORGAO1.ID_GESTOR Left Join CP_PESSOA CP_PESSOA2 On CP_PESSOA2.ID_PESSOA = PESSOA2.ID_PESSOA Left Join ORGAO ORGAO2 On ORGAO2.ID_GESTOR = PESSOA.ID_PESSOA Left Join PESSOA SUBORDINADO On SUBORDINADO.ID_ORGAO = ORGAO2.ID_ORGAO Left Join CP_PESSOA CP_SUBORDINADO On CP_SUBORDINADO.ID_PESSOA = SUBORDINADO.ID_PESSOA Where SUBORDINADO.ID_PESSOA = '"+OrdemServico['FAVORECIDO_COBRA'].ToString()+"'")
if gestor.Rows.Count != 0 or gestor.Rows.Count != None:
    for i in gestor.Rows:
        id_gestor = Convert.ToInt32(i['ID_PESSOA'])
        gtor = Pessoa.Carrega(id_gestor)
        Atores.Adiciona(gtor)
```

## Gerente de centro do favorecido todos
```python
subordinado = OrdemServico.GetCustom("FAVORECIDO_TODOS")
gestor = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL As CargoPessoa, PESSOA1.NOME As NomeGestor, CP_PESSOA1.CARGO_FUNCIONAL As CargoGestor, PESSOA2.NOME As NomeGestorDoGestor, CP_PESSOA2.CARGO_FUNCIONAL As CargoGestorDoGestor, SUBORDINADO.NOME As NomeSubordinado, CP_SUBORDINADO.CARGO_FUNCIONAL As CargoSubordinado, PESSOA1.ID_PESSOA From PESSOA Left Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Left Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Left Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = ORGAO.ID_GESTOR Left Join CP_PESSOA CP_PESSOA1 On CP_PESSOA1.ID_PESSOA = PESSOA1.ID_PESSOA Left Join ORGAO ORGAO1 On ORGAO1.ID_ORGAO = PESSOA1.ID_ORGAO Left Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = ORGAO1.ID_GESTOR Left Join CP_PESSOA CP_PESSOA2 On CP_PESSOA2.ID_PESSOA = PESSOA2.ID_PESSOA Left Join ORGAO ORGAO2 On ORGAO2.ID_GESTOR = PESSOA.ID_PESSOA Left Join PESSOA SUBORDINADO On SUBORDINADO.ID_ORGAO = ORGAO2.ID_ORGAO Left Join CP_PESSOA CP_SUBORDINADO On CP_SUBORDINADO.ID_PESSOA = SUBORDINADO.ID_PESSOA Where SUBORDINADO.ID_PESSOA = '"+OrdemServico['FAVORECIDO_TODOS'].ToString()+"'")
if gestor.Rows.Count != 0 or gestor.Rows.Count != None:
    for i in gestor.Rows:
        id_gestor = Convert.ToInt32(i['ID_PESSOA'])
        gtor = Pessoa.Carrega(id_gestor)
        Atores.Adiciona(gtor)
```

## Gerente de Divisão Confecção de Materiais
```python
idGestorDisei=DB.ExecuteScalar("select DISTINCT O.ID_GESTOR from ORGAO O WHERE O.SIGLA LIKE '%3000003160%' AND O.ATIVO = 'Sim'")
idGestorDiapa=DB.ExecuteScalar("select DISTINCT O.ID_GESTOR from ORGAO O WHERE O.SIGLA LIKE '%3000003150%' AND O.ATIVO = 'Sim'")
if OrdemServico.ContaExecucaoAtividade("APROV_GESTOR") < 2:
    Atores.Adiciona(Pessoa.Carrega(idGestorDisei))
else:
    Atores.Adiciona(Pessoa.Carrega(idGestorDiapa))
```

## Gerente de Divisão da UOR
```python
gestor = OrdemServico.Cliente.Orgao.Gestor
Uor_Solicitante = ""
usuario = OrdemServico.UsuarioAutenticadoId
uor = DB.ExecuteDataTable("Select ORGAO.DESCRICAO From ORGAO Inner Join PESSOA On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Where PESSOA.ID_PESSOA = '" + usuario.ToString() + "'")
for i in uor.Rows:
    Uor_Solicitante = i['DESCRICAO']
query = DB.ExecuteScalar("SELECT ORGAO.ID_GESTOR from ORGAO WHERE ORGAO.DESCRICAO = '" + Uor_Solicitante.ToString() + "'")
gestor = Pessoa.Carrega(Convert.ToInt32(query))
OrdemServico.AdicionaComentario(gestor.ToString(), True)
Atores.Adiciona(gestor, "Gerente de Divisão" + OrdemServico.Cliente.ToString())
```

## Gerente de Divisão de Cliente
```python
gestor = OrdemServico.Cliente.Orgao.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Gerência Executiva") and countLoop < 6):
    if gestor['CARGO_FUNCIONAL'].ToString() == "COORDENADOR" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE DIVISAO" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE REGIONAL DE OPERACOES" or gestor['CARGO_FUNCIONAL'].ToString() == "SUPERINTENDENTE" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE PROJETOS I" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE PROJETOS II" :
        gestor = gestor
        break
    else:
        gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente de Divisão" + OrdemServico.Cliente.ToString())
```

## Gerente de Divisão DICOC
```python
gestor = OrdemServico.Cliente.Orgao.Gestor
Atores.Adiciona(gestor, "Gerente de Divisão" + OrdemServico.Cliente.ToString())
```

## Gerente de Divisão do Contrato
```python
idScr = Convert.ToInt32(OrdemServico["NN_SCR_GERENCIAS"])
scr = Orgao.Carrega(idScr)
gestor = scr.Gestor
countLoop = 0;
Atores.Adiciona(gestor, "Gerente de Divisão do SCR " + scr.ToString())
```

## Gerente de Divisão do Favorecido Cobra
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
gestor = favorecidoBBTec.ObtemChefia(False)
if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente de Divisão do Favorecido Cobra 2
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
gestor = favorecidoBBTec.ObtemChefia(False)
if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Gerência Executiva") and countLoop < 6):
    if gestor['CARGO_FUNCIONAL'].ToString() == "COORDENADOR" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE DIVISAO" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE REGIONAL DE OPERACOES" or gestor['CARGO_FUNCIONAL'].ToString() == "SUPERINTENDENTE":
        gestor = gestor
        break
    else:
        gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente de Divisão" + OrdemServico.Cliente.ToString())
```

## Gerente de Divisão do Favorecido Telefonia
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("SCR_TODOS_DESTINO"))
scr = Orgao.Carrega(idScr)
gestor = scr.Gestor
countLoop = 0;
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Gerência Executiva") and countLoop < 6):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    Utils.LogInformation("acessou", "Papel aprovação")
    countLoop = countLoop + 1
if (countLoop >= 6):
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE DE DIVISÃO", "ERROR")
Atores.Adiciona(gestor, "Gerente de Divisão do SCR " + scr.ToString())
```

## Gerente de Divisão Favorecido Cobra 3 / Gerente Favorecido Todos 2
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_TODOS"]))
gestor = favorecidoBBTec.ObtemChefia(False)
if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Gerência Executiva") and countLoop < 6):
    if gestor['CARGO_FUNCIONAL'].ToString() == "COORDENADOR" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE DE DIVISAO" or gestor['CARGO_FUNCIONAL'].ToString() == "GERENTE REGIONAL DE OPERACOES" or gestor['CARGO_FUNCIONAL'].ToString() == "SUPERINTENDENTE":
        gestor = gestor
        break
    else:
        gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente de Divisão" + OrdemServico.Cliente.ToString())
```

## Gerente de Divisão Posição do Cliente
```python
cliente = Pessoa.Carrega(Convert.ToInt32(OrdemServico.Cliente.Id))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+cliente["GESTOR_POSICAO"].ToString()+"'")))
aprovador = gestor
i = 0
while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO" and aprovador["CARGO_FUNCIONAL"] != "SUPERINTENDENTE" and aprovador["CARGO_FUNCIONAL"] != "GERENTE DE DIVISAO":
    if i > 5:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE DE DIVISAO", "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(aprovador, "Gerente de" + OrdemServico.Cliente.ToString())
```

## Gerente de Posição Cliente
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
matriculaGestor = favorecido["GESTOR_POSICAO"]
if matriculaGestor != None and matriculaGestor.ToString() != "":
    idGestor = DB.ExecuteScalar("SELECT P.ID_PESSOA FROM CP_PESSOA CP INNER JOIN PESSOA P ON P.ID_PESSOA = CP.ID_PESSOA WHERE P.ATIVO = 'Sim' AND LTRIM(CP.MATRICULA, '0') = LTRIM(SUBSTR('" + matriculaGestor.ToString().Replace("'", "''") + "', 1, 6), '0')")
    if idGestor != None and idGestor != DBNull.Value:
        Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idGestor)))
```

## Gerente de Projetos Sistemas
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))
Atores.Adiciona(favorecidoBBTec, "Gerente do Favorecido")
```

## Gerente Divisão Favorecido Cobra
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"])
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
    nomeFavorecido = favorecidoCustom.Nome
    orgaoFavorecido = favorecidoCustom.OrgaoId
else:
    nomeFavorecido = OrdemServico.Favorecido.Nome
    orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
scr = Orgao.Carrega(orgaoFavorecido)
gestor = scr.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Gerência Executiva"  and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Gerência Rede") and countLoop < 6):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    Utils.LogInformation("acessou", "Papel aprovação")
    countLoop = countLoop + 1
if (countLoop >= 6):
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE DE DIVISÃO", "ERROR")
Atores.Adiciona(gestor, "Gerente de Divisão do SCR " + scr.ToString())
```

## Gerente Divisão para reprogramação
```python
orgao = Orgao.Carrega("Sigla", OrdemServico.GetCustom("GER_DIV_RESPONSA"));
if (orgao != None):
    gestor = orgao.Gestor;
    if (gestor != None):
        Atores.Adiciona(gestor, "Gestor Selecionado");
```

## Gerente divisão SCR_TODOS_RH
```python
idSrc = DB.ExecuteScalar("select id_orgao from orgao where sigla = '"+ OrdemServico["SCR_TODOS_RH"].ToString() +"' ")
orgao = Orgao.Carrega(Convert.ToInt32(idSrc))
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao == "Gerência Divisão"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE DIVISÃO", "ERROR")
    Atores.Adiciona(gestor, "Gerente Divisão")
```

## Gerente do Cliente / Gestor do Cliente
```python
if OrdemServico.Cliente.Orgao.GestorId.ToString() == OrdemServico.ClienteId.ToString():
    Atores.Add(OrdemServico.Cliente.Orgao.OrgaoPai.Gestor)
else:
    Atores.Add(OrdemServico.Cliente.ObtemChefia(False))
```

## Gerente do Cliente - DCOM
```python
gestor = OrdemServico.Cliente.ObtemChefia(False)
if (gestor == OrdemServico.Cliente):
	gestor = OrdemServico.Cliente.Orgao.OrgaoPai.Gestor
if (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>)  or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>) or (gestor.Id == <id>):
	gestor = Pessoa.Carrega(5490)
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())
```

## Gerente do Favorecido
```python
gestor = OrdemServico.Favorecido.ObtemChefia(True)
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = Pessoa.Carrega(4751)
if (DateTime.Now >= gestor.DataInicioSubstituicao and DateTime.Now <= gestor.DataFimSubstituicao):
    substituto = Pessoa.Carrega(gestor.SubstitutoAprovacaoId)
    if substituto.Nome == OrdemServico.Favorecido.Nome:
        substituto = substituto.ObtemChefia(True)
        Atores.Adiciona(substituto, "Superior imediato de " + OrdemServico.Favorecido.ToString())
    else:
        Atores.Adiciona(substituto, "Substituto do(a) " + gestor.Nome)
else:
    if gestor.Nome == OrdemServico.Favorecido.Nome:
        gestor = gestor.ObtemChefia(True)
        Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Favorecido.ToString())
    else:
        Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Favorecido.ToString())
```

## Gerente do favorecido todos
```python
subordinado = OrdemServico.GetCustom("FAVORECIDO_TODOS")
gestor = DB.ExecuteDataTable("Select PESSOA.NOME As NomePessoa, CP_PESSOA.CARGO_FUNCIONAL As CargoPessoa, PESSOA1.NOME As NomeGestor, CP_PESSOA1.CARGO_FUNCIONAL As CargoGestor, PESSOA2.NOME As NomeGestorDoGestor, CP_PESSOA2.CARGO_FUNCIONAL As CargoGestorDoGestor, SUBORDINADO.NOME As NomeSubordinado, CP_SUBORDINADO.CARGO_FUNCIONAL As CargoSubordinado, PESSOA1.ID_PESSOA From PESSOA Left Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Left Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Left Join PESSOA PESSOA1 On PESSOA1.ID_PESSOA = ORGAO.ID_GESTOR Left Join CP_PESSOA CP_PESSOA1 On CP_PESSOA1.ID_PESSOA = PESSOA1.ID_PESSOA Left Join ORGAO ORGAO1 On ORGAO1.ID_ORGAO = PESSOA1.ID_ORGAO Left Join PESSOA PESSOA2 On PESSOA2.ID_PESSOA = ORGAO1.ID_GESTOR Left Join CP_PESSOA CP_PESSOA2 On CP_PESSOA2.ID_PESSOA = PESSOA2.ID_PESSOA Left Join ORGAO ORGAO2 On ORGAO2.ID_GESTOR = PESSOA.ID_PESSOA Left Join PESSOA SUBORDINADO On SUBORDINADO.ID_ORGAO = ORGAO2.ID_ORGAO Left Join CP_PESSOA CP_SUBORDINADO On CP_SUBORDINADO.ID_PESSOA = SUBORDINADO.ID_PESSOA Where SUBORDINADO.ID_PESSOA = '"+OrdemServico['FAVORECIDO_COBRA'].ToString()+"'")
if gestor.Rows.Count != 0 or gestor.Rows.Count != None:
    for i in gestor.Rows:
        id_gestor = Convert.ToInt32(i['ID_PESSOA'])
        gtor = Pessoa.Carrega(id_gestor)
        Atores.Adiciona(gtor)
```

## Gerente do Novo Usuário
```python
idOrgao = OrdemServico.GetCustom("SCR_ORIGEM")
if idOrgao != None:
  orgao = Orgao.Load(Convert.ToInt32(idOrgao))
  Atores.Adiciona(orgao.Gestor, "Gestor da área do novo usuário")
```

## Gerente do Projeto
```python
Atores.Adiciona(OrdemServico.Responsavel, "Responsável pela Ordem de Serviço")
```

## Gerente do SCR
```python
idScr = OrdemServico.GetCustom("SCR_ORIGEM")
scr = Orgao.Carrega(idScr)
if (scr != None):
	pessoa = scr.Gestor
	if (pessoa != None):
		Atores.Adiciona(pessoa)
```

## Gerente do SCR Demandante Comunicação
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("SCR_MOVI"))
scr = Orgao.Carrega(idScr)
if (scr != None):
	pessoa = scr.Gestor
	if (pessoa != None):
		Atores.Adiciona(pessoa)
```

## Gerente do SCR Movimentação
```python
idScr = OrdemServico.GetCustom("SCR_MOVI")
scr = Orgao.Carrega(idScr)
if (scr != None):
	pessoa = scr.Gestor
	if (pessoa != None):
		Atores.Adiciona(pessoa)
```

## Gerente Executivo - ACD
```python
orgao = Orgao.Carrega("Id",OrdemServico.GetCustom("GEREX"));
if (orgao != None):
    gestor = orgao.Gestor;
    if (gestor != None):
        Atores.Adiciona(gestor, "Gestor Executivo");
```

## Gerente Executivo - GEREX
```python
ator = DB.ExecuteScalar("SELECT CPO.PPGEREX_NEGOCIO FROM CP_ORDEM_SERVICO CPO WHERE CPO.ID_OCORRENCIA = '"+OrdemServico.Id.ToString()+"' ")
if ator != None:
    gerente = Convert.ToInt32(ator)
    Atores.Adiciona(Pessoa.Carrega("Id", gerente))
```

## Gerente Executivo de Origem
```python
scrOrgao = OrdemServico.GetCustom("SCR_TODOS_RH").ToString()
lista = Utils.ExecuteDataTable(" SELECT id_orgao FROM orgao where sigla = '"+ scrOrgao +"' ")
for linha in lista.Rows:
    idOrgao = Convert.ToInt32(linha["ID_ORGAO"])
orgao = Orgao.Carrega(idOrgao)
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência") and (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Atores.Adiciona(gestor, "Diretor de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo de Posição do Cliente
```python
cliente = Pessoa.Carrega(Convert.ToInt32(OrdemServico.Cliente.Id))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+cliente["GESTOR_POSICAO"].ToString()+"'")))
aprovador = gestor
i = 0
while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO":
    if i > 5:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(aprovador, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo de Posição do Favorecido
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.Favorecido.Id))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = gestor
i = 0
while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO" and aprovador["CARGO_FUNCIONAL"] != "DIRETOR" :
    if i > 5:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
if favorecido["CARGO_FUNCIONAL"] == "GERENTE EXECUTIVO":
    Atores.Adiciona(favorecido, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
elif favorecido["CARGO_FUNCIONAL"] == "DIRETOR":
    Atores.Adiciona(favorecido, "DIRETOR de" + OrdemServico.Cliente.ToString())
else:
    Atores.Adiciona(aprovador, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo de Posição do Favorecido Cobra
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"]))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = favorecido
i = 0
while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO":
    if i > 5:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO do cliente:"+favorecido.Nome.ToString()+" Chamado: "+OrdemServico.Numero.ToString() , "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(aprovador, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo de Posição do Favorecido Todos
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_TODOS"]))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = favorecido
i = 0
while aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO":
    if i > 5:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(aprovador, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo do Cliente
```python
gestor = OrdemServico.Cliente.Orgao.Gestor
countLoop = 0;
while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop <6):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    countLoop = countLoop + 1
if (countLoop >= 6):
   Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
Atores.Adiciona(gestor, "Gerente Executivo de " + OrdemServico.Cliente.ToString())
```

## Gerente Executivo do Contrato
```python
idScr = Convert.ToInt32(OrdemServico["NN_SCR_GERENCIAS"])
scr = Orgao.Carrega(idScr)
pessoa = Pessoa.Carrega(scr.GestorId)
gestor = Pessoa.ObtemChefia(pessoa, True)
Atores.Adiciona(gestor, "Gerente Executivo do SCR " + scr.ToString())
```

## Gerente Executivo do Favorecido
```python
gestor = OrdemServico.Favorecido.Orgao.Gestor
countLoop = 0;
while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    countLoop = countLoop + 1
if (countLoop >= 6):
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo do Responsável atual
```python
gestor = OrdemServico.Responsavel.Orgao.Gestor
countLoop = 0;
while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência" ))  and countLoop <8 ):
	gestor = gestor.Orgao.OrgaoPai.Gestor
	idgestor = gestor.Id
	if (gestor.Orgao.OrgaoPai == None or gestor.Orgao.OrgaoPai == DBNull.Value):
		break
	countLoop = countLoop + 1
if (countLoop >= 8):
	Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Responsavel.ToString())
```

## Gerente Executivo do SCR
```python
idSrc = DB.ExecuteScalar("select id_orgao from orgao where sigla = '"+ OrdemServico["SCR_TODOS_RH"].ToString() +"' ")
orgao = Orgao.Carrega(Convert.ToInt32(idSrc))
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao == "Gerência Executiva"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Atores.Adiciona(gestor, "Gerente Executivo")
```

## Gerente Executivo do Órgão Emitente
```python
s = OrdemServico.GetCustom("GESTOR_PATRIMONIALEMI").ToString()
idOrgao = Convert.ToString(s[0:s.find("-->")-1])
orgao = Orgao.Carrega(Convert.ToInt32(idOrgao))
Utils.LogError(idOrgao, "erro")
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo Favorecido Cobra
```python
demandante = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
countLoop = 0;
while (((demandante.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (demandante.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and demandante.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
    demandante = demandante.Orgao.OrgaoPai.Gestor
    countLoop = countLoop + 1
if (countLoop >= 6):
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
Atores.Adiciona(demandante, "Gerente Executivo de " + demandante.Nome.ToString())
```

## Gerente Executivo para aprovação de Prestador
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_PRESTA"))
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
	nomeFavorecido = favorecidoCustom.Nome
	orgaoFavorecido = favorecidoCustom.OrgaoId
else:
	nomeFavorecido = OrdemServico.Favorecido.Nome
	orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
orgao = Orgao.Carrega(orgaoFavorecido)
if orgao != None:
	gestor = orgao.Gestor
	countLoop = 0;
	while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 7):
		gestor = gestor.Orgao.OrgaoPai.Gestor
		countLoop = countLoop + 1
	if (countLoop >= 7):
		Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
	Atores.Adiciona(gestor, "Gerente Executido de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo para aprovação de transferências
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA"))
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
    nomeFavorecido = favorecidoCustom.Nome
    orgaoFavorecido = favorecidoCustom.OrgaoId
else:
    nomeFavorecido = OrdemServico.Favorecido.Nome
    orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
orgao = Orgao.Carrega(orgaoFavorecido)
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    if orgaoFavorecido == 934:
        Atores.Adiciona(gestor, "Presidente" + OrdemServico.Cliente.ToString())
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 9 and orgaoFavorecido != 934):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        Utils.LogInformation(gestor.Nome, OrdemServico.Numero + " - Gestor do favorecido")
        countLoop = countLoop + 1
    if (countLoop >= 9):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Cliente.ToString())
    Utils.LogInformation(countLoop.ToString(), OrdemServico.Numero + " - LoopFinal")
```

## Gerente Executivo para aprovação de Transferências - Prestador
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_PRESTA"))
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
    nomeFavorecido = favorecidoCustom.Nome
    orgaoFavorecido = favorecidoCustom.OrgaoId
else:
    nomeFavorecido = OrdemServico.Favorecido.Nome
    orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
orgao = Orgao.Carrega(orgaoFavorecido)
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 9):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 9):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Atores.Adiciona(gestor, "Gerente Executido de" + OrdemServico.Cliente.ToString())
```

## Gerente Executivo para Reclassificação Destino
```python
reg = OrdemServico.GetCustom("LISTA_LANCAMENTO")
qtdlinhas = reg.Rows.Count
origem = 0
for dr in reg.Rows:
    idOrgaoOrigem = DB.ExecuteScalar("SELECT ID_ORGAO FROM ORGAO WHERE ATIVO= 'Sim' AND SIGLA = '"+dr["UOR_ORIGEM"]+"'")
    idOrgaoDestino = DB.ExecuteScalar("SELECT ID_ORGAO FROM ORGAO WHERE ATIVO= 'Sim' AND SIGLA = '"+dr["UOR_DESTINO"]+"'")
    orgaoOrigem = Orgao.Carrega(Convert.ToInt32(idOrgaoOrigem))
    orgaoDestino = Orgao.Carrega(Convert.ToInt32(idOrgaoDestino))
    if orgaoOrigem != None:
        gestorOrigem = orgaoOrigem.Gestor
        if orgaoOrigem.OrgaoPai.Sigla == '4000001300':
            origem = orgaoOrigem.Sigla
        else:
            countLoop = 0;
            while (((gestorOrigem.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestorOrigem.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestorOrigem.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 6):
                gestorOrigem = gestorOrigem.Orgao.OrgaoPai.Gestor
                origem = gestorOrigem.Orgao.Sigla
                countLoop = countLoop + 1
    if orgaoDestino != None:
        gestorDestino = orgaoDestino.Gestor
        if orgaoDestino.OrgaoPai.Sigla == '4000001300':
            Atores.Adiciona(gestorDestino, "Gerente Executido de Destino")
        else:
            countLoop = 0;
            while (((gestorDestino.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestorDestino.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestorDestino.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência")) and countLoop < 6):
                if gestorDestino.Orgao.OrgaoPai.Sigla == '2000004017' and origem == '2000004017':
                    countLoop = 7
                    gestorDestino = gestorDestino.Orgao.Gestor
                else:
                    gestorDestino = gestorDestino.Orgao.OrgaoPai.Gestor
                    countLoop = countLoop + 1
            if (countLoop >= 8):
               Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
            Atores.Adiciona(gestorDestino, "Gerente Executido de Destino")
```

## Gerente Executivo para Reclassificação Origem
```python
reg = OrdemServico.GetCustom("LISTA_LANCAMENTO")
qtdlinhas = reg.Rows.Count
for dr in reg.Rows:
    idOrgaoOrigem = DB.ExecuteScalar("SELECT ID_ORGAO FROM ORGAO WHERE ATIVO= 'Sim' AND SIGLA = '"+dr["UOR_ORIGEM"]+"'")
    idOrgaoDestino = DB.ExecuteScalar("SELECT ID_ORGAO FROM ORGAO WHERE ATIVO= 'Sim' AND SIGLA = '"+dr["UOR_DESTINO"]+"'")
    orgaoOrigem = Orgao.Carrega(Convert.ToInt32(idOrgaoOrigem))
    orgaoDestino = Orgao.Carrega(Convert.ToInt32(idOrgaoDestino))
    if orgaoDestino != None:
        gestorDestino = orgaoDestino.Gestor
        destino = orgaoDestino.Sigla
        if orgaoDestino.OrgaoPai.Sigla == '4000001300':
            destino = orgaoDestino.Sigla
        else:
            countLoop = 0;
            while (((gestorDestino.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestorDestino.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestorDestino.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência"))  and countLoop < 8):
                gestorDestino = gestorDestino.Orgao.OrgaoPai.Gestor
                destino = gestorDestino.Orgao.Sigla
                countLoop = countLoop + 1
    if orgaoOrigem != None:
        gestorOrigem = orgaoOrigem.Gestor
        if gestorOrigem.PerfilCliente.Descricao == "Gerência Executiva":
            Atores.Adiciona(gestorOrigem, "Gerente Executido de Origem")
        if orgaoOrigem.OrgaoPai.Sigla == '4000001300':
            Atores.Adiciona(gestorOrigem, "Gerente Executido de Origem")
        else:
            countLoop = 0;
            while (((gestorOrigem.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestorOrigem.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestorOrigem.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência")) and countLoop < 8):
                if gestorOrigem.Orgao.OrgaoPai.Sigla.ToString() == '2000004017' and destino.ToString() == '2000004017':
                    countLoop = 9
                    gestorOrigem = gestorOrigem.Orgao.Gestor
                else:
                    gestorOrigem = gestorOrigem.Orgao.OrgaoPai.Gestor
                    countLoop = countLoop + 1
            if (countLoop >= 10):
               Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
            Atores.Adiciona(gestorOrigem, "Gerente Executido de Origem")
```

## Gerente Executivo para reprogramação de prazo
```python
orgao = Orgao.Carrega("Id",OrdemServico.GetCustom("GESTORES_RESPONSA"));
if (orgao != None):
	gestor = orgao.Gestor;
	if (gestor != None):
		Atores.Adiciona(gestor, "Gestor Selecionado");
```

## Gerente executivo SCR_TODOS_RH
```python
idSrc = DB.ExecuteScalar("select id_orgao from orgao where sigla = '"+ OrdemServico["SCR_TODOS_RH"].ToString() +"' ")
orgao = Orgao.Carrega(Convert.ToInt32(idSrc))
if orgao != None:
    gestor = orgao.Gestor
    countLoop = 0;
    while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência") or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao == "Gerência Executiva"))  and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO" + gestor['CARGO_FUNCIONAL'].ToString(), "ERROR")
    Atores.Adiciona(gestor, "Gerente Executivo")
```

## Gerente Executivo Solicitante
```python
solicitante = Formulario["FAVORECIDO_TODOS"].Valor
if solicitante == OrdemServico.Cliente.Orgao.GestorId.ToString():
    Atores.Add(OrdemServico.Cliente.Orgao.OrgaoPai.Gestor)
else:
    Atores.Add(OrdemServico.Cliente.ObtemChefia(False))
```

## Gerente Executivo solucionador serviço
```python
gestor = OrdemServico.Servico.ResponsavelTecnico.Orgao.Gestor
countLoop = 0;
while (((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência" ))  and countLoop <8 ):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    idgestor = gestor.Id
    if (gestor.Orgao.OrgaoPai == None or gestor.Orgao.OrgaoPai == DBNull.Value):
        break
    countLoop = countLoop + 1
if (countLoop >= 8):
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
Atores.Adiciona(gestor, "Gerente Executivo de" + OrdemServico.Responsavel.ToString())
```

## Gerente Favorecido Cobra
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Favorecido Cobra 2
```python
if OrdemServico["FAVORECIDO_TODOS"]:
    favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA2"]))
    gestor = favorecidoBBTec.ObtemChefia(False)
    if favorecidoBBTec == gestor:
        gestor = gestor.Orgao.OrgaoPai.Gestor
    Atores.Adiciona(gestor, "Gerente")
```

## Gerente Favorecido Cultura
```python
favorecidoCultura = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_CULTURA")))
gestor = favorecidoCultura.ObtemChefia(False)
if favorecidoCultura == gestor:
	gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Favorecido Deslocamento
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
gestor = favorecidoBBTec.ObtemChefia(False)
if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente Favorecido Deslocamento")
```

## Gerente Favorecido Funcio
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_FUNCIO")))
gestor = favorecidoBBTec.ObtemChefia(False)
if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Favorecido Todos
```python
if OrdemServico["FAVORECIDO_TODOS"]:
    favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_TODOS"]))
    gestor = favorecidoBBTec.ObtemChefia(False)
    if favorecidoBBTec == gestor:
        gestor = gestor.Orgao.OrgaoPai.Gestor
    Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Posição Aprova Admissao
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+OrdemServico.GetCustom("MATRICULA").ToString()+"'")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor)
```

## Gerente Posição do Cliente / Gestor de Posição do Cliente
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor)
```

## Gerente Posição do Cliente Alçada
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
if gestor["CARGO_FUNCIONAL"] == "PRESIDENTE":
    gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select id_gestor from orgao where sigla='4000008015'")))
Atores.Adiciona(gestor)
```

## Gerente Posição do Cliente ou Substituto Aprovação
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
idPessoa = DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")
tabela = Utils.ExecuteDataTable(" select ID_SUBSTITUTO_APROVACAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON (P.ID_PESSOA = CP.ID_PESSOA) WHERE P.ID_PESSOA = '"+ idPessoa.ToString() +"'  AND SYSDATE BETWEEN DT_INICIO_SUBSTIT_APROV   AND DT_FIM_SUBSTIT_APROV ")
if tabela.Rows.Count > 0 :
    for substituto in tabela.Rows:
        idPessoa = substituto["ID_SUBSTITUTO_APROVACAO"]
gestor = Pessoa.Carrega(Convert.ToInt32(idPessoa))
Atores.Adiciona(gestor)
```

## Gerente Posição do Favorecido
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.Favorecido.Id))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
if ((OrdemServico.Servico.Sigla == "WIRELESS") and (favorecido["CARGO_FUNCIONAL"] == "GERENTE EXECUTIVO" or favorecido["CARGO_FUNCIONAL"] == "DIRETOR" or favorecido["CARGO_FUNCIONAL"] == "PRESIDENTE" or favorecido["CARGO_FUNCIONAL"] == "GERENTE REGIONAL DE REDE" or favorecido["CARGO_FUNCIONAL"] == "GERENTE DE SETOR" or favorecido["CARGO_FUNCIONAL"] == "GERENTE DE EQUIPE" or favorecido["CARGO_FUNCIONAL"] == "GERENTE DE DIVISAO")):
    Atores.Adiciona(favorecido, "Favorecido gestor da área")
else:
    aprovador = gestor
    if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
        aprovador = Pessoa.Carrega(4751)
    if (DateTime.Now >= gestor.DataInicioSubstituicao and DateTime.Now <= gestor.DataFimSubstituicao):
        substituto = Pessoa.Carrega(gestor.SubstitutoAprovacaoId)
        Atores.Adiciona(substituto, "Substituto do(a) " + gestor.Nome)
    else:
        Atores.Adiciona(aprovador, "Superior imediato de " + OrdemServico.Favorecido.ToString())
```

## Gerente Posição do Responsável
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ResponsavelId))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor)
```

## Gerente Posição Favorecido Cobra
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = OrdemServico.Cliente
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Posição Favorecido CSC
```python
favorecidoCSC = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("CSC_FAVORECIDO")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoCSC["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Posição Favorecido Cultura
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_CULTURA")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = OrdemServico.Cliente
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Posição Favorecido Funcio
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_FUNCIO")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = OrdemServico.Cliente
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Posição Favorecido Todos
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Posição Favorecido Treinamento Externo
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico["TE_NOME_EMPREGADO"]))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecidoBBTec["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerente Posição para Aprovação VPN
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.Favorecido.Id))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = gestor
i = 0
while (aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO" and aprovador["CARGO_FUNCIONAL"] != "DIRETOR" and aprovador["CARGO_FUNCIONAL"] != "PRESIDENTE") and aprovador["CARGO_FUNCIONAL"] != "SUPERINTENDENTE":
    if i > 8:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
if (favorecido["CARGO_FUNCIONAL"] == "GERENTE EXECUTIVO" or favorecido["CARGO_FUNCIONAL"] == "DIRETOR" or favorecido["CARGO_FUNCIONAL"] == "PRESIDENTE") or favorecido["CARGO_FUNCIONAL"] == "SUPERINTENDENTE":
    aprovador = favorecido
    Atores.Adiciona(aprovador, "Gerente Posição para aprovação de VPN" + OrdemServico.Cliente.ToString())
else:
    if aprovador["CARGO_FUNCIONAL"] == "SUPERINTENDENTE":
        sup_dites = DB.ExecuteScalar("select count(1)from cobra_hierarquia where hierarquia LIKE '%4000008015%' and scr = '"+aprovador.Orgao.Sigla.ToString()+"'")
        if sup_dites != 0:
            aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
            while (aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO" and aprovador["CARGO_FUNCIONAL"] != "DIRETOR" and aprovador["CARGO_FUNCIONAL"] != "PRESIDENTE") and aprovador["CARGO_FUNCIONAL"] != "SUPERINTENDENTE" and (aprovador["CARGO_FUNCIONAL"].Contains("GERENTE DE CENTRO") == False) :
                if i > 8:
                    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE DE CENTRO", "ERROR")
                    break
                i = i + 1
                aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
    Atores.Adiciona(aprovador, "Gerente Posição para aprovação de VPN" + OrdemServico.Cliente.ToString())
```

## Gerente Posição para Aprovação VPN Terceiro
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico["FAVORECIDO_TODOS"]))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
aprovador = favorecido
i = 0
while (aprovador["CARGO_FUNCIONAL"] != "GERENTE EXECUTIVO" and aprovador["CARGO_FUNCIONAL"] != "DIRETOR" and aprovador["CARGO_FUNCIONAL"] != "PRESIDENTE") and (aprovador["CARGO_FUNCIONAL"] != "GERENTE REGIONAL DE REDE" or (aprovador.Orgao.Sigla.ToString()!= '2000004032' and aprovador.Orgao.Sigla.ToString()!= '2000004028' and aprovador.Orgao.Sigla.ToString()!= '2000004029' and aprovador.Orgao.Sigla.ToString()!= '2000004020')):
    if i > 5:
        Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE EXECUTIVO", "ERROR")
        break
    i = i + 1
    aprovador = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+aprovador["GESTOR_POSICAO"].ToString()+"'")))
Atores.Adiciona(aprovador, "Gerente Posição para aprovação de VPN" + OrdemServico.Cliente.ToString())
```

## Gerente Precificação / Gerente de SCR / Gerente TI Infra / Gerente TI SW
```python
if OrdemServico["SCR_TODOS_DESTINO"]:
    idScr = Convert.ToInt32(OrdemServico["SCR_TODOS_DESTINO"])
    scr = Orgao.Carrega(idScr)
    if (scr != None):
        pessoa = scr.Gestor
        if (pessoa != None):
            Atores.Adiciona(pessoa)
```

## Gerente Regional Favorecido Cobra
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"])
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
    nomeFavorecido = favorecidoCustom.Nome
    orgaoFavorecido = favorecidoCustom.OrgaoId
else:
    nomeFavorecido = OrdemServico.Favorecido.Nome
    orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
scr = Orgao.Carrega(orgaoFavorecido)
gestor = scr.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Gerência Executiva"  and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Superintendente") and countLoop < 8):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    Utils.LogInformation("acessou", "Papel aprovação")
    countLoop = countLoop + 1
if (countLoop >= 8):
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE REGIONAL DE OPERAÇÕES", "ERROR")
Atores.Adiciona(gestor, "Gerente Regional do SCR " + scr.ToString())
```

## Gerente Regional Favorecido Todos
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico["FAVORECIDO_TODOS"])
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
    nomeFavorecido = favorecidoCustom.Nome
    orgaoFavorecido = favorecidoCustom.OrgaoId
else:
    nomeFavorecido = OrdemServico.Favorecido.Nome
    orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
scr = Orgao.Carrega(orgaoFavorecido)
gestor = scr.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Gerência Executiva"  and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao != "Superintendente") and countLoop < 8):
    gestor = gestor.Orgao.OrgaoPai.Gestor
    Utils.LogInformation("acessou", "Papel aprovação")
    countLoop = countLoop + 1
if (countLoop >= 8):
    Utils.LogError("SAIDA DO LOOP - PAPEL GERENTE REGIONAL DE OPERAÇÕES", "ERROR")
Atores.Adiciona(gestor, "Gerente Regional do SCR " + scr.ToString())
```

## Gerente SCR_TODOS_RH
```python
id = DB.ExecuteScalar("select id_orgao from orgao where sigla = '"+ OrdemServico["SCR_TODOS_RH"].ToString() +"'")
idScr = Convert.ToInt32(id)
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## Gerente Selecionado
```python
if OrdemServico.GetCustom("GESTORES"):
	s = OrdemServico.GetCustom("GESTORES")
	s = Convert.ToString(s[s.find("- ")+2:len(s)])
	gestores = Orgao.ObtemTodosGestores()
	for gestor in gestores:
		if (gestor.Nome == s):
			Atores.Adiciona(gestor, "Gestor Selecionado")
```

## Gerente Superior Imediato
```python
gestor = OrdemServico.Cliente.Orgao.OrgaoPai.Gestor
if gestor != None:
    Utils.LogError(gestor.ToString(), "erro")
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = OrdemServico.Cliente
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())
```

## Gerente Superior Imediato Favorecido Cobra
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_COBRA")))
gestor = favorecidoBBTec.ObtemChefia(False)
if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente do Imediato Favorecido")
```

## Gerente Superior Imediato Favorecido Todos
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_TODOS")))
gestor = favorecidoBBTec.ObtemChefia(False)
if favorecidoBBTec == gestor:
    gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Gerente do Imediato Favorecido")
```

## Gerente Superior Imediato Posição
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.ClienteId))
gestor = Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+favorecido["GESTOR_POSICAO"].ToString()+"'")))
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = OrdemServico.Cliente
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())
```

## Gerente TE Favorecido
```python
if (OrdemServico.GetCustom("TE_NOME_EMPREGADO")):
    favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("TE_NOME_EMPREGADO")))
    gestor = favorecidoBBTec.ObtemChefia(False)
    if favorecidoBBTec == gestor:
        gestor = gestor.Orgao.OrgaoPai.Gestor
    Atores.Adiciona(gestor, "Gerente do Favorecido")
```

## Gerentes de Centro
```python
if OrdemServico.GetCustom("GERENTES_DE_CENTRO"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("GERENTES_DE_CENTRO")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```

## Gerentes de Divisão
```python
if OrdemServico.GetCustom("GERENTE_DE_DIVISAO"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("GERENTE_DE_DIVISAO")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```

## Gestor - Reparo Especial Interno
```python
cristiano   = 23478
joao_paitax = 9763
carla       = 11622
acyr        = 25347
lidiane     = 19681
pessoa_id     = 24465
if OrdemServico.GetCustom("COMBOBOX") == "SPO":
    pessoa = Pessoa.Carrega(pessoa_id)
    Atores.Adiciona(pessoa)
elif OrdemServico.GetCustom("COMBOBOX") == "BEL":
    pessoa = Pessoa.Carrega(carla)
    Atores.Adiciona(pessoa)
elif OrdemServico.GetCustom("COMBOBOX") == "BRA":
    pessoa = Pessoa.Carrega(cristiano)
    Atores.Adiciona(pessoa)
elif OrdemServico.GetCustom("COMBOBOX") == "RIO":
    pessoa = Pessoa.Carrega(acyr)
    Atores.Adiciona(pessoa)
elif OrdemServico.GetCustom("COMBOBOX") == "CUR":
    pessoa = Pessoa.Carrega(joao_paitax)
    Atores.Adiciona(pessoa)
elif OrdemServico.GetCustom("COMBOBOX") == "REC":
    pessoa = Pessoa.Carrega(lidiane)
    Atores.Adiciona(pessoa)
else:
    OrdemServico.AdicionaComentario('Não foi encontrado ninguém para ser o aprovador.\n', True)
```

## Gestor Contrato
```python
import clr
clr.AddReference("Supravizio.Custom")
if OrdemServico.GetCustom("MATRICULA"):
    result_table = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA From CP_PESSOA Where CP_PESSOA.MATRICULA = '"+str(Convert.ToInt32(OrdemServico.GetCustom("MATRICULA")))+"'")
    OrdemServico.AdicionaComentario(str(result_table.Rows), True)
    for row in result_table.Rows:
        favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(row["ID_PESSOA"]))
        if favorecidoCobra != None:
            Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Gestor Contratual
```python
import clr
clr.AddReference("Supravizio.Custom")
if OrdemServico.GetCustom("MATRICULA"):
    result_table = DB.ExecuteDataTable("Select CP_PESSOA.MATRICULA, CP_PESSOA.ID_PESSOA From CP_PESSOA Where CP_PESSOA.MATRICULA = '"+str(Convert.ToInt32(OrdemServico.GetCustom("MATRICULA")))+"'")
    for row in result_table.Rows:
        favorecidoCobra = Pessoa.Carrega(Convert.ToInt32(row["ID_PESSOA"]))
        if favorecidoCobra != None:
            Atores.Adiciona(favorecidoCobra, "Favorecido")
else:
    Atores.Adiciona(OrdemServico.Cliente, "Favorecido")
```

## Gestor da UOR
```python
pesquisaGestorUOR = DB.ExecuteDataTable("select ID_GESTOR FROM orgao WHERE SIGLA ='"+OrdemServico["SCR_PRESTADOR"].ToString()+"'")
for gestorPessoa in pesquisaGestorUOR.Rows:
    gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_GESTOR"]))
    Atores.Adiciona(gestor)
```

## Gestor da UOR (TE_UOR)
```python
if not String.IsNullOrEmpty(OrdemServico['TE_UOR'].ToString()):
    num_uor = OrdemServico['TE_UOR'].split(' - ')[0]
    pesquisaGestorUOR = DB.ExecuteDataTable("select ID_GESTOR FROM orgao WHERE SIGLA LIKE '"+num_uor.ToString()+"'")
    for gestorPessoa in pesquisaGestorUOR.Rows:
        gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_GESTOR"]))
        Atores.Adiciona(gestor)
else:
    pesquisaGestorUOR = DB.ExecuteDataTable("select ID_GESTOR FROM orgao WHERE SIGLA ='"+OrdemServico["SCR_TODOS_RH"].ToString()+"'")
    for gestorPessoa in pesquisaGestorUOR.Rows:
        gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_GESTOR"]))
        Atores.Adiciona(gestor)
```

## Gestor da UOR do Trab Temporario
```python
id = DB.ExecuteScalar(" select id_orgao from orgao where sigla = "+ OrdemServico["CSC_UOR_LISTA"] +" ")
idScr = Convert.ToInt32(id)
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## Gestor da área de cobertura DDD
```python
nome_abreviado = ""
estados = "Rio de Janeiro,Espírito Santo,Minas Gerais,Bahia,Sergipe,Alagoas,Pernambuco,Paraíba,Rio Grande do Norte,Piauí"
uf = OrdemServico.GetCustom("UF")
if uf in estados:
    nome_abreviado = "Fila Telefonia Móvel - Rio"
if nome_abreviado == "":
    estados = "Santa Catarina, São Paulo, Paraná, Rio Grande do Sul"
    if uf in estados:
        nome_abreviado = "Fila Telefonia Móvel - São Paulo"
if nome_abreviado == "":
    estados = "Distrito Federal, Goiás, Mato Grosso do Sul, Mato Grosso, Rondônia, Acre, Amazonas, Roraima, Pará, Amapá, Maranhão,Ceará, Tocantins"
    if uf in estados:
        nome_abreviado = "Fila Telefonia Móvel - Brasília"
if nome_abreviado != "" :
    tabela = Utils.ExecuteDataTable("SELECT P.ID_PESSOA, P.NOME_ABREVIADO FROM PESSOA P WHERE P.NOME_ABREVIADO = '" + nome_abreviado + "'")
    for dr in tabela.Rows:
        pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
        Atores.Adiciona(pessoa)
```

## Gestor da área de Pessoas
```python
idGestorRecurso = OrdemServico.GetCustom("GESTOR_PESSOA")
if idGestorRecurso != None:
    gestorRecurso = Pessoa.Carrega(Convert.ToInt32(idGestorRecurso))
    if gestorRecurso != None:
        Atores.Adiciona(gestorRecurso, "Gestor da área Pessoas")
```

## Gestor da área do Favorecido
```python
idGestor = OrdemServico.GetCustom("GESTOR_SOLICITA")
if idGestor != None:
  gestorFav = Pessoa.Carrega(Convert.ToInt32(idGestor))
  Atores.Adiciona(gestorFav, "Gestor do Favorecido")
```

## Gestor Demandante Contratual / Gestor Titular do Contrato
```python
idPessoa = OrdemServico["GESTOR_DO_CONTRATO"]
if idPessoa!= None:
    p = Pessoa.Carrega("Id",idPessoa )
    Atores.Adiciona(p);
```

## Gestor Demandante do Contrato
```python
pesquisa03 = DB.ExecuteDataTable("select ID_OCORRENCIA, GESTOR_CONTRATO, GESTOR_CONTRATO_SUPLENTE FROM Z_00143_GESTOR_CONTRATO WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa03.Rows:
    gestorContrato = Pessoa.Carrega(Convert.ToInt32(pessoa["GESTOR_CONTRATO"]))
    gestorContratoSuplente = Pessoa.Carrega(Convert.ToInt32(pessoa["GESTOR_CONTRATO_SUPLENTE"]))
    Atores.Adiciona(gestorContrato)
    Atores.Adiciona(gestorContratoSuplente)
```

## Gestor do Contrato / Gestor da Unidade
```python
idPessoa = OrdemServico["FAVORECIDO_COBRA"]
if idPessoa!= None:
    p = Pessoa.Carrega("Id",idPessoa )
    Atores.Adiciona(p);
```

## Gestor do FISCAL_ADM_SGPS
```python
favorecidoBBTec = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FISCAL_ADM_SGPS")))
gestor = favorecidoBBTec.ObtemChefia(False)
Atores.Adiciona(gestor, "Gerente do Fiscal Administrativo")
```

## Gestor do Recurso
```python
idGestorRecurso = OrdemServico.GetCustom("RES_BKP_GESTOR_RECURSO")
if idGestorRecurso != None:
    gestorRecurso = Pessoa.Carrega(Convert.ToInt32(idGestorRecurso))
    if gestorRecurso != None:
        Atores.Adiciona(gestorRecurso, "Gestor do recurso")
```

## Gestor do Responsável
```python
gestor = OrdemServico.Responsavel.ObtemChefia(False)
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = Pessoa.Carrega(1194)
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Responsavel.ToString())
```

## Gestor do SCR Movimentação
```python
idScr = OrdemServico.GetCustom("SCR_MOVI")
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## Gestor do Serviço
```python
Atores.Adiciona(OrdemServico.Servico.ResponsavelArea, "Pessoa cadastrada como responsável pelo Serviço '" + OrdemServico.Servico.Descricao + "' na área de negócio")
```

## Gestor do Solicitante
```python
idGestor = Formulario["Cliente.valor"]
query = "SELECT PESSOA1.NOME AS gestor, ORGAO.ID_GESTOR, PESSOA.NOME AS responsaccael, PESSOA1.CARGO AS Cargo FROM PESSOA INNER JOIN OCORRENCIA ON PESSOA.ID_PESSOA = OCORRENCIA.ID_RESPONSAVEL INNER JOIN ORGAO ON ORGAO.ID_ORGAO = PESSOA.ID_ORGAO INNER JOIN PESSOA PESSOA1 ON PESSOA1.ID_PESSOA = ORGAO.ID_GESTOR WHERE ORGAO.ID_GESTOR = {0}".format(idGestor)
tableDicoc = DB.ExecuteDataTable(query)
```

## Gestor do Solucionador
```python
gestor = OrdemServico.Responsavel.ObtemChefia(False)
if gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id> or gestor.Id == <id>:
    gestor = Pessoa.Carrega(4751)
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Responsavel.ToString())
```

## Gestor GESTOR_DO_COLABORADOR
```python
idGestor = OrdemServico["GESTOR_DO_COLABORADOR"]
pessoaGestor = Pessoa.Carrega(Convert.ToInt32(idGestor))
Atores.Adiciona(pessoaGestor)
```

## Gestor GESTOR_LOCALIDADE
```python
Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom('GESTOR_LOCALIDADE'))))
```

## Gestor Gurep Aprova
```python
if not String.IsNullOrEmpty(OrdemServico['TE_UOR'].ToString()):
    num_uor = OrdemServico['TE_UOR'].split(' - ')[0]
else:
    num_uor = OrdemServico['SCR_TODOS_RH']
aprova1 = ["2000004422"]
aprova2 = ["2000004419"]
aprova3 = ["2000004420"]
aprova4 = ["2000004418"]
aprova5 = ["2000004417"]
aprova6 = ["2000044211"]
aprova7 = ["2000004031"]
if num_uor in aprova1:
    Atores.Adiciona(Pessoa.Carrega(25347), "Aprovador GERED")
elif num_uor in aprova2:
    Atores.Adiciona(Pessoa.Carrega(11622), "Aprovador GERED")
elif num_uor in aprova3:
    Atores.Adiciona(Pessoa.Carrega(23478), "Aprovador GERED")
elif num_uor in aprova4:
    Atores.Adiciona(Pessoa.Carrega(19681), "Aprovador GERED")
elif num_uor in aprova5:
    Atores.Adiciona(Pessoa.Carrega(9763), "Aprovador GERED")
elif num_uor in aprova6:
    Atores.Adiciona(Pessoa.Carrega(24465), "Aprovador GERED")
elif num_uor in aprova7:
    Atores.Adiciona(Pessoa.Carrega(11403), "Aprovador GERED")
else:
    Utils.LogError("Não faz parte da Gered: " + str(num_uor), "INFO")
```

## Gestor Jurídico Atual / Especialista Atual
```python
Atores.Adiciona(OrdemServico.ResponsavelInicial,"Cadastrado como Primeiro Solucionador responsável pelo atendimento")
```

## Gestor Patrimonial Órgão Destinatário
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("SCR1"))
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## Gestor Patrimonial Órgão Emitente
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("SCR"))
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## Gestor PCCS GERED
```python
uor = DB.ExecuteDataTable(" SELECT DISTINCT nvl(SUBSTR(tmp.hierarquia,34,10),0) AS cat, nvl(SUBSTR(tmp.hierarquia,23,10),0) AS coord, nvl(SUBSTR(tmp.hierarquia,12,10),0) AS super, nvl(SUBSTR(tmp.hierarquia,1,10),0) AS gerex FROM tmp_gered tmp WHERE uor in (SELECT DISTINCT z.uor_destino FROM Z_00143_LISTA_GERED z WHERE z.ID_OCORRENCIA = '"+ OrdemServico.Id.ToString() +"') ")
gerencia = '0'
for lista in uor.Rows:
    cat = lista["CAT"]
    coord = lista["COORD"]
    super = lista["SUPER"]
    gerex = lista["GEREX"]
    gerencia = gerex
    if cat != '0' :
        gerencia = super
    if cat == '0' and coord != '0':
        gerencia = super
    if coord == '0' and super != '0':
        gerencia = gerex
    tabela = Utils.ExecuteDataTable(" SELECT DISTINCT cpp.ID_PESSOA FROM TMP_GERED tmp INNER JOIN CP_PESSOA cpp ON tmp.MATRICULA_GESTOR = cpp.MATRICULA  inner join  pessoa p on p.id_pessoa = cpp.id_pessoa WHERE tmp.uor = '"+ gerencia +"'  and p.ATIVO='Sim'")
    for dr in tabela.Rows:
        pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
        Atores.Adiciona(pessoa)
```

## Gestor Resp Demanda
```python
idOrgao = OrdemServico.GetCustom("RESP_ATEND_DOD")
if idOrgao != None:
  orgao = Orgao.Carrega(Convert.ToInt32(idOrgao))
  Atores.Adiciona(orgao.Gestor, "Gestor responsável pela demanda")
```

## Gestor UOR
```python
pesquisaGestorUOR = DB.ExecuteDataTable("select ID_GESTOR FROM orgao WHERE SIGLA ='"+OrdemServico["SCR_TODOS_DESTINO"].ToString()+"'")
for gestorPessoa in pesquisaGestorUOR.Rows:
    gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_GESTOR"]))
    Atores.Adiciona(gestor)
```

## Gestor UOR PAI
```python
pesquisaGestorUOR = DB.ExecuteDataTable("select orgao1.ID_ORGAO_PAI, orgao2.ID_GESTOR from orgao orgao1 inner join orgao orgao2 on orgao1.ID_ORGAO_PAI = orgao2.ID_ORGAO where orgao1.SIGLA ='"+OrdemServico["SCR_TODOS_DESTINO"].ToString()+"'")
for gestorPessoa in pesquisaGestorUOR.Rows:
    gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_GESTOR"]))
    Atores.Adiciona(gestor)
```

## Gestores
```python
tabela = Utils.ExecuteDataTable("select nvl(p2.ID_SUBSTITUTO_APROVACAO,p.ID_PESSOA ) as ID_PESSOA FROM PESSOA p INNER JOIN cp_pessoa cp ON P.Id_Pessoa = Cp.Id_Pessoa LEFT OUTER JOIN pessoa p2 ON P2.Id_Pessoa = p.Id_Pessoa and (p2.dt_inicio_substit_aprov<=SYSDATE and p2.dt_fim_substit_aprov>=sysdate and p2.ID_SUBSTITUTO_APROVACAO is not null) WHERE p.ATIVO LIKE 'Sim' AND (Cp.Cargo_Funcional LIKE '%COORDENADOR%' OR Cp.Cargo_Funcional LIKE '%SUPERINTENDENTE%' OR Cp.Cargo_Funcional LIKE '%GERENTE%' OR cp.Cargo_Funcional LIKE '%DIRETOR%' OR cp.Cargo_Funcional LIKE '%PRESIDENTE%')")
for dr in tabela.Rows:
    pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Gestores - Cargo Funcional
```python
tabela = Utils.ExecuteDataTable("select ID_PESSOA from PESSOA where ATIVO like 'Sim' and (CARGO like '%GERENTE%' or CARGO like '%ASSESSOR%' or CARGO like '%DIRETOR%' or CARGO like '%PRESIDENTE%') and ID_PESSOA NOT IN (SELECT ID_GESTOR from ORGAO where ID_GESTOR IS NOT NULL and ATIVO = 'Sim')")
for dr in tabela.Rows:
    pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
    Atores.Adiciona(pessoa)
gestores = Orgao.ObtemTodosGestores()
for gestor in gestores:
    if gestor.Ativo:
        Atores.Adiciona(gestor)
```

## Gestores da UOR 3611
```python
pesquisaGestorUOR = DB.ExecuteDataTable("Select PESSOA.NOME, CP_PESSOA.CARGO_FUNCIONAL, CP_PESSOA.GESTOR_POSICAO, PESSOA.ID_PESSOA From ORGAO Inner Join PESSOA On PESSOA.ID_ORGAO = ORGAO.ID_ORGAO Inner Join CP_PESSOA On CP_PESSOA.ID_PESSOA = PESSOA.ID_PESSOA Where ORGAO.SIGLA = '3000003611' And CP_PESSOA.CARGO_FUNCIONAL Like 'GERENTE%' Group By PESSOA.ID_PESSOA, PESSOA.NOME, CP_PESSOA.CARGO_FUNCIONAL, CP_PESSOA.GESTOR_POSICAO")
for gestorPessoa in pesquisaGestorUOR.Rows:
    gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_PESSOA"]))
    Atores.Adiciona(gestor)
```

## Gestores de Transferências
```python
tabela = Utils.ExecuteDataTable("select distinct p.ID_PESSOA from pessoa p inner join CAD_FUNCIONARIO_V f on f.NOME = p.NOME where p.ATIVO like 'Sim' and (p.CARGO like '%GERENTE%' or p.CARGO like '%ASSESSOR%' or p.CARGO like '%DIRETOR%' or p.CARGO like '%PRESIDENTE%') or p.ID_PESSOA IN (SELECT ID_GESTOR from ORGAO o where ID_GESTOR IS NOT NULL and o.ATIVO = 'Sim')")
for dr in tabela.Rows:
	pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
	Atores.Adiciona(pessoa)
gestores = Orgao.ObtemTodosGestores()
for gestor in gestores:
    if gestor.Ativo:
        Atores.Adiciona(gestor)
```

## Gestores de Área e Substitutos
```python
gestor = DB.ExecuteDataTable(" select ID_GESTOR FROM orgao where ativo='Sim' and ID_GESTOR is not null")
for linha in gestor.Rows:
    Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(linha['ID_GESTOR'])))
    tabela = Utils.ExecuteDataTable("select ID_SUBSTITUTO_APROVACAO FROM PESSOA P INNER JOIN CP_PESSOA CP ON (P.ID_PESSOA = CP.ID_PESSOA) WHERE P.ID_PESSOA = '"+ linha['ID_GESTOR'].ToString() +"'  AND SYSDATE BETWEEN DT_INICIO_SUBSTIT_APROV   AND DT_FIM_SUBSTIT_APROV ")
    if tabela.Rows.Count > 0 :
        for linhaS in tabela.Rows:
            Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(linhaS["ID_SUBSTITUTO_APROVACAO"])))
```

## Gestores Lista SCR
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join z_00143_lista_scr li on oc.id_ocorrencia = li.id_ocorrencia inner join orgao o on li.scr = o.id_orgao inner join pessoa pe on o.id_gestor = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Gestores LISTA_INTER
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join Z_00143_LISTA_INTER li on oc.id_ocorrencia = li.id_ocorrencia inner join orgao o on li.SCR_INTER = o.descricao inner join pessoa pe on o.id_gestor = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
	pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
	Atores.Adiciona(pessoa)
```

## Gestores NN_LISTA_RISCOS
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join z_00143_NN_LISTA_RISCOS li on oc.id_ocorrencia = li.id_ocorrencia inner join orgao o on li.scr = o.descricao inner join pessoa pe on o.id_gestor = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Gestores NN_LISTA_SCR
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join z_00143_nn_lista_scr li on oc.id_ocorrencia = li.id_ocorrencia inner join orgao o on li.scr = o.descricao inner join pessoa pe on o.id_gestor = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
	pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
	Atores.Adiciona(pessoa)
```

## Gestores PCCS GERED
```python
tabela = Utils.ExecuteDataTable(" SELECT distinct cpp.ID_PESSOA FROM TMP_GERED tmp INNER JOIN CP_PESSOA cpp ON tmp.MATRICULA_GESTOR = cpp.MATRICULA ")
for dr in tabela.Rows:
    pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Gestores Setor de Engenharia
```python
sql = DB.ExecuteDataTable("Select PESSOA.NOME, CP_PESSOA.CARGO_FUNCIONAL, ORGAO.SIGLA, PESSOA.ID_PESSOA From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Inner Join ORGAO On ORGAO.ID_ORGAO = PESSOA.ID_ORGAO Where (CP_PESSOA.CARGO_FUNCIONAL Like '%GERENTE%' Or CP_PESSOA.CARGO_FUNCIONAL Like '%ASSESSOR%') And ORGAO.SIGLA Like '%2000007792%'")
for i in sql.Rows:
    funcionario = i['ID_PESSOA']
    pessoa = Pessoa.Carrega(Convert.ToInt32(funcionario))
    Atores.Adiciona(pessoa)
```

## Grid Pessoas
```python
pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, PESSOAS FROM Z_00143_GRID_PESSOAS WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa01.Rows:
    aprovadores = Pessoa.Carrega(Convert.ToInt32(pessoa["PESSOAS"]))
    Atores.Adiciona(aprovadores)
```

## Homologador
```python
favorecidoList = OrdemServico.GetCustom("FAVORECIDO_LIST")
for favorecido in favorecidoList:
	Atores.Adiciona(favorecido)
```

## Intervenientes
```python
tabela = Utils.ExecuteDataTable(" SELECT pe.id_pessoa FROM OCORRENCIA OC inner join z_00143_intervenientes_TI inter on oc.id_ocorrencia = inter.id_ocorrencia inner join pessoa pe on inter.favorecido = pe.id_pessoa where oc.numero = '"+ OrdemServico.Numero.ToString() +"' ")
for ator in tabela.Rows:
	pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
	Atores.Adiciona(pessoa)
```

## Key Users
```python
tabela = Utils.ExecuteDataTable(" SELECT ku.id_pessoa FROM keyuser_erp ku INNER JOIN servico se ON ku.sigla = se.sigla WHERE se.sigla = '"+ OrdemServico.Servico.Sigla +"' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## LISTA_FUNCIONARIO
```python
tabela = DB.ExecuteDataTable(" SELECT cpp.ID_PESSOA FROM Z_00143_LISTA_FUNCIONARIO lif inner join CP_PESSOA cpp on cpp.MATRICULA = lif.MATRICULA WHERE id_ocorrencia = '"+ OrdemServico.Id.ToString() +"' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(ator["ID_PESSOA"])
    Atores.Adiciona(pessoa)
```

## Matricula Favorecido
```python
favorecidoMatricula = str(OrdemServico.GetCustom('TE_MATRICULA'))
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + favorecidoMatricula + "'")
idAnalista = 0
for row in lista.Rows:
    idAnalista = row['ID_PESSOA']
```

## Matrícula Gestor
```python
gestorMatricula = str(OrdemServico.GetCustom('MATRICULA'))
lista = Utils.ExecuteDataTable("Select PESSOA.ID_PESSOA, CP_PESSOA.MATRICULA, PESSOA.EMAIL, PESSOA.NOME From PESSOA Inner Join CP_PESSOA On PESSOA.ID_PESSOA = CP_PESSOA.ID_PESSOA Where CP_PESSOA.MATRICULA ='" + gestorMatricula + "'")
idAnalista = 0
for row in lista.Rows:
    idAnalista = row['ID_PESSOA']
```

## Membros do Projeto
```python
tabela = Utils.ExecuteDataTable("select ID_PESSOA from PESSOA where ATIVO like 'Sim' and (CARGO like '%GERENTE%' or CARGO like '%ACESSOR%' or CARGO like '%DIRETOR%' or CARGO like '%PRESIDENTE%')")
for dr in tabela.Rows:
	pessoa = Pessoa.Carrega(dr["ID_PESSOA"])
	Atores.Adiciona(pessoa)
gestores = Orgao.ObtemTodosGestores()
for gestor in gestores:
    if gestor.Ativo:
        Atores.Adiciona(gestor)
```

## MP - Gerente Posição do Substituído
```python
idSBSTITUIDO = OrdemServico["MP_FUNCIONARIO_SUBSTITUIDO"]
gestor=Pessoa.Carrega(Convert.ToInt32(DB.ExecuteScalar("SELECT CASE WHEN P.ID_PESSOA = O.ID_GESTOR THEN (SELECT PAI.ID_GESTOR FROM ORGAO PAI WHERE PAI.ID_ORGAO = O.ID_ORGAO_PAI)ELSE O.ID_GESTOR END AS ID_GESTOR FROM PESSOA P INNER JOIN ORGAO O ON P.ID_ORGAO = O.ID_ORGAO WHERE P.ID_PESSOA ="+idSBSTITUIDO)))
Atores.Adiciona(gestor)
```

## NN - Diretor Negócio
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("NN_GERENCIA_NEGOCIO"))
scr = Orgao.Carrega(idScr)
if (scr != None):
	pessoa = scr.OrgaoPai.Gestor
	if (pessoa != None):
		Atores.Adiciona(pessoa)
```

## NN - Gerente Destino
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("NN_GERENCIA_DESTINO"))
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## NN - Gerente Destino Posição
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("NN_GERENCIA_DESTINO"))
listapessoascr = DB.ExecuteDataTable("select cpp.ID_PESSOA, cpp.CARGO_FUNCIONAL, cpp.GESTOR_POSICAO from GRUPO_TRABALHO gt inner join tecnico te on te.id_grupo_trabalho = gt.id_grupo_trabalho inner join pessoa pe on pe.id_pessoa = te.id_pessoa inner join cp_pessoa cpp on cpp.id_pessoa = te.id_pessoa inner join orgao org on org.id_orgao = pe.id_orgao where gt.descricao like '%Estrutura%' and te.ativo = 'Sim' and pe.ativo = 'Sim' and org.ID_ORGAO='"+idScr.ToString()+"'")
edivisao=0
for pessoascr in listapessoascr.Rows:
    cargofuncao = pessoascr["CARGO_FUNCIONAL"].ToString()
    idpessoa=pessoascr["ID_PESSOA"].ToString()
    if cargofuncao == 'GERENTE DE DIVISAO':
        edivisao=1
        Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idpessoa)))
if edivisao==0 :
   for pessoascr in listapessoascr.Rows:
       cargofuncao = pessoascr["CARGO_FUNCIONAL"].ToString()
       idpessoa=pessoascr["ID_PESSOA"].ToString()
       matriculagestor=pessoascr["GESTOR_POSICAO"].ToString()
       cargogestor=''
       i=0
       while cargogestor.ToString() != "GERENTE DE DIVISAO" or cargogestor.ToString() != "GERENTE EXECUTIVO" or cargogestor.ToString() != "DIRETOR" or cargogestor.ToString() != "PRESIDENTE":
           if matriculagestor.ToString() == '' or i > 5:
               break
           i = i + 1
           cargogestor = DB.ExecuteScalar("select CARGO_FUNCIONAL FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor+"'")
           if cargogestor.ToString() == "GERENTE DE DIVISAO" or cargogestor.ToString() == "GERENTE EXECUTIVO" or cargogestor.ToString() == "DIRETOR" or cargogestor.ToString() == "PRESIDENTE":
               idgestor = DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor+"'")
               Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idgestor)))
           else:
               idpessoa=DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor.ToString()+"'")
               matriculagestor=DB.ExecuteScalar("select GESTOR_POSICAO FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor.ToString()+"'")
```

## NN - Gerência Executiva Destino
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("NN_GERENCIA_DESTINO"))
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.OrgaoPai.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## NN - Gerência Executiva Destino Posição
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("NN_GERENCIA_DESTINO"))
listapessoascr = DB.ExecuteDataTable("select cpp.ID_PESSOA, cpp.CARGO_FUNCIONAL, cpp.GESTOR_POSICAO from GRUPO_TRABALHO gt inner join tecnico te on te.id_grupo_trabalho = gt.id_grupo_trabalho inner join pessoa pe on pe.id_pessoa = te.id_pessoa inner join cp_pessoa cpp on cpp.id_pessoa = te.id_pessoa inner join orgao org on org.id_orgao = pe.id_orgao where gt.descricao like '%Estrutura%' and te.ativo = 'Sim' and pe.ativo = 'Sim' and org.ID_ORGAO='"+idScr.ToString()+"'")
edivisao=0
for pessoascr in listapessoascr.Rows:
    cargofuncao = pessoascr["CARGO_FUNCIONAL"].ToString()
    idpessoa=pessoascr["ID_PESSOA"].ToString()
    if cargofuncao == 'GERENTE EXECUTIVO':
        edivisao=1
        Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idpessoa)))
if edivisao==0 :
    cargofuncao = pessoascr["CARGO_FUNCIONAL"].ToString()
    idpessoa=pessoascr["ID_PESSOA"].ToString()
    matriculagestor=pessoascr["GESTOR_POSICAO"].ToString()
    cargogestor=''
    i=0
    while cargogestor.ToString() != "GERENTE EXECUTIVO" or cargogestor.ToString() != "DIRETOR" or cargogestor.ToString() != "PRESIDENTE":
        if matriculagestor.ToString() == '' or i > 5:
            break
        i = i + 1
        cargogestor = DB.ExecuteScalar("select CARGO_FUNCIONAL FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor+"'")
        if cargogestor.ToString() == "GERENTE EXECUTIVO" or cargogestor.ToString() == "DIRETOR" or cargogestor.ToString() == "PRESIDENTE":
            idgestor = DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor+"'")
            Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(idgestor)))
        else:
            idpessoa=DB.ExecuteScalar("select ID_PESSOA FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor.ToString()+"'")
            matriculagestor=DB.ExecuteScalar("select GESTOR_POSICAO FROM CP_PESSOA WHERE MATRICULA = '"+matriculagestor.ToString()+"'")
```

## NN - Gerência Executiva Negócio
```python
idScr = Convert.ToInt32(OrdemServico.GetCustom("NN_GERENCIA_NEGOCIO"))
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```

## NN - Líder do Projeto
```python
lider = Convert.ToInt32(OrdemServico.GetCustom("NN_RESPONSAVEL_RELACIONAMENTO"))
idPessoa = Pessoa.Carrega(lider)
if idPessoa != None:
	Atores.Adiciona(idPessoa)
```

## Pagamento IUVP
```python
pessoas = DB.ExecuteDataTable("Select PESSOA.ID_PESSOA AS PESSOAS From PESSOA Where PESSOA.NOME In ('<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>', '<NOME>') AND PESSOA.ATIVO = 'Sim'")
for i in pessoas.Rows:
    pessoa = Pessoa.Carrega(i["PESSOAS"])
    Atores.Adiciona(pessoa)
```

## PEAD Gestor Cesec
```python
ator = DB.ExecuteScalar(
    (
        "SELECT O.ID_GESTOR "
        "<NOME> "
        "WHERE TRIM(O.SIGLA) = '3000003810' "
        "AND O.ATIVO = 'Sim' "
        "AND O.ID_GESTOR IS NOT NULL "
        "AND ROWNUM = 1"
    )
)
if ator is not None:
    gerente = Convert.ToInt32(
        ator
    )
    gestor = Pessoa.Carrega(
        "Id",
        gerente
    )
    if gestor is not None:
        Atores.Adiciona(
            gestor,
            "Gestor Executivo"
        )
```

## Precificação
```python
precificador = OrdemServico.ResponsavelId
pessoa = Pessoa.Carrega(Convert.ToInt32(precificador));
if (pessoa != None):
    Atores.Adiciona(pessoa, "Precificador");
```

## Presidente
```python
lista = Utils.ExecuteDataTable("select ID_ORGAO from ORGAO where upper(DESCRICAO) LIKE '%PRESID%' and ATIVO = 'Sim' AND ROWNUM = 1");
for registro in lista.Rows:
    idOrgao = registro["ID_ORGAO"].ToString();
orgao = Orgao.Carrega("Id",idOrgao);
if (orgao != None):
    presidente = orgao.Gestor;
    if (presidente != None):
        Atores.Adiciona(presidente, "Presidente")
```

## Presidente CIPA PRESIDENTE_CIPA
```python
Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom('PRESIDENTE_CIPA'))))
```

## Presidente da Cobra
```python
gestor = OrdemServico.Cliente.Orgao.Gestor
countLoop = 0;
while (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente != "Presidência" and countLoop < 6):
	gestor = gestor.Orgao.OrgaoPai.Gestor
	countLoop = countLoop + 1
if (countLoop >= 6):
	Utils.LogError("SAIDA DO LOOP - PAPEL DIRETOR EXECUTIVO", "ERROR")
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Cliente.ToString())
```

## Presidente ou Gestor CIPA
```python
if OrdemServico["SIM_NAO"] == "Sim":
    Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom('PRESIDENTE_CIPA'))))
if OrdemServico["SIM_NAO"] == "Não":
    Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom('GESTOR_LOCALIDADE'))))
```

## Prestação de Contas Viagem e Hospedagem - Conforme NI006v.87
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_DESLOCAMENTO")))
cargoFavorecido = favorecido["CARGO_FUNCIONAL"]
orgaoFavorecido = favorecido.Orgao.Sigla
gestorPosicao = ""
if (cargoFavorecido == "PRESIDENTE" or cargoFavorecido == "DIRETOR" or cargoFavorecido == "ASSESSOR EXECUTIVO PRESIDENCIA" or cargoFavorecido == "<NOME>" or cargoFavorecido == "CONSELHEIRO DE ADMINISTRACAO" or cargoFavorecido == "CONSELHEIRO FISCAL") or (cargoFavorecido == "GERENTE EXECUTIVO" and orgaoFavorecido == "3000009200" or orgaoFavorecido == "3000001330" or orgaoFavorecido == "3000009400" or orgaoFavorecido == "3000004052") or (cargoFavorecido == "GERENTE DE PROJETOS I" and orgaoFavorecido == "3000004051" or orgaoFavorecido == "3000004055"):
    uor = Orgao.Carrega("Sigla", "3000009430")
    gestor = uor.Gestor
    aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003402":
        uor = Orgao.Carrega("Sigla", "3000009430")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003401":
        uor = Orgao.Carrega("Sigla", "3000003410")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003200":
        uor = Orgao.Carrega("Sigla", "3000003260")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000003100":
        uor = Orgao.Carrega("Sigla", "3000009350")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000008810":
        uor = Orgao.Carrega("Sigla", "3000002050")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000002026":
        uor = Orgao.Carrega("Sigla", "3000002023")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "3000008800":
        uor = Orgao.Carrega("Sigla", "3000008406")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000008422":
        uor = Orgao.Carrega("Sigla", "2000008260")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000008100":
        uor = Orgao.Carrega("Sigla", "2000008110")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000008300":
        uor = Orgao.Carrega("Sigla", "2000008310")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000004039":
        uor = Orgao.Carrega("Sigla", "2000004049")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO") and orgaoFavorecido == "2000004017":
        uor = Orgao.Carrega("Sigla", "2000004019")
        gestor = uor.Gestor
        aprovador = gestor
elif (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO")and orgaoFavorecido == "3000004060":
        uor = Orgao.Carrega("Sigla", "3000004045")
        gestor = uor.Gestor
        aprovador = gestor
else:
    if (cargoFavorecido == "GERENTE EXECUTIVO" or cargoFavorecido=="GERENTE EXECUTIVO_" or cargoFavorecido=="GERENTE_EXECUTIVO")and orgaoFavorecido == "4000001110":
        uor = Orgao.Carrega("Sigla", "4000001112")
        gestor = uor.Gestor
        aprovador = gestor
    else:
        gestorid = favorecido.Orgao.GestorId
        gestor = favorecido.Orgao.Gestor
        if gestorid == favorecido.Id:
            gestor = favorecido.Orgao.OrgaoPai.Gestor
        aprovador = gestor
Atores.Adiciona(aprovador, "Alçadas de Aprovação por Posição Viagem e Hospedagem - Conforme NI006v.77")
```

## publico alvo PCCS
```python
tabela = Utils.ExecuteDataTable(" SELECT P.Id_Pessoa FROM pessoa p INNER JOIN cp_pessoa cp ON P.Id_Pessoa = Cp.Id_Pessoa INNER JOIN orgao O ON P.Id_Orgao = O.Id_Orgao INNER JOIN CAD_FUNCIONARIO_V cad on cad.matricula = cp.matricula WHERE Cp.Tipo_Contratacao IN ('H', 'A') AND P.ATIVO = 'Sim' AND P.Cargo <> 'AUXILIAR DE OPERACOES' ")
for ator in tabela.Rows:
    pessoa = Pessoa.Carrega(Convert.ToInt32(ator["ID_PESSOA"]))
    Atores.Adiciona(pessoa)
```

## Responsavel Processo
```python
if OrdemServico.GetCustom("RESPONSAVEL_PROCESSO"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("RESPONSAVEL_PROCESSO")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```

## Responsavel Sistema Corporativo Selecionado
```python
if (OrdemServico.GetCustom("<NOME>") == True):
    s = OrdemServico.GetCustom("GESTORES")
    s = Convert.ToString(s[s.find("- ")+2:len(s)])
    Utils.LogInformation("Papel - Responsavel Sistema Corporativo Selecionado",s)
    gestores = Orgao.ObtemTodosGestores()
    for gestor in gestores:
        if (gestor.Nome == s):
            if (DateTime.Now >= gestor.DataInicioSubstituicao and DateTime.Now <= gestor.DataFimSubstituicao):
                substituto = Pessoa.Carrega(gestor.SubstitutoAprovacaoId)
                Atores.Adiciona(substituto, "Substituto do Gestor Selecionado")
            else:
                Atores.Adiciona(gestor, "Gestor Selecionado")
if (OrdemServico.GetCustom("<NOME>") == True):
    Atores.Adiciona(OrdemServico.Favorecido, "Cliente")
```

## Responsavel Tarefa Inicial
```python
if OrdemServico.GetCustom("RESPONSAVEL_TAREFA_INICIAL"):
    favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("RESPONSAVEL_TAREFA_INICIAL")))
    if favorecido != None:
        Atores.Adiciona(favorecido, "Favorecido")
```

## Responsável atual / Responsável pelo Negócio / Substituto
```python
Atores.Adiciona(OrdemServico.Responsavel, "Pessoa identificada como responsável na Ordem de Serviço")
```

## Responsável compras
```python
idResponsavelCompras = OrdemServico.GetCustom("RESPONSAVEL_COMPRAS")
responsavelCompras = Pessoa.Carrega(Convert.ToInt32(idResponsavelCompras ))
if responsavelCompras != None:
	Atores.Adiciona(responsavelCompras, "Favorecido")
```

## Responsável pela atividade
```python
if OrdemServico.Servico.Sigla == "CONTRACHEQUE1":
    if OrdemServico.GetCustom("TIPO_SERV") == "Plano de Saúde" or (OrdemServico.GetCustom("TIPO_SERV") == "Afastamento") or (OrdemServico.GetCustom("TIPO_SERV") == "Previdência"):
        aprovador = Pessoa.Carrega(Convert.ToInt32(26600))
        Atores.Adiciona(aprovador, "Responsável da atividade")
    else:
        Atores.Adiciona(OrdemServico.Servico.ResponsavelTecnico, "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
else:
    Atores.Adiciona(OrdemServico.Servico.ResponsavelTecnico, "Responsável técnico cadastrado no Serviço '" + OrdemServico.Servico.Descricao + "'")
```

## Responsável pelo início do subprocesso
```python
Atores.Adiciona(OrdemServico.ClasseSubProcesso.Responsavel,"Cadastrado como responsável na Classe de Sub-processo")
```

## Responsável pelo Negócio indicado pelo GEREX
```python
s = OrdemServico.GetCustom("FAVORECIDO_TODOS").ToString()
id = Convert.ToString(s)
pessoa = Pessoa.Carrega(Convert.ToInt32(id));
Atores.Adiciona(pessoa)
```

## Responsável técnico
```python
s = OrdemServico.GetCustom("FAVORECIDO_DITEC").ToString()
id = Convert.ToString(s)
pessoa = Pessoa.Carrega(Convert.ToInt32(id));
Atores.Adiciona(pessoa)
```

## Seleção de aprovadores
```python
pesquisa01 = DB.ExecuteDataTable("select ID_OCORRENCIA, APROVADORES FROM Z_00143_SELECAPROV WHERE ID_OCORRENCIA ='"+OrdemServico.Id.ToString()+"'")
for pessoa in pesquisa01.Rows:
    aprovadores = Pessoa.Carrega(Convert.ToInt32(pessoa["APROVADORES"]))
    Atores.Adiciona(aprovadores)
```

## Solucionador da área de cobertura DDD
```python
sigla = ""
regional = ''
estados = "Rio de Janeiro,Espírito Santo,Minas Gerais,Bahia,Sergipe,Alagoas,Pernambuco,Paraíba,Rio Grande do Norte,Piauí"
uf = OrdemServico.GetCustom("UF")
if uf in estados:
    regional = "REGIONALRJ"
    sigla = "03150"
if regional == "":
    estados = "Santa Catarina, São Paulo, Paraná, Rio Grande do Sul"
    if uf in estados:
        regional = "REGIONALSP"
        sigla = "03710"
if regional == "":
    estados = "Distrito Federal, Goiás, Mato Grosso do Sul, Mato Grosso, Rondônia, Acre, Amazonas, Roraima, Pará, Amapá, Maranhão,Ceará"
    if uf in estados:
        regional = "REGIONALDF"
        sigla = "03810"
if regional != "" :
    qry = "SELECT P.ID_PESSOA, P.NOME FROM AUTORIZA_FILA AF INNER JOIN GRUPO_TRABALHO GT ON (AF.ID_GRUPO_TRABALHO = GT.ID_GRUPO_TRABALHO) INNER JOIN PESSOA P ON (AF.ID_FILA = P.ID_PESSOA AND P.NOME LIKE ('%Telefonia%')) WHERE GT.ATIVO = 'Sim' AND GT.SIGLA =  '" + regional + "'"
    tabela = Utils.ExecuteDataTable(qry)
    for linha in tabela.Rows:
        pessoa = Pessoa.Carrega(linha["ID_PESSOA"])
        Atores.Adiciona(pessoa)
```

## Substituto Aprovação do Gestor de Uor
```python
tabela = Utils.ExecuteDataTable(" select p.id_substituto_aprovacao from pessoa P INNER JOIN orgao o ON p.id_orgao = o.id_orgao WHERE (p.id_substituto_aprovacao is not null AND (SYSDATE BETWEEN p.DT_INICIO_SUBSTIT_APROV   AND p.DT_FIM_SUBSTIT_APROV)) and o.id_gestor = p.id_pessoa AND p.ativo = 'Sim' AND o.ativo = 'Sim' ")
if tabela.Rows.Count > 0 :
    for substituto in tabela.Rows:
        idPessoa = substituto["ID_SUBSTITUTO_APROVACAO"]
        gestor = Pessoa.Carrega(Convert.ToInt32(idPessoa))
        Atores.Adiciona(gestor)
```

## Superintendente
```python
from System import Convert, DBNull
def vazio(valor):
    return valor is None or valor == DBNull.Value or valor.ToString().strip() == ""
def campo_os(nome):
    try:
        return OrdemServico[nome]
    except:
        return None
idOrgaoInicio = None
origem = ""
sigla = campo_os("SCR_TODOS_RH")
if not vazio(sigla):
    idSrc = DB.ExecuteScalar("select id_orgao from orgao where sigla = '" + sigla.ToString().strip() + "' ")
    if not vazio(idSrc):
        idOrgaoInicio = Convert.ToInt32(idSrc)
        origem = "SCR_TODOS_RH (" + sigla.ToString().strip() + ")"
if idOrgaoInicio is None:
    idFav = campo_os("FAVORECIDO_TODOS")
    if not vazio(idFav):
        idSrc = DB.ExecuteScalar("select id_orgao from pessoa where id_pessoa = " + Convert.ToInt32(idFav).ToString())
        if not vazio(idSrc):
            idOrgaoInicio = Convert.ToInt32(idSrc)
            origem = "lotacao do favorecido"
if idOrgaoInicio is None:
    idSrc = DB.ExecuteScalar("select p.id_orgao from ocorrencia o inner join pessoa p on p.id_pessoa = o.id_cliente where o.id_ocorrencia = " + OrdemServico.Id.ToString())
    if not vazio(idSrc):
        idOrgaoInicio = Convert.ToInt32(idSrc)
        origem = "lotacao do solicitante"
if idOrgaoInicio is None:
    Utils.LogInformation("OS " + OrdemServico.Id.ToString() + ": UOR nao encontrada. Papel sem ator.", "Papel Superintendente UOR")
else:
    qry = "select min(id_orgao) keep (dense_rank first order by nivel) from (" + \
          " select o.id_orgao, level as nivel," + \
          " (select max(upper(trim(cp.cargo_funcional))) from cp_pessoa cp where cp.id_pessoa = o.id_gestor) as cargo" + \
          " from orgao o" + \
          " start with o.id_orgao = " + idOrgaoInicio.ToString() + \
          " connect by nocycle prior o.id_orgao_pai = o.id_orgao" + \
          ") where cargo like 'SUPERINTENDENTE%'"
    idOrgaoSup = DB.ExecuteScalar(qry)
    if vazio(idOrgaoSup):
        Utils.LogInformation("OS " + OrdemServico.Id.ToString() + ": sem superintendente acima da " + origem + ". Papel sem ator.", "Papel Superintendente UOR")
    else:
        orgaoSup = Orgao.Carrega(Convert.ToInt32(idOrgaoSup))
        if orgaoSup is not None and orgaoSup.Gestor is not None:
            Atores.Adiciona(orgaoSup.Gestor, "Superintendente UOR")
            Utils.LogInformation("OS " + OrdemServico.Id.ToString() + ": superintendente " + orgaoSup.Gestor.Nome + " (orgao " + orgaoSup.Sigla + ") a partir da " + origem + ".", "Papel Superintendente UOR")
```

## Superintendente do Cliente / Superintendentes BBTS
```python
gestor = OrdemServico.Cliente.Orgao.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Gerência Executiva") and countLoop < 6):
    if gestor['CARGO_FUNCIONAL'].ToString() == "SUPERINTENDENTE":
        gestor = gestor
        break
    else:
        gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Superintendente do Cliente" + OrdemServico.Cliente.ToString())
```

## Superintendente do Favorecido Cobra
```python
idFavorecidoCustom = Convert.ToInt32(OrdemServico["FAVORECIDO_COBRA"])
favorecidoCustom = Pessoa.Carrega(idFavorecidoCustom)
if favorecidoCustom != None:
    nomeFavorecido = favorecidoCustom.Nome
    orgaoFavorecido = favorecidoCustom.OrgaoId
else:
    nomeFavorecido = OrdemServico.Favorecido.Nome
    orgaoFavorecido = OrdemServico.Favorecido.OrgaoId
scr = Orgao.Carrega(orgaoFavorecido)
gestor = scr.Gestor
countLoop = 0
while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Gerência Executiva") and countLoop < 6):
    if gestor['CARGO_FUNCIONAL'].ToString() == "SUPERINTENDENTE":
        gestor = gestor
        break
    else:
        gestor = gestor.Orgao.OrgaoPai.Gestor
Atores.Adiciona(gestor, "Superintendente do Favorecido Cobra" + OrdemServico.Cliente.ToString())
```

## Superintendente SCR_TODOS_RH
```python
idSrc = DB.ExecuteScalar("select id_orgao from orgao where sigla = '"+ OrdemServico["SCR_TODOS_RH"].ToString() +"' ")
orgao = Orgao.Carrega(Convert.ToInt32(idSrc))
if orgao != None:
    gestor = orgao.Gestor
    perfil = gestor.PerfilCliente
    countLoop = 0
    while ((gestor.Orgao.OrgaoPai.Gestor.PerfilCliente == None) or (gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Diretoria" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Presidência" and gestor.Orgao.OrgaoPai.Gestor.PerfilCliente.Descricao.ToString() != "Gerência Executiva") and countLoop < 6):
        gestor = gestor.Orgao.OrgaoPai.Gestor
        countLoop = countLoop + 1
    if (countLoop >= 6):
        Utils.LogError("SAIDA DO LOOP - PAPEL SUPERINTENDENTE", "ERROR")
    if gestor['CARGO_FUNCIONAL'].ToString() == "SUPERINTENDENTE":
        gestor = gestor
    else:
        scr = Orgao.Carrega("Sigla", "3000003200")
        gestor = scr.Gestor
        Atores.Adiciona(gestor, "Gerente Executivo GEPES em nome de Gerente Executivo UOR")
    Atores.Adiciona(gestor, "Superintendente UOR")
```

## Superior Imediato do Responsável
```python
gestor = OrdemServico.Responsavel.Orgao.OrgaoPai.Gestor
Utils.LogError(gestor.ToString(), "erro")
Atores.Adiciona(gestor, "Superior imediato de " + OrdemServico.Responsavel.ToString())
```

## Supervisor de estagiário
```python
favorecido = Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom("FAVORECIDO_MONITOR")))
if favorecido != None:
    Atores.Adiciona(favorecido, "Favorecido")
```

## Time Desenvolvimento GESAP
```python
sql = "SELECT PESSOA.NOME, PESSOA.ID_PESSOA, ORGAO.DESCRICAO FROM ORGAO INNER JOIN PESSOA ON PESSOA.ID_ORGAO = ORGAO.ID_ORGAO WHERE (ORGAO.DESCRICAO LIKE '3%9430%' OR ORGAO.DESCRICAO LIKE '3%3402%' OR ORGAO.DESCRICAO LIKE '3%3150%' OR ORGAO.DESCRICAO LIKE '3%3154%' OR ORGAO.DESCRICAO LIKE '3%3341%' OR ORGAO.DESCRICAO LIKE '3%33412%' OR ORGAO.DESCRICAO LIKE '3%3610%' OR ORGAO.DESCRICAO LIKE '3%3611%' OR ORGAO.DESCRICAO LIKE '3%3612%' OR ORGAO.DESCRICAO LIKE '3%3810%') AND PESSOA.ATIVO = 'Sim' AND LOWER(PESSOA.NOME) NOT LIKE '%fila%' ORDER BY PESSOA.NOME ASC"
tabela = DB.ExecuteDataTable(sql)
for i in tabela.Rows:
    pessoa = Pessoa.Carrega(i['ID_PESSOA'])
    Atores.Adiciona(pessoa)
```

## UOR de destino
```python
uor = OrdemServico.GetCustom('UOR_ORIGEM')
num_uor = uor.split(' - ')[0]
gestor = DB.ExecuteDataTable("Select ORGAO.ID_GESTOR From ORGAO O WHERE O.DESCRICAO = '"+num_uor.ToString()+"'")
for gestorPessoa in gestor.Rows:
    gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_GESTOR"]))
    Atores.Adiciona(gestor)
```

## UOR de origem
```python
uor = OrdemServico.GetCustom('UOR_ORIGEM')
num_uor = uor.split(' - ')[0]
pesquisaGestorUOR = DB.ExecuteDataTable("select orgao1.ID_ORGAO_PAI, orgao2.ID_GESTOR from orgao orgao1 inner join orgao orgao2 on orgao1.ID_ORGAO_PAI = orgao2.ID_ORGAO where orgao1.SIGLA ='"+ num_uor.ToString()+"'")
for gestorPessoa in pesquisaGestorUOR.Rows:
    gestor = Pessoa.Carrega(Convert.ToInt32(gestorPessoa["ID_GESTOR"]))
    Atores.Adiciona(gestor)
```

## Vice Presidente CIPA VICE_PRESIDENTE_CIPA
```python
Atores.Adiciona(Pessoa.Carrega(Convert.ToInt32(OrdemServico.GetCustom('VICE_PRESIDENTE_CIPA'))))
```
