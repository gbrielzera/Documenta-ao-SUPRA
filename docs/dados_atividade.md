# ATIVIDADE

Caminho: Customização > Modelo de dados > Processo > ATIVIDADE

Uma Atividade de Processo corresponde a Tarefas, Subprocessos e Eventos de Processos.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Atividade | int | number(6,0) | Não |
| **TIPO** | Indica o Tipo de Atividade que pode ser uma Tarefa ou um Evento | varchar(250) | varchar(250) | Não |
| **ID_SUB_PROCESSO** | Identificador do Subprocesso | int | number(6,0) | Sim |
| **DESCRICAO** | Texto resumido que descreve uma Tarefa, Evento ou chamada de Subprocesso. Dependendo do tipo de objeto este descritivo é exibido no diagrama e no assistente de processos para faciliar o entendimento do fluxo. No caso de eventos intermediários do tipo mensagem este texto é utilizado no assunto do email enviado. | varchar(500) | varchar(500) | Sim |
| **REFERENCIA** | Texto descrevendo detalhes sobre a execução da Atividade. Este texto é exibido no assistente de processos e utilizado na geração de documentação do processo. | text | clob | Sim |
| **REGRA** | Em iniciadores por regra ou temporizador esta fórmula é retornada para identificar o momento de geração de novas ocorrências. Neste caso ele pode retornar um valor lógico indicando que é necessário gerar ocorrências ou uma tabela via comando SQL e, neste último caso, é gerada uma ocorrência para cada linha retornada. Em eventos intermediários utilizamos esta fórmula para retornar um valor lógico indicando que é necessário executar uma transição entre tarefas. | text | clob | Sim |
| **ID_PAPEL_RESPONSAVEL** | Identificador do PapelProcesso associado | int | number(6,0) | Sim |
| **SCRIPT_INICIO** | Script de Event executado quando uma Atividade é Iniciada | text | clob | Sim |
| **SCRIPT_FIM** | Script de Event executado quando uma Atividade é Finalizada | text | clob | Sim |
| **SCRIPT_EVENTO** | Script executado após uma transição de Atividade originada por um Fluxo ou Evento | text | clob | Sim |
| **TIPO_FINALIZACAO** | Tipo de finalização | varchar(250) | varchar(250) | Não |
| **ID_CLASSE_PESQ_SATISF** | Identificador do ClassePesquisaSatisfacao associado | int | number(6,0) | Sim |
| **CHAM_ASSINC** | Indica que não é possível avançar no processo até que o Subprocesso seja finalizado. Se for atribuído o valor falso então o sistema invocará o Subprocesso em questão e em seguida avançará para a próxima atividade automaticamente. | char(3) | char(3) | Não |
| **ID_PROCESSO** | Identificador do Processo associado | int | number(6,0) | Sim |
| **ID_CLASSE_SUB_PROCESSO** | Identificador do Tipo de Subprocesso associado | int | number(6,0) | Sim |
| **ID_ASSOCIACAO** | Identificador do Associacao associado | int | number(6,0) | Sim |
| **MULT_INSTANCIA** | Permite a criação de múltiplas instâncias da Atividade do tipo Subprocesso. | char(3) | char(3) | Não |
| **TIPO_CICLO** | Tipo ciclo | varchar(250) | varchar(250) | Não |
| **CICLO_DIA_HORA** | Hora para execução | int | number(6,0) | Sim |
| **CICLO_MEN_ULT_DIA** | Executar no último dia do mês | char(3) | char(3) | Não |
| **CICLO_MEN_DIA_MES** | Dia do mês para execução | int | number(6,0) | Sim |
| **CICLO_SEM_DIA_SEM** | Dia da semana para execução | varchar(250) | varchar(250) | Não |
| **CICLO_DIA_MINUTO** | Minuto para execução de um Ciclo Diário. | int | number(6,0) | Sim |
| **CICLO_DIA_DOM** | Gera ocorrências no Domingo | char(3) | char(3) | Não |
| **CICLO_DIA_SEG** | Gera ocorrências na Segunda-feira | char(3) | char(3) | Não |
| **CICLO_DIA_TER** | Gera ocorrências na Terça-feira | char(3) | char(3) | Não |
| **CICLO_DIA_QUA** | Gera ocorrências na Quarta-feira | char(3) | char(3) | Não |
| **CICLO_DIA_QUI** | Gera ocorrências na Quinta-feira | char(3) | char(3) | Não |
| **CICLO_DIA_SEX** | Gera ocorrências na Sexta-feira | char(3) | char(3) | Não |
| **CICLO_DIA_SAB** | Gera ocorrências no Sábado | char(3) | char(3) | Não |
| **CICLO_SEM_HOR** | Hora para execução | int | number(6,0) | Sim |
| **CICLO_SEM_MIN** | Minuto para execução | int | number(6,0) | Sim |
| **CICLO_MEN_HOR** | Hora para execução | int | number(6,0) | Sim |
| **CICLO_MEN_MIN** | Minuto para execução | int | number(6,0) | Sim |
| **CICLO_ANO_MES** | Mês para execução | int | number(6,0) | Sim |
| **CICLO_ANO_ULT_DIA** | Executar no último dia do mês | char(3) | char(3) | Não |
| **CICLO_ANO_DIA_MES** | Dia do mês para execução | int | number(6,0) | Sim |
| **CICLO_ANO_HOR** | Hora para execução | int | number(6,0) | Sim |
| **CICLO_ANO_MIN** | Minuto para execução | int | number(6,0) | Sim |
| **CODIGO** | Código utilizado para recuperação de dados sobre a execução da Atividade. Este código pode ser utilizado em scripts para determinar a realização de alguma ação prevista em processo (verificar se algo foi aprovado). O código deve ser único dentro de uma versão do Subprocesso. O código também é uma referência para a cópia de aprovações realizadas durante a reclassificação de versão do processo. | varchar(100) | varchar(100) | Sim |
| **SCRIPT_VALIDACAO** | Script para Validação da Atividade | text | clob | Sim |
| **TRANS_AUTO** | Habilita a transição automática para a próxima Atividade. Esta transição automática ocorre após Aprovações e Finalizações de Subprocessos. | char(3) | char(3) | Não |
| **TEMPO_MIN** | Tempo máximo para início do evento. | int | number(6,0) | Sim |
| **ID_MOTIVO_INTER_SLA** | Identificador do Motivo de interrupção de tempo de atendimento definido em Acordo de Nível de Serviço | int | number(6,0) | Sim |
| **CICLO_MEN_JAN** | Gera ocorrências no mês de Janeiro | char(3) | char(3) | Não |
| **CICLO_MEN_FEV** | Gera ocorrências no mês de Fevereito | char(3) | char(3) | Não |
| **CICLO_MEN_MAR** | Gera ocorrências no mês de Março | char(3) | char(3) | Não |
| **CICLO_MEN_ABR** | Gera ocorrências no mês de Abril | char(3) | char(3) | Não |
| **CICLO_MEN_MAI** | Gera ocorrências no mês de Maio | char(3) | char(3) | Não |
| **CICLO_MEN_JUN** | Gera ocorrências no mês de Junho | char(3) | char(3) | Não |
| **CICLO_MEN_JUL** | Gera ocorrências no mês de Julho | char(3) | char(3) | Não |
| **CICLO_MEN_AGO** | Gera ocorrências no mês de Agosto | char(3) | char(3) | Não |
| **CICLO_MEN_SET** | Gera ocorrências no mês de Setembro | char(3) | char(3) | Não |
| **CICLO_MEN_OUT** | Gera ocorrências no mês de Outubro | char(3) | char(3) | Não |
| **CICLO_MEN_NOV** | Gera ocorrências no mês de Novembro | char(3) | char(3) | Não |
| **CICLO_MEN_DEZ** | Gera ocorrências no mês de Dezembro | char(3) | char(3) | Não |
| **PASS_TODOS_ITENS** | Em chamadas de Subprocessos ou link final todos os Itens anexados na Ordem de Serviço chamadora são atribuídos a nova Ordem de Serviço chamada. | char(3) | char(3) | Não |
| **RET_TODOS_ITENS** | Em chamadas de Subprocessos e link final todos os Itens de Configuração são retornados para a chamadora. | char(3) | char(3) | Não |
| **RELATORIO_OBRIG** | Indica que para avançar para a próxima atividade é necessário preencher um relatório de execução da atividade corrente. | char(3) | char(3) | Não |
| **PERM_REST_PAPEL** | Indica que somente usuários que possuem o papel configurado na atividade podem assumir responsabilidade. | char(3) | char(3) | Não |
| **ID_CONTROLE** | Identificador do(a) Controle associado(a) | int | number(6,0) | Sim |
| **EXIGE_APONTAMENTO** | Exige que o usuário aponte horas trabalhadas na ocorrência. A validação é realizada ao término da atividade. | char(3) | char(3) | Não |
| **PREENCH_MOTIV_REP** | Preenche o motivo de Cancelamento com o(s) motivo(s) de reprovação das aprovações executadas no processo. São desconsideradas aprovações relacionadas com interrupções de ANS. O preenchimento ocorre no instante em que a ocorrência inicia evento e o conteúdo prévio é desconsiderado se realmente existirem motivos de reprovação. | char(3) | char(3) | Não |
| **SINCRONIZA_CANCELA** | Cancela a ocorrência se todas as invocadas forem canceladas | char(3) | char(3) | Não |
| **ID_TIPO_SOLICITACAO** | Identificador do Tipo de solicitacao associado | int | number(6,0) | Sim |
| **VISIBILIDADE** | Permite configurar a disponibilidade do iniciador nas diversas aplicações do sistema. | varchar(250) | varchar(250) | Não |
| **LISTA_DESTINATARIOS** | Relação de endereços de emails separados por ponto e vírgula que são utilizados como destinatários do comunicado. Pode ser preenchido em conjunto com o papel de processo de Destinatários. | varchar(500) | varchar(500) | Sim |
| **ID_MODELO_COMUNICA** | Identificador do Modelo de comunicado utilizado para gerar a mensagem | int | number(6,0) | Sim |
| **ID_PAPEL_DESTINATARIO** | Identificador do papel de processo utilizado para definir os destinatários do comunicado | int | number(6,0) | Sim |
| **ANEXAR_TODOS_DOCS** | Quando o evento é utilizado para envio esta propriedade indica que todos os arquivos da Ordem de Serviço serão anexados no email. Se o evento se refere a chegada de um email então todos os arquivos anexados na mensagem serão anexados na Ordem de Serviço. | char(3) | char(3) | Não |
| **ID_CLASSE_ANEXO_RESP** | Identificador do tipo de arquivo retornado em anexo | int | number(6,0) | Sim |
| **FINAL_INTERR** | Finaliza a interrupção de ANS corrente quando o cliente da ocorrência responder o comunicado. | char(3) | char(3) | Não |
| **MAX_EXECUCAO** | Define o número máximo de execuções do evento intermediário. Este atributo é válido apenas para eventos intermediários acoplados em atividades. | int | number(6,0) | Sim |
| **TEMPORALIDADE** | Define para eventos intermediários de mensagem após quantos dias a mensagem será excluída da base de dados. Se for 0 (zero) ela será excluída assim que o email for enviado. Se estiver sem preenchimento a mensagem não será excluída. | int | number(6,0) | Sim |
| **GRUPO_ANO** | Nome do agrupamento de tarefas que compartilham a mesma configuração de Acordo de Nível Operacional. Todas as mudanças em configurações de ANO de uma tarefa do grupo são replicadas nas demais tarefas do agrupamento. | varchar(50) | varchar(50) | Sim |
| **PERMITE_VOLTAR** | Permite que o solucionador cancele a execução da atividade executando o comando Voltar do assistente de processos | char(3) | char(3) | Não |
| **UNIDADE_ANO** | Unidade de medida para definição do Acordo de Nível Operacional. Se for selecionada a unidade 'Percentual ANS' então nenhum caminho pode totalizar o valor superior a 100%. | varchar(250) | varchar(250) | Não |
| **CONFIRM_RESP** | Em transições manuais para esta atividade será exibido o diálogo de encaminhamento para confirmação de responsabilidade. | char(3) | char(3) | Não |
| **PERMITE_CANCELAR_AA** | Permite que o cliente cancele a solicitação utilizando a página de consulta do Autoatendimento. | char(3) | char(3) | Não |
| **ID_CAIXA_EMAIL** | Identificador da caixa de email monitorada pela máquina de processos para os eventos intermediário e inicial por mensagem | int | number(6,0) | Sim |
| **TIPO_MENSAGEM** | Tipo de mensagem monitorada pelo evento. | varchar(250) | varchar(250) | Não |
| **NOME_MENSAGEM** | Nome resumido que identifica uma mensagem. Este nome é referênciado na chamada de Webservices. Na comparação dos nomes são descartados espaços em branco no início e fim do nome. A caixa (maiúsculo/minúsculo) também é ignorada. | varchar(100) | varchar(100) | Sim |
| **ENVIA_MSG_INDIVID** | Indica se será enviada uma mensagem para cada destinatário (caso verdadeiro) ou se será enviada uma única mensagem para todos os destinatários (caso falso) | char(3) | char(3) | Não |
| **ATIVO** | Indica se a Atividade está ativa ou inativa | char(3) | char(3) | Não |
| **TIPO_ABERT_LNK_INICIAL** | Indica o tipo de abertura se for um LinkInicial | varchar(250) | varchar(250) | Não |
| **PREENCH_CLI_SOLUC** | Indica que o campo Cliente deve ser preenchido automaticamente com o solucionador conectado na aplicação. Este comportamento só é possível para iniciadores disponíveis somente no Workspace. | char(3) | char(3) | Não |
| **ENDERECO_REPLY** | Conta configurada na mensagem para reply | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PROCESSO](dados_processo) | \| **PROCESSO** \| **ATIVIDADE** \| \|---\|---\| \| ID_PROCESSO \| ID_PROCESSO \| |
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **ATIVIDADE** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_RESPONSAVEL \| |
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **ATIVIDADE** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_DESTINATARIO \| |
| [CLASSE_PESQ_SATISF](dados_classe_pesq_satisf) | \| **CLASSE_PESQ_SATISF** \| **ATIVIDADE** \| \|---\|---\| \| ID_CLASSE_PESQ_SATISF \| ID_CLASSE_PESQ_SATISF \| |
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **ATIVIDADE** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |
| [ASSOCIACAO](dados_associacao) | \| **ASSOCIACAO** \| **ATIVIDADE** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |
| [MOTIVO_INTER_SLA](dados_motivo_inter_sla) | \| **MOTIVO_INTER_SLA** \| **ATIVIDADE** \| \|---\|---\| \| ID_MOTIVO_INTER_SLA \| ID_MOTIVO_INTER_SLA \| |
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **ATIVIDADE** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |
| [TIPO_SOLICITACAO](dados_tipo_solicitacao) | \| **TIPO_SOLICITACAO** \| **ATIVIDADE** \| \|---\|---\| \| ID_TIPO_SOLICITACAO \| ID_TIPO_SOLICITACAO \| |
| [MODELO_COMUNICA](dados_modelo_comunica) | \| **MODELO_COMUNICA** \| **ATIVIDADE** \| \|---\|---\| \| ID_MODELO_COMUNICA \| ID_MODELO_COMUNICA \| |
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **ATIVIDADE** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_ANEXO_RESP \| |
| [CAIXA_MENSAGEM](dados_caixa_mensagem) | \| **CAIXA_MENSAGEM** \| **ATIVIDADE** \| \|---\|---\| \| ID_CAIXA_MENSAGEM \| ID_CAIXA_EMAIL \| |
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **ATIVIDADE** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

Tabelas que dependem de ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RECEPTOR](dados_receptor) | \| **RECEPTOR** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [EMISSOR](dados_emissor) | \| **EMISSOR** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [FLUXO_SEQUENCIA](dados_fluxo_sequencia) | \| **FLUXO_SEQUENCIA** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE_DESTINO \| ID_ATIVIDADE \| |
| [EXECUCAO_ATIVIDADE](dados_execucao_atividade) | \| **EXECUCAO_ATIVIDADE** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [TIME_SHEET](dados_time_sheet) | \| **TIME_SHEET** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [EXEC_TIMER](dados_exec_timer) | \| **EXEC_TIMER** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [INTER_SLA](dados_inter_sla) | \| **INTER_SLA** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE_GERADORA \| ID_ATIVIDADE \| |
| [FIGURA](dados_figura) | \| **FIGURA** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [ASSOCIACAO_OCORR](dados_associacao_ocorr) | \| **ASSOCIACAO_OCORR** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE_GER \| ID_ATIVIDADE \| |
| [FLUXO_SEQUENCIA](dados_fluxo_sequencia) | \| **FLUXO_SEQUENCIA** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE_ORIGEM \| ID_ATIVIDADE \| |
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [VALOR_INPUT](dados_valor_input) | \| **VALOR_INPUT** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [RETORNO_ITEM](dados_retorno_item) | \| **RETORNO_ITEM** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [PASSAGEM_ITEM](dados_passagem_item) | \| **PASSAGEM_ITEM** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [CLIENTE_AUTORIZADO](dados_cliente_autorizado) | \| **CLIENTE_AUTORIZADO** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [ANEXO_EVNT_MSG](dados_anexo_evnt_msg) | \| **ANEXO_EVNT_MSG** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [ACAO_ACORDO](dados_acao_acordo) | \| **ACAO_ACORDO** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [OPCAO_ATIVIDADE](dados_opcao_atividade) | \| **OPCAO_ATIVIDADE** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [ASSOCIACAO_SUBPROCESSO](dados_associacao_subprocesso) | \| **ASSOCIACAO_SUBPROCESSO** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
| [REL_ATIVIDADE](dados_rel_atividade) | \| **REL_ATIVIDADE** \| **ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela PROCESSO**

```
select ATIVIDADE.*, PROCESSO.DESCRICAO
from ATIVIDADE left outer join PROCESSO on ATIVIDADE.ID_PROCESSO = PROCESSO.ID_PROCESSO
```

**Exemplo 2: join com a tabela PAPEL_PROCESSO**

```
select ATIVIDADE.*, PAPEL_PROCESSO.NOME
from ATIVIDADE left outer join PAPEL_PROCESSO on ATIVIDADE.ID_PAPEL_RESPONSAVEL = PAPEL_PROCESSO.ID_PAPEL_PROCESSO
```

**Exemplo 3: join com a tabela PAPEL_PROCESSO**

```
select ATIVIDADE.*, PAPEL_PROCESSO.NOME
from ATIVIDADE left outer join PAPEL_PROCESSO on ATIVIDADE.ID_PAPEL_DESTINATARIO = PAPEL_PROCESSO.ID_PAPEL_PROCESSO
```

**Exemplo 4: join com a tabela CLASSE_PESQ_SATISF**

```
select ATIVIDADE.*, CLASSE_PESQ_SATISF.DESCRICAO
from ATIVIDADE left outer join CLASSE_PESQ_SATISF on ATIVIDADE.ID_CLASSE_PESQ_SATISF = CLASSE_PESQ_SATISF.ID_CLASSE_PESQ_SATISF
```

**Exemplo 5: join com a tabela CLASSE_SUB_PROCESSO**

```
select ATIVIDADE.*, CLASSE_SUB_PROCESSO.DESCRICAO
from ATIVIDADE left outer join CLASSE_SUB_PROCESSO on ATIVIDADE.ID_CLASSE_SUB_PROCESSO = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```

**Exemplo 6: join com a tabela ASSOCIACAO**

```
select ATIVIDADE.*, ASSOCIACAO.FRASE_ASSOC
from ATIVIDADE left outer join ASSOCIACAO on ATIVIDADE.ID_ASSOCIACAO = ASSOCIACAO.ID_ASSOCIACAO
```

**Exemplo 7: join com a tabela CONTROLE**

```
select ATIVIDADE.*, CONTROLE.DESCRICAO
from ATIVIDADE left outer join CONTROLE on ATIVIDADE.ID_CONTROLE = CONTROLE.ID_CONTROLE
```

**Exemplo 8: join com a tabela TIPO_SOLICITACAO**

```
select ATIVIDADE.*, TIPO_SOLICITACAO.DESCRICAO
from ATIVIDADE left outer join TIPO_SOLICITACAO on ATIVIDADE.ID_TIPO_SOLICITACAO = TIPO_SOLICITACAO.ID_TIPO_SOLICITACAO
```

**Exemplo 9: join com a tabela MODELO_COMUNICA**

```
select ATIVIDADE.*, MODELO_COMUNICA.DESCRICAO
from ATIVIDADE left outer join MODELO_COMUNICA on ATIVIDADE.ID_MODELO_COMUNICA = MODELO_COMUNICA.ID_MODELO_COMUNICA
```

**Exemplo 10: join com a tabela CAIXA_MENSAGEM**

```
select ATIVIDADE.*, CAIXA_MENSAGEM.NOME
from ATIVIDADE left outer join CAIXA_MENSAGEM on ATIVIDADE.ID_CAIXA_EMAIL = CAIXA_MENSAGEM.ID_CAIXA_MENSAGEM
```

**Exemplo 11: join com a tabela SUB_PROCESSO**

```
select ATIVIDADE.*
from ATIVIDADE, SUB_PROCESSO
where ATIVIDADE.ID_SUB_PROCESSO = SUB_PROCESSO.ID_SUB_PROCESSO
```
