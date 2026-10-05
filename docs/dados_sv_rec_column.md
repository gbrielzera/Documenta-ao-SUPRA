# SV_REC_COLUMN

Caminho: Customização > Modelo de dados > Utilitários > SV_REC_COLUMN

Campos de registros utilizados em propriedades customizadas do tipo Listagem de registros

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CUSTOM_PROPERTY** | Identificador da Propriedade Customizada | int | number(6,0) | Não |
| **NAME** | Nome da coluna do registro. No caso de campos persistentes este nome é utilizado para criar uma coluna na tabela onde são persistidos os registros. | varchar(100) | varchar(100) | Não |
| **TYPE** | Tipo de dado da coluna | varchar(500) | varchar(500) | Não |
| **SEQUENCE** | Sequencial para apresentação no controle grid utilizado para visualização e edição | int | number(6,0) | Não |
| **CONTROL** | Controle utilizado para edição da coluna do registro | varchar(500) | varchar(500) | Não |
| **LIST_ITEMS** | Listagem de itens disponíveis para seleção em um controle do tipo combobox. | varchar(500) | varchar(500) | Sim |
| **LOOKUP_SCRIPT** | Script utilizado para recuperação de itens utilizados como opções de preenchimento para o campo. Para o caso específico de recuperação a partir de banco de dados, se for fornecida uma tabela com dois campos então o primeiro será utilizado para preenchimento do campo enquanto o segundo fornecerá as opções exibidas no controle. | text | clob | Sim |
| **LENGTH** | Tamanho de campos string em quantidade de caracteres. Se não for preenchido então é adotado o tamanho padrão de 250 caracteres | int | number(6,0) | Sim |
| **TEXT** | Descrição resumida que é exibida no rótulo de controles utilizados na edição da coluna. | varchar(500) | varchar(500) | Não |
| **CALC_FORMULA** | Fórmla utilizada para cálculo de campos. Campos calculado não são persistidos em banco de dados. | varchar(500) | varchar(500) | Sim |
| **WIDTH** | Largura do controle utilizado para Edição da coluna. Quando não definido o sistema assume valor default conforme controle selecionado. | int | number(6,0) | Sim |

Tabelas referenciadas por SV_REC_COLUMN

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CUSTOM_PROPERTY](dados_sv_custom_property) | \| **SV_CUSTOM_PROPERTY** \| **SV_REC_COLUMN** \| \|---\|---\| \| ID_CUSTOM_PROPERTY \| ID_CUSTOM_PROPERTY \| |

**Exemplo 1: join com a tabela SV_CUSTOM_PROPERTY**

```
select SV_REC_COLUMN.*
from SV_REC_COLUMN, SV_CUSTOM_PROPERTY
where SV_REC_COLUMN.ID_CUSTOM_PROPERTY = SV_CUSTOM_PROPERTY.ID_CUSTOM_PROPERTY
```
