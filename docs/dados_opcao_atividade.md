# OPCAO_ATIVIDADE

Caminho: Customização > Modelo de dados > Processo > OPCAO_ATIVIDADE

Opções em atividades de processo. Uma opção diferencia-se de uma configuração de atividade por ser algo não-necessário durante a execução do processo. Exemplo típico de uma opção: configuração de relatórios.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATIVIDADE** | Identificador da atividade dona da opção | int | number(6,0) | Não |
| **INDISPONIBILIDADE** | Indica que a tarefa ou evento configura indisponibilidade de Serviço. Esta opção fará efeito no relatório de Disponibilidade de Serviços interferindo no cálculo de MTBF e MTTR. | char(3) | char(3) | Não |

Tabelas referenciadas por OPCAO_ATIVIDADE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **OPCAO_ATIVIDADE** \| \|---\|---\| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |

**Exemplo 1: join com a tabela ATIVIDADE**

```
select OPCAO_ATIVIDADE.*
from OPCAO_ATIVIDADE, ATIVIDADE
where OPCAO_ATIVIDADE.ID_ATIVIDADE = ATIVIDADE.ID_ATIVIDADE
```
