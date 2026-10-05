# ItemSLA

Caminho: Customização > Modelo de objetos > Recurso > ItemSLA

Conjunto prazos de atendimento de uma Ordem de Serviço com respectivos critérios de aplicação.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AcordoNivelServicoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um AcordoNivelServico | Inteiro |
| **ClasseServico** | Classe de Serviços atendidos pelo Acordo de Nível de Serviço. Quando preenchido o campo Serviço a Classe de Serviço é atribuída automaticamente. Se não for preenchido o campo Serviço então são considerados todos os Serviços da Classe selecionada. | [ClasseServico](objetos_classeservico) |
| **ClasseServicoId** | Identificador do Tipo de Serviço associado | Inteiro |
| **GrauPrioridade** | Grau de Prioridade determinado por um Método de Priorização. | [GrauPrioridade](objetos_grauprioridade) |
| **GrauPrioridadeId** | Identificador do Grau de Prioridade | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ItemSLA | Inteiro |
| **PerfilCliente** | Perfil de Cliente que será atendido pelo Acordo. O Perfil é uma característica do Cliente e configurado no cadastro de Pessoas. | [PerfilCliente](objetos_perfilcliente) |
| **PerfilClienteId** | Identificador do Perfil de cliente | Inteiro |
| **PeriodosExcecao** | Redefinição do tempo de atendimento para períodos de exceção em um mês ou ano. | [Lista de ExcecaoSLA](objetos_excecaosla) |
| **Servico** | Serviço atendido pelo Acordo de Nível de Serviço. | [Servico](objetos_servico) |
| **ServicoId** | Identificador do Servico associado | Inteiro |
| **TempoAtendimento** | Script que define o tempo de atendimento, o resultado da execução do script deve ser um número que representa o número de minutos | String |
