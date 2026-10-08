# TipoApontamentoContrato

Caminho: TipoApontamentoContrato

Tipo de apontamento em um contrato.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ContratoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato | Inteiro |
| **RestricaoHorarioApontamento** | Restrições de horários | [Lista de RestricaoHorarioApontamento](objetos_restricaohorarioapontamento) |
| **TipoApontamento** | Um Tipo de Apontamento pode ser utilizado no cadastro de Contratos para definir um fator aplicado a um valor/recurso também registrado no contrato. | [TipoApontamento](objetos_tipoapontamento) |
| **TipoApontamentoId** | Identificador do TipoApontamento associado | Inteiro |
| **Variacao** | Variação percentual em relação a valor contratado (de 0% a 100%) que é aplicado no relatório de apropriações. | Decimal |
