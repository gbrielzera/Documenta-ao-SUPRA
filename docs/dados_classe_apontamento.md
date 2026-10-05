# CLASSE_APONTAMENTO

Caminho: Customização > Modelo de dados > Processo > CLASSE_APONTAMENTO

Classe de Apontamento

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CLASSE_APONTAMENTO** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseApontamento | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do ClasseApontamento | varchar(500) | varchar(500) | Não |
| **DESC_INTEIRO_1** | Descrição para entrada de dados no Campo Inteiro 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_INTEIRO_2** | Descrição para entrada de dados no Campo Inteiro 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_STRING_1** | Descrição para entrada de dados no Campo String 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_STRING_2** | Descrição para entrada de dados no Campo String 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_DATA_HORA_1** | Descrição para entrada de dados no Campo Data/hora 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_DATA_HORA_2** | Descrição para entrada de dados no Campo Data/hora 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_DECIMAL_1** | Descrição para entrada de dados no Campo Decimal 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_DECIMAL_2** | Descrição para entrada de dados no Campo Decimal 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_BOOLEANO_1** | Descrição para entrada de dados no Campo Booleano 1. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **DESC_BOOLEANO_2** | Descrição para entrada de dados no Campo Booleano 2. O preenchimento deste descritivo indica que o Campo será habilitado para entrada de dados. | varchar(500) | varchar(500) | Sim |
| **ID_TIPO_EVENTO** | Identificador do TipoEvento associado | int | number(6,0) | Sim |
| **PERMITE_MOTIVO_DIGITADO** | Permite a informação do Motivo do Apontamento por digitação e não por seleção de Item mantido na propriedade Motivos. | char(3) | char(3) | Não |
| **FONTE** | Fonte | varchar(250) | varchar(250) | Não |
| **CODIGO** | Código | varchar(50) | varchar(50) | Não |
| **PERMITE_MULTI_MOTIVOS** | Permite a informação de vários motivos no Apontamento | char(3) | char(3) | Não |
| **SEQUENCIAL_INTEGER_1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Inteiro 1 | int | number(6,0) | Sim |
| **SEQUENCIAL_INTEGER_2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Inteiro 2 | int | number(6,0) | Sim |
| **SEQUENCIAL_STRING_1** | Define a sequencia de apresentação do controle utilizado para edição do Campo String 1 | int | number(6,0) | Sim |
| **SEQUENCIAL_STRING_2** | Define a sequencia de apresentação do controle utilizado para edição do Campo String 2 | int | number(6,0) | Sim |
| **SEQUENCIAL_DATA_HORA_1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Data/hora 1 | int | number(6,0) | Sim |
| **SEQUENCIAL_DATA_HORA_2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Data/hora 2 | int | number(6,0) | Sim |
| **SEQUENCIAL_DECIMAL_1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Decimal 1 | int | number(6,0) | Sim |
| **SEQUENCIAL_DECIMAL_2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Decimal 2 | int | number(6,0) | Sim |
| **SEQUENCIAL_BOOLEANO_1** | Define a sequencia de apresentação do controle utilizado para edição do Campo Booleano 1 | int | number(6,0) | Sim |
| **SEQUENCIAL_BOOLEANO_2** | Define a sequencia de apresentação do controle utilizado para edição do Campo Booleano 2 | int | number(6,0) | Sim |
| **PERMITE_MULTIPLOS_APONT** | Permite vários apontamentos para uma ocorrência de Processo. | char(3) | char(3) | Não |
| **MOTIVO_OBRIGATORIO** | A informação de um Motivo é obrigatória no instante em que é realizado o Apontamento. | char(3) | char(3) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |

Tabelas referenciadas por CLASSE_APONTAMENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TIPO_EVENTO](dados_tipo_evento) | \| **TIPO_EVENTO** \| **CLASSE_APONTAMENTO** \| \|---\|---\| \| ID_TIPO_EVENTO \| ID_TIPO_EVENTO \| |

Tabelas que dependem de CLASSE_APONTAMENTO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [APONTAMENTO](dados_apontamento) | \| **APONTAMENTO** \| **CLASSE_APONTAMENTO** \| \|---\|---\| \| ID_CLASSE_APONTAMENTO \| ID_CLASSE_APONTAMENTO \| |
| [MOTIVO_CLASSE_APONT](dados_motivo_classe_apont) | \| **MOTIVO_CLASSE_APONT** \| **CLASSE_APONTAMENTO** \| \|---\|---\| \| ID_CLASSE_APONTAMENTO \| ID_CLASSE_APONTAMENTO \| |

**Exemplo 1: join com a tabela TIPO_EVENTO**

```
select CLASSE_APONTAMENTO.*, TIPO_EVENTO.NOME
from CLASSE_APONTAMENTO left outer join TIPO_EVENTO on CLASSE_APONTAMENTO.ID_TIPO_EVENTO = TIPO_EVENTO.ID_TIPO_EVENTO
```
