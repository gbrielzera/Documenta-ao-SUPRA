# Propriedades Customizadas

Caminho: Janelas > Utilitários > Classes de Negócio > Propriedades Customizadas

Propriedade de uma Classe de Negócio criada pelo próprio usuário com escopo válido para um determinado Domínio de uso. Propriedades customizadas são gravadas em tabelas adicionais criadas dinamicamente pelo sistema na medida em que o usuário estende Classes de Negócio. Para cada Classe de Negócio pode existir uma tabele adicional para manutenção de customizações (todos os campos adicionais são criados nesta mesma tabela)

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Nome** | Nome da Propriedade customizada. Este nome será utilizado em outras telas ou scripts do aplicativo. Não utilize aqui espaços em branco. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo Este campo é mantido na coluna NAME da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
|---|---|
| **Descrição resumida** | Descrição resumida que é exibida no rótulo de controles utilizados na edição da Propriedade. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TEXT da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Descrição** | Descrição completa da Propriedade. É utilizada para orientar o usuário sobre o preenchimento do campo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRIPTION da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Tipo** | Tipo da Propriedade conforme biblioteca de tipos da tecnologia Microsoft .NET Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TYPE da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Nome Tabela** | Nome da Tabela de banco de dados responsável por manter a Propriedade. Esta tabela é criada automaticamente pelo sistema quando o usuário define a primeira Propriedade Customizada de uma determinada Classe de Negócio e o seu nome é dado em função do nome de tabela da classe original acrescido de um prefixo CP_ Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo Este campo é mantido na coluna TABLE_NAME da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Nome Coluna** | Coluna da Tabela que mantém dados da Propriedade. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo Este campo é mantido na coluna TABLE_COLUMN da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Quantidade caracteres** | Tamanho de campos string em quantidade de caracteres. Se não for preenchido então é adotado o tamanho padrão de 250 caracteres |
| **Inválido** | Indica que o campo é inválido por não existir em banco de dados. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna INVALID da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Ordem de exibição** | Sequencial para apresentação na tela de Edição Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna SEQUENCE da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Controle** | Controle para edição da Propriedade Customizada Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CONTROL da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Habilitado** | Indica que o controle para Edição da Propriedade está Habilitado Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ENABLED da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Visível** | Indica que o Controle para Edição da Propriedade está Visível Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna VISIBLE da tabela [SV_CUSTOM_PROPERTY](dados_sv_custom_property). |
| **Largura** | Largura do controle utilizado para Edição da Propriedade. Quando não definido o sistema assume valor default conforme controle selecionado |
| **Altura** | Altura do controle utilizado para Edição da Propriedade. Quando não definido o sistema assume valores default conforme controle selecionado. Esta propriedade é importante para controles do tipo Memo |
| **Listagem de itens** | Listagem de Itens exibido para o usuário para seleção. Para separação de itens utilize o caracter ';' (ponto e vírgula). |
| **Cadastro associado** | Indica o cadastro que fornecerá as opções de preenchimento para o campo. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Script para recuperação de opções** | Script utilizado para recuperação de itens utilizados como opções de preenchimento para o campo. Para o caso específico de recuperação a partir de banco de dados, se for fornecida uma tabela com dois campos então o primeiro será utilizado para preenchimento do campo enquanto o segundo fornecerá as opções exibidas no controle. |

| **Lista de registros: definição de campos** | Listagem de colunas do registro Todos os registros desta coleção de dados são mantidos na tabela [SV_REC_COLUMN](dados_sv_rec_column). |
|---|---|

| **Escopo** | Conjunto de condições que devem ser atendidas pela Ordem de Serviço para que o campo seja visível. Todos os registros desta coleção de dados são mantidos na tabela [SV_CUSTOM_PROPERTY_SCOPE](dados_sv_custom_property_scope). |
|---|---|
