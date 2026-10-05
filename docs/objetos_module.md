# Module

Caminho: Customização > Modelo de objetos > Utilitários > Module

Um Módulo define um conjunto de funcionalidades pertencentes a uma aplicação. Para cada Módulo existe um item de menu raiz denominado 'Comando raiz' e a partir deste item são associados todos as opções de comandos do módulo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CommandRoot** | Item de menu utilizado como comando pai de todas as opções do módulo. Um Módulo possui obrigatoriamente um único comando raiz. Todos os demais comandos estão abaixo deste item (direto ou indiretamente). | [Command](objetos_command) |
| **CommandRootId** | Identificador do item de menu denominado 'Comando raiz' | Inteiro |
| **Description** | Descrição detalhada do Módulo para documentação do Módulo. | String |
| **Enabled** | Indica que o Módulo está ativo no sistema. Uma vez inativo o Módulo não pode ser acessado por Usuários. | Booleano |
| **Id** | Identificador do Módulo | Inteiro |
| **Name** | Nome sucinto para o Módulo. | String |
| **OriginalDescription** | Descrição original do Módulo | String |
| **OriginalText** | Descrição resumida original | String |
| **ParameterClass** | Nome da Classe responsável por manter os parâmetros do Módulo. | String |
| **ShortName** | Nome resumido (código) que identifica um Módulo. | String |
| **Text** | Descrição resumida para utilização na interface com usuário. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Module Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Module | Module Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Module Carrega(string nomePropriedade, object valorPropriedade); |
