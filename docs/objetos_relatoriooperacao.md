# RelatorioOperacao

Caminho: Customização > Modelo de objetos > Processo > RelatorioOperacao

Relatórios envolvidos em aprovações ou utilizados para geração de arquivos anexados na ocorrência.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **FormatoExportacao** | Formato do arquivo que será gerado pelo relatório e anexado na ocorrência. | [FormatoExportacaoRelatorio](enum_formatoexportacaorelatorio) |
| **OperacaoAtividadeId** | Número sequencial gerado automaticamente pelo sistema para Identificar uma OperacaoAtividade | Inteiro |
| **Parametros** | Parâmetros e respectivos valores que serão utilizados no processamento do relatório. | [Lista de ParamRelatorioOperacao](objetos_paramrelatoriooperacao) |
| **RotuloLink** | Texto utilizado no link disponível na página de aprovação da aplicação de Autoatendimento. Ao clicar neste link será exibido em uma nova página o conteúdo do relatório. Se não for preenchido então será utilizado o próprio título do relatório. | String |
| **UserReport** | Relatório que fará parte da solicitação de aprovação. Este relatório estará disponível na tela de aprovação da ocorrência e o aprovador poderá consultar o conteúdo do documento. | [UserReport](objetos_userreport) |
| **UserReportId** | Identificador do relatório que será utilizado na aprovação. | Inteiro |
