# GrupoQuestao

Caminho: Customização > Modelo de objetos > Processo > GrupoQuestao

Um Grupo de Questões define um agrupamento de questões de Pesquisa de Satisfação que possuem um objetivo comum na avaliação de um Serviço. Todas as questões associadas a um grupo possuem as mesmas opções de respostas. Um Grupo de Questões pode ser alvo de avaliação em um Indicador de Desempenho.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Descricao** | Descrição detalhada do Grupo de Questões | String |
| **Escore** | Escore de Questão | [Lista de Escore](objetos_escore) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Grupo de Questões | Inteiro |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | GrupoQuestao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo GrupoQuestao | GrupoQuestao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | GrupoQuestao Carrega(string nomePropriedade, object valorPropriedade); |
