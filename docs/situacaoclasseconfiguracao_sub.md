# Situação Tipo Item

Caminho: Janelas > Ativos > Tipo Item Configuração > Situação Tipo Item

Configura todos os Estados possíveis para um Item do Tipo de Item de Configuração associada.

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Nome** | Descrição que é exibida para o Usuário Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna NOME da tabela [SITUACAO_CLASSE](dados_situacao_classe). |
|---|---|
| **Inicial** | Indica que a Situação é Inicial. Para uma Classe é possível apenas uma Situação Inicial. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna INICIAL da tabela [SITUACAO_CLASSE](dados_situacao_classe). |
| **Visibilidade no Autoatendimento** | Configuração da disponibilidade do 'Tipo de Configuração' na aplicação no Autoatendimento. Alguns 'Tipos de Configuração' são utilizados internamente pela área de Tecnologia da Informação e por isto nunca serão visíveis para o Cliente. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DISP_AA da tabela [SITUACAO_CLASSE](dados_situacao_classe). |
| **Desativado** | Indica que itens nesta situação foram descontinuados. No caso de artigos da base de conhecimento este campo é utilizado para incluir o item na recuperação feita pelo mecanismo de busca. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESATIVADO da tabela [SITUACAO_CLASSE](dados_situacao_classe). |
