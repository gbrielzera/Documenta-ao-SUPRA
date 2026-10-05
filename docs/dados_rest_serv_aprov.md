# REST_SERV_APROV

Caminho: Customização > Modelo de dados > Processo > REST_SERV_APROV

Restrição de Itens por Serviço ou Tipo de Serviço

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REST_SER_APROV** | Número sequencial gerado automaticamente pelo sistema para Identificar um RestricaoServicoAprovacao | int | number(6,0) | Não |
| **ID_CLASSE_APROVACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseAprovacao | int | number(6,0) | Não |
| **ID_SERVICO** | Identificador do Serviço | int | number(6,0) | Sim |
| **ID_CLASSE_SERVICO** | Identificador do Tipo de Serviço | int | number(6,0) | Não |

Tabelas referenciadas por REST_SERV_APROV

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SERVICO](dados_servico) | \| **SERVICO** \| **REST_SERV_APROV** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **REST_SERV_APROV** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [CLASSE_APROVACAO](dados_classe_aprovacao) | \| **CLASSE_APROVACAO** \| **REST_SERV_APROV** \| \|---\|---\| \| ID_CLASSE_APROVACAO \| ID_CLASSE_APROVACAO \| |

**Exemplo 1: join com a tabela SERVICO**

```
select REST_SERV_APROV.*, SERVICO.DESCRICAO
from REST_SERV_APROV left outer join SERVICO on REST_SERV_APROV.ID_SERVICO = SERVICO.ID_SERVICO
```

**Exemplo 2: join com a tabela CLASSE_APROVACAO**

```
select REST_SERV_APROV.*
from REST_SERV_APROV, CLASSE_APROVACAO
where REST_SERV_APROV.ID_CLASSE_APROVACAO = CLASSE_APROVACAO.ID_CLASSE_APROVACAO
```
