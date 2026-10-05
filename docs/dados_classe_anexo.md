# CLASSE_ANEXO

Caminho: Customização > Modelo de dados > Processo > CLASSE_ANEXO

Classe de Item para Anexar

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_ANEXO** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseAnexo | int | number(6,0) | Não |
| **ID_OPERACAO_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial | int | number(6,0) | Não |
| **DESCRICAO** | Descrição do Item de Configuração para associação com a ocorrência. Se não for especificado então o sistema assume como descritivo do objeto a listagem de descrições de todos os Tipos e Super Tipos configuradas na listagem 'Escopo de Tipos/Super Tipos'. | varchar(500) | varchar(500) | Sim |
| **REQUERIDO_INCIAL** | É obrigatória a associação do Item de Configuração para que seja iniciada a atividade. 'Requerido inicialização' e 'Produzido ao término' são campos mutualmente exclusivos, ou seja, habilitando um o outro é automaticamente desmarcado. | char(3) | char(3) | Não |
| **PRODUZIDO_TERMINO** | O Item de Configuração é gerado ao términdo da Atividade. 'Requerido inicialização' e 'Produzido ao término' são campos mutualmente exclusivos, ou seja, habilitando um o outro é automaticamente desmarcado. | char(3) | char(3) | Não |
| **EXIBICAO_AUTOMATICA_AA** | Lista os itens de configuração automaticamente na tela de procura de itens de configuração no Autoatendimento | char(3) | char(3) | Não |
| **PERMITE_MULTIPLOS_ITENS** | Permite inclusão de múltiplos | char(3) | char(3) | Não |
| **CONFIG_USUARIOS** | Ação realizada nos Itens de Configuração na finalização de uma Ordem de Serviço ou atividade de processo. Esta ação não é reversível quando executada a Reabertura de Ordem de Serviço ou cancelamento de atividade via botão Voltar do assistente. | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por CLASSE_ANEXO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **CLASSE_ANEXO** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

Tabelas que dependem de CLASSE_ANEXO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM_OCORRENCIA](dados_item_ocorrencia) | \| **ITEM_OCORRENCIA** \| **CLASSE_ANEXO** \| \|---\|---\| \| ID_CLASSE_ANEXO \| ID_CLASSE_ANEXO \| |
| [REST_SERV_ANEXO](dados_rest_serv_anexo) | \| **REST_SERV_ANEXO** \| **CLASSE_ANEXO** \| \|---\|---\| \| ID_CLASSE_ANEXO \| ID_CLASSE_ANEXO \| |
| [ESCOPO_CLASSE_ANEXO](dados_escopo_classe_anexo) | \| **ESCOPO_CLASSE_ANEXO** \| **CLASSE_ANEXO** \| \|---\|---\| \| ID_CLASSE_ANEXO \| ID_CLASSE_ANEXO \| |

**Exemplo 1: join com a tabela OPERACAO_ATIVIDADE**

```
select CLASSE_ANEXO.*
from CLASSE_ANEXO, OPERACAO_ATIVIDADE
where CLASSE_ANEXO.ID_OPERACAO_ATIVIDADE = OPERACAO_ATIVIDADE.ID_OPERACAO_ATIVIDADE
```
