# CampoPreenchimento

Caminho: Customização > Modelo de objetos > Processo > CampoPreenchimento

Campo para Preenchimento durante a execução do Processo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ConfiguracaoControle** | Informações sobre a configuração de controles utilizados para edição do campo | String |
| **ExibeAutoAtendimento** | Permite exibir ou não o campo nas consultas da respectiva Ordem de Serviço no Autoatendimento | Booleano |
| **ExibeIncluirClienteAA** | Permite exibir ou não o comando para incluir o Cliente em preenchimento de campo (lista) Favorecido no Autoatendimento | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um CampoPreenchimento | Inteiro |
| **IncluirClienteAA** | Caso o campo seja Favorecido automaticamente inclui o Cliente da OS na listagem de pessoas. | Booleano |
| **Nome** | Nome do Campo para preenchimento | [NomeCampo](enum_nomecampo) |
| **NomeCustomizado** | Nome do campo customizado | String |
| **Obrigatorio** | Indica que o preenchimento é obrigatório ou opcional. | Booleano |
| **OperacaoAtividadeId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | Inteiro |
| **Rotulo** | Rótulo para edição do Campo. Se não preenchido o sistema exibe descritivo original definido no Dicionário de Classes. | String |
| **Sequencia** | Sequencia de apresentação do Campo | Inteiro |
