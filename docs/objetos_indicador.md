# Indicador

Caminho: Customização > Modelo de objetos > Processo > Indicador

Um Indicador de Desempenho, também conhecido como KPI (Key Performance Indicator), define uma medição realizada sobre a execução de Processos ou base de Ativos. Indicadores representam uma importante ferramenta para monitoramento e gerenciamento dos Serviços.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Agregacao** | Função de agregação utilizada para apuração de Indicador. | [AgregacaoIndicador](enum_agregacaoindicador) |
| **ClassesConfiguracao** | Tipos ou super tipos de Itens de Configuração utilizados como filtro na recuperação de Ativos. Esta relação só faz sentido para Indicadores apurados a partir da base de dados de Itens de Configuração. | [Lista de ClasseConfiguracaoIndicador](objetos_classeconfiguracaoindicador) |
| **ClassesSubProcesso** | Tipos de Subprocesso utilizados como filtro na recuperação de Ocorrências. Esta relação de Tipos de Subprocesso só faz sentido para Indicadores apurados a partir da base de dados de Ocorrências de Processos. | [Lista de ClasseSubProcessoIndicador](objetos_classesubprocessoindicador) |
| **Codigo** | Código de identificação do Indicador | String |
| **Descricao** | Texto que descreve claramente a finalizada de um Indicador de Desempenho. Este texto é utilizado na publicação do Indicador na página Executive Dashboard da tela Workspace. | String |
| **ExpressaoSelecao** | Fórmula para seleção de registros baseados no Provedor do Indicador. Indicadores do tipo Percentual devem obrigatoriamente definir uma fórmula de seleção. | String |
| **ExpressaoValor** | Fórmula para determinar o Valor do Indicador. Se não for preenchido é assumida a Projeção de Contagem de registros que atendam Fórmula de Seleção. A Fórmula de Valor deve ser utilizada em conjunto com a função de Agregação para determinar o valor final de apuração do Indicador. | String |
| **FormulaFiltroComplementar** | Fórmula para filtro complementar | String |
| **FormulaResponsavel** | Fórmula para recuperação responsável por uma Ordem de Serviço ou Pesquisa de Satisfação. | String |
| **GrupoIndicador** | Um Grupo de Indicadores é utilizado para classificar um Indicador de Desempenho. Também permite que Indicadores relacionados sejam agrupados na exibição feita pelo Executive Dashboard. | [GrupoIndicador](objetos_grupoindicador) |
| **GrupoIndicadorId** | Identificador do(a) GrupoIndicador associado(a) | Inteiro |
| **GruposQuestoes** | Grupos de Questões para Filtro durante a Apuração de Pesquisas de Satisfação | [Lista de GrupoQuestaoIndicador](objetos_grupoquestaoindicador) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Indicador. Este número não pode ser modificado pelo usuário. | Inteiro |
| **OrdemServicoFiltroAberta** | Seleciona Ordens de Serviço Abertas no Período de apuração do Indicador | Booleano |
| **OrdemServicoFiltroCancelada** | Seleciona Ordens de Serviço Canceladas no Período de apuração do Indicador | Booleano |
| **OrdemServicoFiltroFinalizadaFalha** | Seleciona Ordens de Serviço Finalizadas como Falha no Período de apuração do Indicador. | Booleano |
| **OrdemServicoFiltroFinalizadaNReal** | Seleciona Ordens de Serviço Finalizadas como Não-realizada no Período de apuração do Indicador. | Booleano |
| **OrdemServicoFiltroFinalizadaSucesso** | Seleciona Ordens de Serviço Finalizadas como Sucesso no Período de apuração do Indicador. Para determinar a finalização no período é utilizada a Data/hora de Execução de Mudança. | Booleano |
| **OrdemServicoProcesso** | Seleciona Ordens de Serviço do Processo | [Processo](objetos_processo) |
| **OrdemServicoProcessoId** | Identificador do Processo associado | Inteiro |
| **PesquisaClassePesquisa** | Tipo de pesquisa de satisfação que será considerada no cálculo do indicador. | [ClassePesquisaSatisfacao](objetos_classepesquisasatisfacao) |
| **PesquisaClassePesquisaId** | Identificador do ClassePesquisaSatisfacao associado | Inteiro |
| **PesquisaFiltroAndamento** | Seleciona Pesquisas de Satisfação não respondidas | Booleano |
| **PesquisaFiltroCancelada** | Seleciona Pesquisas de Satisfação canceladas | Booleano |
| **PesquisaFiltroConcluida** | Seleciona Pesquisas de Satisfação respondidas por Clientes | Booleano |
| **PesquisaTipoApuracao** | Tipo de Apuração para Pesquisas de Satisfação. | [TipoApuracaoPesquisa](enum_tipoapuracaopesquisa) |
| **Provedor** | Banco de dados utilizado para apuração do Indicador. | [ProvedorIndicador](enum_provedorindicador) |
| **ReferenciaCalculo** | Texto explicativo sobre como o Indicador é calculado. | String |
| **SentidoMelhor** | Indica o melhor desempenho para um valor apurado em relação a Meta estipulada para o Indicador. | [SentidoMelhorDesempenho](enum_sentidomelhordesempenho) |

Operações:

| **Nome** | **Descrição** | **Assinatura** |
|---|---|---|
| **Carrega** | Recupera do banco de dados o objeto com o identificador fornecido como parâmetro. | Indicador Carrega(int i); |
| **Novo** | Cria um novo registro do tipo Indicador | Indicador Novo(); |
| **Carrega** | Recupera do banco de dados o objeto com a chave de busca fornecida como parâmetro. | Indicador Carrega(string nomePropriedade, object valorPropriedade); |
