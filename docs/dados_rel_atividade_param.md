# REL_ATIVIDADE_PARAM

Caminho: Customização > Modelo de dados > Processo > REL_ATIVIDADE_PARAM

Configuração de valores para os parâmetros existentes no relatório. Estes parâmetros são definidos no Editor de Relatórios.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_ATIVIDADE** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Atividade | int | number(6,0) | Não |
| **ID_REPORT** | Identificador do relatório de apoio ou utilizado como anexo em evento de mensagem. | int | number(6,0) | Não |
| **NAME** | Nome do parâmetro do relatório definido no Editor de Relatórios. | varchar(500) | varchar(500) | Não |
| **VALOR** | Fórmula que determina o valor para o parâmetro do relatório. Este valor é utilizado sempre que for necessário exibir o conteúdo do relatório. | varchar(500) | varchar(500) | Sim |
| **PERMITE_MODIFICAR** | Permite que um valor de parâmetro previamente configurado seja modificado pelo usuário no instante em que o relatório for exibido. A modificação é feita utilizando o painel de parâmetros localizado a esquerda da tela de visualização de relatório. | char(3) | char(3) | Não |

Tabelas referenciadas por REL_ATIVIDADE_PARAM

| **Tabela** | **Colunas de ligação** |
|---|---|
| [REL_ATIVIDADE](dados_rel_atividade) | \| **REL_ATIVIDADE** \| **REL_ATIVIDADE_PARAM** \| \|---\|---\| \| ID_REPORT \| ID_REPORT \| \| ID_ATIVIDADE \| ID_ATIVIDADE \| |
