# Aprovacao

Caminho: Customização > Modelo de objetos > Processo > Aprovacao

Registro de Aprovação por Aprovador

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Aprovador** | Pessoa encarregada de realizar a aprovação. Se esta pessoa possui um substituto então esta segunda pessoa pode também realizar esta aprovação sendo persistido no campo AprovadorReal quem efetivamente realizou a operação. | [Pessoa](objetos_pessoa) |
| **AprovadorReal** | Na ausência do Aprovador o Aprovador Real pode realizar a Aprovação. Sendo o próprio Aprovador, armazena a mesma informação | [Pessoa](objetos_pessoa) |
| **AprovadorRealId** | Identificador da Pessoa que realizou a Aprovação | Inteiro |
| **AssuntoAprovacaoId** | Assunto para Aprovação associado | Inteiro |
| **DataHoraEvidencia** | Data e hora em que foi realizado o último evento. | Data/hora |
| **DescricaoPapelAprovador** | Descrição do Papel que o Aprovador possui no Processo. | String |
| **ExplicacaoAprovador** | Texto explicativo sobre o aprovador. | String |
| **Motivo** | Motivo ou Comentário feito pelo Cliente durante a realização da Aprovação, Reprovação ou Cancelamento (estados terminais para o processo). | String |
| **Passo** | Passo do aprovador em aprovações por hierarquia | Inteiro |
| **PessoaId** | Identificador da Pessoa responsável pela Aprovação | Inteiro |
| **Situacao** | Situação para a Versão a ser Aprovada. | [SituacaoAprovacao](enum_situacaoaprovacao) |
| **UtilizouPreAprovacao** | Foi utilizado algum critério de pré-aprovação | Booleano |
| **Versao** | Sequencial gerado automaticamente pelo sistema para cada Assunto de uma determinada Ordem de Serviço | Inteiro |
