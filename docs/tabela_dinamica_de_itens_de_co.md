# Tabela Dinâmica de Itens de Configuração

Caminho: Relatórios > Tabelas Dinâmicas > Tabela Dinâmica de Itens de Configuração

Atenção para entendimento correto deste tópico, recomenda-se leitura do tópico [Tabelas Dinâmicas](tabelas_dinamicas)

A Tabela Dinâmica de itens de configuração possibilita ao usuário construir dinamicamente uma consulta relacionada com de itens de configuração (Equipamentos, Software, Dispositivos telefônicos, Artigos da Base de conhecimento e Artefatos) permitindo também associação com Ordens de Serviço.

**Itens de configuração associados**

Através dela o usuário poderá, por exemplo, contabilizar a Quantidade de Itens de configuração, a Quantidade média de Ordens de Serviço associadas ao item de configuração e a Quantidade de Ordens de Serviço associadas levando em consideração, por exemplo, informações do Tipo de item.

Tabela dinâmica de Itens de Configuração

**Filtros Disponíveis**

A Tabela Dinâmica de itens de Configuração disponibiliza os seguintes campos para a configuração de um relatório:

Dados disponíveis na tabela

Os dados das tabelas são relacionadas com os Itens de configuração.

| **Custo aquisição** | Custo de aquisição do item de configuração. |
|---|---|
| **Custo aquisição médio** | Custo de aquisição médio dos itens de configuração. |
| **Custo mensal** | Custo mensal do item de configuração. |
| **Custo mensal médio** | Custo mensal médio dos itens de configuração. |
| **Data cadastro** | Data de cadastro do item de configuração. |
| **Descrição** | Descrição do item de configuração. |
| **Empresa responsável** | Empresa responsável pelo Item de configuração. |
| **Fabricante** | Fabricante do Item de configuração. |
| **Local** | local informado no cadastro do Item de configuração. |
| **Média Ordens Serviço** | Quantidade Média de Ordens de Serviço associadas ao Item de configuração. |
| **Mês cadastro** | mês de cadastro do Item de configuração |
| **Modelo** | Modelo do item de configuração. |
| **Área responsável** | Área responsável do item de configuração. |
| **Preço aquisição (Charge-back)** | Preço de aquisição do item de configuração (custo para o cliente). |
| **Preço aquisição médio (Charge-back)** | Preço de aquisição médio dos itens de configuração (custo para o cliente). |
| **Preço mensal (Charge-back)** | Preço mensal do item de configuração (custo para o cliente). |
| **Preço mensal médio (Charge-back)** | Preço mensal médio dos itens de configuração (custo para o cliente). |
| **Prédio** | Prédio do local informado no cadastro do Item de configuração. |
| **Quant. média usuários** | Quantidade média de usuários do item de configuração (obtida pela relação de usuários do próprio item de configuração). |
| **Quant. usuários** | Filtro por Quantidade de usuários do item de configuração (obtida pela relação de usuários do próprio item de configuração). |
| **Quantidade** | Quantidade total do Item de configuração. |
| **Quantidade Ordens Serviço** | Quantidade de Ordens de Serviço associadas ao item de configuração (Totalizador). |
| **Responsável** | Responsável pelo item de configuração. |
| **Responsável ativo** | Responsáveis ativos (verdadeiro ou falso, utilizado como Totalizador). |
| **Situação** | Situação do item de configuração. |
| **Super tipo** | Super tipo de item de configuração. |
| **Tipo de item** | Tipo de item de configuração. |
| **Tipo posse** | Tipo de posse do item de configuração. |
| **Unidade de Negócio** | [Unidade de Negócio](unidadenegocio_sub) do local informado no cadastro do Item de configuração. |

**Especificação de dados dos campos de filtro**

**Outros filtros:**

Especificamente no relatório de Itens de configuração, há dois filtros diferentes. O filtro de Tipo de Item e o de Subprocesso:

**Filtros específicos**

Tanto o filtro de itens de configuração quanto o de tipos de Subprocessos podem restringir o resultado da consulta, e é necessário definir ao menos um tipo de item de configuração (para todas consultas dessa tabela dinâmica obterem resultado) e é necessário definir ao menos um tipo de subprocesso (para utilizar campos relacionados com Ordens de Serviço)**.**

Exemplos

Nos exemplos 1 e 2 é utilizado o seguinte filtro por tipo de item de configuração:

Filtro utilizado nos exemplos 1 e 2

Nos exemplo 3 é utilizado o seguinte filtro por tipo de item de configuração:

Filtro utilizado nos exemplo 3

### Exemplo 1:

Filtro de Tipo de Itens: Equipamentos (Desktop, Impressora, Notebook e Servidor)

Linhas: Unidade de Negócio

Colunas:

Totalizadores: Quantidade

**Tabela Dinâmica Exemplo 1**

### Exemplo 2:

Filtro de Tipo de Itens: Equipamentos (Desktop, Impressora, Notebook e Servidor)

Linhas: Área responsável

Colunas: Modelo

Totalizadores: Quantidade

**Tabela Dinâmica Exemplo 2**

### Exemplo 3:

Filtro de Tipo de Itens: Base de Conhecimento (Problema Conhecido)

Linhas: Situação

Colunas:

Totalizadores: Quantidade

**Tabela Dinâmica Exemplo 3**
