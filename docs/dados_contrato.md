# CONTRATO

Caminho: Customização > Modelo de dados > Recurso > CONTRATO

Um Contrato relaciona recursos (pessoas), Itens de configuração e regras para apontamento de horas trabalhadas. Além destas informações o contrato possui uma vigência, um fornecedor e um contratante. Um contrato pode ser informado em uma Ordem de Serviço por meio de um campo nativo denominado Contrato. Este campo é editado em um controle do tipo DropDownList contendo os contratos vigentes do Cliente da Ordem de Serviço. O Contrato é visível para seu gestor na aplicação de Autoatendimento, onde é possível acompanhar os apontamentos associados.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CONTRATO** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada do Contrato | varchar(500) | varchar(500) | Não |
| **DATA_INICIO_VALIDADE** | Data início de Validade do Contrato | datetime | date | Não |
| **DATA_FIM_VALIDADE** | Data de fim de Validade do Contrato | datetime | date | Não |
| **ID_CONTRATANTE** | Identificador do Orgao Contratante do Serviço | int | number(6,0) | Não |
| **ID_FORNECEDOR** | Identificador do Fornecedor associado | int | number(6,0) | Não |
| **CODIGO_REFERENCIA** | Código do contrato gerado pela área de suprimentos. | varchar(500) | varchar(500) | Sim |
| **ID_RESPONSAVEL** | Identificador da Pessoa associada | int | number(6,0) | Não |
| **RESPONSAVEL_FORNECEDOR** | Nome da pessoa responsavável pelo Contrato pelo Fornecedor contratado. | varchar(500) | varchar(500) | Sim |
| **CONTATO_FORNECEDOR** | Telefone ou email de contato com Responsável pelo Contrato pelo Fornecedor. | varchar(500) | varchar(500) | Sim |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **ID_PLANO_GESTAO** | Identificador do Plano de Gestão | int | number(6,0) | Sim |
| **FORMA_APONTAMENTO** | Forma de definição de apontamentos, se por total de horas ou por período | varchar(250) | varchar(250) | Não |
| **PUBLICA_VIGENCIA_AA** | Publicar a vigência do contrato (data de início e fim de validade) na página de contratos do Autoatendimento | char(3) | char(3) | Não |

Tabelas referenciadas por CONTRATO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **CONTRATO** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |
| [FORNECEDOR](dados_fornecedor) | \| **FORNECEDOR** \| **CONTRATO** \| \|---\|---\| \|  \| ID_FORNECEDOR \| |
| [EMPRESA](dados_empresa) | \| **EMPRESA** \| **CONTRATO** \| \|---\|---\| \| ID_EMPRESA \| ID_CONTRATANTE \| |
| [PLANO_GESTAO](dados_plano_gestao) | \| **PLANO_GESTAO** \| **CONTRATO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |

Tabelas que dependem de CONTRATO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [RECURSO_APLICADO](dados_recurso_aplicado) | \| **RECURSO_APLICADO** \| **CONTRATO** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| |
| [CONTRATO_ITEM](dados_contrato_item) | \| **CONTRATO_ITEM** \| **CONTRATO** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| |
| [TIPO_APONT_CONT](dados_tipo_apont_cont) | \| **TIPO_APONT_CONT** \| **CONTRATO** \| \|---\|---\| \| ID_CONTRATO \| ID_CONTRATO \| |

**Exemplo 1: join com a tabela PESSOA**

```
select CONTRATO.*, PESSOA.NOME_ABREVIADO
from CONTRATO, PESSOA
where CONTRATO.ID_RESPONSAVEL = PESSOA.ID_PESSOA
```

**Exemplo 2: join com a tabela EMPRESA**

```
select CONTRATO.*, EMPRESA.DESCRICAO
from CONTRATO, EMPRESA
where CONTRATO.ID_CONTRATANTE = EMPRESA.ID_EMPRESA
```
