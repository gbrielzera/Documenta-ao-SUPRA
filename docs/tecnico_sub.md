# Solucionador

Caminho: Janelas > Recurso > Grupo Trabalho > Solucionador

Um Solucionador é uma Pessoa que trabalha no atendimento de solicitações de Serviço. Este solucionador deve estar lotado em somente um Grupo de Trabalho e pode exercer função de coordenação.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Pessoa** | Pessoa que está lotada no Grupo de Trabalho Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
|---|---|
| **Ativo** | Indica que o Solucionador está Ativo no Grupo de Trabalho. Em um dado momento o Solucionador pode estar Ativo em somente um Grupo de Trabalho. Ele também não pode ser ativado em um Grupo de Trabalho desativado. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [TECNICO](dados_tecnico). |
| **Data/hora associacao** | Data e hora em que a Pessoa foi associada ao Grupo de Trabalho Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_HORA_ASSOCIACAO da tabela [TECNICO](dados_tecnico). |
| **Data/hora desativacao** | Data e hora em que o Solucionador teve sua associação com o Grupo de Trabalho desativada |
| **Calendário de disponibilidade do recurso** | Calendário de disponibilidade do recurso. Se não for preenchido então é adotado o calendário da unidade onde está localizada a pessoa. Se a pessoa não possuir associação de Local então entende-se que o recurso terá disponibilidade total (24x7) nos cálculos de Acordo de Nível Operacional. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Alertar Solucionadores do Grupo** | Indica que Solucionadores do Grupo receberão alertas quando uma nova Ordem de Serviço for encaminhada para a fila. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ALERTA_SOL_GRUPO da tabela [TECNICO](dados_tecnico). |
