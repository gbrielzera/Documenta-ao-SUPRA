# GRUPO_TRABALHO

Caminho: Customização > Modelo de dados > Recurso > GRUPO_TRABALHO

Um Grupo de Trabalho define uma estrutura hierárquica de equipes contendo um coordenador e um ou mais solucionadores. O coordenador de um Grupo de Trabalho possui atribuições especiais podendo realizar diversas ações sobre Ordens de Serviço sob responsabilidade de seus subordinados. Um Grupo de Trabalho pode corresponder a um nível na hierarquia de Órgãos, porém não existe uma relação automática com este cadastro.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_GRUPO_TRABALHO** | Número sequencial gerado automaticamente pelo sistema para Identificar um GrupoTrabalho | int | number(6,0) | Não |
| **DESCRICAO** | Texto que descreve claramente o objetivo do Grupo de Trabalho. Este texto é utilizado em diversas telas e relatórios da aplicação Supravizio. | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que o Grupo de Trabalho está ativo. Quando ativo o Grupo de Trabalho pode ser utilizado na implementação de Papéis de Processo ou para lotação de profissionais. Quando um Grupo de Trabalho se torna Inativo automaticamente todos os profissionais associados também são desativados. | char(3) | char(3) | Não |
| **ID_GRUPO_TRABALHO_PAI** | Identificador do Grupo de Trabalho Pai. Esta associação permite a criação de uma hierarquia de Grupos de Trabalho. | int | number(6,0) | Sim |
| **ID_COORDENADOR** | Identificador da Pessoa responsável pela Coordenação do Grupo de Trabalho. O coordenador possui atribuições especiais podendo realizar diversas operações e edições nas Ordens de Serviço sob responsabilidade dos seus subordinados. | int | number(6,0) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **SIGLA** | Nome resumido (código) utilizado para identificar um Grupo de Trabalho. | varchar(50) | varchar(50) | Não |
| **PERMITE_CANCELAR** | Regra de autorização para execução da operação de Cancelamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | varchar(250) | varchar(250) | Não |
| **PERMITE_ENCAMINHAR** | Regra de autorização para execução da operação de Encaminhamento de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | varchar(250) | varchar(250) | Não |
| **PERMITE_CLASSIFICAR** | Regra de autorização para execução da operação de Classificação de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | varchar(250) | varchar(250) | Não |
| **PERMITE_REABRIR** | Regra de autorização para execução da operação de Reabertura de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | varchar(250) | varchar(250) | Não |
| **PERMITE_INTERROMPER_ANS** | Regra de autorização para execução da operação de adicionar uma Interrupção de ANS de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | varchar(250) | varchar(250) | Não |
| **PERMITE_PRIORIZAR** | Regra de autorização para execução da operação de Priorização de Ordens de Serviço. Esta regra não é aplicada recursivamente nos níveis inferiores de Grupos de Trabalho. | varchar(250) | varchar(250) | Não |
| **PERMITE_VER_GRUPOS** | Permite visualizar outros Grupos de Trabalho na árvore de Grupos de Trabalho. Caso esta propriedade seja desmarcada o solucionador deste grupo poderá visualizar apenas o seu grupo de trabalho e sub-grupos. | char(3) | char(3) | Não |
| **EXIBE_ALERTA_OS_GRUPO** | Regra de autorização para exibição de Ordens de Serviço no Painel de Alertas do Workspace. | varchar(250) | varchar(250) | Não |

Tabelas referenciadas por GRUPO_TRABALHO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **GRUPO_TRABALHO** \| \|---\|---\| \| ID_PESSOA \| ID_COORDENADOR \| |
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **GRUPO_TRABALHO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO_PAI \| |

Tabelas que dependem de GRUPO_TRABALHO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **GRUPO_TRABALHO** \| \|---\|---\| \| ID_GRUPO_TRABALHO_PAI \| ID_GRUPO_TRABALHO \| |
| [CONTRATO_TECNICO](dados_contrato_tecnico) | \| **CONTRATO_TECNICO** \| **GRUPO_TRABALHO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [TECNICO](dados_tecnico) | \| **TECNICO** \| **GRUPO_TRABALHO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |

**Exemplo 1: join com a tabela PESSOA**

```
select GRUPO_TRABALHO.*, PESSOA.NOME_ABREVIADO
from GRUPO_TRABALHO, PESSOA
where GRUPO_TRABALHO.ID_COORDENADOR = PESSOA.ID_PESSOA
```

**Exemplo 2: join com a tabela GRUPO_TRABALHO**

```
select GRUPO_TRABALHO.*, GRUPO_TRABALHO2.DESCRICAO
from GRUPO_TRABALHO left outer join GRUPO_TRABALHO GRUPO_TRABALHO2 on GRUPO_TRABALHO.ID_GRUPO_TRABALHO_PAI = GRUPO_TRABALHO2.ID_GRUPO_TRABALHO
```
