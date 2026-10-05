# SuperClasseServico

Caminho: Customização > Modelo de objetos > Processo > SuperClasseServico

Uma Classe de Serviço é o maior nível hierárquico de classificação de Serviços.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada da ClasseServico | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma ClasseServico | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | SuperClasseServico Carrega(int i); |
| **Novo** | Cria um novo registro do tipo SuperClasseServico | SuperClasseServico Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | SuperClasseServico Carrega(string nomePropriedade, object valorPropriedade); |
