# CategoriaRisco

Caminho: Customização > Modelo de objetos > Processo > CategoriaRisco

Categoria de Riscos e Controles

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do CategoriaRisco | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um CategoriaRisco | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | CategoriaRisco Carrega(int i); |
| **Novo** | Cria um novo registro do tipo CategoriaRisco | CategoriaRisco Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | CategoriaRisco Carrega(string nomePropriedade, object valorPropriedade); |
