# Exceção

Caminho: Janelas > Utilitários > Exceção

Uma Exceção representa uma situação de erro verificada e documentada pelo sistema. Neste cadastro um usuário especial do sistema, denominado Administrador, pode customizar mensagens exibidas em situações de erro. Nesta customização é possível a utilização de propriedades na classe de negócio associada (veja o conteúdo da classe no Dicionário de Classes).

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Utilitários | Dicionário de Classes | Exceções**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Identificador** | Identificador da Exceção Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ID_EXCEPTION_CLASS da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
|---|---|
| **Código de Erro** | Código identificador do erro. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CODE da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
| **Classe de Negócio** | Classe de Negócio que implementa objeto de exceção para o erro. Esta classe mantém propriedades que podem ser utilizadas na formação de campos diversos da exceção: Mensagem, Causa, Efeito e Ação. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Mensagem** | Mensagem que é exibida para o usuário na ocorrência do erro. Esta mensagem pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna MESSAGE da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
| **Causa** | Descritivo da Causa do Erro. Este descritivo pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna CAUSE da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
| **Efeito** | Efeito que o Erro possa ter provocado no sistema. O descritivo do efeito pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna EFFECT da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
| **Ação** | Orientação para o Usuário para resolução do problema. O descritivo da ação pode ser formada por um texto simples ou conteúdo dinâmico por uso de propriedades da classe de negócio associada (veja propriedades da classe no Dicionário de Classes) Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ACTION da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |

| **Ação original** | Conteúdo do campo Ação gerado pelo fabricante deste software e disponível para reversão de texto customizado. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_ACTION da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
|---|---|
| **Efeito original** | Conteúdo do campo Efeito gerado pelo fabricante deste software e disponível para reversão de texto customizado. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_EFFECT da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
| **Causa original** | Conteúdo do campo Causa gerado pelo fabricante deste software e disponível para reversão de texto customizado. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_CAUSE da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
| **Mensagem Original** | Conteúdo do campo Mensagem gerado pelo fabricante deste software e disponível para reversão de texto customizado. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ORIGINAL_MESSAGE da tabela [SV_EXCEPTION_CLASS](dados_sv_exception_class). |
