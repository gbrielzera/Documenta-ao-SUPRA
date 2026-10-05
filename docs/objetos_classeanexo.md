# ClasseAnexo

Caminho: Customização > Modelo de objetos > Processo > ClasseAnexo

Classe de Item para Anexar

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ConfiguracaoUsuarios** | Ação realizada nos Itens de Configuração na finalização de uma Ordem de Serviço ou atividade de processo. Esta ação não é reversível quando executada a Reabertura de Ordem de Serviço ou cancelamento de atividade via botão Voltar do assistente. | [AcaoConfiguracaoUsuarios](enum_acaoconfiguracaousuarios) |
| **Descricao** | Descrição do Item de Configuração para associação com a ocorrência. Se não for especificado então o sistema assume como descritivo do objeto a listagem de descrições de todos os Tipos e Super Tipos configuradas na listagem 'Escopo de Tipos/Super Tipos'. | String |
| **EscopoClasses** | Tipos e super tipos de Itens de Configuração que podem ter itens associados. Pelo menos um dos Tipos e/ou Super tipos especificados devem ser atendidas para conformidade com Processo. | [Lista de EscopoClasseAnexo](objetos_escopoclasseanexo) |
| **ExibicaoAutomaticaAA** | Lista os itens de configuração automaticamente na tela de procura de itens de configuração no Autoatendimento | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseAnexo | Inteiro |
| **OperacaoAtividadeId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | Inteiro |
| **PermiteMultiplosItens** | Permite inclusão de múltiplos | Booleano |
| **ProduzidoTermino** | O Item de Configuração é gerado ao términdo da Atividade. 'Requerido inicialização' e 'Produzido ao término' são campos mutualmente exclusivos, ou seja, habilitando um o outro é automaticamente desmarcado. | Booleano |
| **RequeridoInicial** | É obrigatória a associação do Item de Configuração para que seja iniciada a atividade. 'Requerido inicialização' e 'Produzido ao término' são campos mutualmente exclusivos, ou seja, habilitando um o outro é automaticamente desmarcado. | Booleano |
| **Restricoes** | Limita o escopo da regra de associação a Ordens de Serviço cujo campo Serviço ou sua Classe esteja relacionados como Escopo | [Lista de RestricaoServicoAnexo](objetos_restricaoservicoanexo) |
| **Sequencial** | Sequencial | Inteiro |
