# AreaRisco

Caminho: Customização > Modelo de objetos > Processo > AreaRisco

Área de negócio atingida pelo Risco

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do AreaRisco | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um AreaRisco | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | AreaRisco Carrega(int i); |
| **Novo** | Cria um novo registro do tipo AreaRisco | AreaRisco Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | AreaRisco Carrega(string nomePropriedade, object valorPropriedade); |
