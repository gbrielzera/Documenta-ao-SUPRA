# RestricaoServico

Caminho: Customização > Modelo de objetos > Processo > RestricaoServico

Restringe a seleção de Serviços para uma determinado Tipo de Subprocesso (tipo de Solicitação). Esta restrição é visível no assistente de abertura de Ordens de Serviço da aplicação de Autoatendimento.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClasseServico** | Tipo de Serviço que está habilitado para o fluxo. Este campo é preenchido automaticamente quando for atribuído o Serviço. Quando for preenchido apenas o campo Tipo de Serviço então são é possível a abertura de Ordens de Serviço para todos os Serviços do tipo especificada. | [ClasseServico](objetos_classeservico) |
| **ClasseServicoId** | Identificador do tipo de Serviço associado | Inteiro |
| **ClasseSubProcessoId** | Identificador do Tipo de Subprocesso | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um RestricaoServico | Inteiro |
| **Servico** | Serviço que pode ser utilizado em Ordens de Serviço deste processo. | [Servico](objetos_servico) |
| **ServicoId** | Identificador do Servico associado | Inteiro |
