# ClasseAprovacao

Caminho: Customização > Modelo de objetos > Processo > ClasseAprovacao

Tipo de Item de Configuração sujeito a aprovação

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **CopiarAnexado** | Copia para a solicitação de aprovação Itens de Configuração que atendam os critérios de Tipo e Super tipo configurados no Data object de aprovação. Este campo não possui ação quando for configurado no Data Object a cópia de todos os Itens de Configuração associados a Ocorrência. | Booleano |
| **Descricao** | Descrição do Item de Configuração para associação com a solicitação de aprovação. Se não for especificado então o sistema assume como descritivo do objeto a listagem de descrições de todos os Tipos e Super tipos configurados na listagem 'Escopo de Tipos/Super tipos' | String |
| **EscopoClasses** | Tipos e Super tipos de Itens de Configuração que podem ter itens associados na solicitação de aprovação. Pelo menos uma dos Tipos e/ou Super tipos especificados devem ser atendidos para conformidade com Processo. | [Lista de EscopoClasseAprovacao](objetos_escopoclasseaprovacao) |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseAprovacao | Inteiro |
| **Obrigatorio** | Obrigatoriedade de preenchimento na execução do Processo | Booleano |
| **OperacaoAtividadeId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | Inteiro |
| **Restricoes** | Restrição de Itens por Serviço ou Tipo de Serviço | [Lista de RestricaoServicoAprovacao](objetos_restricaoservicoaprovacao) |
