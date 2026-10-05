# RecursoAplicado

Caminho: Customização > Modelo de objetos > Recurso > RecursoAplicado

Recurso a ser Aplicado no cumprimento do Contrato

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ContratoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | Inteiro |
| **DescricaoRecurso** | Descrição completa do Recurso. Utilze descritivos de Função, Cargo ou Nome da Pessoa de forma a facilitar a referência na associação com Grupos de Trabalho. | String |
| **GruposSolucionadores** | Grupos de trabalho onde estão lotados os Solucionadores correspondentes ao tipo de recurso do contrato. | [Lista de ContratoTecnico](objetos_contratotecnico) |
| **Id** | Identificador do Recurso Aplicado | Inteiro |
| **QuantidadeHoras** | Quantidade de horas contratadas por mês. | Inteiro |
| **UtilizaAcumuladosPrimeiramente** | Utiliza créditos/débitos de saldos anteriores antes de utilizar o saldo de horas disponíveis para o mês. | Booleano |
| **ValidadeSaldo** | Quantidade de meses para validade das horas que não forem utilizadas no mês apurado. Se não for preenchido ou for preenchido com o valor 0 significará que as horas devem ser consumidas no mesmo mês. Se for uma quantidade de meses igual ou superior ao restante de meses do contrato significará que as horas formarão um banco. | Inteiro |
| **ValorHora** | Valor hora padrão para o recurso. O valor final pode variar em função do fator atribuiído ao tipo de apontamento realizado. | Decimal |
| **ValorMensal** | Valor mensal | Decimal |
