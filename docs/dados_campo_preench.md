# CAMPO_PREENCH

Caminho: Customização > Modelo de dados > Processo > CAMPO_PREENCH

Campo para Preenchimento durante a execução do Processo.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CAMPO_PREENCH** | Número sequencial gerado automaticamente pelo sistema para Identificar um CampoPreenchimento | int | number(6,0) | Não |
| **NOME** | Nome do Campo para preenchimento | varchar(250) | varchar(250) | Não |
| **ID_OPERACAO_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | int | number(6,0) | Não |
| **OBRIGATORIO** | Indica que o preenchimento é obrigatório ou opcional. | char(3) | char(3) | Não |
| **SEQUENCIA** | Sequencia de apresentação do Campo | int | number(6,0) | Não |
| **NOME_CUSTOM** | Nome do campo customizado | varchar(100) | varchar(100) | Sim |
| **ROTULO** | Rótulo para edição do Campo. Se não preenchido o sistema exibe descritivo original definido no Dicionário de Classes. | varchar(500) | varchar(500) | Sim |
| **EXIBE_AA** | Permite exibir ou não o campo nas consultas da respectiva Ordem de Serviço no Autoatendimento | char(3) | char(3) | Não |
| **EXIBE_BTN_INC_CLIENTE_AA** | Permite exibir ou não o comando para incluir o Cliente em preenchimento de campo (lista) Favorecido no Autoatendimento | char(3) | char(3) | Não |
| **INCLUIR_CLI_AUTO_AA** | Caso o campo seja Favorecido automaticamente inclui o Cliente da OS na listagem de pessoas. | char(3) | char(3) | Não |
| **CONFIG_CONTROLE** | Informações sobre a configuração de controles utilizados para edição do campo | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por CAMPO_PREENCH

| **Tabela** | **Colunas de ligação** |
|---|---|
| [OPERACAO_ATIVIDADE](dados_operacao_atividade) | \| **OPERACAO_ATIVIDADE** \| **CAMPO_PREENCH** \| \|---\|---\| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |

**Exemplo 1: join com a tabela OPERACAO_ATIVIDADE**

```
select CAMPO_PREENCH.*
from CAMPO_PREENCH, OPERACAO_ATIVIDADE
where CAMPO_PREENCH.ID_OPERACAO_ATIVIDADE = OPERACAO_ATIVIDADE.ID_OPERACAO_ATIVIDADE
```
