# QuestaoPesquisa

Caminho: Customização > Modelo de objetos > Processo > QuestaoPesquisa

Uma Questão de Pesquisa pode ser utilizada na elaboração de Pesquisas de Satisfação enviadas para Clientes após a finalização de uma Ordem de Serviço.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que o Indicador está ativo. Somente Indicadores ativos são exibidos na Pesquisa de Satisfação | Booleano |
| **Descricao** | Descrição do Indicador | String |
| **GrupoQuestao** | Grupo associado com a Questão | [GrupoQuestao](objetos_grupoquestao) |
| **GrupoQuestaoId** | Identificador do GrupoQuestao associado | Inteiro |
| **Id** | Identificador | Inteiro |
| **Texto** | Texto apresentado para o Cliente no momento de aplicação da Pesquisa de Satisfação | String |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | QuestaoPesquisa Carrega(int i); |
| **Novo** | Cria um novo registro do tipo QuestaoPesquisa | QuestaoPesquisa Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | QuestaoPesquisa Carrega(string nomePropriedade, object valorPropriedade); |
