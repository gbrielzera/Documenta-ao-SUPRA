# CampoPreenchimentoAprovacao

Caminho: Customização > Modelo de objetos > Processo > CampoPreenchimentoAprovacao

Campo para Preenchimento em Aprovação

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um CampoPreenchimentoAprovacao | Inteiro |
| **Nome** | Campo da Ocorrência que deve ser preenchido em aprovado. São permitidos apenas campos com controles do tipo TextBox, Memo e DropDownList. | [NomeCampo](enum_nomecampo) |
| **NomeCustomizado** | Nome do campo customizado para preenchimento. São permitidos apenas campos com controles do tipo TextBox, Memo e DropDownList. | String |
| **Obrigatoriedade** | Indica a obrigatoriedade de preenchimento do campo para Aprovação | [ObrigatoriedadePreenchimentoAprovacao](enum_obrigatoriedadepreenchimentoaprovacao) |
| **OperacaoAtividadeId** | Identificador da OperacaoAtividade associada | Inteiro |
| **PermiteModificarAprovado** | Indica que mesmo após a aprovação será possível modificar o conteúdo do campo. | Booleano |
| **Rotulo** | Rótulo para aprovação do Campo. Se não preenchido o sistema exibe descritivo original definido no Dicionário de Classes. | String |
| **Sequencia** | Sequência de apresentação do Campo | Inteiro |
