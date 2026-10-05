# RetornoItens

Caminho: Customização > Modelo de objetos > Processo > RetornoItens

Configura uma regra de retorno de Itens de Configuração para Ordens de Serviço invocadas como Subprocessos ou link final. Quando uma Ordem de Serviço chamada é finalizada então os itens que atenderem a regra serão aidionado a Ordem de Serviço chamadora.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **AtividadeId** | Identificador da Atividade | Inteiro |
| **ClasseConfiguracao** | Tipo Item de Configuração | [ClasseConfiguracao](objetos_classeconfiguracao) |
| **ClasseConfiguracaoId** | Identificador do Tipo de Item de Configuração associado | Inteiro |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar um RetornoItens | Inteiro |
