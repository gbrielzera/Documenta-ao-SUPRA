# UserReport

Caminho: Customização > Modelo de objetos > Utilitários > UserReport

Relatório criado pelo usuário utilizando o Editor de Relatórios

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CreationDate** | Data/hora de criação do relatório | Data/hora |
| **Creator** | Usuário que criou o relatório | [User](objetos_user) |
| **CreatorId** | Identificador do usuário criador do relatório | Inteiro |
| **Description** | Descrição detalhada do Report | String |
| **Enabled** | Indica que o Report está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Report | Inteiro |
| **LockComment** | Comentário registrado pelo usuário que realizou ou cancelou o bloqueio de edição | String |
| **LockedBy** | Usuário que bloqueou o relatório para edição. Durante a existência do bloqueio somente este usuário pode realizar modificações. O desbloqueio pode ser desfeito pelo criador do relatório, autor do bloqueio ou qualquer outro que possua o perfil 'Admin' | [User](objetos_user) |
| **LockedById** | Identificador do usuário que bloqueou o relatório para edição. Usuário que bloqueou o relatório para edição. Durante a existência do bloqueio somente este usuário pode realizar modificações. O desbloqueio pode ser desfeito pelo criador do relatório, autor do bloqueio ou qualquer outro que possua o perfil 'Admin'. | Inteiro |
| **Parameters** | Parâmetros do relatório | [Lista de ReportParam](objetos_reportparam) |
| **Queries** | Consultas utilizadas no relatório. Todo relatório pode conter uma ou mais consultas. Para cada banda Detail Report existirá uma consulta. | [Lista de ReportQuery](objetos_reportquery) |
| **ReportLayout** | Layout do relatório mantidos em um controle Report serializado | System.Object |
| **Unlocker** | Pessoa que realizou o desbloqueio na edição do relatório. Somente o criador do relatório, o responsável pelo bloqueio e usuários com o perfil 'Admin' estão autorizados a desbloquear o relatório. | [User](objetos_user) |
| **UnlockerId** | Identificador do usuário responsável pelo último do relatório. | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | UserReport Carrega(int i); |
| **Novo** | Cria um novo registro do tipo UserReport | UserReport Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | UserReport Carrega(string nomePropriedade, object valorPropriedade); |
