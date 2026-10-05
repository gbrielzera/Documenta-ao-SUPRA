# Tabela Dinâmica de Ordens de Serviço

Caminho: Relatórios > Tabelas Dinâmicas > Tabela Dinâmica de Ordens de Serviço

Atenção Para Entendimento correto deste tópico, recomenda-se leitura do tópico [Tabelas Dinâmicas](tabelas_dinamicas)

A Tabela Dinâmica de Ordens de Serviço possibilita ao usuário construir dinamicamente uma consulta relacionada com a listagem de Ordens de Serviço do Supravizio em um determinado período.

Além da Tabela Dinâmica poder ser iniciada pelo menu, ela também pode ser iniciada pelo Editor de Processos, que então automaticamente será aberta uma tabela dinâmica com filtro para Ordens de Serviços que executaram as atividades selecionadas:

Tabela Dinâmica pelo Editor de Processos

Através dela o usuário poderá, por exemplo, contabilizar as Ordens de Serviço levando em consideração, por exemplo, informações relacionadas com os Macroprocessos, associados aos Subprocessos relacionados com as Ordens de Serviço, e informações relacionadas com Área Cliente.

Tabela dinâmica de Ordens de Serviço

Para acessar todos os campos disponíveis, na barra de ferramentas da transação clique em "Mais Campos":

Botão Mais Campos

A Tabela Dinâmica de Ordens de Serviço disponibiliza os seguintes campos para a configuração de um relatório:

Dados disponíveis na tabela

Os dados das tabelas são relacionados com suas respectivas Ordens de Serviço.

| **Abertura** | Data de abertura da Ordem de Serviço. |
|---|---|
| **Abertura (Dia da Semana)** | Dia da semana de abertura da Ordem de Serviço. ex: Segunda-Feira |
| **Abertura (Mês)** | Mês de abertura da Ordem de Serviço. |
| **Abertura (Semana)** | Semana de abertura da Ordem de Serviço. (ex: 1) |
| **Área Cliente** | Área do Cliente da Ordem de Serviço. |
| **Assunto** | Assunto da Ordem de Serviço |
| **Atividade corrente** | Atividade atual em que se encontra a Ordem de Serviço. |
| **Cliente** | Cliente que realizou a abertura da Ordem de Serviço. |
| **Descrição Detalhada** | Campo Descrição Detalhada preenchido na Ordem de Serviço. |
| **Empresa Cliente** | Empresa do Cliente que realizou a abertura da Ordem de Serviço. |
| **Esforço Médio** | Média dos Esforços Estimados. |
| **Esforço Total** | Soma dos Esforços Estimados. |
| **Grupo Trabalho** | Grupo de Trabalho do Solucionador responsável da Ordem de Serviço. |
| **HH Médio** | Quantidade de horas apontadas em média. |
| **HH Total** | Quantidade de horas apontadas totais. |
| **Local** | Local informado no cadastro do Cliente da Ordem de Serviço. |
| **Macroprocesso** | Macroprocesso da Ordem de Serviço. |
| **Nível ANS** | [Nível de Acordo de Nível de Serviço](nivelsla_sub) (ANS) definido nas configurações. (ex: 1) |
| **Ordem de Serviço** | Número e assunto da Ordem de Serviço. |
| **Prédio** | Prédio do local informado no cadastro do Cliente da Ordem de Serviço. |
| **Prioridade** | Prioridade da Ordem de Serviço. |
| **Processo** | Processo referente a Ordem de Serviço. |
| **Qtd. Violou ANS** | Quantidade de Violações do tempo limite do ANS. |
| **Qtd. possuiu ANS** | Quantidade de Ordens de Serviço que possuem ANS. |
| **Quantidade** | Quantidade (totalizador). |
| **Serviço** | Serviço da Ordem de Serviço. |
| **Situação** | Situação da Ordem de Serviço. |
| **Solucionador** | Solucionador da Ordem de Serviço. |
| **Subprocesso** | Subprocesso da Ordem de Serviço. |
| **Tempo corrido médio** | Tempo corrido médio. |
| **Tempo corrido total** | Tempo corrido total. |
| **Tempo útil médio** | Tempo útil médio (No tempo líquido é contabilizado apenas o "[período útil de serviço](periodoutil_sub)" configurado em [calendários](calendario_sub)). |
| **Tempo útil total** | Tempo útil total (No tempo líquido é contabilizado apenas o "[período útil de serviço](periodoutil_sub)" configurado em [calendários](calendario_sub)). |
| **Tempo útil s/ paradas ANS médio** | Tempo útil s/ paradas ANS médio é uma contagem de tempo relativo ao "Tempo útil médio", que contabiliza o tempo dentro do calendário, porém não adiciona as paradas de ANS. |
| **Tempo útil s/ paradas ANS total** | Tempo útil s/ paradas ANS total é uma contagem de tempo relativo ao "Tempo útil total", que contabiliza o tempo dentro do calendário, porém não adiciona as paradas de ANS. |
| **Tipo atividade corrente** | Tipo da atividade atual da Ordem de Serviço. |
| **Tipo Serviço** | Tipo de Serviço (Classes de serviços) da Ordem de Serviço. |
| **Unidade de Negócio** | [Unidade de Negócio](unidadenegocio_sub) do local informado no cadastro do Cliente da Ordem de Serviço. |

**Especificação de dados dos campos de filtro por padrão**

Também é possível incluir propriedades customizadas criadas nos processos. Para isso, basta clicar na opção "Adicionar campos customizados":

Botão para adicionar campos customizados

Ao clicar no botão, irá aparecer uma tela para seleção dos campos customizados para serem adicionados no relatório.

Tela de seleção de campos

## Exemplos

### Exemplo 1:

Linhas: Abertura (Dia semana)

Colunas: Empresa Cliente

Totalizadores: Quantidade

Tabela Dinâmica Exemplo 1

### Exemplo 2:

Linhas: Abertura (Mês), Abertura(Dia Semana)

Colunas: Empresa Cliente

Totalizadores: Quantidade

Tabela Dinâmica Exemplo 2

### Exemplo 3:

Linhas: Grupo Trabalho, Solucionador

Colunas: Empresa Cliente

Totalizadores: Tempo corrido médio, Tempo útil médio

Tabela Dinâmica Exemplo 3

### Exemplo 4:

Linhas:Unidade de Negócio, Prédio, Local, Cliente

Colunas:

Totalizadores: Quantidade

Tabela Dinâmica Exemplo 4

Obs: note o resultado se o Cliente não tiver nenhum local preenchido.

### Exemplo 5:

Linhas: Grupo Trabalho

Colunas: Ordem de Serviço

Totalizadores: Tempo útil médio

Tabela Dinâmica Exemplo 5

Atividades Canceladas

As atividades canceladas, que podemos visualizar na tela de Ordem de Serviço na aba de Informações sobre Processo, depois na aba de Atividades Canceladas, são contabilizadas em algumas tabelas dinâmicas como a [Tabela Dinâmica de Ordens de Serviço](tabela_dinamica_de_ordens_de_s) e a [Tabela Dinâmica de Atividades Executadas](tabela_dinamica_de_atividades_).

Ordem de Serviço - Atividades Canceladas

Nesta Ordem de Serviço, a atividade cancelada foi a "Tarefa: Testar", na qual foi cancelada duas vezes.

Podemos observar no fluxo, que a atividade atual é a "Construir" e não foi avançada para a "Testar" já que ela foi cancelada:

Fluxo da Ordem de Serviço
