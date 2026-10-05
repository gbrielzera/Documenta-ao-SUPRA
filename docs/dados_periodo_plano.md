# PERIODO_PLANO

Caminho: Customização > Modelo de dados > Processo > PERIODO_PLANO

Período de Plano de Gestão

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **MES** | Mês | int | number(6,0) | Não |
| **ANO** | Ano | int | number(6,0) | Não |
| **ID_PLANO_GESTAO** | Identificador do Plano de Gestão | int | number(6,0) | Não |
| **ID_INDICADOR** | Identificador do(a) Indicador associado(a) | int | number(6,0) | Não |
| **META** | Meta estabelecida para o Indicador no mês e ano do período. Pode ser atualizado automaticamente quando for modificada a Meta geral do Indicador (atualizado somente se a Meta do período for igual a Meta anterior do Indicador). | decimal(15,2) | number(15,2) | Não |
| **VALOR_APURADO** | Valor apurado para Indicadores de Desempenho cujo provedor de dados for igual a Lançamento Manual. | decimal(15,2) | number(15,2) | Sim |
| **ANOT_GERAL** | Anotação geral sobre dados apurados para o Indicador no Período. | varchar(500) | varchar(500) | Sim |
| **ANOT_CAUSA** | Anotação sobre causa | varchar(500) | varchar(500) | Sim |
| **ANOT_PERSPECT** | Perspectiva observada para valor apurado do Indicador no Período | varchar(500) | varchar(500) | Sim |
| **ANOT_PROV** | Proviência tomada sobre apuração do Indicador no Período | varchar(500) | varchar(500) | Sim |
| **DESAFIO** | Valor acima da meta definido desafio no plano de metas da gestão. No painel de Indicadores do Executive Dashboard períodos que atingirem este valor são exibidos na cor azul. Assim como no campo Metas o Desafio pode ser redefinido nos diversos períodos do Plano de Gestão. | decimal(15,2) | number(15,2) | Sim |

Tabelas referenciadas por PERIODO_PLANO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [INDICADOR_PLANO](dados_indicador_plano) | \| **INDICADOR_PLANO** \| **PERIODO_PLANO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| \| ID_INDICADOR \| ID_INDICADOR \| |
