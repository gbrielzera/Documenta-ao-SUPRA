# REST_SERV_ANEXO

Caminho: Customização > Modelo de dados > Processo > REST_SERV_ANEXO

Restrições de Anexos por Serviço ou Tipo de Serviço.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REST_SERV_ANEXO** | Número sequencial gerado automaticamente pelo sistema para Identificar um RestricaoServicoAnexo | int | number(6,0) | Não |
| **ID_CLASSE_ANEXO** | Identificador da Classe para Associação. | int | number(6,0) | Não |
| **ID_SERVICO** | Identificador do Servico associado | int | number(6,0) | Sim |
| **ID_CLASSE_SERVICO** | Identificador do Tipo de Serviço associado | int | number(6,0) | Não |

Tabelas referenciadas por REST_SERV_ANEXO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SERVICO](dados_servico) | \| **SERVICO** \| **REST_SERV_ANEXO** \| \|---\|---\| \| ID_SERVICO \| ID_SERVICO \| |
| [CLASSE_SERVICO](dados_classe_servico) | \| **CLASSE_SERVICO** \| **REST_SERV_ANEXO** \| \|---\|---\| \| ID_CLASSE_SERVICO \| ID_CLASSE_SERVICO \| |
| [CLASSE_ANEXO](dados_classe_anexo) | \| **CLASSE_ANEXO** \| **REST_SERV_ANEXO** \| \|---\|---\| \| ID_CLASSE_ANEXO \| ID_CLASSE_ANEXO \| |

**Exemplo 1: join com a tabela SERVICO**

```
select REST_SERV_ANEXO.*, SERVICO.DESCRICAO
from REST_SERV_ANEXO left outer join SERVICO on REST_SERV_ANEXO.ID_SERVICO = SERVICO.ID_SERVICO
```

**Exemplo 2: join com a tabela CLASSE_ANEXO**

```
select REST_SERV_ANEXO.*
from REST_SERV_ANEXO, CLASSE_ANEXO
where REST_SERV_ANEXO.ID_CLASSE_ANEXO = CLASSE_ANEXO.ID_CLASSE_ANEXO
```
