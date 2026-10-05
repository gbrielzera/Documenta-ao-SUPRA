# CAMPO_PREENCH_APROV

Caminho: Customização > Modelo de dados > Processo > CAMPO_PREENCH_APROV

Campo para Preenchimento em Aprovação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CAMPO_PREENCH_APROV** | Número sequencial gerado automaticamente pelo sistema para Identificar um CampoPreenchimentoAprovacao | int | number(6,0) | Não |
| **NOME** | Campo da Ocorrência que deve ser preenchido em aprovado. São permitidos apenas campos com controles do tipo TextBox, Memo e DropDownList. | varchar(250) | varchar(250) | Não |
| **NOME_CUSTOM** | Nome do campo customizado para preenchimento. São permitidos apenas campos com controles do tipo TextBox, Memo e DropDownList. | varchar(100) | varchar(100) | Sim |
| **ROTULO** | Rótulo para aprovação do Campo. Se não preenchido o sistema exibe descritivo original definido no Dicionário de Classes. | varchar(500) | varchar(500) | Sim |
| **ID_OPERACAO_ATIVIDADE** | Identificador da OperacaoAtividade associada | int | number(6,0) | Não |
| **SEQUENCIA** | Sequência de apresentação do Campo | int | number(6,0) | Não |
| **OBRIGATORIEDADE** | Indica a obrigatoriedade de preenchimento do campo para Aprovação | varchar(250) | varchar(250) | Não |
| **PERMITE_MODIFICAR** | Indica que mesmo após a aprovação será possível modificar o conteúdo do campo. | char(3) | char(3) | Não |

Tabelas referenciadas por CAMPO_PREENCH_APROV

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **CAMPO_PREENCH_APROV** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

**Exemplo 1: join com a tabela OPERACAO_ATIVIDADE**

```
select CAMPO_PREENCH_APROV.*
from CAMPO_PREENCH_APROV, OPERACAO_ATIVIDADE
where CAMPO_PREENCH_APROV.ID_OPERACAO_ATIVIDADE = OPERACAO_ATIVIDADE.ID_OPERACAO_ATIVIDADE
```
