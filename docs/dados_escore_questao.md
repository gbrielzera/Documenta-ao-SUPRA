# ESCORE_QUESTAO

Caminho: Customização > Modelo de dados > Processo > ESCORE_QUESTAO

Escore de Questão

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ESCORE** | Número sequencial gerado automaticamente pelo sistema para Identificar um Escore | int | number(6,0) | Não |
| **ID_GRUPO_QUESTAO** | Número sequencial gerado automaticamente pelo sistema para Identificar um GrupoQuestao | int | number(6,0) | Não |
| **SEQUENCIAL** | Define a sequência de apresentação da opção de resposta. | int | number(6,0) | Não |
| **ROTULO** | Descritivo apresentado para o usuário como opção. Exemplos: Ótimo, Péssimo, Bom. | varchar(500) | varchar(500) | Não |
| **VALOR** | Valor atribuído a opção de resposta. Este valor pode ser comparado em fórmulas de cálculo de Indicadores de Desempenho. | int | number(6,0) | Não |

Tabelas referenciadas por ESCORE_QUESTAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_QUESTAO](dados_grupo_questao) | \| **GRUPO_QUESTAO** \| **ESCORE_QUESTAO** \| \|---\|---\| \| ID_GRUPO_QUESTAO \| ID_GRUPO_QUESTAO \| |

**Exemplo 1: join com a tabela GRUPO_QUESTAO**

```
select ESCORE_QUESTAO.*
from ESCORE_QUESTAO, GRUPO_QUESTAO
where ESCORE_QUESTAO.ID_GRUPO_QUESTAO = GRUPO_QUESTAO.ID_GRUPO_QUESTAO
```
