# GrupoServico

Caminho: Customização > Modelo de objetos > Processo > GrupoServico

Um Grupo de Serviço é o segundo mais elevado nível hierárquico de classificação de Serviços.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do GrupoServico | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um GrupoServico | Inteiro |
| **SuperClasseServico** | Nível mais elevado na hierarquia de classificações de Serviços. | [SuperClasseServico](objetos_superclasseservico) |
| **SuperClasseServicoId** | Identificador da Classe de Serviço associada | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | GrupoServico Carrega(int i); |
| **Novo** | Cria um novo registro do tipo GrupoServico | GrupoServico Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | GrupoServico Carrega(string nomePropriedade, object valorPropriedade); |
