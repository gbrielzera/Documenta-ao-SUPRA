# TESTE_CONTROLE

Caminho: Customização > Modelo de dados > Processo > TESTE_CONTROLE

Ocorrências de Teste do Controle

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_OCORRENCIA** | Identificador da Ocorrencia associada | int | number(6,0) | Não |
| **ID_CONTROLE** | Identificador do(a) Controle associado(a) | int | number(6,0) | Não |
| **CRITERIO_SELECAO** | Critério de seleção utilizado na realização do Teste | text | clob | Sim |

Tabelas referenciadas por TESTE_CONTROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OCORRENCIA](dados_ocorrencia) | \| **OCORRENCIA** \| **TESTE_CONTROLE** \| \|---\|---\| \| ID_OCORRENCIA \| ID_OCORRENCIA \| |
| [CONTROLE](dados_controle) | \| **CONTROLE** \| **TESTE_CONTROLE** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |

**Exemplo 1: join com a tabela CONTROLE**

```
select TESTE_CONTROLE.*, CONTROLE.DESCRICAO
from TESTE_CONTROLE, CONTROLE
where TESTE_CONTROLE.ID_CONTROLE = CONTROLE.ID_CONTROLE
```
