# SV_CUSTOM_PROPERTY

Caminho: Customização > Modelo de dados > Utilitários > SV_CUSTOM_PROPERTY

Propriedade de uma Classe de Negócio criada pelo próprio usuário com escopo válido para um determinado Domínio de uso. Propriedades customizadas são gravadas em tabelas adicionais criadas dinamicamente pelo sistema na medida em que o usuário extende Classes de Negócio. Para cada Classe de Negócio pode existir uma tabele adicional para manutenção de customizações (todos os campos adicionais são criados nesta mesma tabela)

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CUSTOM_PROPERTY** | Identificador da Propriedade Customizada | int | number(6,0) | Não |
| **ID_CLASS** | Idenficador da Classe | int | number(6,0) | Não |
| **NAME** | Nome da Propriedade customizada. Este nome será utilizado em outras telas ou scripts do aplicativo. Não utilize aqui espaços em branco. | varchar(100) | varchar(100) | Não |
| **TEXT** | Descrição resumida que é exibida no rótulo de controles utilizados na edição da Propriedade. | varchar(500) | varchar(500) | Não |
| **DESCRIPTION** | Descrição completa da Propriedade. É utilizada para orientar o usuário sobre o preenchimento do campo. | varchar(500) | varchar(500) | Não |
| **TYPE** | Tipo da Propriedade conforme biblioteca de tipos da tecnologia Microsoft .NET | varchar(250) | varchar(250) | Não |
| **TABLE_NAME** | Nome da Tabela de banco de dados responsável por manter a Propriedade. Esta tabela é criada automaticamente pelo sistema quando o usuário define a primeira Propriedade Customizada de uma determinada Classe de Negócio e o seu nome é dado em função do nome de tabela da classe original acrescido de um prefixo CP_ | varchar(100) | varchar(100) | Não |
| **TABLE_COLUMN** | Coluna da Tabela que mantém dados da Propriedade. | varchar(100) | varchar(100) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **SEQUENCE** | Sequencial para apresentação na tela de Edição | int | number(6,0) | Não |
| **CONTROL** | Controle para edição da Propriedade Customizada | varchar(250) | varchar(250) | Não |
| **CONTROL_URL** | Caminho para carga do Controle | varchar(500) | varchar(500) | Sim |
| **VISIBLE** | Indica que o Controle para Edição da Propriedade está Visível | char(3) | char(3) | Não |
| **ENABLED** | Indica que o controle para Edição da Propriedade está Habilitado | char(3) | char(3) | Não |
| **HEIGHT** | Altura do controle utilizado para Edição da Propriedade. Quando não definido o sistema assume valores default conforme controle selecionado. Esta propriedade é importante para controles do tipo Memo | int | number(6,0) | Sim |
| **WIDTH** | Largura do controle utilizado para Edição da Propriedade. Quando não definido o sistema assume valor default conforme controle selecionado | int | number(6,0) | Sim |
| **LIST_ITEMS** | Listagem de Itens exibido para o usuário para seleção. Para separação de itens utilize o caracter ';' (ponto e vírgula). | varchar(500) | varchar(500) | Sim |
| **ID_CLASS_REF** | Identificador do Cadastro associado | int | number(6,0) | Sim |
| **LENGTH** | Tamanho de campos string em quantidade de caracteres. Se não for preenchido então é adotado o tamanho padrão de 250 caracteres | int | number(6,0) | Sim |
| **LOOKUP_SCRIPT** | Script utilizado para recuperação de itens utilizados como opções de preenchimento para o campo. Para o caso específico de recuperação a partir de banco de dados, se for fornecida uma tabela com dois campos então o primeiro será utilizado para preenchimento do campo enquanto o segundo fornecerá as opções exibidas no controle. | text | clob | Sim |
| **INVALID** | Indica que o campo é inválido por não existir em banco de dados. | char(3) | char(3) | Não |

Tabelas referenciadas por SV_CUSTOM_PROPERTY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_DOMAIN](dados_sv_domain) | \| **SV_DOMAIN** \| **SV_CUSTOM_PROPERTY** \| \|---\|---\| \| ID_DOMAIN \| ID_DOMAIN \| |
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_CUSTOM_PROPERTY** \| \|---\|---\| \| ID_CLASS \| ID_CLASS_REF \| |
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_CUSTOM_PROPERTY** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |

Tabelas que dependem de SV_CUSTOM_PROPERTY

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CUSTOM_PROPERTY_SCOPE](dados_sv_custom_property_scope) | \| **SV_CUSTOM_PROPERTY_SCOPE** \| **SV_CUSTOM_PROPERTY** \| \|---\|---\| \| ID_CUSTOM_PROPERTY \| ID_CUSTOM_PROPERTY \| |
| [SV_REC_COLUMN](dados_sv_rec_column) | \| **SV_REC_COLUMN** \| **SV_CUSTOM_PROPERTY** \| \|---\|---\| \| ID_CUSTOM_PROPERTY \| ID_CUSTOM_PROPERTY \| |

**Exemplo 1: join com a tabela SV_DOMAIN**

```
select SV_CUSTOM_PROPERTY.*, SV_DOMAIN.NAME
from SV_CUSTOM_PROPERTY, SV_DOMAIN
where SV_CUSTOM_PROPERTY.ID_DOMAIN = SV_DOMAIN.ID_DOMAIN
```

**Exemplo 2: join com a tabela SV_CLASS**

```
select SV_CUSTOM_PROPERTY.*, SV_CLASS.NAME
from SV_CUSTOM_PROPERTY left outer join SV_CLASS on SV_CUSTOM_PROPERTY.ID_CLASS_REF = SV_CLASS.ID_CLASS
```

**Exemplo 3: join com a tabela SV_CLASS**

```
select SV_CUSTOM_PROPERTY.*
from SV_CUSTOM_PROPERTY, SV_CLASS
where SV_CUSTOM_PROPERTY.ID_CLASS = SV_CLASS.ID_CLASS
```
