# PESSOA

Caminho: Customização > Modelo de dados > Recurso > PESSOA

Uma Pessoa pode representar um Cliente, um Solucionador ou uma fila de atendimento. Um registro do tipo Pessoa deve obrigatoriamente estar associado a um Órgão, e por meio desta associação é possível determinar seu gestor. No cadastro de uma Ordem de Serviço encontramos os campos Cliente e Responsável que representam a pessoa que solicitou e a responsável pelo atendimento respectivamente.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PESSOA** | Número sequencial gerado automaticamente pelo sistema para identificar uma Pessoa. | int | number(6,0) | Não |
| **NOME** | Nome completo da Pessoa | varchar(500) | varchar(500) | Não |
| **NOME_ABREVIADO** | Nome abreviado da Pessoa | varchar(50) | varchar(50) | Não |
| **TELEFONE** | Número do Telefone (ramal) de contato. | varchar(50) | varchar(50) | Sim |
| **CELULAR_PARTICULAR** | Telefone Celular particular da Pessoa | varchar(50) | varchar(50) | Sim |
| **CELULAR_EMPRESA** | Telefone Celular fornecido pela empresa | varchar(50) | varchar(50) | Sim |
| **SEGUNDO_CONTATO** | Segunda Pessoa para contato | varchar(50) | varchar(50) | Sim |
| **TELEFONE_SEGUNDO_CONTATO** | Telefone da Segunda Pessoa de contato | varchar(50) | varchar(50) | Sim |
| **EMAIL** | Email da Pessoa | varchar(50) | varchar(50) | Sim |
| **EMAIL_ALTERNATIVO** | Email alternativo de contato para a Pessoa | varchar(50) | varchar(50) | Sim |
| **ATIVO** | Indica que a Pessoa está Ativa no sistema. | char(3) | char(3) | Não |
| **USUARIO_REDE** | Nome do usuário de rede utilizado pela Pessoa para acesso a ambiente de rede | varchar(50) | varchar(50) | Não |
| **ID_ORGAO** | Identificador do Órgão onde a Pessoa está lotada | int | number(6,0) | Não |
| **TIPO_COLABORADOR** | Tipo de Colaborador que pode ser Empregado ou Terceiro. No caso de Terceiro é necessário informar a Empresa Fornecedora | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **CARGO** | Descrição do Cargo da Pessoa | varchar(500) | varchar(500) | Sim |
| **ID_FORNECEDOR** | Identificador do Fornecedor em caso de Terceiros. | int | number(6,0) | Sim |
| **ID_FATOR_PRIORIDADE** | Identificador do Fator de Prioridade utilizado em cálculos de Prioridade. | int | number(6,0) | Sim |
| **ID_PERFIL_CLIENTE** | Identificador do(a) PerfilCliente associado(a) | int | number(6,0) | Sim |
| **ID_LOCAL** | Identificador do Local de trabalho da Pessoa | int | number(6,0) | Sim |
| **ID_CULTURA_CLIENTE** | Identificador da Cultura preferencial do Cliente | int | number(6,0) | Sim |
| **ID_SUBSTITUTO_APROVACAO** | Identificador do Substituto para Aprovação | int | number(6,0) | Sim |
| **DT_INICIO_SUBSTIT_APROV** | Data de Início de validade para a autorização de substituição. Importante: a data de início não está associada a data de início de aprovação (instante em que soliictação de aprovação é enviada para o aprovador) e sim com a data instantânea em que a página de aprovação é exibida para o Cliente. | datetime | date | Sim |
| **DT_FIM_SUBSTIT_APROV** | Data de Fim de validade para a autorização de substituição. Importante: a data de fim não está associada a data de início de aprovação (instante em que soliictação de aprovação é enviada para o aprovador) e sim com a data instantânea em que a página de aprovação é exibida para o Cliente. | datetime | date | Sim |
| **ID_PESSOA_REG_SUBSTIT** | Identificador da Pessoa que realizou o registro de Substituição para Aprovação | int | number(6,0) | Sim |
| **SENHA** | Senha do usuário formada por no mínimo 4 caracteres que podem ser somente números ou letras. A comparação é insensível a letras minúsculas ou maiúsculas. Quando preenchida ignora validação de senha no Active Directory. | varchar(50) | varchar(50) | Sim |
| **TIPO** | Cliente em Ordens de Serviço ou Fila de Grupos de Trabalho | varchar(250) | varchar(250) | Não |
| **DATA_HORA_ULT_AA** | Data/hora do último acesso ao Autoatendimento. | datetime | date | Sim |
| **ID_USER** | Identificador do Usuário associado | int | number(6,0) | Sim |

Tabelas referenciadas por PESSOA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PESSOA** \| \|---\|---\| \| ID_PESSOA \| ID_SUBSTITUTO_APROVACAO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PESSOA** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA_REG_SUBSTIT \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **PESSOA** \| \|---\|---\| \| ID_ORGAO \| ID_ORGAO \| |
| [FORNECEDOR](dados_fornecedor) | \| **FORNECEDOR** \| **PESSOA** \| \|---\|---\| \|  \| ID_FORNECEDOR \| |
| [FATOR_PRIORIDADE](dados_fator_prioridade) | \| **FATOR_PRIORIDADE** \| **PESSOA** \| \|---\|---\| \| ID_FATOR_PRIORIDADE \| ID_FATOR_PRIORIDADE \| |
| [PERFIL_CLIENTE](dados_perfil_cliente) | \| **PERFIL_CLIENTE** \| **PESSOA** \| \|---\|---\| \| ID_PERFIL_CLIENTE \| ID_PERFIL_CLIENTE \| |
| [LOCAL](dados_local) | \| **LOCAL** \| **PESSOA** \| \|---\|---\| \| ID_LOCAL \| ID_LOCAL \| |
| [SV_CULTURE](dados_sv_culture) | \| **SV_CULTURE** \| **PESSOA** \| \|---\|---\| \| ID_CULTURE \| ID_CULTURA_CLIENTE \| |
| [SV_USER](dados_sv_user) | \| **SV_USER** \| **PESSOA** \| \|---\|---\| \| ID_USER \| ID_USER \| |

Tabelas que dependem de PESSOA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [TECNICO](dados_tecnico) | \| **TECNICO** \| **PESSOA** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **PESSOA** \| \|---\|---\| \| ID_COORDENADOR \| ID_PESSOA \| |
| [ORGAO](dados_orgao) | \| **ORGAO** \| **PESSOA** \| \|---\|---\| \| ID_GESTOR \| ID_PESSOA \| |
| [CONTRATO](dados_contrato) | \| **CONTRATO** \| **PESSOA** \| \|---\|---\| \| ID_RESPONSAVEL \| ID_PESSOA \| |
| [AUSENCIA](dados_ausencia) | \| **AUSENCIA** \| **PESSOA** \| \|---\|---\| \| ID_SUBSTITUTO \| ID_PESSOA \| |
| [AUSENCIA](dados_ausencia) | \| **AUSENCIA** \| **PESSOA** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PESSOA** \| \|---\|---\| \| ID_SUBSTITUTO_APROVACAO \| ID_PESSOA \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PESSOA** \| \|---\|---\| \| ID_PESSOA_REG_SUBSTIT \| ID_PESSOA \| |
| [HIST_USUARIO](dados_hist_usuario) | \| **HIST_USUARIO** \| **PESSOA** \| \|---\|---\| \| ID_USUARIO \| ID_PESSOA \| |
| [HIST_ORGAO](dados_hist_orgao) | \| **HIST_ORGAO** \| **PESSOA** \| \|---\|---\| \| ID_GESTOR \| ID_PESSOA \| |
| [HIST_PESSOA](dados_hist_pessoa) | \| **HIST_PESSOA** \| **PESSOA** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [HIST_ITEM](dados_hist_item) | \| **HIST_ITEM** \| **PESSOA** \| \|---\|---\| \| ID_RESPONSAVEL \| ID_PESSOA \| |
| [ITEM_CHARGE_BACK](dados_item_charge_back) | \| **ITEM_CHARGE_BACK** \| **PESSOA** \| \|---\|---\| \| ID_FAVORECIDO \| ID_PESSOA \| |

**Exemplo 1: join com a tabela PESSOA**

```
select PESSOA.*, PESSOA2.NOME_ABREVIADO
from PESSOA left outer join PESSOA PESSOA2 on PESSOA.ID_SUBSTITUTO_APROVACAO = PESSOA2.ID_PESSOA
```

**Exemplo 2: join com a tabela PESSOA**

```
select PESSOA.*, PESSOA2.NOME_ABREVIADO
from PESSOA left outer join PESSOA PESSOA2 on PESSOA.ID_PESSOA_REG_SUBSTIT = PESSOA2.ID_PESSOA
```

**Exemplo 3: join com a tabela ORGAO**

```
select PESSOA.*, ORGAO.DESCRICAO
from PESSOA, ORGAO
where PESSOA.ID_ORGAO = ORGAO.ID_ORGAO
```

**Exemplo 4: join com a tabela FATOR_PRIORIDADE**

```
select PESSOA.*, FATOR_PRIORIDADE.DESCRICAO
from PESSOA left outer join FATOR_PRIORIDADE on PESSOA.ID_FATOR_PRIORIDADE = FATOR_PRIORIDADE.ID_FATOR_PRIORIDADE
```

**Exemplo 5: join com a tabela PERFIL_CLIENTE**

```
select PESSOA.*, PERFIL_CLIENTE.DESCRICAO
from PESSOA left outer join PERFIL_CLIENTE on PESSOA.ID_PERFIL_CLIENTE = PERFIL_CLIENTE.ID_PERFIL_CLIENTE
```
