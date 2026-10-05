# Job

Caminho: Customização > Modelo de objetos > Utilitários > Job

Rotinas para execução em background via mecanismo Schedule

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClassId** | Identificador do(a) Class associado(a) | Inteiro |
| **ContextApplicationId** | Identificador da Aplicação | String |
| **ContextDomainId** | Identificador do Domínio onde será executado o Job | Inteiro |
| **ContextUserId** | Identificador do Usuário proprietário do Job | Inteiro |
| **ContextUsername** | Nome do usuário proprietário do Job | String |
| **CreatedDate** | Data e hora em que o Job foi criado. | Data/hora |
| **Creator** | Usuário criador do Job | [User](objetos_user) |
| **Description** | Descrição detalhada do Job | String |
| **EmailFailure** | Email enviado a usuários em caso de falha na execução | String |
| **EmailSuccess** | Email enviado para usuário em caso de sucesso | String |
| **Enabled** | Indica que o Job está ativo | Booleano |
| **ErrorCount** | Número de execuções seguindas com ocorrência de Erros. Se for excedido um número máximo de erros seguidos então o Job não é mais processado. Sempre que ocorrer execução com sucesso então este contador é zerado. | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Job | Inteiro |
| **JobHistory** | Histórico de execuções | [Lista de JobHistory](objetos_jobhistory) |
| **LastRunningDate** | Última informação de execução enquanto o Job estiver em execução. | Data/hora |
| **LastTime** | Data/hora da última execução | Data/hora |
| **Name** | Nome do job que é exibido na transação Gerenciamento de Ambiente | String |
| **NextTime** | Data/hora da próxima execução. | Data/hora |
| **NextTimePeriod** | Período a ser acrescido em NextTime para agendamento da próxima execução. | Inteiro |
| **NextTimePeriodCount** | Quantidade de Períodos a serem acrescentados em NextTime para próxima execução | Inteiro |
| **ProcessClass** | Classe de Processo responsável pela execução do Job | [Class](objetos_class) |
| **ProcessParam** | Parâmetro para Classe de Processo | String |
| **ReportExportFormat** | Formato de saída do arquivo gerado pelo relatório | [ReportExport](enum_reportexport) |
| **RunningProgress** | Progresso do job em execução. | Inteiro |
| **RunningResult** | Último resultado em processamento | String |
| **RunningServer** | Servidor onde está sendo executado o Job. Este valor é preenchido somente enquanto um Job está sendo executado. | String |
| **UserId** | Identificador do Usuário criador do Job | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Job Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Job | Job Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Job Carrega(string nomePropriedade, object valorPropriedade); |
