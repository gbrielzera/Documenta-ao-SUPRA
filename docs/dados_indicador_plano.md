# INDICADOR_PLANO

Caminho: Customização > Modelo de dados > Processo > INDICADOR_PLANO

Indicador de Plano de Gestão

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PLANO_GESTAO** | Identificador do Plano de Gestão | int | number(6,0) | Não |
| **ID_INDICADOR** | Identificador do(a) Indicador associado(a) | int | number(6,0) | Não |
| **META** | Meta estabelecida para o Indicador dentro do plano. Indicadores podem ter metas variadas entre Planos de Gestão distintos ou no mesmo Plano em Períodos distintos. Quando modificado são atualizados os Períodos cuja Meta é igual a valor antigo da Meta de Indicador. No painel de Indicadores do Executive Dashboard valores apurados acima da meta são exibidos na cor verde, enquanto valores abaixo da meta e acima da tolerância são exibidos em amarelo. Para valores apurados abaixo da meta e tolerância a exibição é feita na cor vermelha. Para valores acima da meta ainda existe a possibilidade de exibição na cor azul caso o valor seja também superior ao desafio estabelecido para o Indicador. | decimal(15,2) | number(15,2) | Não |
| **ID_RESPONSAVEL** | Identificador da Pessoa associada | int | number(6,0) | Não |
| **TOLERANCIA** | Indica a tolerância para atingir a meta. Valores apurados abaixo da meta e acima da tolerância (dependo do sentido do melhor resultado) são exibidos com farol Amarelo. | decimal(15,2) | number(15,2) | Não |
| **DESAFIO** | Valor acima da meta definido desafio no plano de metas da gestão. No painel de Indicadores do Executive Dashboard períodos que atingirem este valor são exibidos na cor azul. Assim como no campo Metas o Desafio pode ser redefinido nos diversos períodos do Plano de Gestão. | decimal(15,2) | number(15,2) | Sim |
| **RESTRITO_RESPONSAVEL** | Define que o indicador só será visivel ao Responsável ou seus Coordenadores de Grupo de Trabalho. | char(3) | char(3) | Não |

Tabelas referenciadas por INDICADOR_PLANO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [INDICADOR](dados_indicador) | \| **INDICADOR** \| **INDICADOR_PLANO** \| \|---\|---\| \| ID_INDICADOR \| ID_INDICADOR \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **INDICADOR_PLANO** \| \|---\|---\| \| ID_PESSOA \| ID_RESPONSAVEL \| |
| [PLANO_GESTAO](dados_plano_gestao) | \| **PLANO_GESTAO** \| **INDICADOR_PLANO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| |

Tabelas que dependem de INDICADOR_PLANO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PERIODO_PLANO](dados_periodo_plano) | \| **PERIODO_PLANO** \| **INDICADOR_PLANO** \| \|---\|---\| \| ID_PLANO_GESTAO \| ID_PLANO_GESTAO \| \| ID_INDICADOR \| ID_INDICADOR \| |

**Exemplo 1: join com a tabela INDICADOR**

```
select INDICADOR_PLANO.*, INDICADOR.DESCRICAO
from INDICADOR_PLANO, INDICADOR
where INDICADOR_PLANO.ID_INDICADOR = INDICADOR.ID_INDICADOR
```

**Exemplo 2: join com a tabela PLANO_GESTAO**

```
select INDICADOR_PLANO.*
from INDICADOR_PLANO, PLANO_GESTAO
where INDICADOR_PLANO.ID_PLANO_GESTAO = PLANO_GESTAO.ID_PLANO_GESTAO
```
