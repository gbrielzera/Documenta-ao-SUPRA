# Tabela Dinamica de Atividades Executadas

Caminho: Relatórios > Tabelas Dinâmicas > Tabela Dinamica de Atividades Executadas

Atenção Para Entendimento correto deste tópico, recomenda-se leitura do tópico [Tabelas Dinâmicas](tabelas_dinamicas)

A Tabela Dinâmica de Atividades executadas possibilita ao usuário construir dinamicamente uma consulta relacionada com a listagem de Atividades das Ordens de Serviço do Supravizio em um determinado período.

Além da Tabela Dinâmica poder ser iniciada pelo menu, ela também pode ser iniciada pelo Editor de Processos ou mesmo pelo fluxograma de uma Ordem de Serviço (Clique com o botão direito no finalizador da Ordem de Serviço) que então automaticamente será aberta uma tabela dinâmica com filtro para execução das atividades selecionadas:

Tabela Dinâmica pelo Editor de Processos

Tabela Dinâmica pelo Fluxograma

Através dela o usuário poderá, por exemplo, contabilizar as Atividades Executadas das Ordens de Serviço levando em consideração, por exemplo, informações relacionadas com os Clientes, associados aos Solucionadores.

Tabela dinâmica de Atividades Executadas

A Tabela Dinâmica de Atividades Executadas disponibiliza os seguintes campos para a configuração de um relatório:

Dados disponíveis na tabela

Os dados das tabelas são relacionados com suas respectivas Atividades de Ordens de Serviço.

| **Atividade** | Atividade da ordem de serviço exercida. |
|---|---|
| **Cliente** | Cliente da Ordem de Serviço na qual a Atividade foi executada. |
| **Conformidade de Papel** | Correspondência da Conformidade de Papéis (Retorno booleano, 0 para não e 1 para sim, Totalizador). |
| **Empresa Cliente** | Empresa Cliente da Ordem de Serviço na qual a Atividade foi executada. |
| **Execução Automática** | Execução Automática (Retorno booleano, 0 para não e 1 para sim, Totalizador). |
| **Finalização** | Data de Finalização da Atividade executada. |
| **Finalização (Semana)** | Semana do mês da Finalização da Atividade executada (Varia de 1 até 5). |
| **Grupo de Trabalho** | Grupo de Trabalho do Solucionador da Atividade executada |
| **HH Médio** | Quantidade de horas apontadas em média. |
| **HH Total** | Quantidade de horas apontadas totais. |
| **Macroprocesso** | Macroprocesso referente ao Processo da Ordem de Serviço na qual a Atividade foi executada. |
| **Área Cliente** | Área Cliente da Ordem de Serviço na qual a Atividade foi executada. |
| **Processo** | Processo relativo a Ordem de Serviço na qual a Atividade foi executada. |
| **Quantidade** | Quantidade (totalizador). |
| **Serviço** | Serviço da Ordem de Serviço na qual a Atividade foi executada. |
| **Solucionador** | Solucionador da Atividade executada. |
| **Subprocesso** | Subprocesso da Ordem de Serviço na qual a Atividade foi executada. |
| **Tempo corrido médio** | Tempo corrido médio da Atividade executada. |
| **Tempo corrido total** | Tempo corrido total da Atividade executada. |
| **Tempo útil médio** | Tempo útil médio (No tempo líquido é contabilizado apenas o "[período útil de serviço](periodoutil_sub)" configurado em [calendários](calendario_sub)). |
| **Tempo útil total** | Tempo útil total (No tempo líquido é contabilizado apenas o "[período útil de serviço](periodoutil_sub)" configurado em [calendários](calendario_sub)). |
| **Tempo útil s/ paradas ANS médio** | Tempo útil s/ paradas ANS médio é uma contagem de tempo relativo ao "Tempo útil médio", que contabiliza o tempo dentro do calendário, porém não adiciona as paradas de ANS. |
| **Tempo útil s/ paradas ANS total** | Tempo útil s/ paradas ANS total é uma contagem de tempo relativo ao "Tempo útil total", que contabiliza o tempo dentro do calendário, porém não adiciona as paradas de ANS. |
| **Tipo Serviço** | Tipo de Serviço da Ordem de Serviço na qual a Atividade foi executada (Classes de serviços). |
| **Versão de Processo** | Versão do Processo na qual a Atividade foi executada. |

**Especificação de dados dos campos de filtro**

## Exemplos

### Exemplo 1:

Linhas: Processo, Subprocesso

Colunas: Versão de Processo

Totalizadores: Quantidade

Tabela Dinâmica Exemplo 1

### Exemplo 2:

Linhas: Processo, Subprocesso

Colunas: Versão de Processo

Totalizadores: Conformidade Papel

Tabela Dinâmica Exemplo 2

### Exemplo 3:

Linhas: Processo, Subprocesso

Colunas: Área Cliente

Totalizadores: HH Médio

Tabela Dinâmica Exemplo 3

Atividades Canceladas

As atividades canceladas, que podemos visualizar na tela de Ordem de Serviço na aba de Informações sobre Processo, depois na aba de Atividades Canceladas, são contabilizadas em algumas tabelas dinâmicas como a [Tabela Dinâmica de Ordens de Serviço](tabela_dinamica_de_ordens_de_s) e a [Tabela Dinâmica de Atividades Executadas](tabela_dinamica_de_atividades_).

Ordem de Serviço - Atividades Canceladas

Nesta Ordem de Serviço, a atividade cancelada foi a "Tarefa: Testar", na qual foi cancelada duas vezes.

Podemos observar no fluxo, que a atividade atual é a "Construir" e não foi avançada para a "Testar" já que ela foi cancelada:

Fluxo da Ordem de Serviço
