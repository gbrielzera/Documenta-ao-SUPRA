# REL_OPERACAO_PARAM

Caminho: Customização > Modelo de dados > Processo > REL_OPERACAO_PARAM

Configuração de valores para os parâmetros existentes no relatório da aprovação ou relatório utilizado para gerar arquivos anexados na ocorrência. Estes parâmetros são definidos no Editor de Relatórios.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_REPORT** | Identificador do relatório que será utilizado na aprovação. | int | number(6,0) | Não |
| **ID_OPERACAO_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | int | number(6,0) | Não |
| **NAME** | Nome do parâmetro do relatório definido no Editor de Relatórios. | varchar(500) | varchar(500) | Não |
| **VALOR** | Fórmula que determina o valor para o parâmetro do relatório. Este valor é utilizado sempre que for necessário exibir o conteúdo do relatório. | varchar(500) | varchar(500) | Sim |

Tabelas referenciadas por REL_OPERACAO_PARAM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [REL_OPERACAO](dados_rel_operacao) | \| **REL_OPERACAO** \| **REL_OPERACAO_PARAM** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| \| ID_OPERACAO_ATIVIDADE \| ID_OPERACAO_ATIVIDADE \| |
