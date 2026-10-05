# Class

Caminho: Customização > Modelo de objetos > Utilitários > Class

Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CustomProperties** | Propriedade de uma Classe de Negócio criada pelo próprio usuário com escopo válido para um determinado Domínio de uso. Propriedades customizadas são gravadas em tabelas adicionais criadas dinamicamente pelo sistema na medida em que o usuário extende Classes de Negócio. Para cada Classe de Negócio pode existir uma tabele adicional para manutenção de customizações (todos os campos adicionais são criados nesta mesma tabela) | [Lista de CustomProperty](objetos_customproperty) |
| **Description** | Documentação sobre a Classe de Negócio utilizada como ajuda para usuário em telas de cadastro e outras funções do sistema. | String |
| **Events** | Coleção de Eventos que podem ser customizados para a Classe de Negócio em determinado Domínio. Todos os eventos são implementados por scripts na linguagem Python. | [Lista de CustomEvent](objetos_customevent) |
| **Id** | Idenficador da Classe | Inteiro |
| **LocalizeEnabled** | Indica que a Classe possui o recurso de localização de objetos ativado. Quando ativado é possível a tradução de propriedades do tipo texto para diversas culturas. | Booleano |
| **LogChangeEnabled** | Indica que o Log de modificações está ativado. Quando ativado o sistema gera registro (log) de todas as modificações em objetos deste tipo. | Booleano |
| **Module** | Um Módulo define um conjunto de funcionalidades pertencentes a uma aplicação. Para cada Módulo existe um item de menu raiz denominado 'Comando raiz' e a partir deste item são associados todos as opções de comandos do módulo. | [Module](objetos_module) |
| **ModuleId** | Identificador do Módulo Associado | Inteiro |
| **Name** | Nome da Classe incluindo namespace | String |
| **OriginalDescription** | Descrição completa definida originalmente pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | String |
| **OriginalLocalizeEnabled** | Opção de ativação do recurso de Localização definido pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | Booleano |
| **OriginalLogChangeEnabled** | Opção de ativação do log de modificações definida pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | Booleano |
| **OriginalText** | Descrição resumida originalmente definida pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. | String |
| **ParentClass** | Classe Pai | [Class](objetos_class) |
| **ParentClassId** | Identificador da Classe Pai | Inteiro |
| **Properties** | Propriedades nativas de uma Classe de Negócio. | [Lista de Property](objetos_property) |
| **TableName** | Nome da tabela que mantém objetos da Classe. Válido apenas para Classes de Entidades. | String |
| **Text** | Descrição resumida da Classe. Este texto é muito usado para identificar objetos deste tipo. | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Class Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Class | Class Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Class Carrega(string nomePropriedade, object valorPropriedade); |
