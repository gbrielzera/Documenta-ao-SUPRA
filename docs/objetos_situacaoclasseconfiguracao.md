# SituacaoClasseConfiguracao

Caminho: Customização > Modelo de objetos > Ativos > SituacaoClasseConfiguracao

Configura todos os Estados possíveis para um Item do Tipo de Item de Configuração associada.

Propriedades:

| **Nome** | **Descrição** | **Tipo** |
|---|---|---|
| **ClasseConfiguracaoId** | Número sequencial gerado automaticamente pelo sistema para Identificar um Tipo de Item de Configuração | Inteiro |
| **Desativado** | Indica que itens nesta situação foram descontinuados. No caso de artigos da base de conhecimento este campo é utilizado para incluir o item na recuperação feita pelo mecanismo de busca. | Booleano |
| **DisponibilidadeAA** | Configuração da disponibilidade do 'Tipo de Configuração' na aplicação no Autoatendimento. Alguns 'Tipos de Configuração' são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente. | Booleano |
| **Id** | Número sequencial gerado automaticamente pelo sistema para Identificar uma Situação para Tipos de Itens de Configuração | Inteiro |
| **Inicial** | Indica que a Situação é Inicial. Para uma Classe é possível apenas uma Situação Inicial. | Booleano |
| **Nome** | Descrição que é exibida para o Usuário | String |
