# APURACAO_INDICADOR

Caminho: Customização > Modelo de dados > Processo > APURACAO_INDICADOR

Valores apurador para um Indicador de Desempenho

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_INDICADOR** | Identificador do(a) Indicador associado(a) | int | number(6,0) | Não |
| **MES** | Mês | int | number(6,0) | Não |
| **ANO** | Ano | int | number(6,0) | Não |
| **SEQUENCIA** | Sequencia | int | number(6,0) | Não |
| **ID_PLANO_GESTAO** | Identificador do Plano de Gestão proprietário da apuração | int | number(6,0) | Não |
| **ID_ORGAO_CLIENTE** | Identificador do Orgao solicitante | int | number(6,0) | Não |
| **VALOR** | Valor apurado para o Indicador | decimal(15,2) | number(15,2) | Não |
| **DATA_HORA_APURACAO** | Data e hora em que foi apurado o valor do Indicador | datetime | date | Não |
| **RITMO_NUMERADOR** | Valor do Numerador utilizado na razao para cálculo de Ritmo. Este valor só é importante em Indicadores que realizem Contagem (Count). | int | number(6,0) | Sim |
| **RITMO_DENOMINADOR** | Valor do denominador da razão utilizada para cálculo de Ritmo. Este valor só é importante em Indicadores que realizem Contagem (Count). | int | number(6,0) | Sim |
| **RITMO_VALOR** | Valor de Ritmo do Indicador estimado até fim do Período associado. Este valor será igual ao Valor apurado se o período estiver finalizado e só é importante em Indicadores que realizem Contagem (Count). | decimal(15,2) | number(15,2) | Sim |
| **TIPO_APURACAO** | Tipo de dado Apurado. | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **NUMERADOR** | Numerador para apuração de indicadores que possuem como função de agregação Percentual | decimal(15,2) | number(15,2) | Sim |
| **DENOMINADOR** | Denominador para apuração de indicadores que possuem como função de agregação Percentual | decimal(15,2) | number(15,2) | Sim |
| **MEMORIA** | Memória de cálculo com as chaves e valores. Formato: {IdObjeto}{S=atendeu critério;N=não atendeu critério}, ex: 1028S (Id igual 1028 e atendeu critério) | varbinary(4000) | blob | Sim |

Tabelas referenciadas por APURACAO_INDICADOR

| **Tabela** | **Colunas de ligação** |
|---|---|
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **APURACAO_INDICADOR** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |
| [PLANO_GESTAO](dados_plano_gestao) | \| **PLANO_GESTAO** \| **APURACAO_INDICADOR** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **APURACAO_INDICADOR** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO_CLIENTE \| |

**Exemplo 1: join com a tabela INDICADOR**

```
select APURACAO_INDICADOR.*, INDICADOR.DESCRICAO
from APURACAO_INDICADOR, INDICADOR
where APURACAO_INDICADOR.ID_INDICADOR = INDICADOR.ID_INDICADOR
```

**Exemplo 2: join com a tabela PLANO_GESTAO**

```
select APURACAO_INDICADOR.*, PLANO_GESTAO.DESCRICAO
from APURACAO_INDICADOR, PLANO_GESTAO
where APURACAO_INDICADOR.ID_PLANO_GESTAO = PLANO_GESTAO.ID_PLANO_GESTAO
```
