# GrupoIndicador

Caminho: Customização > Modelo de objetos > Processo > GrupoIndicador

Um Grupo de Indicadores é utilizado para classificar um Indicador de Desempenho. Também permite que Indicadores relacionados sejam agrupados na exibição feita pelo Executive Dashboard.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Texto que descreve com clareza a classificação de Indicadores. | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Grupo Indicador. Este Identificador não pode ser modificado pelo usuário. | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | GrupoIndicador Carrega(int i); |
| **Novo** | Cria um novo registro do tipo GrupoIndicador | GrupoIndicador Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | GrupoIndicador Carrega(string nomePropriedade, object valorPropriedade); |
