# TipoSolicitacao

Caminho: Customização > Modelo de objetos > Processo > TipoSolicitacao

Agrupamento de solicitações exibido em um dos primeiros passos da Abertura de Ordens de Serviço do Autoatendimento.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do TipoSolicitacao | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um TipoSolicitacao | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | TipoSolicitacao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo TipoSolicitacao | TipoSolicitacao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | TipoSolicitacao Carrega(string nomePropriedade, object valorPropriedade); |
