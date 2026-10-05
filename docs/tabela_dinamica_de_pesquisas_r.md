# Tabela Dinamica de Pesquisas Respondidas

Caminho: Relatórios > Tabelas Dinâmicas > Tabela Dinamica de Pesquisas Respondidas

Atenção para entendimento correto deste tópico, recomenda-se leitura do tópico [Tabelas Dinâmicas](tabelas_dinamicas)

A Tabela Dinâmica de Pesquisas Respondidas possibilita ao usuário construir dinamicamente uma consulta relacionada com a listagem de resultados das [pesquisas de satisfação](pesquisas_de_satisfacao) que ocorreram nas Ordens de Serviço do Supravizio em um determinado período.

Além da Tabela Dinâmica poder ser iniciada pelo menu, ela também pode ser iniciada pelo fluxograma de uma Ordem de Serviço (Clique com o botão direito no finalizador da Ordem de Serviço), que então automaticamente será aberta uma tabela dinâmica com filtro para Pesquisas geradas e respondidas pelo finalizador:

Tabela Dinâmica pelo Fluxograma

Através dela o usuário poderá, por exemplo, contabilizar o Total de pesquisas respondidas levando em consideração, por exemplo, informações do Tipo de Pesquisa e informações de Subprocessos.

Tabela dinâmica de Pesquisas Respondidas

**Filtros Disponíveis**

A Tabela Dinâmica de Pesquisas Respondidas disponibiliza os seguintes campos para a configuração de um relatório:

Dados disponíveis na tabela

Os dados das tabelas são relacionadas com Pesquisas de Satisfação relacionadas com suas respectivas Ordens de Serviço.

| **Avaliador** | Avaliadores de pesquisas de satisfação (Cliente). |
|---|---|
| **Empresa Avaliador** | Empresa dos Avaliadores. |
| **Grupo Responsável Final** | Grupo de Trabalho Responsável ao fim das Ordens de Serviço. |
| **Local** | Local informado no cadastro do Avaliador da Pesquisa de Satisfação. |
| **Macroprocesso** | Macroprocesso referente ao Processo da Ordem de Serviço na qual gerou a Pesquisa de Satisfação. |
| **Área Avaliador** | Área dos Avaliadores. |
| **Prédio** | Prédio do local informado no cadastro do Avaliador da Pesquisa de Satisfação. |
| **Processo** | Processo da Ordem de Serviço na qual gerou a Pesquisa de Satisfação. |
| **Serviço** | Serviço da Ordem de Serviço na qual gerou a Pesquisa de Satisfação. |
| **Solucionador Final** | Solucionador no final da Ordem de Serviço. |
| **Subprocesso** | Subprocesso da Ordem de Serviço na qual gerou a Pesquisa de Satisfação. |
| **Tipo Pesquisa** | Descrição do Tipo de Pesquisa. |
| **Tipo Serviço** | Tipo de Serviço (Classes de serviços). |
| **Total Respostas** | Total de Questões de Pesquisas de Satisfação respondidas (totalizador). |
| **Total Respostas Negativas** | Total de Questões de Pesquisas de Satisfação com resultados negativos (totalizador). As respostas consideradas negativas, são as que possuem escore menor que 0 configurado ([em grupo de questões](itempesquisa_sub) de [pesquisa de satisfação](pesquisa_sub)). |
| **Total Respostas Positivas** | Total de Questões de Pesquisas de Satisfação com resultados positivos (totalizador).As respostas consideradas positivas, são as que possuem escore maior ou igual a 0 configurado ([em grupo de questões](itempesquisa_sub) de [pesquisa de satisfação](pesquisa_sub)). |
| **Unidade de Negócio** | [Unidade de Negócio](unidadenegocio_sub) do local informado no cadastro do Avaliador da Pesquisa de Satisfação. |

**Especificação de dados dos campos de filtro**

## Exemplos

### Exemplo 1:

Linhas: Solucionador Final

Colunas:

Totalizadores: Total Respostas, Total Respostas Negativas

Tabela Dinâmica Exemplo 1

### Exemplo 2:

Linhas: Avaliador (Cliente)

Colunas:

Totalizadores: Total Respostas, Total Respostas Negativas

Tabela Dinâmica Exemplo 2

### Exemplo 3:

Linhas: Subprocesso

Colunas: Solucionador final

Totalizadores: Total Respostas, Total Respostas Negativas

Tabela Dinâmica Exemplo 3

### Exemplo 4:

Linhas: Macroprocesso, Subprocesso, Serviço

Colunas: Grupo responsável final, Solucionador final

Totalizadores: Total Respostas, Total Respostas Positivas

Tabela Dinâmica Exemplo 4

### Exemplo 5:

Linhas:Unidade de Negócio, Prédio, Local, Avaliador

Colunas:

Totalizadores: Total respostas

Tabela Dinâmica Exemplo 5

Obs: note o resultado se o avaliador não tiver nenhum local preenchido.
