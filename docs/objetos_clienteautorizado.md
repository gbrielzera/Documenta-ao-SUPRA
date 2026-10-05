# ClienteAutorizado

Caminho: Customização > Modelo de objetos > Processo > ClienteAutorizado

Papel de processo utilizado para identificar as pessoas autorizadas a gerar solicitações em um determinado Subprocesso. Estas autorizações são verificadas no instante em que abrimos uma solicitação no Workspace e também no Autoatendimento. Neste último caso o iniciador associado não é exibido para o usuário conectado caso este não atenda ao mecanismo de restrição.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AtividadeId** | Identificador da Atividade de processo que contém a regra de autorização descrita pelo objeto. | Inteiro |
| **PapelAutorizado** | Papel de processo que define uma pessoa ou grupo de pessoas que estão autorizados a iniciar uma solicitação do Subprocesso em questão | [PapelProcesso](objetos_papelprocesso) |
| **PapelProcessoId** | Identificador do Papel de processo autorizado a iniciar uma solicitação | Inteiro |
