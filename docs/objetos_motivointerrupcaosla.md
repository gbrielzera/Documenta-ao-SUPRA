# MotivoInterrupcaoSLA

Caminho: Customização > Modelo de objetos > Recurso > MotivoInterrupcaoSLA

Motivo para interrupção na cronometragem do tempo de atendimento de uma ocorrência.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ComentarioObrigatorio** | Quando ativado obriga o usuário que estiver registrando a interrupção (somente inclusão manual) a informar um motivo. Este motivo é replicado no campo de comentários e publicado no Autoatendimento. | Booleano |
| **Descricao** | Descrição detalhada do Motivo de interrupção de ANS | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Motivo de interrução de cronometragem de tempo de ANS | Inteiro |
| **TempoPadrao** | Tempo máximo (em horas) para finalização de interrupção manuais (exclui interrupções configuradas no processo). | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | MotivoInterrupcaoSLA Carrega(int i); |
| **Novo** | Cria um novo registro do tipo MotivoInterrupcaoSLA | MotivoInterrupcaoSLA Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | MotivoInterrupcaoSLA Carrega(string nomePropriedade, object valorPropriedade); |
