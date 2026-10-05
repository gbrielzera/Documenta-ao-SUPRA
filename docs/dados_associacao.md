# ASSOCIACAO

Caminho: Customização > Modelo de dados > Processo > ASSOCIACAO

Uma Associação define um relacionamento entre duas Ocorrências de Processo. Estas associações podem ser estabelecidas pelo usuário na tela de edição de Ordens de Serviço ou automaticamente por configuração de Processo. Para criação de uma Associação é necessário definir: um Tipo de Subprocesso para cada uma das ocorrências, uma frase para leitura da Associação, outra fase para leitura inversa da Associação e finalmente a cardinalidade desejada.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ASSOCIACAO** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Associacao | int | number(6,0) | Não |
| **ATIVO** | Indica que a Associacao está ativa no Sistema. Se estiver inativa então não é possível a criação de novas associações desta natureza. | char(3) | char(3) | Não |
| **ID_CLASSE_FONTE** | Identificador do Tipo de Subprocesso que é responsável por invocar uma outra ocorrência de processo (rotina chamadora). | int | number(6,0) | Não |
| **ID_CLASSE_ALVO** | Identificador do Tipo de Subprocesso que é invocado pela associação. | int | number(6,0) | Não |
| **FRASE_ASSOC** | Frase utilizada para estabelecer a Associação. | varchar(500) | varchar(500) | Não |
| **FRASE_INV_ASSOC** | Frase utilizada para representar o sentido inverso da Associação. | varchar(500) | varchar(500) | Não |
| **CARD_FONTE** | Cardinalidade da Associação no sentido Alvo para Fonte | varchar(250) | varchar(250) | Não |
| **CARD_ALVO** | Cardinalidade da Associação no sentido Fonte para Alvo. Indica que podemos ter várias ou uma única ocorrência como Alvo no relacionamento. | varchar(250) | varchar(250) | Não |
| **ID_DOMAIN** | Identificador do Domínio associado | int | number(6,0) | Não |
| **NOME** | Nome para identificação e recuperação da Associação. O nome não pode conter espaços e deve conter apenas caracteres alfanuméricos. Também deve ser único entre todas as Associações e utilizado em scripts para recuperação da Associação. | varchar(500) | varchar(500) | Não |

Tabelas referenciadas por ASSOCIACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **ASSOCIACAO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_ALVO \| |
| [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) | \| **CLASSE_SUB_PROCESSO** \| **ASSOCIACAO** \| \|---\|---\| \| ID_CLASSE_SUB_PROCESSO \| ID_CLASSE_FONTE \| |

Tabelas que dependem de ASSOCIACAO

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ASSOCIACAO_OCORR](dados_associacao_ocorr) | \| **ASSOCIACAO_OCORR** \| **ASSOCIACAO** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **ASSOCIACAO** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |
| [ASSOCIACAO_SUBPROCESSO](dados_associacao_subprocesso) | \| **ASSOCIACAO_SUBPROCESSO** \| **ASSOCIACAO** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |
| [GATILHO_ASSOC](dados_gatilho_assoc) | \| **GATILHO_ASSOC** \| **ASSOCIACAO** \| \|---\|---\| \| ID_ASSOCIACAO \| ID_ASSOCIACAO \| |

**Exemplo 1: join com a tabela CLASSE_SUB_PROCESSO**

```
select ASSOCIACAO.*, CLASSE_SUB_PROCESSO.DESCRICAO
from ASSOCIACAO, CLASSE_SUB_PROCESSO
where ASSOCIACAO.ID_CLASSE_ALVO = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```

**Exemplo 2: join com a tabela CLASSE_SUB_PROCESSO**

```
select ASSOCIACAO.*, CLASSE_SUB_PROCESSO.DESCRICAO
from ASSOCIACAO, CLASSE_SUB_PROCESSO
where ASSOCIACAO.ID_CLASSE_FONTE = CLASSE_SUB_PROCESSO.ID_CLASSE_SUB_PROCESSO
```
