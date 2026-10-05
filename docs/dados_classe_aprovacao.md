# CLASSE_APROVACAO

Caminho: Customização > Modelo de dados > Processo > CLASSE_APROVACAO

Tipo de Item de Configuração sujeito a aprovação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_APROVACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseAprovacao | int | number(6,0) | Não |
| **ID_OPERACAO_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | int | number(6,0) | Não |
| **OBRIGATORIO** | Obrigatoriedade de preenchimento na execução do Processo | char(3) | char(3) | Não |
| **COPIAR_ANEXADO** | Copia para a solicitação de aprovação Itens de Configuração que atendam os critérios de Tipo e Super tipo configurados no Data object de aprovação. Este campo não possui ação quando for configurado no Data Object a cópia de todos os Itens de Configuração associados a Ocorrência. | char(3) | char(3) | Não |
| **DESCRICAO** | Descrição do Item de Configuração para associação com a solicitação de aprovação. Se não for especificado então o sistema assume como descritivo do objeto a listagem de descrições de todos os Tipos e Super tipos configurados na listagem 'Escopo de Tipos/Super tipos' | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por CLASSE_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **CLASSE_APROVACAO** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

Tabelas que dependem de CLASSE_APROVACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [REST_SERV_APROV](dados_rest_serv_aprov) | \| **REST_SERV_APROV** \| **CLASSE_APROVACAO** \| \|---\|---\| \| ID_CLASSE_APROVACAO \| ID_CLASSE_APROVACAO \| |
| [ESCOPO_CLASSE_APROV](dados_escopo_classe_aprov) | \| **ESCOPO_CLASSE_APROV** \| **CLASSE_APROVACAO** \| \|---\|---\| \| ID_CLASSE_APROVACAO \| ID_CLASSE_APROVACAO \| |

**Exemplo 1: join com a tabela OPERACAO_ATIVIDADE**

```
select CLASSE_APROVACAO.*
from CLASSE_APROVACAO, OPERACAO_ATIVIDADE
where CLASSE_APROVACAO.ID_OPERACAO_ATIVIDADE = OPERACAO_ATIVIDADE.ID_OPERACAO_ATIVIDADE
```
