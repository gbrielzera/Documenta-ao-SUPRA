# Item de Acordo de Nível de Serviço

Caminho: Janelas > Recurso > Acordo de Nível de Serviço > Item de Acordo de Nível de Serviço

Conjunto prazos de atendimento de uma Ordem de Serviço com respectivos critérios de aplicação.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Perfil Cliente** | Perfil de Cliente que será atendido pelo Acordo. O Perfil é uma característica do Cliente e configurado no cadastro de Pessoas. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
|---|---|
| **Tipo de Serviço** | Classe de Serviços atendidos pelo Acordo de Nível de Serviço. Quando preenchido o campo Serviço a Classe de Serviço é atribuída automaticamente. Se não for preenchido o campo Serviço então são considerados todos os Serviços da Classe selecionada. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Serviço** | Serviço atendido pelo Acordo de Nível de Serviço. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Grau de Prioridade** | Grau de Prioridade determinado por um Método de Priorização. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Tempo de Atendimento** | Script que define o tempo de atendimento, o resultado da execução do script deve ser um número que representa o número de minutos Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TEMPO_ATEND da tabela [ITEM_SLA](dados_item_sla). |

| **Períodos de Exceção** | Redefinição do tempo de atendimento para períodos de exceção em um mês ou ano. Todos os registros desta coleção de dados são mantidos na tabela [EXCECAO_SLA](dados_excecao_sla). |
|---|---|
