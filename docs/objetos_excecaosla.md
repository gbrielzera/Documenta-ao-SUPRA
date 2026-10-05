# ExcecaoSLA

Caminho: Customização > Modelo de objetos > Recurso > ExcecaoSLA

Redefinição do tempo de atendimento para períodos de exceção em um mês ou ano.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **Fim** | Dia de fim se o período for Mês ou mês de fim se o período for Ano. | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um ExcecaoSLA | Inteiro |
| **Inicio** | Dia de início se o período for Mês ou mês de início se o período for Ano. | Inteiro |
| **ItemSLAId** | Número sequencial gerado automaticamente pelo sistema para Identificar um ItemSLA | Inteiro |
| **Periodo** | Tipo de Período de Exceção que pode ser um período compreendido em um Mês (dias de um mês para exceção) ou Ano (meses do ano para exceção). | [PeriodoExcecaoSLA](enum_periodoexcecaosla) |
| **TempoAtendimento** | Tempo de atendimento (em minutos) para Ordens de Serviço enquadradas no critério de período de exceção. | Inteiro |
