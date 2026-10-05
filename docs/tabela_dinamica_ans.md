# Tabela Dinâmica de interrupções de ANS

Caminho: Relatórios > Tabelas Dinâmicas > Tabela Dinâmica de interrupções de ANS

Atenção para entendimento correto deste tópico, recomenda-se leitura do tópico [Tabelas Dinâmicas](tabelas_dinamicas)

A Tabela Dinâmica de [interrupção de ANS](acordo_de_nivel_servico) possibilita ao usuário construir dinamicamente uma consulta relacionada com a listagem de interrupções de ANS que ocorreram nas Ordens de Serviço do Supravizio em um determinado período.

Através dela o usuário poderá, por exemplo, contabilizar o Tempo de interrupção médio levando em consideração, por exemplo, informações do Tipo de Serviço e informações de Macroprocessos.

Tabela dinâmica de Interrupção de ANS

**Filtros Disponíveis**

A Tabela Dinâmica de interrupção de ANS disponibiliza os seguintes campos para a configuração de um relatório:

Dados disponíveis na tabela

Os dados das tabelas são relacionadas com interrupções de ANS relacionadas com suas respectivas Ordens de Serviço.

| **Acordo** | Filtro por tipo de Acordo de Nível de Serviço (ANS). |
|---|---|
| **Cliente** | Filtro por Cliente. |
| **Empresa Cliente** | Filtro por Empresa Cliente. |
| **Grupo Trabalho** | Filtro por Grupo de Trabalho. |
| **Macroprocesso** | Filtro por Macroprocessos. |
| **Motivo** | Filtro por Motivo de interrupção do ANS. |
| **Área Cliente** | Filtro por Área Cliente. |
| **Processo** | Filtro por Processo. |
| **Serviço** | Filtro por Serviço. |
| **Solucionador** | Filtro por Solucionador. |
| **Subprocesso** | Filtro por Subprocesso. |
| **Tempo interrupção médio** | Filtro por Tempo de interrupção médio. |
| **Tempo manual médio** | Filtro por Tempo de interrupção manual médio (Interrupções automáticas não são contabilizadas). |
| **Tempo processo médio** | Filtro por Tempo de interrupção automática médio (Interrupções manuais não são contabilizadas). |
| **Tipo Serviço** | Filtro por Tipo de Serviço (Classes de serviços). |

**Especificação de dados dos campos de filtro**

## Exemplos

### Exemplo 1:

Linhas: Solucionador

Colunas:

Totalizadores: Tempo interrupção médio, Tempo manual médio, Tempo processo médio

Tabela Dinâmica Exemplo 1

### Exemplo 2:

Linhas: Motivo

Colunas:

Totalizadores: Tempo interrupção médio, Tempo manual médio, Tempo processo médio

Tabela Dinâmica Exemplo 2

### Exemplo 3:

Linhas: Grupos de Trabalho, Solucionadores

Colunas:

Totalizadores: Tempo interrupção médio, Tempo manual médio, Tempo processo médio

Tabela Dinâmica Exemplo 3

### Exemplo 4:

Linhas: Acordo, Motivo

Colunas: Grupo de Trabalho

Totalizadores: Tempo interrupção médio

Tabela Dinâmica Exemplo 4

### Exemplo 5:

Linhas: Área Cliente, Cliente

Colunas: Acordo, Motivo

Totalizadores: Tempo Interrupção Médio

Tabela Dinâmica Exemplo 5

### Exemplo 6:

Linhas: Cliente

Colunas: Motivo

Totalizadores: Tempo interrupção Médio

Tabela Dinâmica Exemplo 6
