# CLASSE_SUB_PROCESSO

Caminho: Customização > Modelo de dados > Processo > CLASSE_SUB_PROCESSO

Um Tipo de Subprocesso mantém características de um fluxo que são invariáveis entre suas diversas versões.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_SUB_PROCESSO** | Número sequencial gerado automaticamente pelo sistema para identificar um Tipo de Subprocesso. Um Identificador não pode ser modificado pelo usuário. | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente a utilização de um Tipo de Subprocesso | varchar(500) | varchar(500) | Não |
| **SIGLA** | Nome abreviado (código) que identifica um Tipo de Subprocesso. Este código pode ser utilizado em scripts para automatismo de processos. | varchar(50) | varchar(50) | Não |
| **ATIVO** | Indica que o Tipo de Subprocesso está Ativo. Quando ativo o tipo é visível em formulários de entrada de dados para Ordens de Serviço ou Consultas diversas. | char(3) | char(3) | Não |
| **OBJETIVO** | Texto de Referência sobre o Objetivo do Tipo de Subprocesso | text | clob | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **DESCRICAO_CLIENTE** | Descritivo apresentado para o Cliente. Se não for preenchido é apresentado o Descritivo padrão do Tipo de Subprocesso. | varchar(500) | varchar(500) | Sim |
| **ID_METODO_PRIORIZACAO** | Identificador do MetodoPriorizacao associado | int | number(6,0) | Sim |
| **ID_FATOR_PRIORIDADE** | Identificador do(a) FatorPrioridade associado(a) | int | number(6,0) | Sim |
| **ORDEM_EXIBICAO** | Ordem de exibição da Solicitação na página de Abertura de Ordens de Serviço da aplicação de Autoatendimento. Quando preenchido a Solicitação é exibida em um grupo denominado "Principais solicitações", caso contrário é agrupado em "Demais solicitações". Em caso de empate por ordenação deste campo então é adotado como segundo critério a ordenação alfabética por Descritivo do Cliente | int | number(6,0) | Sim |
| **VALOR_CHARGE_BACK** | Valor para cobrança pela rotina de Charge-back. Se o critério de charge-back for 'Hora' então o valor total é obtido pela multiplicação do 'Valor' pela quantidade de horas apontadas no período de apuração. Se o critério de charge-back for 'Ocorrência' então o total é obtido pela multiplicação do 'Valor' pela quantidade total de ocorrências finalizadas no período de apuração. | decimal(15,2) | number(15,2) | Sim |
| **CRIT_CHARGE_BACK** | Forma de Charge-back para Ocorrências do Subprocesso. | varchar(250) | varchar(250) | Não |
| **ID_ORGAO_DONO** | Identificador do Órgão proprietário do Processo | int | number(6,0) | Sim |
| **ID_RESPONSAVEL** | Identificador da Pessoa associada | int | number(6,0) | Sim |
| **DISP_CONS_CONH** | Ordens de Serviço deste Subprocesso podem ser recuperadas pela ferramenta de busca de base de conhecimento. | char(3) | char(3) | Não |
| **REGRA_AUTORIZA** | Regra de autorização para visualização de Ordens de Serviço do Subprocesso. Se este campo não for preenchido o sistema utilizará o parâmetro default cadastrado na tela de Configurações. | varchar(250) | varchar(250) | Sim |
| **ACESSO_ADMIN** | Indica que usuários com o perfil Administrador possuem acesso total em ocorrências do Subprocesso. | char(3) | char(3) | Não |
| **REABERTURA_AA** | Permite que clientes reabram a Ordem de Serviço utilizando a página de consulta do Autoatendimento. Esta permissão também está condicionada ao parâmetro 'Máximo dias para reabertura' da tela de Configurações. | char(3) | char(3) | Não |
| **HAB_CONS_AUTO_CON** | Indica que Ordens de Serviço deste Subprocesso acionam a busca automática de artigos da Base de Conhecimento a partir dos campos Assunto, Descrição detalhada ou Sintoma analisado. Esta busca ocorre quando o usuário visualiza a tela de edição da Ordem de Serviço, quando os campos citados são utilizados como critério de recuperação por palavras-chave. | char(3) | char(3) | Não |
| **VISIBILIDADE_AA** | Indica o tipo de visibilidade das ocorrências deste tipo de subprocesso no Autoatendimento, levando em consideração o cliente ou favorecido como referência | varchar(250) | varchar(250) | Não |
| **PUBLIC_APONTAMT_AA** | Indica a regra de publicação de apontamentos de horas trabalhadas no Autoatendimento | varchar(500) | varchar(500) | Não |
| **EMAIL_COPIA** | Serão enviados para este(s) email(s) os emails enviados manualmente relacionados com este Tipo de Subprocesso. Separar por ponto-e-vírgula (;). | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por CLASSE_SUB_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [METODO_PRIORIZACAO](dados_metodo_priorizacao) | \| **METODO_PRIORIZACAO** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_METODO_PRIORIZACAO \| ID_METODO_PRIORIZACAO \| |
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO_DONO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |

Tabelas que dependem de CLASSE_SUB_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROC \| ID_CLASSE_SUB_PROCESSO \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROC_INI \| ID_CLASSE_SUB_PROCESSO \| |
| [CLASSE_SUBPROC_INDICADOR](dados_classe_subproc_indicador) | \| **CLASSE_SUBPROC_INDICADOR** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |
| [ASSOCIACAO](dados_associacao) | \| **ASSOCIACAO** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_FONTE \| ID_CLASSE_SUB_PROCESSO \| |
| [ASSOCIACAO](dados_associacao) | \| **ASSOCIACAO** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_ALVO \| ID_CLASSE_SUB_PROCESSO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |
| [REST_SERVICO](dados_rest_servico) | \| **REST_SERVICO** \| **CLASSE_SUB_PROCESSO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_SUB_PROCESSO \| |

**Exemplo 1: join com a tabela METODO_PRIORIZACAO**

```
select CLASSE_SUB_PROCESSO.*, METODO_PRIORIZACAO.DESCRICAO
from CLASSE_SUB_PROCESSO left outer join METODO_PRIORIZACAO on CLASSE_SUB_PROCESSO.ID_METODO_PRIORIZACAO = METODO_PRIORIZACAO.ID_METODO_PRIORIZACAO
```

**Exemplo 2: join com a tabela FATOR_PRIORIDADE**

```
select CLASSE_SUB_PROCESSO.*, FATOR_PRIORIDADE.DESCRICAO
from CLASSE_SUB_PROCESSO left outer join FATOR_PRIORIDADE on CLASSE_SUB_PROCESSO.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```
