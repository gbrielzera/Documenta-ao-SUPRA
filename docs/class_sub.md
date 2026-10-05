# Classes de Negócio

Caminho: Janelas > Utilitários > Classes de Negócio

Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Utilitários | Dicionário de Classes | Dicionário de Classes**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Idenficador** | Idenficador da Classe Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_CLASS da tabela [SV_CLASS](dados_sv_class). |
|---|---|
| **Nome** | Nome da Classe incluindo namespace Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna NAME da tabela [SV_CLASS](dados_sv_class). |
| **Descrição resumida** | Descrição resumida da Classe. Este texto é muito usado para identificar objetos deste tipo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TEXT da tabela [SV_CLASS](dados_sv_class). |
| **Descrição** | Documentação sobre a Classe de Negócio utilizada como ajuda para usuário em telas de cadastro e outras funções do sistema. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRIPTION da tabela [SV_CLASS](dados_sv_class). |
| **Ativar geração de log de modificações** | Indica que o Log de modificações está ativado. Quando ativado o sistema gera registro (log) de todas as modificações em objetos deste tipo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CHANGE_LOG_ENABLED da tabela [SV_CLASS](dados_sv_class). |
| **Ativar tradução de campos** | Indica que a Classe possui o recurso de localização de objetos ativado. Quando ativado é possível a tradução de propriedades do tipo texto para diversas culturas. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna LOCALIZATION_ENABLED da tabela [SV_CLASS](dados_sv_class). |
| **Módulo** | Um Módulo define um conjunto de funcionalidades pertencentes a uma aplicação. Para cada Módulo existe um item de menu raiz denominado 'Comando raiz' e a partir deste item são associados todos as opções de comandos do módulo. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Tabela** | Nome da tabela que mantém objetos da Classe. Válido apenas para Classes de Entidades. |
| **Descrição resumida original** | Descrição resumida originalmente definida pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_TEXT da tabela [SV_CLASS](dados_sv_class). |
| **Descrição original** | Descrição completa definida originalmente pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_DESCRIPTION da tabela [SV_CLASS](dados_sv_class). |
| **Localização original** | Opção de ativação do recurso de Localização definido pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIG_LOCAL_ENABLED da tabela [SV_CLASS](dados_sv_class). |
| **Log de modificações original** | Opção de ativação do log de modificações definida pelo fabricante do software. Este valor pode ser utilizado para reverter modificações realizadas pelo usuário. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIG_CHNG_LOG_ENABLED da tabela [SV_CLASS](dados_sv_class). |

| **Propriedades** | Propriedades nativas de uma Classe de Negócio. Todos os registros desta coleção de dados são mantidos na tabela [SV_PROPERTY](dados_sv_property). |
|---|---|

| **Propriedades Customizadas** | Propriedade de uma Classe de Negócio criada pelo próprio usuário com escopo válido para um determinado Domínio de uso. Propriedades customizadas são gravadas em tabelas adicionais criadas dinamicamente pelo sistema na medida em que o usuário estende Classes de Negócio. Para cada Classe de Negócio pode existir uma tabele adicional para manutenção de customizações (todos os campos adicionais são criados nesta mesma tabela) Todos os registros desta coleção de dados são mantidos na tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
|---|---|

| **Eventos Customização** | Coleção de Eventos que podem ser customizados para a Classe de Negócio em determinado Domínio. Todos os eventos são implementados por scripts na linguagem Python. Todos os registros desta coleção de dados são mantidos na tabela [SV_CUSTOM_EVENT](dados_sv_custom_event). |
|---|---|
