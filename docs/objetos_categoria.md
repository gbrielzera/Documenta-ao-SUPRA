# Categoria

Caminho: Customização > Modelo de objetos > Processo > Categoria

Classificação manual atribuída a Ordens de Serviço associadas com uma cor e com possibilidade de exibição na barra de rolagem de Ordens de Serviço. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Ativo** | Indica que a Categoria está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema. | Booleano |
| **Azul** | Fator azul para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. | Inteiro |
| **Descricao** | Descrição detalhada da Categoria | String |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Categoria | Inteiro |
| **Verde** | Fator verde para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. | Inteiro |
| **Vermelho** | Fator vermelho para formação da cor da categoria. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática. | Inteiro |
| **VisivelPainelWorkspace** | Indica que Ordens de Serviço desta categoria serão visíveis na barra de rolagem localizada na parte inferior da tela Workspace (Painel de Alertas). Esta configuração ainda está condicionada a regra de visualização do Grupo de Trabalho (veja as configurações do Grupo de Trabalho do solucionador). | Booleano |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Categoria Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Categoria | Categoria Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Categoria Carrega(string nomePropriedade, object valorPropriedade); |
