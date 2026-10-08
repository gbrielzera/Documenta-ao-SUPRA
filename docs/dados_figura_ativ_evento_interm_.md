# FIGURA_ATIV_EVENTO_INTERM

Caminho: FIGURA_ATIV_EVENTO_INTERM

Relacionamento de Figuras de atividades com eventos intermediários

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_FIG_AT_EVENTO_INT** | Número sequencial gerado automaticamente pelo sistema para Identificar uma FiguraAtividadeEventoIntermediario | int | number(6,0) | Não |
| **ID_FIGURA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Figura | int | number(6,0) | Não |
| **ID_FIGURA_EVENTO_INTER** | Identificador da figura de evento intermediário | int | number(6,0) | Não |

Tabelas referenciadas por FIGURA_ATIV_EVENTO_INTERM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FIGURA](dados_figura) | \| **FIGURA** \| **FIGURA_ATIV_EVENTO_INTERM** \| \|---\|---\| \| ID_FIGURA \| ID_FIGURA_EVENTO_INTER \| |
| [FIGURA](dados_figura) | \| **FIGURA** \| **FIGURA_ATIV_EVENTO_INTERM** \| \|---\|---\| \| ID_FIGURA \| ID_FIGURA \| |

**Exemplo 1: join com a tabela FIGURA**

```
select FIGURA_ATIV_EVENTO_INTERM.*
from FIGURA_ATIV_EVENTO_INTERM, FIGURA
where FIGURA_ATIV_EVENTO_INTERM.ID_FIGURA = FIGURA.ID_FIGURA
```
