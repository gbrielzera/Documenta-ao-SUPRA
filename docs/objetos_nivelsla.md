# NivelSLA

Caminho: Customização > Modelo de objetos > Processo > NivelSLA

Nível de ANS define faixas de tempo para escalonamento de ANS em um Método de Priorização (por exemplo Incidentes).

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CorIndicadorGrafico** | Cor associada ao nível de ANS. Na tela da de Fila de Ordens de Serviço é exibido um ícone nesta cor indicando o Nível atual de ANS. | [CorIndicadorGrafico](enum_corindicadorgrafico) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um NivelSLA | Inteiro |
| **PercentualTempoTotal** | Percentual do tempo total do Acordo de Nível de Serviço | Inteiro |
| **Sequencial** | Sequencial | Inteiro |
| **VisivelPainelWorkspace** | Indica que Ordens de Serviço neste nível serão exibidas no Painel de Alertas da transação Workspace. Esta configuração ainda está condicionada a regra de visualização do Grupo de Trabalho (veja as configurações do Grupo de Trabalho do solucionador). | Booleano |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | NivelSLA Carrega(int i); |
| **Novo** | Cria um novo registro do tipo NivelSLA | NivelSLA Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | NivelSLA Carrega(string nomePropriedade, object valorPropriedade); |
