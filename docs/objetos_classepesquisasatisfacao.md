# ClassePesquisaSatisfacao

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao

Uma Classe de Pesquisa de Satisfação define um conjunto de configurações utilizado para geração de Pesquisas de Satisfação enviadas para clientes após finalização de uma Ordem de Serviço. O envio da pesquisa está condicionado ao evento terminador utilizado na definição do processo aplicado em Ordens de Serviço alvo da pesquisa.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que a ClassePesquisaSatisfacao está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | Booleano |
| **Descricao** | Descrição detalhada da ClassePesquisaSatisfacao | String |
| **ExpressaoPercentualEnvio** | Fórmula que é avaliada para determinar o Percentual de Envio de Pesquisas de Satisfação. Quando preenchido será desconsiderado o campo 'Percentual envio'. | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma ClassePesquisaSatisfacao | Inteiro |
| **PercentualEnvio** | Número percentual entre 0 e 100 que indica a probabilidade de envio de Pesquisa de Satisfação. O valor 0 indica que nenhuma Pesquisa será enviada enquanto 100 estabelece que sempre será enviada Pesquisa de Satisfação | Inteiro |
| **QuestaoGeral** | Questão que é exibida no fim da Pesquisa de Satisfação para obter a satisfação geral do Cliente | [QuestaoPesquisa](objetos_questaopesquisa) |
| **QuestaoGeralId** | Identificador da QuestaoPesquisa associada | Inteiro |
| **Questoes** | Questões que farão parte da Pesquisa de Satisfação | [Lista de QuestaoClassePesquisa](objetos_questaoclassepesquisa) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | ClassePesquisaSatisfacao Carrega(int i); |
| **Novo** | Cria um novo registro do tipo ClassePesquisaSatisfacao | ClassePesquisaSatisfacao Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | ClassePesquisaSatisfacao Carrega(string nomePropriedade, object valorPropriedade); |
