# Modificar o Subprocesso

Caminho: Guia para Administradores > Configurando Processos > Tutoriais > Tutorial 4: Interface entre Processos > Modificar o Subprocesso

Ao término deste tutorial teremos o um fluxo de processo de aquisição de suprimentos com o seguinte fluxo:

Fluxo previsto

Também criaremos um outro fluxo para cadastro de fornecedores:

Novo fluxo para cadastrar fornecedor

### 1. Remova o fluxo que sai da tarefa Realizar Compra

Remoção de link para introduzir uma decisão

### 2. Adicione uma [Decisão Exclusiva por Eventos](decisoes) e uma tarefa denominada Emitir Ordem de Compra conforme a figura abaixo:

Fluxo preliminar

### 3. Na janela Toolbox selecione o elemento [Subprocesso](subprocessos)

### Elemento Subprocesso para inclusão no diagrama

### 4. Clique no diagrama para adicionar a chamada de Subprocesso e depois adicione dois fluxos da seguinte forma:

### Resultado preliminar com inclusão do Subprocesso

Neste ponto precisamos incluir um novo [Tipo de Subprocesso](classesubprocesso_sub) referente a outro fluxo que será invocado. Os próximos passos descrevem esta criação:

### 5. Acesse o cadastro de Tipos de Subprocessos e clique no botão Novo para incluir um novo registro

Cadastro do novo Subprocesso

Salve o registro acima e retorne ao Editor de Processos.

### 6. Na janela Process Explorer do Editor de Processos adicione o Subprocesso anterior utilizando o menu de contexto do item Em edição

Adicionar o subprocesso criado anteriormente

Após clicar em **Adicionar Subprocesso existente** será exibido o diálogo abaixo. Neste diálogo preencha o campo **Tipo de Subprocesso** com o valor **Cadastrar Fornecedor**. Veja a figura abaixo:

Associação do subprocesso de cadastro de fornecedor

Após a inclusão podemos visualizar um diagrama vazio onde iniciaremos a construção do novo fluxo:

Novo fluxo de cadastro de fornecedores

### 7. Na janela Toolbox selecione o elemento Link Inicial

### 8. Clique no diagrama de Cadastro de Fornecedores para incluir o Link Inicial:

Elementos adicionados ao novo subprocesso

### 9. Adicione os fluxos no subprocesso Cadastrar Fornecedor

### Subprocesso com fluxos configurados

### 10. Selecione o Link Incial e na janela de Propriedades faça as seguintes configurações:

Para finalizar a configuração do Link Inicial vamos definir um novo papel denominado Gestor de Cadastro de Fornecedores. Vamos utilizar o próprio campo Responsável no iniciador para criar este papel. Neste campo selecione a opção** <Novo...>**

Criação de um papel a partir da janela de Propriedades

No cadastro exibido em sequência preencha as propriedades Nome e Referência:

Cadastro de Papéis

Feito como na imagem clique em OK, de volta ao cadastro no campo Tipo, selecione a opção "Customização por script":

Na propriedade **Script Seleção Atores** vamos implementar a seleção da pessoa responsável por este papel. Preencha o campo de script com o seguinte conteúdo:

Script para seleção do responsável

Copie o conteúdo abaixo e cole no editor de script:

# a lista Atores acumula as pessoas relacionadas com o papel. O segundo parâmetro serve como documentação

Atores.Adiciona(OrdemServico.ClasseSubProcesso.Responsavel, "Cadastrado como responsável no Tipo de Subprocesso")

Confirme o diálogo e atribua o mesmo papel para todas as atividades do subprocesso de cadastro. Para facilitar esta manutenção selecione todas as Tarefas e o finalizador e edite a propriedade Responsável.

Atribuição de Responsável

Neste ponto foi finalizado o novo fluxo de Cadastro. Então vamos retornar ao Adquirir suprimentos e configurar a chamada para o fluxo de cadastro.

### 11. Retorne ao subprocesso Adquirir Suprimentos e selecione a nova associação:

Configuração da regra de associação entre os fluxos

Após selecionar o item <Nova...> será exibido o seguinte diálogo:

Cadastro de Associação entre os dois novos

### 12. Crie e configure uma [Associação](associacao_sub) entre os dois fluxos:

Configuração do Subprocesso que será invocado

Além da configuração do fluxo que será invocado atribua também o papel Comprador como responsável.

Configuração de papel Responsável

### 13. Selecione a alternativa da decisão de cadastro que atinge o subprocesso Cadastrar Fornecedor e preencha o campo Texto com o valor Não:

### Alternativa para cadastrar fornecedor

### 14. Selecione a alternativa da decisão de cadastro que atinge a tarefa Emitir Ordem de Compra e preencha o campo Texto como o valor Sim:

### Alternativa para fornecedor já cadastrado

### 15. Retorne ao fluxo do processo Cadastro de Fornecedor e, no Link Inicial, selecione a Associação criada:

Na propriedade de Lista "Associações" do Link Inicial, adicione uma nova associação referenciando à criada neste tutorial. A associação aparecerá aqui utilizando a frase inversa:

### Link Inicial de Cadastrar Fornecedor

No dialogo de configuração de associação, clique no botão Adicionar e em seguida selecione a associação "Aquisição que gerou o cadastro". Observe que nesta listagem a Associação é exibida como a frase inversa da associação:

Adicionando uma Associação ao Link Inicial

Obserque que o Link Inicial já exibe o descritivo do subprocesso chamador (fonte):

Link Inicial com Associação

### 16. Valide a nova versão do processo:

### Validação do Processo

### 17. Ative a nova versão do processo:

Ativação do processo
