# Criando uma Propriedade Customizada

Caminho: Guia para Administradores > Roteiro de implantação > Propriedades Customizadas > Criando uma Propriedade Customizada

Todas as classes envolvidas no sistema estão cadastradas em um cadastro chamado **Dicionário de Classes** (para mais detalhes, acesse o tópico [Classes](class_sub)). Através deste cadastro, como exemplificamos acima, é possível criar novas propriedades para uma determinada classe.

Neste tópico listamos os passos para criar o cadastro de uma propriedade customizada:

### 1. Para criar uma propriedade customizada acesse Utilitários | Dicionário de Classes | Dicionário de Classes. Localize a classe que o cadastro desejado faz parte. Vamos utilizar em nosso exemplo o cadastro de Pessoas. Utilize o filtro de busca da listagem através do botão Localizar, digitando o termo "pessoa":

Localizando um registro no Dicionário de Classes

### 2. Realize um duplo clique no registro Venki.Supravizio.Recurso.Pessoa e será exibido o cadastro da classe:

Cadastro de Classe

### 3. Selecione a aba Propriedades Customizadas e caso já existam propriedades customizadas, todas serão listadas.

Lista de propriedades customizadas

### 4. Para criar uma nova propriedade, clique em Novo. Logo após será exibida a seguinte tela de cadastro:

Nova propriedade customizada.

Neste exemplo vamos criar então um campo de Email Adicional. No campo **Nome** vamos preencher "EMAIL_ADICIONAL". Vamos incluir no campo **Descrição Resumida** o termo "E-mail Pessoal". No campo **Descrição** incluiremos "E-mail Pessoal". O campo **Tipo** permanece como campo alfanumérico. Selecione o item "TextBox" no campo **Controle**. Preencha o campo Largura com o valor "200". Após isso clique em **Confirmar e Fechar**.

## 5. Após preencher os campos acima, clique em Salvar e Voltar:

Nova propriedade customizada.

**Importante**: Nesta caso, habilitamos a opção **Permitir inclusão em listagens de edição**. Deste modo, a propriedade que estamos criando estará disponível para exibição na tela de listagem de cadastros, que pode ser customizada conforme vimos no tópico [Configurações do Grid de Ordens de Serviço](configuracao_do_grid_de_ordens):

Exibição da propriedade customizada na tela de listagem

## 6. Após isso, clique em Salvar no cadastro da classe Pessoa:

Campo no cadastro
