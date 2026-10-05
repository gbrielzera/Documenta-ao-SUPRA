# PAPEL_PROCESSO

Caminho: Customização > Modelo de dados > Processo > PAPEL_PROCESSO

Papel de uma Pessoa dentro da execução do Processo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_PAPEL_PROCESSO** | Número sequencial gerado automaticamente pelo sistema para Identificar um PapelProcesso | int | number(6,0) | Não |
| **NOME** | Nome do Papel | varchar(100) | varchar(100) | Não |
| **ID_DESENHO_PROCESSO** | Número sequencial gerado automaticamente pelo sistema para Identificar um DesenhoProcesso | int | number(6,0) | Não |
| **SCRIPT_ATORES** | Script para seleção de Atores de um Papel de Processo | text | clob | Sim |
| **ID_GRUPO_TRABALHO** | Identificador do GrupoTrabalho associado | int | number(6,0) | Sim |
| **ID_PESSOA** | Identificador da Pessoa associada | int | number(6,0) | Sim |
| **ATOR_GRUPO_TRABALHO** | Critério para seleção de Atores em Grupos de Trabalho | varchar(250) | varchar(250) | Não |
| **ID_PAPEL_CLASSE_NEGOCIO** | Identificador do PapelClasseNegocio associado | int | number(6,0) | Sim |
| **REFERENCIA** | Descritivo completo sobre o Papel de Processo. Se não preenchido e estabelecida uma relação com um Papel global então é utilizada a referência deste último. | text | clob | Sim |
| **INC_COORDENADOR** | Inclui seleção do Coordenador do Grupo de Trabalho. Se o critério de seleção de solucionadores do grupo for Coordenador então este campo é desconsiderado. | char(3) | char(3) | Não |
| **EXC_APROVACAO** | Exclui da contagem de Ocorrências aquelas que estiveram Pendentes de Aprovação. | char(3) | char(3) | Não |

Tabelas referenciadas por PAPEL_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [GRUPO_TRABALHO](dados_grupo_trabalho) | \| **GRUPO_TRABALHO** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_GRUPO_TRABALHO \| ID_GRUPO_TRABALHO \| |
| [PESSOA](dados_pessoa) | \| **PESSOA** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PESSOA \| ID_PESSOA \| |
| [PAPEL_CLASSE_NEGOCIO](dados_papel_classe_negocio) | \| **PAPEL_CLASSE_NEGOCIO** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PAPEL_CLASSE_NEGOCIO \| ID_PAPEL_CLASSE_NEGOCIO \| |
| [DESENHO_PROCESSO](dados_desenho_processo) | \| **DESENHO_PROCESSO** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_DESENHO_PROCESSO \| ID_DESENHO_PROCESSO \| |

Tabelas que dependem de PAPEL_PROCESSO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PAPEL_DESTINATARIO \| ID_PAPEL_PROCESSO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PAPEL_RESPONSAVEL \| ID_PAPEL_PROCESSO \| |
| [ATOR](dados_ator) | \| **ATOR** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_PROCESSO \| |
| [APROVADOR_OPERACAO](dados_aprovador_operacao) | \| **APROVADOR_OPERACAO** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PAPEL_APROVADOR \| ID_PAPEL_PROCESSO \| |
| [CLIENTE_AUTORIZADO](dados_cliente_autorizado) | \| **CLIENTE_AUTORIZADO** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_PROCESSO \| |
| [ACAO_ACORDO](dados_acao_acordo) | \| **ACAO_ACORDO** \| **PAPEL_PROCESSO** \| \|---\|---\| \| ID_PAPEL_PROCESSO \| ID_PAPEL_PROCESSO \| |

**Exemplo 1: join com a tabela PAPEL_CLASSE_NEGOCIO**

```
select PAPEL_PROCESSO.*, PAPEL_CLASSE_NEGOCIO.NOME
from PAPEL_PROCESSO left outer join PAPEL_CLASSE_NEGOCIO on PAPEL_PROCESSO.ID_PAPEL_CLASSE_NEGOCIO = PAPEL_CLASSE_NEGOCIO.ID_PAPEL_CLASSE_NEGOCIO
```

**Exemplo 2: join com a tabela DESENHO_PROCESSO**

```
select PAPEL_PROCESSO.*
from PAPEL_PROCESSO, DESENHO_PROCESSO
where PAPEL_PROCESSO.ID_DESENHO_PROCESSO = DESENHO_PROCESSO.ID_DESENHO_PROCESSO
```
