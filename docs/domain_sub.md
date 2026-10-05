# Domínio

Caminho: Janelas > Utilitários > Domínio

Um Domínio define um namespace de banco de dados. Quando um Usuário realiza uma conexão ele seleciona o Domínio no qual deseja acessar e a partir deste momento os dados apresentados são automaticamente filtrados para o "mundo" definido pelo Domínio. Também dentro de um Domínio é possível a existência de customizações (campos e regras em eventos) próprias

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Utilitários | Domínios**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Identificador do Domínio Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_DOMAIN da tabela [SV_DOMAIN](dados_sv_domain). |
|---|---|
| **Nome** | Nome do Domínio Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna NAME da tabela [SV_DOMAIN](dados_sv_domain). |
| **Nome abreviado** | Nome abreviado (código) que identifica um Domínio. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Não é permitida duplicidade de valores - O Nome Abreviado deve conter somente letras maiúsculas Este campo é mantido na coluna SHORT_NAME da tabela [SV_DOMAIN](dados_sv_domain). |
| **Ativo** | Indica que o Domínio está ativo. Quando desabilitado não é possível ao usuário a operação de Login. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ENABLED da tabela [SV_DOMAIN](dados_sv_domain). |
