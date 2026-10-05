# ItemOcorrencia

Caminho: Customização > Modelo de objetos > Processo > ItemOcorrencia

Item de Configuração associado a uma ocorrência de processo.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClasseAnexo** | Configuração de processo que gerou a associação de Item de Configuração | [ClasseAnexo](objetos_classeanexo) |
| **ClasseAnexoId** | Identificador da configuração de associação de Item de Configuração que gerou a associação. | Inteiro |
| **DataHoraAnexado** | Data e hora em que o Item foi anexado | Data/hora |
| **Explicacao** | Texto explicativo sobre a associação do item na Ocorrência. Pode ser utilizado para depuração de uma ocorrência de processo. | String |
| **ItemConfiguracao** | Item de Configuração anexado a instância de Processo. | [ItemConfiguracao](objetos_itemconfiguracao) |
| **ItemConfiguracaoId** | Identificador do ItemConfiguracao associado | Inteiro |
| **OcorrenciaId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência | Inteiro |
| **UserReport** | Relatório utilizado para geração do arquivo anexado. | [UserReport](objetos_userreport) |
| **UserReportId** | Identificador do relatório que foi utilizado para gerar o arquivo | Inteiro |
