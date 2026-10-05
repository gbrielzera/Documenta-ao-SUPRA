# ITEM_CHARGE_BACK

Caminho: Customização > Modelo de dados > Recurso > ITEM_CHARGE_BACK

Item combrado de uma área em Charge-back. Este item pode se tratar de uso de Ativo, Acordo de Nível de Serviço e Serviço prestado por Ordem de Serviço.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CHARGE_BACK** | Número sequencial gerado automaticamente pelo sistema para Identificar um ChargeBack | int | number(6,0) | Não |
| **ID_ORGAO** | Identificador do Orgao associado | int | number(6,0) | Não |
| **SEQUENCIAL** | Sequencial utilizado para identificar o item dentro do Charge-back de uma Área | int | number(6,0) | Não |
| **DESCRICAO** | Descrição contendo detalhes do lançamento | varchar(500) | varchar(500) | Não |
| **ID_OCORRENCIA** | Identificador da Ordem de Serviço que demanda charge-back. | int | number(6,0) | Sim |
| **ID_SLA** | Identificador do Acordo de Nível de Serviço que gera Charge-back | int | number(6,0) | Sim |
| **ID_ITEM** | Identificador do Ativo que demanda Charge-back | int | number(6,0) | Sim |
| **VALOR_ITEM** | Valor do lançamento que pode ser gerado por um preço de Ativo, valor estabelecido no ANS ou no campo Valor de Charge-back da Ordem de Serviço. | decimal(15,2) | number(15,2) | Não |
| **MEM_CALC** | Dados utilizados pelo sistema para obter o valor do Item. Estes dados podem variar em função da origem da informação (Acordo de Nível de Serviço, Ativo etc) | varchar(500) | varchar(500) | Sim |
| **ID_FAVORECIDO** | Identificador do usuário favorecido pelo uso de um Ativo, atendimento de uma Ordem de Serviço ou Acordo de Nível de Serviço. | int | number(6,0) | Sim |

Tabelas referenciadas por ITEM_CHARGE_BACK

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_CHARGE_BACK** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **ITEM_CHARGE_BACK** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [SLA](dados_sla) | \| **SLA** \| **ITEM_CHARGE_BACK** \| \|---\|---\| \| ID_SLA \| ID_SLA \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ITEM_CHARGE_BACK** \| \|---\|---\| \| ID_PESSOA \| ID_FAVORECIDO \| |
| [CHARGE_BACK_ORGAO](dados_charge_back_orgao) | \| **CHARGE_BACK_ORGAO** \| **ITEM_CHARGE_BACK** \| \|---\|---\| \| ID_CHARGE_BACK \| ID_CHARGE_BACK \| \| ID_ORGAO \| ID_ORGAO \| |

**Exemplo 1: join com a tabela SLA**

```
select ITEM_CHARGE_BACK.*, SLA.DESCRICAO
from ITEM_CHARGE_BACK left outer join SLA on ITEM_CHARGE_BACK.ID_SLA = SLA.ID_SLA
```

**Exemplo 2: join com a tabela PESSOA**

```
select ITEM_CHARGE_BACK.*, PESSOA.NOME_ABREVIADO
from ITEM_CHARGE_BACK left outer join PESSOA on ITEM_CHARGE_BACK.ID_FAVORECIDO = PESSOA.ID_PESSOA
```
