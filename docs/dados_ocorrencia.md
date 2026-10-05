# OCORRENCIA

Caminho: Customização > Modelo de dados > Processo > OCORRENCIA

Ocorrências de Processos

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Número sequencial gerado automaticamente pelo sistema para Identificar um Ocorrência | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_ATIVIDADE** | Identificador da Atividade corrente da Ocorrência. | int | number(6,0) | Não |
| **ID_DESENHO_PROCESSO** | Identificador da versão de Processo da Ocorrência. | int | number(6,0) | Não |
| **ASSUNTO** | Texto resumido que descreve o assunto da ocorrência. | varchar(500) | varchar(500) | Não |
| **ID_CORRENCIA_PRIN** | Identificador da ocorrência principal correspondente ao macro-fluxo que invocou a ocorrência. | int | number(6,0) | Sim |
| **ID_CLASSE_SUB_PROC** | Identificador do tipo de Subprocesso da ocorrência. Este tipo se refere a um Subprocesso definido na versão de processo também associada a ocorrência e define os fluxos e responsabilidade de processo. | int | number(6,0) | Não |
| **DATA_HORA_CRIACAO** | Data e hora de criação da ocorrência. Esta data é preenchida automaticamente pelo sistema e não pode ser modificada pelo usuário. | datetime | date | Não |
| **DATA_HORA_SOL** | Data e hora de solicitação da ocorrência. Esta data é preenchida automaticamente pelo sistema usando a Data/hora corrente e pode ser modificada pelo usuário (se este possui autorização para modificação de dados). | datetime | date | Não |
| **DATA_HORA_INI_PREV** | Data e hora de início previsto de atendimento. O início previsto pode sofrer diversas modificações no decorrer do atendimento. | datetime | date | Sim |
| **DATA_HORA_FIM_PREV** | Data e hora prevista para términdo do atendimento. A previsão de fim pode sofrer diversas modificações no decorrer do atendimento. | datetime | date | Sim |
| **DATA_HORA_INI_REAL** | Data/hora início real | datetime | date | Sim |
| **DATA_HORA_FIM_REAL** | Data/hora fim real | datetime | date | Sim |
| **DATA_HORA_FIM_PREVO** | Data/hora original de finalização prevista | datetime | date | Sim |
| **ID_RESPONSAVEL** | Identificador do Responsável pela ocorrência. A mudança de responsabilidade pode ocorrer em virtude de encaminhamentos ou automatismo de processo (segundo papéis definidos em atividades). | int | number(6,0) | Não |
| **ID_CLIENTE** | Identificador da pessoa que solicitou o serviço. | int | number(6,0) | Não |
| **SITUACAO** | Situação da ocorrência. | varchar(250) | varchar(250) | Não |
| **ID_GRUPO_TRABALHO** | Identificador do GrupoTrabalho responsável pela ocorrência. Assim como o campo Responsável o Grupo de trabalho é mantido pelo sistema quando executada a função de encaminhamento ou segundo papel definido em atividades do processo. | int | number(6,0) | Não |
| **DATA_HORA_RESP** | Data/hora em que foi definido o Responsável corrente da ocorrência. | datetime | date | Não |
| **MOTIVO_CANCELAMENTO** | Texto descrevendo motivo pelo qual o registro foi cancelado. | varchar(500) | varchar(500) | Sim |
| **ID_FINALIZADOR** | Identificador da pessoa que finalizou a ocorrência. | int | number(6,0) | Sim |
| **CLASSE_NEGOCIO** | Classe de Negócio que implementa a Token. Este valor é alimentado automaticamente pelo sistema assim que o item é Classficado. | varchar(250) | varchar(250) | Não |
| **ID_RESP_INICIAL** | Identificador do Solucionador que foi o primeiro responsável pela Ocorrência. | int | number(6,0) | Não |
| **ID_GRUPO_TRAB_INICIAL** | Identificador do Grupo de Trabalho inicial | int | number(6,0) | Não |
| **NUMERO** | Número formatado da Ocorrência | varchar(50) | varchar(50) | Não |
| **ESFORCO_ESTIMADO** | Esforço (em horas) estimado para finalização do serviço. | int | number(6,0) | Sim |
| **JUSTIFICA_ESFORCO** | Justificativa para valor de Esforço estimado | varchar(500) | varchar(500) | Sim |
| **DATA_HORA_INI_PLAN** | Data e hora de início planejado | datetime | date | Sim |
| **DATA_HORA_FIM_PLAN** | Data e hora de fim de planejamento | datetime | date | Sim |
| **ID_DESENHO_PROC_INI** | Identificador da Versão de Processo inicialmente atribuída a Ocorrência. | int | number(6,0) | Não |
| **ID_CLASSE_SUB_PROC_INI** | Identificador do Tipo de Subprocesso inicialmente atribuído a Ocorrência. | int | number(6,0) | Não |
| **ID_OCORR_PAI** | Identificador da ocorrência que invocou o processo da ocorrência. Este campo pode ser diferente de OcorrenciaPrincipal se existirem mais de dois níveis de chamada. | int | number(6,0) | Sim |
| **ID_ORGAO_CLIENTE** | Identificador do Orgao Cliente | int | number(6,0) | Não |
| **REFERENCIA_CIRCULAR** | Indica que em algum momento da execução do processo ocorrêu um Loop infinito caracterizando referência circular entre as atividades de processos. | char(3) | char(3) | Não |
| **DATA_HORA_ULT_ATUA** | Data e hora da última atualização | datetime | date | Não |
| **ID_USU_AUT** | Identificador do usuário autenticado | int | number(6,0) | Sim |
| **PUBLICA_TIMESHEET_AA** | Caso o subprocesso permita que sejam publicados os apontamentos (PublicacaoApontamentosAutoAtendimento diferente de Nunca ou Sempre), sendo verdadeira esta propriedade seram exibidos os apontamentos no Autoatendimento. | char(3) | char(3) | Não |
| **PERM_RETOM_RESP** | Indica que é permitido ao último responsável retormar responsabilidade de uma ocorrência encaminhada para outro solucionador, seja o encaminhamento manual ou automático por configuração de processos. | char(3) | char(3) | Não |
| **ID_SUB_PROCESSO** | Identificador do SubProcesso corrente da ocorrência. Esta informação pode ser obtida também pelo relacionamento da entidade Atividade e está aqui por questão de desempenho da aplicação. | int | number(6,0) | Não |

Tabelas referenciadas por OCORRENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **OCORRENCIA** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROC_INI \| |
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **OCORRENCIA** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROC \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **OCORRENCIA** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **OCORRENCIA** \| \|---\|---\| \| ID_PESSOA \| ID_FINALIZADOR \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **OCORRENCIA** \| \|---\|---\| \| ID_PESSOA \| ID_CLIENTE \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **OCORRENCIA** \| \|---\|---\| \| ID_PESSOA \| ID_RESP_INICIAL \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **OCORRENCIA** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **OCORRENCIA** \| \|---\|---\| \| ID_PESSOA \| ID_USU_AUT \| |
| [DESENHO_PROCESSO](dados_desenho_processo) | \| **DESENHO_PROCESSO** \| **OCORRENCIA** \| \|---\|---\| \| ID_DESENHO_PROCESSO \| ID_DESENHO_PROCESSO \| |
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **OCORRENCIA** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRAB_INICIAL \| |
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **OCORRENCIA** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [DESENHO_PROCESSO](dados_desenho_processo) | \| **DESENHO_PROCESSO** \| **OCORRENCIA** \| \|---\|---\| \| ID_DESENHO_PROCESSO \| ID_DESENHO_PROC_INI \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_CORRENCIA_PRIN \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORR_PAI \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **OCORRENCIA** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO_CLIENTE \| |
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **OCORRENCIA** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

Tabelas que dependem de OCORRENCIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **OCORRENCIA** \| \|---\|---\| \| ID_CORRENCIA_PRIN \| ID_OCORRENCIA \| |
| [TIME_SHEET](dados_time_sheet) | \| **TIME_SHEET** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORR_PAI \| ID_OCORRENCIA \| |
| [APONT_RESPONSAVEL](dados_apont_responsavel) | \| **APONT_RESPONSAVEL** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [APONT_OCORRENCIA](dados_apont_ocorrencia) | \| **APONT_OCORRENCIA** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [ASSOCIACAO_OCORR](dados_associacao_ocorr) | \| **ASSOCIACAO_OCORR** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORR_FONTE \| ID_OCORRENCIA \| |
| [ASSOCIACAO_OCORR](dados_associacao_ocorr) | \| **ASSOCIACAO_OCORR** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORR_ALVO \| ID_OCORRENCIA \| |
| [ACAO_GAP](dados_acao_gap) | \| **ACAO_GAP** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCOR_PLANO \| ID_OCORRENCIA \| |
| [TESTE_CONTROLE](dados_teste_controle) | \| **TESTE_CONTROLE** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [EVENTO_OCORR](dados_evento_ocorr) | \| **EVENTO_OCORR** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [ATOR](dados_ator) | \| **ATOR** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [EXECUCAO_ATIVIDADE](dados_execucao_atividade) | \| **EXECUCAO_ATIVIDADE** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [ASSUNTO_APROVACAO](dados_assunto_aprovacao) | \| **ASSUNTO_APROVACAO** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [ITEM_OCORRENCIA](dados_item_ocorrencia) | \| **ITEM_OCORRENCIA** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [EXECUCAO_GATEWAY](dados_execucao_gateway) | \| **EXECUCAO_GATEWAY** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [GAP](dados_gap) | \| **GAP** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [EXECUCAO_ACAO](dados_execucao_acao) | \| **EXECUCAO_ACAO** \| **OCORRENCIA** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |

**Exemplo 1: join com a tabela CLASSE_SUB_PROCESSO**

```
select OCORRENCIA.*, CLASSE_SUB_PROCESSO.DESCRICAO
from OCORRENCIA, CLASSE_SUB_PROCESSO
where OCORRENCIA.ID_CLASSE_SUB_PROC_INI = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```

**Exemplo 2: join com a tabela CLASSE_SUB_PROCESSO**

```
select OCORRENCIA.*, CLASSE_SUB_PROCESSO.DESCRICAO
from OCORRENCIA, CLASSE_SUB_PROCESSO
where OCORRENCIA.ID_CLASSE_SUB_PROC = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```
