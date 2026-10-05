# Transaction

Caminho: Customização > Modelo de objetos > Utilitários > Transaction

Uma Transação representa o ponto de entrada para uma funcionalidade do sistema (Tela de sistema, Web Services, etc). Para cada Transação é possível a configuração de autorização por Perfil de acesso.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AdapterCRUD** | Classe que customiza o comportamento de telas CRUD | String |
| **Capabilities** | Funcionalidades disponibilizadas na Transação. Exemplos de funções disponíveis: AllowEdit, AllowRemove, AllowNew etc. | String |
| **Description** | Descrição detalhada sobre a transação. | String |
| **Enabled** | Indica que a Transação está ativa. Quando desativada a Transação não é mais visível para o usuário. | Booleano |
| **IconName** | Nome do ícone utilizado na Transação. Este nome corresponde ao objeto adicionado como recurso na aplicação cliente. | String |
| **Id** | Identificador da Transação | Inteiro |
| **Module** | System Module | [Module](objetos_module) |
| **ModuleId** | Identificador do Módulo associado | Inteiro |
| **OriginalDescription** | Descrição detalhada original. | String |
| **OriginalText** | Descrição resumida original | String |
| **ShortName** | Código da transação utilizado para acesso via barra de ferramentas. | String |
| **Text** | Descrição resumida da Transação. | String |
| **Url** | Caminho para objeto inicial da Transação | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Transaction Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Transaction | Transaction Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Transaction Carrega(string nomePropriedade, object valorPropriedade); |
