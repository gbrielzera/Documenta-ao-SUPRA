# Fluxo: Avaliação Período Experiência - GDP (GDPEXPERIENCIA) — versão 8
Caminho: Fluxos > Gestão de Pessoas - Concurso Versão 8 Avaliação Período Experiência - GDP
XML: `XMLs para teste/Gestão_de_Pessoas_-_Concurso_Versão_8_Avaliação_Período_Experiência_-_GDP.xml` | Supravizio 19.1.1 | SubProcessoId 14157 | DesenhoProcessoId 2103 | ProcessoId 411
Órgão dono: 3000009431 - SETOR DE SUPERVISAO DOS SERVICOS COMPARTILHADOS | Responsável: ADIR CORDEIRO DOS SANTOS FILHO
Classe do subprocesso: CriterioChargeBack=Nenhum; RegraAutorizacao=VisivelSolucionadorResponsavel; AcessoTotalAdmin=true; ReaberturaAutoAtendimento=true; VisibilidadeAutoAtendimento=Cliente; PublicarApontamentosAA=Nunca; PermiteVisualizacaoGestorSubNiveis=true
Serviços: Avaliação de Desempenho (AVALDESEM)

## Grafo do fluxo
- [218450] EventoIntermediarioRegra "" → [218439] Comunicar gestor avaiação 85 dias
- [218446] Tarefa "Realizar e Anexar Avaliação 40 dias" {Gerente SCR_TODOS_RH} → [218436] Verificar e Arquivar Avaliação 40 dias | [218444]  | [218449] 
- [218447] EventoIntermediarioRegra "" → [218448] Comunicar gestor avaiação 85 dias
- [218448] EventoIntermediarioMensagem "Comunicar gestor avaiação 85 dias" → [218445] Realizar e Anexar Avaliação 85 dias
- [218449] EventoIntermediarioRegra "" → [218435] Comunicar gestor avaiação 40 dias
- [218437] LinkInicial "" → [218438] Comunicado Avaliação Experiência
- [218438] EventoIntermediarioMensagem "Comunicado Avaliação Experiência" → [218446] Realizar e Anexar Avaliação 40 dias
- [218432] EventoFinal "Rescisão do contrato de trabalho" → (fim)
- [218433] EventoIntermediarioMensagem "Comunica Gestor abertura de chamdo de rescisão" → [218432] Rescisão do contrato de trabalho
- [218434] EventoIntermediarioMensagem "Comunicar gestor avaiação 40 dias" → [218446] Realizar e Anexar Avaliação 40 dias
- [218435] EventoIntermediarioMensagem "Comunicar gestor avaiação 40 dias" → [218446] Realizar e Anexar Avaliação 40 dias
- [218436] Tarefa "Verificar e Arquivar Avaliação 40 dias" {Fila CSC - Concurso} → [218445] Realizar e Anexar Avaliação 85 dias
- [218439] EventoIntermediarioMensagem "Comunicar gestor avaiação 85 dias" → [218445] Realizar e Anexar Avaliação 85 dias
- [218440] EventoFinal "" → (fim)
- [218441] EventoInicial "" → [218438] Comunicado Avaliação Experiência
- [218442] EventoIntermediarioMensagem "Comunica GEPES - Criar GDP" → [218440] 
- [218443] Tarefa "Verificar Avaliação 85 dias" {Fila CSC - Concurso} → [G53578] Contrato Rescindido?
- [218444] EventoIntermediarioRegra "" → [218434] Comunicar gestor avaiação 40 dias
- [218445] Tarefa "Realizar e Anexar Avaliação 85 dias" {Gerente SCR_TODOS_RH} → [218443] Verificar Avaliação 85 dias | [218447]  | [218450] 
- [G53578] Gateway "Contrato Rescindido?" → «Não» [218442] Comunica GEPES - Criar GDP | «Sim» [218433] Comunica Gestor abertura de chamdo de rescisão

## Gateways
### [G53578] Contrato Rescindido? (DataBasedExclusiveDecision)
**ExpressaoComparacaoDecision**
```python
OrdemServico.GetCustom("COMBOBOX")
```
- alternativa → [218442] Comunica GEPES - Criar GDP: OperadorDecision=Equal; ReferenciaDecision=Não; SequenciaAvaliacao=0
**ValorComparacaoDecision**
```python
'Continuado'
```
- alternativa → [218433] Comunica Gestor abertura de chamdo de rescisão: OperadorDecision=Equal; ReferenciaDecision=Sim; SequenciaAvaliacao=1
**ValorComparacaoDecision**
```python
'Rescindido'
```

## Atividades

### [218450] EventoIntermediarioRegra ""
Config: MaximoExecucao=1
**Regra**
```python
DateTime.AddDays(OrdemServico["DATA_POSSE"], 80) == DateTime.Now.Date
```

### [218446] Tarefa "Realizar e Anexar Avaliação 40 dias"
Responsável: Gerente SCR_TODOS_RH (papel 584)
- Operação PR0004 Associar Itens Configuração: Nome=AVALIACAO45
  - anexo "Avaliação de desempemho 40 dias" classes: Avaliação de Desempenho — RequeridoInicial=true

### [218447] EventoIntermediarioRegra ""
Config: MaximoExecucao=1
**Regra**
```python
DateTime.AddDays(OrdemServico["DATA_POSSE"], 85) == DateTime.Now.Date
```

### [218448] EventoIntermediarioMensagem "Comunicar gestor avaiação 85 dias"
Destinatário: Gerente SCR_TODOS_RH (papel 584)
Config: ListaDestinatarios=desenvolvimentoprofissional@bbts.com.br
ModeloComunicado: Comunicado Cesec - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
nomeGestor = DB.ExecuteScalar("select p.nome FROM orgao o inner join pessoa p on o.ID_GESTOR = p.id_pessoa WHERE SIGLA ='"+OrdemServico["SCR_TODOS_RH"].ToString()+"'")


dataAvaliacao = DateTime.AddDays(OrdemServico["DATA_POSSE"], 85)

Mensagem.Assunto = "Avaliação Experiência 85 dias " + OrdemServico["CSC_NOME_COMPLETO"] + " Cargo: " + OrdemServico["CSC_CARGO_FUNCAO"]

Mensagem.Complemento1 = "Prezado(a) " + nomeGestor.ToString() + ",<br><br>Gostaríamos de lembrá-lo(a) de realizar a segunda e última avaliação de desempenho do(a) novo(a) colaborador(a) " + OrdemServico["CSC_NOME_COMPLETO"] + ", antes da efetivação do contrato por prazo indeterminado na BB Tecnologia e Serviços.<br><br>De acordo com a NI139 - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA, a avaliação deve ser realizada no 85º dia de contrato.<br><br>Nessa avaliação, é importante analisar se houve progresso desde a primeira avaliação, realizada aos 40 dias, observando aspectos como a assimilação dos valores e cultura da empresa, a adaptação às atividades e ao ambiente de trabalho, a colaboração com a equipe, o interesse em aprendizado contínuo e o alcance dos objetivos propostos.<br><br>Assim, é primordial oferecer um feedback construtivo, reconhecendo os pontos positivos e apontando áreas de melhoria. É essencial conduzir essa avaliação de forma objetiva e detalhada, visando fundamentar futuras ações e decisões.<br><br>Após concluir a avaliação, solicitamos que anexe o formulário FQ139-001 assinado por você e pelo(a) colaborador(a) ao chamado número <b>"+ OrdemServico.Numero.ToString() + "</b> e o encaminhe para o e-mail convocacao@bbts.com.br para arquivamento no dossiê do(a) colaborador(a).<br><br>Dados do Colaborador(a):<br><br>- Data de posse: " + OrdemServico["DATA_POSSE"].ToString('dd/MM/yyyy') + "<br>- Matrícula: " + OrdemServico["CSC_MATRICULA"] + "<br><br>Por favor, utilize o formulário FQ139-001 Formulário - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA para a avaliação do contrato de experiência conforme as seguintes diretrizes:<br><br>- NI139 - Normas Internas - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br>- PRO139 - Procedimento Operacional - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br><br>Estes documentos estão disponíveis na nossa intranet na seção 'Documentos Corporativos/Normas/Série 1' e podem fornecer o suporte necessário para uma condução adequada deste processo.<br><br>Contamos com sua colaboração para garantir o cumprimento destas diretrizes e prazos.<br><br>Atenciosamente,<br><br>"
```

### [218449] EventoIntermediarioRegra ""
Config: MaximoExecucao=1
**Regra**
```python
DateTime.AddDays(OrdemServico["DATA_POSSE"], 35) == DateTime.Now.Date
```

### [218437] LinkInicial ""
Config: TipoMensagem=MensagemProcesso
- Operação PR0001 Preencher Campos
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - DATA_POSSE "Data da Posse" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_POSSE] obrigatório
  - CARGO_DOTA "Cargo" [TextBox String → CP_ORDEM_SERVICO.CARGO_DOTA] obrigatório
  - SCR_TODOS_RH "UOR Movimentação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
- Associação de subprocesso: AssociacaoId=1111; FraseAssociacao=Convocação -->> Avaliação Experiência; Nome=CONVOCAEXP

### [218438] EventoIntermediarioMensagem "Comunicado Avaliação Experiência"
Destinatário: Gerente SCR_TODOS_RH (papel 584)
ModeloComunicado: Comunicado Cesec - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
nomeGestor = DB.ExecuteScalar("select p.nome FROM orgao o inner join pessoa p on o.ID_GESTOR = p.id_pessoa WHERE SIGLA ='"+OrdemServico["SCR_TODOS_RH"].ToString()+"'")


Mensagem.Assunto = "Avaliação Experiência 40 e 85 dias " + OrdemServico["CSC_NOME_COMPLETO"] + " Cargo: " + OrdemServico["CSC_CARGO_FUNCAO"]

Mensagem.Complemento1 = "Prezado(a) " + nomeGestor.ToString() + ",<br><br> Solicitamos realizar a avaliação do(a) novo(a) colaborador(a) " + OrdemServico["CSC_NOME_COMPLETO"] + ", que se encontra em contrato de experiência, conforme cronograma abaixo:<br><br>- No 40º dia do contrato, visando avaliar o desempenho e propor possíveis ajustes, se necessário;<br>- No 85º dia, para avaliar o desempenho no período e fundamentar a decisão de permanência ou não do empregado na BB Tecnologia e Serviços;<br><br>Ressaltamos que, conforme a NI139 - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA e o PRO139 - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA, é <b>mandatória</b> a realização de avaliações nos períodos acima informados,<b>totalizando duas avaliações ao longo do contrato de experiência</b>.<br><br>Para a condução dessas avaliações, é necessário utilizar o formulário FQ139-001 - Formulário - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA o qual deverá ser impresso pelo gestor e apresentado ao empregado recém-admitido até o 5° dia útil após sua posse, para que tenha conhecimento do instrumento de avaliação.<br><br>Todas as documentações mencionadas estão disponíveis na intranet, dentro da seção 'Documentos corporativos/Normas/Série 1'.<br><br>Contamos com sua colaboração para garantir o cumprimento destas diretrizes e prazos.<br><br>Atenciosamente,<br><br>"
```

### [218432] EventoFinal "Rescisão do contrato de trabalho"

### [218433] EventoIntermediarioMensagem "Comunica Gestor abertura de chamdo de rescisão"
Destinatário: Gerente SCR_TODOS_RH (papel 584)
ModeloComunicado: Comunicado Cesec - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
from Venki.Supravizio.Recurso.Custom import Contrato
from Venki.Supravizio.Recurso.Custom import Empresa
from Venki.Supravizio.Recurso.Custom import Pessoa
nomeGestor = DB.ExecuteScalar("select p.nome FROM orgao o inner join pessoa p on o.ID_GESTOR = p.id_pessoa WHERE SIGLA ='"+OrdemServico["SCR_TODOS_RH"].ToString()+"'")


Mensagem.Assunto = "Rescisão Contrato de Experiência " + OrdemServico["CSC_NOME_COMPLETO"] + " Cargo: " + OrdemServico["CSC_CARGO_FUNCAO"]

Mensagem.Complemento1 = "Prezado(a) " + nomeGestor.ToString() + ",<br><br>Solicitamos abrir chamado de Recição de contrato a pedido da empresa no caminho 18.01. Gestão de Pessoas - Ascensão e Movimentação de Pessoas/Rescisão a pedido da Empresa, com o objetivo de iniciar os procedimentos necessários para o efetivo andamento dessa solicitação.<br><br>Contamos com sua colaboração para garantir o cumprimento destas diretrizes e prazos.<br><br>Atenciosamente,<br><br>"
```

### [218434] EventoIntermediarioMensagem "Comunicar gestor avaiação 40 dias"
Destinatário: Gerente SCR_TODOS_RH (papel 584)
Config: NomeRemetente=desenvolvimentoprofissional@bbts.com.br
ModeloComunicado: Comunicado Cesec - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
nomeGestor = DB.ExecuteScalar("select p.nome FROM orgao o inner join pessoa p on o.ID_GESTOR = p.id_pessoa WHERE SIGLA ='"+OrdemServico["SCR_TODOS_RH"].ToString()+"'")

dataAvaliacao = DateTime.AddDays(OrdemServico["DATA_POSSE"], 40)

Mensagem.Assunto = "Avaliação Experiência 40 dias " + OrdemServico["CSC_NOME_COMPLETO"] + " Cargo: " + OrdemServico["CSC_CARGO_FUNCAO"]

Mensagem.Complemento1 = "Prezado(a) " + nomeGestor.ToString() + ",<br><br>Gostaríamos de lembrá-lo(a) de realizar a primeira avaliação de desempenho do(a) novo(a) colaborador(a) " + OrdemServico["CSC_NOME_COMPLETO"] + ", que atualmente está em contrato de experiência.<br><br>De acordo com a NI139 - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA, a avaliação deve ser realizada no 40º dia de contrato.<br><br>Além de ser uma etapa <b>obrigatória</b>, é um momento importante para avaliar o desempenho do(a) colaborador(a) e identificar possíveis ajustes necessários. É essencial conduzir essa avaliação de forma objetiva e detalhada, visando fundamentar futuras ações e decisões.<br><br>Assim, é primordial oferecer um feedback construtivo, reconhecendo os pontos positivos e apontando áreas de melhoria. Esse feedback é essencial para o desenvolvimento profissional do(a) colaborador(a) e para manter um ambiente de trabalho saudável e produtivo.<br><br>Após concluir a avaliação, solicitamos que anexe o formulário FQ139-001 assinado por você e pelo(a) colaborador(a) ao chamado número <b>"+ OrdemServico.Numero.ToString() + "</b> e o encaminhe para o e-mail convocacao@bbts.com.br para arquivamento no dossiê do(a) colaborador(a).<br><br>Dados do Colaborador(a):<br><br>- Data de posse: " + OrdemServico["DATA_POSSE"].ToString('dd/MM/yyyy') + "<br>- Matrícula: " + OrdemServico["CSC_MATRICULA"] + "<br><br>Por favor, utilize o formulário FQ139-001 Formulário - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA para a avaliação do contrato de experiência conforme as seguintes diretrizes:<br><br>- NI139 - Normas Internas - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br>- PRO139 - Procedimento Operacional - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br><br>Estes documentos estão disponíveis na nossa intranet na seção 'Documentos Corporativos/Normas/Série 1' e podem fornecer o suporte necessário para uma condução adequada deste processo.<br><br>Contamos com sua colaboração para garantir o cumprimento destas diretrizes e prazos.<br><br>Atenciosamente,<br>"
```

### [218435] EventoIntermediarioMensagem "Comunicar gestor avaiação 40 dias"
Destinatário: Gerente SCR_TODOS_RH (papel 584)
ModeloComunicado: Comunicado Cesec - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
nomeGestor = DB.ExecuteScalar("select p.nome FROM orgao o inner join pessoa p on o.ID_GESTOR = p.id_pessoa WHERE SIGLA ='"+OrdemServico["SCR_TODOS_RH"].ToString()+"'")

dataAvaliacao = DateTime.AddDays(OrdemServico["DATA_POSSE"], 40)

Mensagem.Assunto = "Avaliação Experiência 40 dias " + OrdemServico["CSC_NOME_COMPLETO"] + " Cargo: " + OrdemServico["CSC_CARGO_FUNCAO"]

Mensagem.Complemento1 = "Prezado(a) " + nomeGestor.ToString() + ",<br><br>Gostaríamos de lembrá-lo(a) de que está se aproximando a data para a realização da primeira avaliação de desempenho do(a) novo(a) colaborador(a) " + OrdemServico["CSC_NOME_COMPLETO"] + ", que atualmente está em contrato de experiência.<br><br>De acordo com a NI139 - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA, a avaliação deve ser realizada no 40º dia de contrato, prevista para o dia " + dataAvaliacao.ToString('dd/MM/yyyy') + ".<br><br>Além de ser uma etapa <b>obrigatória</b>, é um momento importante para avaliar o desempenho do(a) colaborador(a) e identificar possíveis ajustes necessários. É essencial conduzir essa avaliação de forma objetiva e detalhada, visando fundamentar futuras ações e decisões.<br><br>Assim, é primordial oferecer um feedback construtivo, reconhecendo os pontos positivos e apontando áreas de melhoria. Esse feedback é essencial para o desenvolvimento profissional do(a) colaborador(a) e para manter um ambiente de trabalho saudável e produtivo.<br><br>Após concluir a avaliação, solicitamos que anexe o formulário FQ139-001 assinado por você e pelo(a) colaborador(a) ao chamado número "+ OrdemServico.Numero.ToString() + " e o encaminhe para o e-mail convocacao@bbts.com.br para arquivamento no dossiê do(a) colaborador(a).<br><br>Dados do Colaborador(a):<br><br>- Data de posse: " + OrdemServico["DATA_POSSE"].ToString('dd/MM/yyyy') + "<br>- Matrícula: " + OrdemServico["CSC_MATRICULA"] + "<br><br>Por favor, utilize o formulário FQ139-001 Formulário - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA para a avaliação do contrato de experiência conforme as seguintes diretrizes:<br><br>- NI139 - Normas Internas - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br>- PRO139 - Procedimento Operacional - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br><br>Estes documentos estão disponíveis na nossa intranet na seção 'Documentos Corporativos/Normas/Série 1' e podem fornecer o suporte necessário para uma condução adequada deste processo.<br><br>Contamos com sua colaboração para garantir o cumprimento destas diretrizes e prazos.<br><br>Atenciosamente,<br>"
```

### [218436] Tarefa "Verificar e Arquivar Avaliação 40 dias"
Responsável: Fila CSC - Concurso (papel 511)

### [218439] EventoIntermediarioMensagem "Comunicar gestor avaiação 85 dias"
Destinatário: Gerente SCR_TODOS_RH (papel 584)
ModeloComunicado: Comunicado Cesec - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
nomeGestor = DB.ExecuteScalar("select p.nome FROM orgao o inner join pessoa p on o.ID_GESTOR = p.id_pessoa WHERE SIGLA ='"+OrdemServico["SCR_TODOS_RH"].ToString()+"'")


dataAvaliacao = DateTime.AddDays(OrdemServico["DATA_POSSE"], 85)

Mensagem.Assunto = "Avaliação Experiência 85 dias " + OrdemServico["CSC_NOME_COMPLETO"] + " Cargo: " + OrdemServico["CSC_CARGO_FUNCAO"]

Mensagem.Complemento1 = "Prezado(a) " + nomeGestor.ToString() + ",<br><br>Gostaríamos de lembrá-lo(a) de que está se aproximando a data da segunda e última avaliação de desempenho do(a) novo(a) colaborador(a) " + OrdemServico["CSC_NOME_COMPLETO"] + ", antes da efetivação do contrato por prazo indeterminado na BB Tecnologia e Serviços.<br><br>De acordo com a NI139 - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA, a avaliação deve ser realizada no 85º dia de contrato, prevista para "+ dataAvaliacao.ToString('dd/MM/yyyy') +".<br><br>Nessa avaliação, é importante analisar se houve progresso desde a primeira avaliação, realizada aos 40 dias, observando aspectos como a assimilação dos valores e cultura da empresa, a adaptação às atividades e ao ambiente de trabalho, a colaboração com a equipe, o interesse em aprendizado contínuo e o alcance dos objetivos propostos.<br><br>Assim, é primordial oferecer um feedback construtivo, reconhecendo os pontos positivos e apontando áreas de melhoria. É essencial conduzir essa avaliação de forma objetiva e detalhada, visando fundamentar futuras ações e decisões.<br><br>Após concluir a avaliação, solicitamos que anexe o formulário FQ139-001 assinado por você e pelo(a) colaborador(a) ao chamado número "+ OrdemServico.Numero.ToString() + " e o encaminhe para o e-mail convocacao@bbts.com.br para arquivamento no dossiê do(a) colaborador(a).<br><br>Dados do Colaborador(a):<br><br>- Data de posse: " + OrdemServico["DATA_POSSE"].ToString('dd/MM/yyyy') + "<br>- Matrícula: " + OrdemServico["CSC_MATRICULA"] + "<br><br>Por favor, utilize o formulário FQ139-001 Formulário - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA para a avaliação do contrato de experiência conforme as seguintes diretrizes:<br><br>- NI139 - Normas Internas - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br>- PRO139 - Procedimento Operacional - AVALIAÇÃO DO CONTRATO DE EXPERIÊNCIA.<br><br>Estes documentos estão disponíveis na nossa intranet na seção 'Documentos Corporativos/Normas/Série 1' e podem fornecer o suporte necessário para uma condução adequada deste processo.<br><br>Contamos com sua colaboração para garantir o cumprimento destas diretrizes e prazos.<br><br>Atenciosamente,<br><br>"
```

### [218440] EventoFinal ""

### [218441] EventoInicial ""
TipoSolicitacao: 18.01. Gestão de Pessoas - Ascensão e Movimentação de Pessoas
- Operação PR0001 Preencher Campos
  - CARGO_DOTA "Cargo" [TextBox String → CP_ORDEM_SERVICO.CARGO_DOTA] obrigatório
  - CSC_MATRICULA "Matrícula" [TextBox String → CPE_CSC.CSC_MATRICULA] obrigatório
**CSC_MATRICULA.ScriptModificado**
```python
if Formulario["CSC_MATRICULA"].Valor != None and Formulario["CSC_MATRICULA"].Valor != "":

    nome = ""
    cargo = ""
    matricula = Formulario["CSC_MATRICULA"].Valor
    data_admissao = ""
    UOR = ""
    
    
    lista = Utils.ExecuteDataTable(" SELECT substr(f.cargo, instr(f.cargo, '|') + 1) AS cargo, f.nome, to_char(f.data_de_admissao, 'DD/MM/YYYY') AS data_de_admissao,GESTOR_POSICAO,substr(f.ORGANIZACAO, 0, instr(f.ORGANIZACAO, '|') -1) AS UOR FROM cad_funcionario_v f WHERE matricula  = '"+ matricula.ToString() +"' ")

    for linha in lista.Rows:
        cargo           = linha["CARGO"].ToString()
        nome            = linha["NOME"].ToString()
        data_admissao   = linha["DATA_DE_ADMISSAO"].ToString()
        UOR             = linha["UOR"].ToString()
        

    #Formulario["SC_CARGO"].Itens = cargo
    Formulario["CARGO_DOTA"].Valor = cargo
    Formulario["CSC_NOME_COMPLETO"].Valor = nome
    Formulario["DATA_POSSE"].Valor = data_admissao
    #Formulario["SC_CARGO"].Habilitado = False    
    Formulario["CSC_MATRICULA"].Habilitado = False    
    Formulario["DATA_POSSE"].Habilitado = False    
    Formulario["SCR_TODOS_RH"].Valor = UOR
    Formulario["SCR_TODOS_RH"].Habilitado = False
```
  - CSC_NOME_COMPLETO "Nome Completo" [TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO] obrigatório
  - DATA_POSSE "Data da Posse" [DatePicker DateTime → CP_ORDEM_SERVICO.DATA_POSSE] obrigatório
  - SCR_TODOS_RH "UOR Movimentação" [DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH] obrigatório
- ClientesAutorizados:
  - PapelProcessoId=42472; PapelAutorizado=Supravizio - Administração
  - PapelProcessoId=42473; PapelAutorizado=Pessoas Gepes

### [218442] EventoIntermediarioMensagem "Comunica GEPES - Criar GDP"
Config: ListaDestinatarios=desenvolvimentoprofissional@bbts.com.br;concurso@bbts.com.br
ModeloComunicado: Comunicado Cesec - Concurso
Corpo do comunicado: Complemento1 
 Complemento2 
 Complemento3 
 Complemento4 
 Complemento5
**ScriptEvento**
```python
Mensagem.Assunto = "Criar GDP - Fim contrato de Experiência " + OrdemServico["CSC_NOME_COMPLETO"] + " Cargo: " + OrdemServico["CSC_CARGO_FUNCAO"]

Mensagem.Complemento1 = "Prezados(as),<br><br>Gostaríamos de informar que o contrato de experiência do novo colaborador, "+ OrdemServico["CSC_NOME_COMPLETO"] + ", foi encerrado. Por favor, solicitamos a criação da GPD para o ciclo atual.<br><br>Atenciosamente,<br><br>"
```

### [218443] Tarefa "Verificar Avaliação 85 dias"
Responsável: Fila CSC - Concurso (papel 511)

### [218444] EventoIntermediarioRegra ""
Config: MaximoExecucao=1
**Regra**
```python
DateTime.AddDays(OrdemServico["DATA_POSSE"], 40) == DateTime.Now.Date
```

### [218445] Tarefa "Realizar e Anexar Avaliação 85 dias"
Responsável: Gerente SCR_TODOS_RH (papel 584)
**ScriptFormCarregado**
```python
Formulario["COMBOBOX"].Itens = "Rescindido;Continuado"
```
- Operação PR0001 Preencher Campos
  - COMBOBOX "Após a 2ª avaliação no período de experiênica o contrato do colaborador será?" [DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX] obrigatório
- Operação PR0004 Associar Itens Configuração: Nome=AVALIACAO90
  - anexo "Avaliação de desempemho 85 dias" classes: Avaliação do Gestor — RequeridoInicial=true

## Papéis usados
### papel 584: Gerente SCR_TODOS_RH
Tipo=Script
**ScriptSelecaoAtores**
```python
from Venki.Supravizio.Recurso.Custom import Orgao
from Venki.Supravizio.Processo.Custom import Ator
id = DB.ExecuteScalar("select id_orgao from orgao where sigla = '"+ OrdemServico["SCR_TODOS_RH"].ToString() +"'")

idScr = Convert.ToInt32(id)
scr = Orgao.Carrega(idScr)
if (scr != None):
    pessoa = scr.Gestor
    if (pessoa != None):
        Atores.Adiciona(pessoa)
```
### papel 511: Fila CSC - Concurso
Tipo=RelacaoPessoas | pessoas: Fila CSC - Concurso

## Campos customizados usados (definição global)

### CSC_MATRICULA — Matrícula
TextBox String → CPE_CSC.CSC_MATRICULA

### CSC_NOME_COMPLETO — Nome Completo
TextBox String(500) → CPE_CSC.CSC_NOME_COMPLETO

### DATA_POSSE — Data da Posse
DatePicker DateTime → CP_ORDEM_SERVICO.DATA_POSSE

### CARGO_DOTA — Cargo
TextBox String → CP_ORDEM_SERVICO.CARGO_DOTA

### SCR_TODOS_RH — UOR Movimentação
DropDownList String → CP_ORDEM_SERVICO.SCR_TODOS_RH
Descrição: SCR Movimentação
**LookupScript**
```python
###PGESV###
Itens = DB.ExecuteDataTable("SELECT to_char(SCR) as SCR, NOME FROM VW_SV_CAD_SCR_COB_GL_CENTRO");
```

### COMBOBOX — Combo Box
DropDownList String(900) → CP_ORDEM_SERVICO.COMBOBOX
Itens: Órtese;Órtese Dentária; Prótese;Recurso para Saúde

## Biblioteca de scripts referenciada
teste, teste
(fonte em catalogo/biblioteca/<Nome>.py)
