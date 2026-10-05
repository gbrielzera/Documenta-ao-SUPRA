# SV_REPORT

Caminho: Customização > Modelo de dados > Utilitários > SV_REPORT

Relatório criado pelo usuário utilizando o Editor de Relatórios

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REPORT** | Número sequencial gerado automaticamente pelo sistema para Identificar um Report | int | number(6,0) | Não |
| **DESCRIPTION** | Descrição detalhada do Report | varchar(500) | varchar(500) | Não |
| **ENABLED** | Indica que o Report está ativo no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | char(3) | char(3) | Não |
| **CREATION_DATE** | Data/hora de criação do relatório | datetime | date | Não |
| **ID_USER** | Identificador do usuário criador do relatório | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **LOCK_COMMENT** | Comentário registrado pelo usuário que realizou ou cancelou o bloqueio de edição | varchar(500) | varchar(500) | Sim |
| **LOCKED_BY_ID** | Identificador do usuário que bloqueou o relatório para edição. Usuário que bloqueou o relatório para edição. Durante a existência do bloqueio somente este usuário pode realizar modificações. O desbloqueio pode ser desfeito pelo criador do relatório, autor do bloqueio ou qualquer outro que possua o perfil 'Admin'. | int | number(6,0) | Sim |
| **REPORT_LAYOUT** | Layout do relatório mantidos em um controle Report serializado | varbinary(4000) | blob | Sim |
| **ID_USER_UNLOCKER** | Identificador do usuário responsável pelo último do relatório. | int | number(6,0) | Sim |

Tabelas referenciadas por SV_REPORT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_REPORT** \| \|---\|---\| \| ID_USER \| ID_USER \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_REPORT** \| \|---\|---\| \| ID_USER \| ID_USER_UNLOCKER \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **SV_REPORT** \| \|---\|---\| \| ID_USER \| LOCKED_BY_ID \| |

Tabelas que dependem de SV_REPORT

| **Tabela** | **Colunas de ligação** |
|---|---|
| [SV_REPORT_PARAM](dados_sv_report_param) | \| **SV_REPORT_PARAM** \| **SV_REPORT** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| |
| [SV_REPORT_QUERY](dados_sv_report_query) | \| **SV_REPORT_QUERY** \| **SV_REPORT** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| |

**Exemplo 1: join com a tabela SV_USER**

```
select SV_REPORT.*, SV_USER.USERNAME
from SV_REPORT, SV_USER
where SV_REPORT.ID_USER = SV_USER.ID_USER
```

**Exemplo 2: join com a tabela SV_USER**

```
select SV_REPORT.*, SV_USER.USERNAME
from SV_REPORT left outer join SV_USER on SV_REPORT.ID_USER_UNLOCKER = SV_USER.ID_USER
```

**Exemplo 3: join com a tabela SV_USER**

```
select SV_REPORT.*, SV_USER.USERNAME
from SV_REPORT left outer join SV_USER on SV_REPORT.LOCKED_BY_ID = SV_USER.ID_USER
```
