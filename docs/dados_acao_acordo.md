# ACAO_ACORDO

Caminho: Customização > Modelo de dados > Processo > ACAO_ACORDO

Ações disparadas pela atividade (email, encaminhamento etc) mediante a um marca atingida no tempo do Acordo de Nível Operacional.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ACAO_ACORDO** | Número sequencial gerado automaticamente pelo sistema para Identificar um AcaoAcordo | int | number(6,0) | Não |
| **ACAO** | Ação executada quando for atingido o tempo configurado | varchar(250) | varchar(250) | Não |
| **ID_PAPEL_PROCESSO** | Identificador do papel utilizado para obter as pessoas ou filas de destino | int | number(6,0) | Não |
| **ID_MODELO_COMUNICA** | Identificador do Modelo de comunicado | int | number(6,0) | Sim |
| **ID_ATIVIDADE** | Identificador da Atividade proprietária da Ação. | int | number(6,0) | Não |
| **PERCENTUAL** | Percentual do tempo o Acordo de Nível Operacional que determina o momento de execução da ação. Se for igual a 0 então a ação não será executada. | decimal(15,2) | number(15,2) | Não |
| **TEMPORALIDADE** | Define para a ação do tipo email após quantos dias a mensagem será excluída da base de dados. Se for 0 (zero) ela será excluída assim que o email for enviado. Se estiver sem preenchimento a mensagem não será excluída. | int | number(6,0) | Sim |
| **CODIGO_ANO** | Código utilizado para sincronizar ações entre atividades contidas no mesmo grupo de Acordo de Nível Operacional | varchar(100) | varchar(100) | Não |

Tabelas referenciadas por ACAO_ACORDO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PAPEL_PROCESSO](dados_papel_processo) | \| **PAPEL_PROCESSO** \| **ACAO_ACORDO** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_PROCESSO \| |
| [MODELO_COMUNICA](dados_modelo_comunica) | \| **MODELO_COMUNICA** \| **ACAO_ACORDO** \| \|---\|---\| \| ID_MODELO_COMUNICA \| ID_MODELO_COMUNICA \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **ACAO_ACORDO** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

Tabelas que dependem de ACAO_ACORDO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [EXECUCAO_ACAO](dados_execucao_acao) | \| **EXECUCAO_ACAO** \| **ACAO_ACORDO** \| \|---\|---\| \| ID_ACAO_ACORDO \| ID_ACAO_ACORDO \| |

**Exemplo 1: join com a tabela PAPEL_PROCESSO**

```
select ACAO_ACORDO.*, PAPEL_PROCESSO.NOME
from ACAO_ACORDO, PAPEL_PROCESSO
where ACAO_ACORDO.ID_PAPEL_PROCESSO = PAPEL_PROCESSO.ID_PAPEL_PROCESSO
```

**Exemplo 2: join com a tabela MODELO_COMUNICA**

```
select ACAO_ACORDO.*, MODELO_COMUNICA.DESCRICAO
from ACAO_ACORDO left outer join MODELO_COMUNICA on ACAO_ACORDO.ID_MODELO_COMUNICA = MODELO_COMUNICA.ID_MODELO_COMUNICA
```

**Exemplo 3: join com a tabela ATIVIDADE**

```
select ACAO_ACORDO.*
from ACAO_ACORDO, ATIVIDADE
where ACAO_ACORDO.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```
