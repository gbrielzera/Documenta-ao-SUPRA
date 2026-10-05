# TipoPosse

Caminho: Customização > Modelo de objetos > Ativos > TipoPosse

Tipo de Posse

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Tipo de Posse está ativo no sistema | Booleano |
| **Descricao** | Descrição detalhada para o Tipo de Posse | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Posse | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | TipoPosse Carrega(int i); |
| **Novo** | Cria um novo registro do tipo TipoPosse | TipoPosse Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | TipoPosse Carrega(string nomePropriedade, object valorPropriedade); |
