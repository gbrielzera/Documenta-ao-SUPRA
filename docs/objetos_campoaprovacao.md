# CampoAprovacao

Caminho: Customização > Modelo de objetos > Processo > CampoAprovacao

Campo para Aprovação

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um CampoAprovacao | Inteiro |
| **Nome** | Campo da Ocorrência que deve ser aprovado. | [NomeCampo](enum_nomecampo) |
| **NomeCustomizado** | Nome do campo customizado | String |
| **Obrigatorio** | Indica a obrigatoriedade de preenchimento do campo para Aprovação | Booleano |
| **OperacaoAtividadeId** | Identificação da Operação de Atividade | Inteiro |
| **PermiteModificarAprovado** | Indica que mesmo após a aprovação será possível modificar o conteúdo do campo. | Booleano |
| **Rotulo** | Rótulo para aprovação do Campo. Se não preenchido o sistema exibe descritivo original definido no Dicionário de Classes. | String |
| **Sequencia** | Sequência de apresentação do Campo | Inteiro |
