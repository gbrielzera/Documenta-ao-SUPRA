# Configurando uma assinatura padrão

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Comunicados em Ordens de Serviço > Configurando uma assinatura padrão

Através do Supravizio é possível configurar uma assinatura padrão para e-mails dos solucionadores. Para configurar esta assinatura acesse no menu do Supravizio **Utilitários | Configurações **e na árvore selecione **Processo | Geral**.

Observe que será exibido um campo de edição de texto **Assinatura** em comunicados:

.

Assinatura de comunicados

É possível através deste campo, incluir o preenchimento dinâmico de algumas propriedades do cadastro de Pessoa do solucionador.

Repare no exemplo da imagem acima que na primeira linha, temos um conteúdo** [$Nome]**. No instante que é exibida a aba de [Comunicados da tela de Edição de Ordem de Serviço](editar_ordemservico), é preenchido automaticamente o nome do solucionador. É possível incluir outras propriedades como: E-mail, Área, Telefone, Cargo, etc.

Para visualizar as propriedades que você poderá obter dinamicamente para o preenchimento através do cadastro da classe Venki.Supravizio.Recurso.Pessoa. Para acessá-lo, no menu principal, selecione **Utilitários | Dicionário de Classes | Dicionário de Classes**. Após isso, localize o registro clicando em **Localizar** e digitar Venki.Supravizio.Recurso.Pessoa. Será listado o registro com nome Venki.Supravizio.Recurso.Pessoa. Dê um duplo clique e será exibida a tela de cadastro do registro.

Selecione a aba **Propriedades**. Veja que são exibidas as propriedades desta classe e estas poderão ser utilizadas para criação de uma assinatura de comunicado com conteúdo dinâmico:

Propriedades

Vamos então modificar a configuração da assinatura de comunicados incluindo a propriedade Órgão:

Assinatura de comunicados

Após modificar o campo **Assinatura em comunicados**, clique em **Salvar**.

Abrindo novamente a tela de [Edição de Ordem de Serviço, clicando na aba Comunicados](editar_ordemservico), repare que assinatura agora obedece a formatação estabelecida na configuração:

Aba de comunicados

**Importante**: é importante certificar-se que as informações que deseja exibir na assinatura estejam devidamente cadastradas. Se por exemplo faltar a informação, como no nosso exemplo, do Telefone do solucionador, não será exibida nenhuma informação:

Aba de comunicados
