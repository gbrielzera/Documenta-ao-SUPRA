# ITEM

Caminho: Customização > Modelo de dados > Ativos > ITEM

Classe abstrata para todos os Itens de Configuração do CMDB

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ITEM** | Número sequencial gerado automaticamente para Identificar um Item de Configuração | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada sobre o Item de configuração | varchar(500) | varchar(500) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item associado | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_SITUACAO_CLASSE** | Identificador da Situação corrente do Item | int | number(6,0) | Não |
| **DATA_EXPIRACAO_GARANTIA** | Data para Expiração de uma eventual garantia | datetime | date | Sim |
| **LOCALIZACAO** | Localização do Item. Pode ser um local físico ou pessoa que utiliza | varchar(500) | varchar(500) | Sim |
| **ID_TIPO_POSSE** | Identificador do Tipo de Posse | int | number(6,0) | Sim |
| **ID_MODELO** | Identificador do Modelo | int | number(6,0) | Sim |
| **NUMERO_SERIE** | Número de série do Item | varchar(500) | varchar(500) | Sim |
| **ID_EMPRESA** | Identificador do Fornecedor | int | number(6,0) | Sim |
| **DATA_ENTREGA** | Data em que o Item foi entregue | datetime | date | Sim |
| **DATA_ACEITE** | Data de aceite do Item | datetime | date | Sim |
| **COMENTARIO** | Comentário sobre o Item destinados ao Cliente. Para histórico de observações utilize a relação de Observações. | varchar(500) | varchar(500) | Sim |
| **CUSTO_AQUISICAO** | Custom total de aquisição do Item | decimal(15,2) | number(15,2) | Sim |
| **DATA_PRODUCAO** | Data de entrada em Produção. | datetime | date | Sim |
| **DATA_DESATIVACAO** | Data de desativação do Item. | datetime | date | Sim |
| **CUSTO_MANUTENCAO** | Valor do Custo de Manutenção Mensal do Item | decimal(15,2) | number(15,2) | Sim |
| **ID_FATOR_PRIORIDADE** | Identificador do(a) FatorPrioridade associado(a) | int | number(6,0) | Sim |
| **ID_RESPONSAVEL** | Identificador da Pessoa associada | int | number(6,0) | Sim |
| **PRECO_AQUISICAO** | Preço de aquisição do Item para demonstrativo de custeio pela rotina de Charge-back. O valor de aquisição é lançado no charge-back de competência relativa a Data de Entrega do Ativo. | decimal(15,2) | number(15,2) | Sim |
| **PRECO_MANUTENCAO** | Preço de Charge-back de manutenção mensal | decimal(15,2) | number(15,2) | Sim |
| **DATA_CADASTRO** | Data em que o Item de Configuração foi cadastrado no sistema. | datetime | date | Não |
| **CRIT_CHARGE_BACK** | Critério para destino de custo no cálculo de Charge-back. | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **ITEM** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [SITUACAO_CLASSE](dados_situacao_classe) | \| **SITUACAO_CLASSE** \| **ITEM** \| \|---\|---\| \| ID_SITUACAO_CLASSE \| ID_SITUACAO_CLASSE \| |
| [TIPO_POSSE](dados_tipo_posse) | \| **TIPO_POSSE** \| **ITEM** \| \|---\|---\| \| ID_TIPO_POSSE \| ID_TIPO_POSSE \| |
| [MODELO](dados_modelo) | \| **MODELO** \| **ITEM** \| \|---\|---\| \| ID_MODELO \| ID_MODELO \| |
| [FORNECEDOR](dados_fornecedor) | \| **FORNECEDOR** \| **ITEM** \| \|---\|---\| \|  \| ID_EMPRESA \| |
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **ITEM** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **ITEM** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |

Tabelas que dependem de ITEM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ITEM_COMPONENTE](dados_item_componente) | \| **ITEM_COMPONENTE** \| **ITEM** \| \|---\|---\| \| ID_ITEM_COMPONENTE \| ID_ITEM \| |
| [ITEM_DEPENDENCIA](dados_item_dependencia) | \| **ITEM_DEPENDENCIA** \| **ITEM** \| \|---\|---\| \| ID_DEPENDENCIA \| ID_ITEM \| |
| [ITEM_COPIA](dados_item_copia) | \| **ITEM_COPIA** \| **ITEM** \| \|---\|---\| \| ID_ITEM_COPIA \| ID_ITEM \| |
| [ITEM_DEPENDENCIA](dados_item_dependencia) | \| **ITEM_DEPENDENCIA** \| **ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [ITEM_COMPONENTE](dados_item_componente) | \| **ITEM_COMPONENTE** \| **ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [OBSERVACAO_ITEM](dados_observacao_item) | \| **OBSERVACAO_ITEM** \| **ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [ITEM_COPIA](dados_item_copia) | \| **ITEM_COPIA** \| **ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [USUARIO_ITEM](dados_usuario_item) | \| **USUARIO_ITEM** \| **ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [ATOR_ITEM](dados_ator_item) | \| **ATOR_ITEM** \| **ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |
| [HISTORICO_ITEM](dados_historico_item) | \| **HISTORICO_ITEM** \| **ITEM** \| \|---\|---\| \| ID_ITEM \| ID_ITEM \| |

**Exemplo 1: join com a tabela CLASSE_CONFIGURACAO**

```
select ITEM.*, CLASSE_CONFIGURACAO.DESCRICAO
from ITEM, CLASSE_CONFIGURACAO
where ITEM.ID_CLASSE_CONFIGURACAO = CLASSE_CONFIGURACAO.ID_CLASSE_CONFIGURACAO
```

**Exemplo 2: join com a tabela SITUACAO_CLASSE**

```
select ITEM.*, SITUACAO_CLASSE.NOME
from ITEM, SITUACAO_CLASSE
where ITEM.ID_SITUACAO_CLASSE = SITUACAO_CLASSE.ID_SITUACAO_CLASSE
```

**Exemplo 3: join com a tabela TIPO_POSSE**

```
select ITEM.*, TIPO_POSSE.DESCRICAO
from ITEM left outer join TIPO_POSSE on ITEM.ID_TIPO_POSSE = TIPO_POSSE.ID_TIPO_POSSE
```

**Exemplo 4: join com a tabela MODELO**

```
select ITEM.*, MODELO.DESCRICAO
from ITEM left outer join MODELO on ITEM.ID_MODELO = MODELO.ID_MODELO
```

**Exemplo 5: join com a tabela FATOR_PRIORIDADE**

```
select ITEM.*, FATOR_PRIORIDADE.DESCRICAO
from ITEM left outer join FATOR_PRIORIDADE on ITEM.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```
