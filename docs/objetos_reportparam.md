# ReportParam

Caminho: Customização > Modelo de objetos > Utilitários > ReportParam

Relação de parâmetros do relatório

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **DatabaseConnection** | Configuração de conexão para banco de dados externo utilizado para recuperação de itens utilizados como opções de parâmetros. | [DatabaseConnection](objetos_databaseconnection) |
| **DatabaseConnectionId** | Identificador da configuração de banco externo utilizado para alimentar os itens disponíveis para seleção no parâmetro. | Inteiro |
| **LookupQuery** | Relação de itens separados por ponto e vírtula ou consulta SQL utilizada para recuperar registros que servirão de opções. Todos estes itens são apresentados em um controle do tipo 'Combobox'. | String |
| **Name** | Nome do parâmetro definido no instante em que o usuário monta o comando SQL de select ou manualmente na janela de parâmetros. | String |
| **ReportId** | Identificador do relatório proprietário do parâmetro. | Inteiro |
| **Type** | Tipo de dado do parâmetro | String |
