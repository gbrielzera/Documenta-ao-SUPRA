# CustomProperty

Caminho: Customização > Modelo de objetos > Utilitários > CustomProperty

Propriedade de uma Classe de Negócio criada pelo próprio usuário com escopo válido para um determinado Domínio de uso. Propriedades customizadas são gravadas em tabelas adicionais criadas dinamicamente pelo sistema na medida em que o usuário extende Classes de Negócio. Para cada Classe de Negócio pode existir uma tabele adicional para manutenção de customizações (todos os campos adicionais são criados nesta mesma tabela)

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClassId** | Idenficador da Classe | Inteiro |
| **ClassReference** | Indica o cadastro que fornecerá as opções de preenchimento para o campo. | [Class](objetos_class) |
| **ClassReferenceId** | Identificador do Cadastro associado | Inteiro |
| **ControlUrl** | Caminho para carga do Controle | String |
| **Description** | Descrição completa da Propriedade. É utilizada para orientar o usuário sobre o preenchimento do campo. | String |
| **Domain** | Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias | [Domain](objetos_domain) |
| **Enabled** | Indica que o controle para Edição da Propriedade está Habilitado | Booleano |
| **Height** | Altura do controle utilizado para Edição da Propriedade. Quando não definido o sistema assume valores default conforme controle selecionado. Esta propriedade é importante para controles do tipo Memo | Inteiro |
| **Id** | Identificador da Propriedade Customizada | Inteiro |
| **Invalid** | Indica que o campo é inválido por não existir em banco de dados. | Booleano |
| **Length** | Tamanho de campos string em quantidade de caracteres. Se não for preenchido então é adotado o tamanho padrão de 250 caracteres | Inteiro |
| **ListItems** | Listagem de Itens exibido para o usuário para seleção. Para separação de itens utilize o caracter ';' (ponto e vírgula). | String |
| **LookupScript** | Script utilizado para recuperação de itens utilizados como opções de preenchimento para o campo. Para o caso específico de recuperação a partir de banco de dados, se for fornecida uma tabela com dois campos então o primeiro será utilizado para preenchimento do campo enquanto o segundo fornecerá as opções exibidas no controle. | String |
| **Name** | Nome da Propriedade customizada. Este nome será utilizado em outras telas ou scripts do aplicativo. Não utilize aqui espaços em branco. | String |
| **RecordColumns** | Listagem de colunas do registro | [Lista de RecordColumn](objetos_recordcolumn) |
| **Scopes** | Conjunto de condições que devem ser atendidas pela Ordem de Serviço para que o campo seja visível. | [Lista de CustomPropertyScope](objetos_custompropertyscope) |
| **Sequence** | Sequencial para apresentação na tela de Edição | Inteiro |
| **TableColumn** | Coluna da Tabela que mantém dados da Propriedade. | String |
| **TableName** | Nome da Tabela de banco de dados responsável por manter a Propriedade. Esta tabela é criada automaticamente pelo sistema quando o usuário define a primeira Propriedade Customizada de uma determinada Classe de Negócio e o seu nome é dado em função do nome de tabela da classe original acrescido de um prefixo CP_ | String |
| **Text** | Descrição resumida que é exibida no rótulo de controles utilizados na edição da Propriedade. | String |
| **Type** | Tipo da Propriedade conforme biblioteca de tipos da tecnologia Microsoft .NET | [CustomPropertyType](enum_custompropertytype) |
| **Visible** | Indica que o Controle para Edição da Propriedade está Visível | Booleano |
| **Width** | Largura do controle utilizado para Edição da Propriedade. Quando não definido o sistema assume valor default conforme controle selecionado | Inteiro |
