# ITEM_COMPONENTE

Caminho: Customização > Modelo de dados > Ativos > ITEM_COMPONENTE

Componentes de um Item de Configuração

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_COMPONENTE** | Número sequencial gerado automaticamente pelo sistema para Identificar um Componente | int | number(6,0) | Não |
| **ID_ITEM** | Identificador do Item de Configuração proprietário do Componente | int | number(6,0) | Não |
| **ID_ITEM_COMPONENTE** | Identificador do Item de Configuração que é o Componente | int | number(6,0) | Sim |
| **TAMANHO** | Tamanho do Componente | decimal(15,2) | number(15,2) | Sim |
| **COMENTARIO** | Comentário sobre a relação Componente. Para conhecimento do autor do Comentário utilize a ferramenta de Consulta de Trilha de Modificações do Item. | varchar(500) | varchar(500) | Sim |
| **DESCRICAO** | Descritivo do componente | varchar(500) | varchar(500) | Sim |
| **ID_MODELO** | Identificador do Modelo associado | int | number(6,0) | Sim |
| **NUMERO_SERIE** | Número de série | varchar(500) | varchar(500) | Sim |
| **CUSTO_AQUISICAO** | Custom total de aquisição do Item | decimal(15,2) | number(15,2) | Sim |
| **CUSTO_MANUTENCAO** | Valor do Custo de Manutenção Mensal do Componente | decimal(15,2) | number(15,2) | Sim |
| **DATA_ENTREGA** | Data de entrega do Componente | datetime | date | Sim |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item de Configuração do Componente | int | number(6,0) | Não |
| **ID_OCORRENCIA** | Identificador da Ocorrencia associada | int | number(6,0) | Sim |
| **PRECO_AQUISICAO** | Preço de aquisição para Charge-Back do Componente. O valor de aquisição é lançado no charge-back de competência relativa a Data de Entrega do componente. | decimal(15,2) | number(15,2) | Sim |
| **PRECO_MANUTENCAO** | Preço de Charge-back de manutenção mensal | decimal(15,2) | number(15,2) | Sim |
| **CODIGO_OCS** | Código do componente original do banco de dados OCS | varchar(500) | varchar(500) | Sim |
| **TABELA_OCS** | Tabela original do OCS que gerou o componente | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por ITEM_COMPONENTE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_COMPONENTE** \| \|---\|---\| \| ID_ITEM \| ID_ITEM_COMPONENTE \| |
| [MODELO](dados_modelo) | \| **MODELO** \| **ITEM_COMPONENTE** \| \|---\|---\| \| ID_MODELO \| ID_MODELO \| |
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **ITEM_COMPONENTE** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **ITEM_COMPONENTE** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [ITEM](dados_item) | \| **ITEM** \| **ITEM_COMPONENTE** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela ITEM**

```
select ITEM_COMPONENTE.*, ITEM.DESCRICAO
from ITEM_COMPONENTE left outer join ITEM on ITEM_COMPONENTE.ID_ITEM_COMPONENTE = ITEM.ID_ITEM
```

**Exemplo 2: join com a tabela MODELO**

```
select ITEM_COMPONENTE.*, MODELO.DESCRICAO
from ITEM_COMPONENTE left outer join MODELO on ITEM_COMPONENTE.ID_MODELO = MODELO.ID_MODELO
```

**Exemplo 3: join com a tabela CLASSE_CONFIGURACAO**

```
select ITEM_COMPONENTE.*, CLASSE_CONFIGURACAO.DESCRICAO
from ITEM_COMPONENTE, CLASSE_CONFIGURACAO
where ITEM_COMPONENTE.ID_CLASSE_CONFIGURACAO = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

**Exemplo 4: join com a tabela ITEM**

```
select ITEM_COMPONENTE.*
from ITEM_COMPONENTE, ITEM
where ITEM_COMPONENTE.ID_ITEM = ITEM.ID_ITEM
```
