# CONTROLE

Caminho: Customização > Modelo de dados > Processo > CONTROLE

Controles

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CONTROLE** | Número sequencial gerado automaticamente pelo sistema para Identificar um Controle | int | number(6,0) | Não |
| **DESCRICAO** | Descrição do Controle | text | clob | Não |
| **CLASSIFICACAO** | Tipo de Controle | varchar(250) | varchar(250) | Não |
| **CONTROLE_CHAVE** | Controle chave | char(3) | char(3) | Não |
| **AUTO_CONTROLE** | Tipo de operacionalização do Controle. | varchar(250) | varchar(250) | Não |
| **ID_FREQ_CONTROLE** | Identificador do(a) FrequenciaControle associado(a) | int | number(6,0) | Não |
| **ROTEIRO_TESTE** | Roteiro de teste do Controle | text | clob | Sim |
| **AMOSTRA_TESTE** | Orientação para amostragem de teste | text | clob | Sim |
| **ID_SUB_PROCESSO** | Identificador do Tipo de Subprocesso | int | number(6,0) | Não |
| **ID_CLASSE_CONTROLE** | Identificador do(a) ClasseControle associado(a) | int | number(6,0) | Não |
| **ID_RISCO** | Identificador do RiscoProcesso associado | int | number(6,0) | Não |
| **ID_SUB_PROC_RISCO** | Identificador do RiscoProcesso associado | int | number(6,0) | Não |
| **EFETIV_DESENHO** | Possui | char(3) | char(3) | Não |
| **EFETIV_OPERACIONAL** | Possui efetividade operacional | char(3) | char(3) | Não |
| **CONTROLE_ADEQUADO** | O Controle está adequado | char(3) | char(3) | Não |
| **COSO_ATIV_CONTROL** | Atividade de Controle | char(3) | char(3) | Não |
| **COSO_AVAL_RISCO** | Avaliação de Risco | char(3) | char(3) | Não |
| **COSO_CTRL_ENV** | Control Enviroment | char(3) | char(3) | Não |
| **COSO_INF_COM** | Informação e Comunicação | char(3) | char(3) | Não |
| **COSO_MONITORA** | Monitoramento | char(3) | char(3) | Não |
| **OBJ_TOTALIDADE** | Totalidade | char(3) | char(3) | Não |
| **OBJ_EXATIDAO** | Exatidão | char(3) | char(3) | Não |
| **OBJ_VALIDADE** | Validade | char(3) | char(3) | Não |
| **OBJ_ACESS_REST** | Acesso restrito | char(3) | char(3) | Não |
| **TESTE_HABILITADO** | Controle deve ser testado | char(3) | char(3) | Não |
| **ID_FREQ_TESTE** | Frequência de teste do Controle | int | number(6,0) | Não |

Tabelas referenciadas por CONTROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [FREQ_CONTROLE](dados_freq_controle) | \| **FREQ_CONTROLE** \| **CONTROLE** \| \|---\|---\| \| ID_FREQ_CONTROLE \| ID_FREQ_TESTE \| |
| [FREQ_CONTROLE](dados_freq_controle) | \| **FREQ_CONTROLE** \| **CONTROLE** \| \|---\|---\| \| ID_FREQ_CONTROLE \| ID_FREQ_CONTROLE \| |
| [CLASSE_CONTROLE](dados_classe_controle) | \| **CLASSE_CONTROLE** \| **CONTROLE** \| \|---\|---\| \| ID_CLASSE_CONTROLE \| ID_CLASSE_CONTROLE \| |
| [RISCO_PROCESSO](dados_risco_processo) | \| **RISCO_PROCESSO** \| **CONTROLE** \| \|---\|---\| \| ID_RISCO \| ID_RISCO \| \| ID_SUB_PROCESSO \| ID_SUB_PROC_RISCO \| |
| [SUB_PROCESSO](dados_sub_processo) | \| **SUB_PROCESSO** \| **CONTROLE** \| \|---\|---\| \| ID_SUB_PROCESSO \| ID_SUB_PROCESSO \| |

Tabelas que dependem de CONTROLE

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ATIVIDADE](dados_atividade) | \| **ATIVIDADE** \| **CONTROLE** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |
| [TESTE_CONTROLE](dados_teste_controle) | \| **TESTE_CONTROLE** \| **CONTROLE** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |
| [FIGURA](dados_figura) | \| **FIGURA** \| **CONTROLE** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |
| [CONTROL_AFIRM](dados_control_afirm) | \| **CONTROL_AFIRM** \| **CONTROLE** \| \|---\|---\| \| ID_CONTROLE \| ID_CONTROLE \| |

**Exemplo 1: join com a tabela FREQ_CONTROLE**

```
select CONTROLE.*, FREQ_CONTROLE.DESCRICAO
from CONTROLE, FREQ_CONTROLE
where CONTROLE.ID_FREQ_TESTE = FREQ_CONTROLE.ID_FREQ_CONTROLE
```

**Exemplo 2: join com a tabela FREQ_CONTROLE**

```
select CONTROLE.*, FREQ_CONTROLE.DESCRICAO
from CONTROLE, FREQ_CONTROLE
where CONTROLE.ID_FREQ_CONTROLE = FREQ_CONTROLE.ID_FREQ_CONTROLE
```

**Exemplo 3: join com a tabela CLASSE_CONTROLE**

```
select CONTROLE.*, CLASSE_CONTROLE.DESCRICAO
from CONTROLE, CLASSE_CONTROLE
where CONTROLE.ID_CLASSE_CONTROLE = CLASSE_CONTROLE.ID_CLASSE_CONTROLE
```

**Exemplo 4: join com a tabela SUB_PROCESSO**

```
select CONTROLE.*
from CONTROLE, SUB_PROCESSO
where CONTROLE.ID_SUB_PROCESSO = SUB_PROCESSO.ID_SUB_PROCESSO
```
