# CATEGORIA

Caminho: Customização > Modelo de dados > Processo > CATEGORIA

Classificação manual atribuída a Ordens de Serviço associadas com uma cor e com possibilidade de exibição na barra de rolagem de Ordens de Serviço. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática.

Campos desta tabela:

| **Nome** | **Descrição** | **Tipo SQL Server** | **Tipo Oracle** | **Permite nulos** |
|---|---|---|---|---|
| **ID_CATEGORIA** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Categoria | int | number(6,0) | Não |
| **DESCRICAO** | Descrição detalhada da Categoria | varchar(500) | varchar(500) | Não |
| **ATIVO** | Indica que a Categoria está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | char(3) | char(3) | Não |
| **VERMELHO** | Fator vermelho para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. | int | number(6,0) | Não |
| **VERDE** | Fator verde para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. | int | number(6,0) | Não |
| **AZUL** | Fator azul para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. | int | number(6,0) | Não |
| **VISIVEL_PAINEL_WS** | Indica que Ordens de Serviço desta categoria serão visíveis na barra de rolagem localizada na parte inferior da tela Workspace (Painel de Alertas). Esta configuração ainda está condicionada a regra de visualização do Grupo de Trabalho (veja as configurações do Grupo de Trabalho do solucionador). | char(3) | char(3) | Não |

Tabelas que dependem de CATEGORIA

| **Tabela** | **Colunas de ligação** |
|---|---|
| [ORDEM_SERVICO](dados_ordem_servico) | \| **ORDEM_SERVICO** \| **CATEGORIA** \| \|---\|---\| \| ID_CATEGORIA \| ID_CATEGORIA \| |
