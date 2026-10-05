# CAMPO_APROV

Caminho: Customização > Modelo de dados > Processo > CAMPO_APROV

Campo para Aprovação

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CAMPO_APROV** | Número sequencial gerado automaticamente pelo sistema para Identificar um CampoAprovacao | int | number(6,0) | Não |
| **NOME** | Campo da Ocorrência que deve ser aprovado. | varchar(250) | varchar(250) | Não |
| **NOME_CUSTOM** | Nome do campo customizado | varchar(100) | varchar(100) | Sim |
| **ROTULO** | Rótulo para aprovação do Campo. Se não preenchido o sistema exibe descritivo original definido no Dicionário de Classes. | varchar(500) | varchar(500) | Sim |
| **ID_OPERACAO_ATIVIDADE** | Identificação da Operação de Atividade | int | number(6,0) | Não |
| **SEQUENCIA** | Sequência de apresentação do Campo | int | number(6,0) | Não |
| **OBRIGATORIO** | Indica a obrigatoriedade de preenchimento do campo para Aprovação | char(3) | char(3) | Não |
| **PERMITE_MODIFICAR** | Indica que mesmo após a aprovação será possível modificar o conteúdo do campo. | char(3) | char(3) | Não |

Tabelas referenciadas por CAMPO_APROV

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **CAMPO_APROV** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

**Exemplo 1: join com a tabela OPERACAO_ATIVIDADE**

```
select CAMPO_APROV.*
from CAMPO_APROV, OPERACAO_ATIVIDADE
where CAMPO_APROV.ID_OPERACAO_ATIVIDADE = OPERACAO_ATIVIDADE.ID_OPERACAO_ATIVIDADE
```
