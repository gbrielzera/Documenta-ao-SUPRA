# Autorização de Perfil

Caminho: Janelas > Utilitários > Perfil de acesso > Autorização de Perfil

Autorização para um Perfil de acesso

Na tabela abaixo temos os principais campos deste cadastro:

## Campos do cadastro

| **Transação** | Tela do sistema autorizada para o usuário Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
|---|---|

| **Restrições registros** | Uma 'Restrição de registro' permite filtrar os registros que são exibidos em uma transação de Cadastro. Todas as restrições formam uma única expressão montada com o operador lógico AND, ou seja, são recuperados e disponibilizados para edição os registros que atendam TODAS as restrições de registro. Se o usuário possui vários perfis vale sempre o princípio da restritividade, ou seja, todas as restrições são acumuladas entre todos os perfis atribuídos. Todos os registros desta coleção de dados são mantidos na tabela [DATA_REST](dados_data_rest). |
|---|---|
| **Restrições campos** | Uma 'Restrição de campo' permite ocultar ou desabilitar um campo de uma tela de listagem ou edição de registros (Cadastros). IMPORTANTE: Uma ação do tipo Ocultar prevalece sobre uma do tipo Desabilitar. Se o usuário possui vários perfis então vale o princípio da restritividade, ou seja, são aplicadas todas as restrições acumuladas entre os diversos perfis atribuídos. Todos os registros desta coleção de dados são mantidos na tabela [FIELD_REST](dados_field_rest). |
