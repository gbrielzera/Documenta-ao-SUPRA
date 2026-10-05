# Tecnico

Caminho: Customização > Modelo de objetos > Recurso > Tecnico

Um Solucionador é uma Pessoa que trabalha no atendimento de solicitações de Serviço. Este solucionador deve estar lotado em somente um Grupo de Trabalho e pode exercer função de coordenação.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AlertaSolucionadoresGrupo** | Indica que Solucionadores do Grupo receberão alertas quando uma nova Ordem de Serviço for encaminhada para a fila. | Booleano |
| **Ativo** | Indica que o Solucionador está Ativo no Grupo de Trabalho. Em um dado momento o Solucionador pode estar Ativo em somente um Grupo de Trabalho. Ele também não pode ser ativado em um Grupo de Trabalho desativado. | Booleano |
| **Calendario** | Calendário de disponibilidade do recurso. Se não for preenchido então é adotado o calendário da unidade onde está localizada a pessoa. Se a pessoa não possuir associação de Local então entende-se que o recurso terá disponibilidade total (24x7) nos cálculos de Acordo de Nível Operacional. | [Calendario](objetos_calendario) |
| **CalendarioId** | Identificador do Calendário do recurso | Inteiro |
| **DataHoraAssociacao** | Data e hora em que a Pessoa foi associada ao Grupo de Trabalho | Data/hora |
| **DataHoraDesativacao** | Data e hora em que o Solucionador teve sua associação com o Grupo de Trabalho desativadda | Data/hora |
| **GrupoTrabalhoId** | Identificador do Grupo de Trabalho | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tecnico | Inteiro |
| **Pessoa** | Pessoa que está lotada no Grupo de Trabalho | [Pessoa](objetos_pessoa) |
| **PessoaId** | Identificador da Pessoa associado | Inteiro |
