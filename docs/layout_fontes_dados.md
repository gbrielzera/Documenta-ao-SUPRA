# Layout para Fontes de Dados

Caminho: Guia para Administradores > Roteiro de implantação > Importando Dados > Rotina de Importação de Dados de Recursos Humanos > Layout para Fontes de Dados

Os layouts abaixo servem para definição de suas respectivas fontes de dados em bancos de dados. Estas fontes de dados podem ser simplesmente tabelas ou views de banco de dados.

**Fonte de dados para Calendários:**

| **Nome do Campo** | **Documentação** | **Permite** **duplicidade** | **Permite nulos** | **Tipo de dado** | **Exemplo de saída** |
|---|---|---|---|---|---|
| **DESCRICAO_CALENDARIO** | Descrição do Calendário. Pode ser um calendário regional (municipal, estadual ou calendário federal). | Sim | Não | Varchar(500) | ‘Rio de Janeiro’, ‘Nacional’, ‘Vitória’. |
| **DATA_FERIADO** | Data do feriado. | Sim | Não | Varchar(50) | ‘2009-12-13’, ‘13/12/2009’ |
| **DESCRICAO_FERIADO** | Nome do feriado. | Sim | Não | Varchar(500) | ‘Proclamação da República’, ‘Aniversário da Cidade’ |

**Fonte de dados para Clientes:**

| **Nome do Campo** | **Documentação** | **Permite** **duplicidade** | **Permite nulos** | **Tipo de dado** | **Exemplo de saída** |
|---|---|---|---|---|---|
| **NOME** | Nome completo da pessoa | Sim | Não | Varchar(500) | ‘João da Silva’. |
| **TELEFONE** | Telefone de contato | Sim | Sim | Varchar(50) | ‘39.2393.9393’ |
| **CELULAR_PARTICULAR** | Celular particular de contato | Sim | Sim | Varchar (50) | ‘39.9393.9393’ |
| **CELULAR_EMPRESA** | Celular corporativo | Sim | Sim | Varchar (50) | ‘21.9393.9393’ |
| **EMAIL** | Email | Sim (no entanto, para a funcionalidade de recuperação de senha, é necessário que este não possua duplicidade em cadastros) | Sim | Varchar (50) | ‘joao.silva@empr.com.br’ |
| **USUARIO_REDE** | Usuário de rede. Se não existir projetar o Email sem domínio. | Não | Não | Varchar (50) | ‘joao.silva’ |
| **SIGLA_ORGAO** | Código de identificação da área onde está lotada a pessoa. | Sim | Não | Varchar (50) | ‘GERTI’ |
| **DESCRICAO_ORGAO** | Descritivo da área onde está lotada a pessoa. Este campo é utilizado para resolver a lotação se não existir um campo de sigla. | Sim | Não | Varchar (500) | ‘Gerência de TI’ |
| **TIPO_COLABORADOR** | Valores possíveis (somente): • ‘EMPREGADO’ • ‘TERCEIRO’ | Sim | Não | Varchar (50) | ‘EMPREGADO’, ‘TERCEIRO’ |
| **CARGO** | Cargo da pessoa. Importante: não existe no Supravizio uma tabela de cargos. | Sim | Sim | Varchar (500) | ‘Analista de Sistemas Júnior’ |
| **CODIGO_FORNECEDOR** | Código do Fornecedor para colaboradores do tipo TERCEIRO. Caso EMPREGADO, código da própria empresa. | Sim | Não | Varchar (50) | ‘VENKI’ |
| **DESCRICAO_FORNECEDOR** | Descritivo do Fornecedor para colaboradores do tipo TERCEIRO. Caso EMPREGADO, código da própria empresa. | Sim | Não | Varchar(500) | ‘Venki Tecnologia em Software Ltda’ |
| **UNIDADE_NEGOCIO** | Unidade de Negócio onde está localizada a pessoa. | Sim | Sim | Varchar (50) | ‘Rio de Janeiro’ |
| **SIGLA_UNIDADE_NEGOCIO** | Sigla da Unidade de Negócio onde está localizada a pessoa. | Sim | Sim | Varchar (50) | ‘RJ’ |
| **PREDIO** | Prédio de uma UNIDADE_NEGOCIO onde está localizada a pessoa. | Sim | Sim | Varchar (50) | ‘Ed. Central’, ‘Ed. Monsarás’ |
| **LOCAL** | Sala ou andar de um PREDIO onde está localizada a pessoa. | Sim | Sim | Varchar (50) | ‘Sala 203’, ‘3.o Andar’ |
| **DESC_CALENDARIO_UN_NEGOCIO** | Descrição do calendário associado a Unidade de Negócio associado a pessoa. | Sim | Não | Varchar (500) | ‘São Paulo’ |
| **ATIVO** | ‘S’ se a pessoa estiver ativa e ‘N’ caso contrário (somente estes 2 valores). Caso nulo, admite ‘S’. | Sim | Sim | Varchar(1) | ‘S’ e ‘N’ apenas. |

**Fonte de Dados de Áreas (Órgãos):**

| **Nome do Campo** | **Documentação** | **Permite** **duplicidade** | **Permite nulos** | **Tipo de dado** | **Exemplo de saída** |
|---|---|---|---|---|---|
| **SIGLA** | Sigla ou código que identifica uma determinada área. | Não | Não | Varchar(50) | ‘COSUP’, ‘DIROP’, ‘PRES’ |
| **DESCRICAO** | Descritivo da área. | Não | Não | VARCHAR(500) | ‘Gerência de TI’ |
| **GESTOR** | Usuário de rede do gestor da área. | Sim | Sim | VARCHAR(20) | ‘admin’ |
| **NOME_GESTOR** | Nome completo do gestor da área | Sim | Sim | VARCHAR(500) | ‘Jorge Antunes da Silva’ |
| **SIGLA_ORGAO_PAI** | Código da área superior na hierarquia. Se não preenchido então o registro da área representa um item raiz. | Sim | Sim | VARCHAR(50) | ‘PRES’ |
| **DESCRICAO_ORGAO_PAI** | Descritivo da área superior na hierarquia. | Sim | Sim | VARCHAR(500) | ‘Presidência’ |
| **EMPRESA** | Descritivo da empresa a qual pertence a área. | Sim | Não | VARCHAR(500) | ‘Lojas S.A.’ |
| **SIGLA_EMPRESA** | Sigla da empresa a qual pertence à área. | Sim | Não | VARCHAR(50) | 'LJ' |
| **ATIVO** | ‘S’ se a pessoa estive ativa e ‘N’ caso contrário. | Sim | Não | VARCHAR(1) | ‘S’, ‘N’ (apenas) |
