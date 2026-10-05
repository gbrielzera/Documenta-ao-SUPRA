# SV_ATTACHMENT_FILE

Caminho: Customização > Modelo de dados > Utilitários > SV_ATTACHMENT_FILE

Arquivos anexados aos registros

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATTACHMENT_FILE** | Identificador do arquivo | int | number(6,0) | Não |
| **KEY_VALUE** | Chave de identificação do Objeto de Negócio modificado. | varchar(500) | varchar(500) | Não |
| **TEXTUAL_REPRESENTATION** | Representação textual | varchar(500) | varchar(500) | Não |
| **ID_CLASS** | Identificador do(a) Class associado(a) | int | number(6,0) | Não |
| **FILE_NAME** | Nome do arquivo salvo | varchar(500) | varchar(500) | Não |
| **ID_FILE_TYPE** | Identificador do(a) FileType associado(a) | int | number(6,0) | Não |
| **ATTACH_DATE** | Data/hora em que o arquivo foi anexado no registro | datetime | date | Não |
| **ID_USER** | Identificador do usuário responsável por anexar o arquivo ao registro | int | number(6,0) | Não |
| **USER_COMMENT** | Comentário feito pelo usuário no instante de anexação do arquivo ao registro | varchar(500) | varchar(500) | Sim |
| **FULL_FILE_NAME** | Nome do arquivo no servidor de arquivos | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por SV_ATTACHMENT_FILE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_CLASS](dados_sv_class) | \| **SV_CLASS** \| **SV_ATTACHMENT_FILE** \| \|---\|---\| \| ID_CLASS \| ID_CLASS \| |
| [SV_FILE_TYPE](dados_sv_file_type) | \| **SV_FILE_TYPE** \| **SV_ATTACHMENT_FILE** \| \|---\|---\| \| ID_FILE_TYPE \| ID_FILE_TYPE \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_ATTACHMENT_FILE** \| \|---\|---\| \| ID_USER \| ID_USER \| |

**Exemplo 1: join com a tabela SV_CLASS**

```
select SV_ATTACHMENT_FILE.*, SV_CLASS.NAME
from SV_ATTACHMENT_FILE, SV_CLASS
where SV_ATTACHMENT_FILE.ID_CLASS = SV_CLASS.ID_CLASS
```

**Exemplo 2: join com a tabela SV_FILE_TYPE**

```
select SV_ATTACHMENT_FILE.*, SV_FILE_TYPE.DESCRICAO
from SV_ATTACHMENT_FILE, SV_FILE_TYPE
where SV_ATTACHMENT_FILE.ID_FILE_TYPE = SV_FILE_TYPE.ID_FILE_TYPE
```

**Exemplo 3: join com a tabela SV_USER**

```
select SV_ATTACHMENT_FILE.*, SV_USER.USERNAME
from SV_ATTACHMENT_FILE, SV_USER
where SV_ATTACHMENT_FILE.ID_USER = SV_USER.ID_USER
```
