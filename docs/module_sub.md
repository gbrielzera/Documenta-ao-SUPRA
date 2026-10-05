# Módulo

Caminho: Janelas > Utilitários > Módulo

Um Módulo define um conjunto de funcionalidades pertencentes a uma aplicação. Para cada Módulo existe um item de menu raiz denominado 'Comando raiz' e a partir deste item são associados todos as opções de comandos do módulo.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Utilitários | Segurança | Módulos**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Nome** | Nome sucinto para o Módulo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna NAME da tabela [SV_MODULE](dados_sv_module). |
|---|---|
| **Abreviatura** | Nome resumido (código) que identifica um Módulo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores Este campo é mantido na coluna SHORT_NAME da tabela [SV_MODULE](dados_sv_module). |
| **Descrição resumida** | Descrição resumida para utilização na interface com usuário. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna TEXT da tabela [SV_MODULE](dados_sv_module). |
| **Descrição** | Descrição detalhada do Módulo para documentação do Módulo. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRIPTION da tabela [SV_MODULE](dados_sv_module). |
| **Ativo** | Indica que o Módulo está ativo no sistema. Uma vez inativo o Módulo não pode ser acessado por Usuários. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ENABLED da tabela [SV_MODULE](dados_sv_module). |
| **Descrição resumida original** | Descrição resumida original Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_TEXT da tabela [SV_MODULE](dados_sv_module). |
| **Descrição original** | Descrição original do Módulo Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_DESCRIPTION da tabela [SV_MODULE](dados_sv_module). |
