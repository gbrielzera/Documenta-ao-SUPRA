# ESCOPO_CLASSE_ANEXO

Caminho: Customização > Modelo de dados > Processo > ESCOPO_CLASSE_ANEXO

Relação de Tipos de Itens de Configuração que podem ser associados na ocorrência.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ESCOPO_CLASSE_ANEXO** | Número sequencial gerado automaticamente pelo sistema para Identificar um EscopoClasseAnexo | int | number(6,0) | Não |
| **ID_CLASSE_ANEXO** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseAnexo | int | number(6,0) | Não |
| **ID_CLASSE_CONFIGURACAO** | Identificador do Tipo de Item de Configuração que pode ter itens associados na ocorrência. Quando não preenchido o filtro é realizado apenas pelo super tipo. | int | number(6,0) | Sim |
| **SUPER_CLASSE** | Super tipo que pode ter itens associados na ocorrência. Se for preenchida o Tipo de Item de Configuração então este campo é preenchido automaticamente com o Super tipo correspondente. | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por ESCOPO_CLASSE_ANEXO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_CONFIGURACAO](dados_classe_configuracao) | \| **CLASSE_CONFIGURACAO** \| **ESCOPO_CLASSE_ANEXO** \| \|---\|---\| \| ID_CLASSE_CONFIGURACAO \| ID_CLASSE_CONFIGURACAO \| |
| [CLASSE_ANEXO](dados_classe_anexo) | \| **CLASSE_ANEXO** \| **ESCOPO_CLASSE_ANEXO** \| \|---\|---\| \| ID_CLASSE_ANEXO \| ID_CLASSE_ANEXO \| |

**Exemplo 1: join com a tabela CLASSE_ANEXO**

```
select ESCOPO_CLASSE_ANEXO.*
from ESCOPO_CLASSE_ANEXO, CLASSE_ANEXO
where ESCOPO_CLASSE_ANEXO.ID_CLASSE_ANEXO = CLASSE_ANEXO.ID_CLASSE_ANEXO
```
