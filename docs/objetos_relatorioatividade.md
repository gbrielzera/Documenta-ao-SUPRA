# RelatorioAtividade

Caminho: Customização > Modelo de objetos > Processo > RelatorioAtividade

Relatório de apoio utilizado na execução de alguma tarefa de processo ou relatório anexado no envio de emails configurados no processo como eventos intermediários.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AtividadeId** | Identificador da tarefa de processo ou evento intermediário que contém a regra de relatório. | Inteiro |
| **DisponivelAutoatendimento** | Indica que o relatório estará disponível na página de consulta de Ordens de Serviço do sistema de Autoatendimento. O relatório estará acessível por um link que exibirá o conteúdo em outra página web. | Booleano |
| **FormatoExportacao** | Formato do arquivo gerado pelo relatório e que será anexado no email. | [FormatoExportacaoRelatorio](enum_formatoexportacaorelatorio_) |
| **Parametros** | Parâmetros e respectivos valores que serão utilizados no processamento do relatório. | [Lista de ParamRelatorioAtividade](objetos_paramrelatorioatividade_) |
| **UserReport** | Relatório criado pelo usuário utilizando o Editor de Relatórios | [UserReport](objetos_userreport) |
| **UserReportId** | Identificador do relatório de apoio ou utilizado como anexo em evento de mensagem. | Inteiro |
