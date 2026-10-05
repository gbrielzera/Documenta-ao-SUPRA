# Visualização Condicional

Caminho: Guia para Administradores > Roteiro de implantação > Propriedades Customizadas > Visualização Condicional

Para execução desse tutorial é recomendado a leitura de [Criando uma Propriedade Customizada](criando_propriedade_customizada).

Todas as classes envolvidas no sistema estão cadastradas em um cadastro chamado **Dicionário de Classes** (para mais detalhes, acesse o tópico [Classes](class_sub)). Através deste cadastro é possível criar novas propriedades para uma determinada classe.

Neste tópico listamos os passos para editar o cadastro de uma propriedade customizada para adicionar um escopo (Visualização Condicional):

## Adicionando Escopo em Cadastros do Supravizio

### 1. Para modificar uma propriedade customizada acesse Utilitários | Dicionário de Classes | Dicionário de Classes. Localize a classe que o cadastro desejado faz parte. Vamos utilizar em nosso exemplo o cadastro de Pessoas. Utilize o filtro de busca da listagem através do botão Localizar, digitando o termo "pessoa":

Localizando um registro no Dicionário de Classes

### 2. Realize um duplo clique no registro Venki.Supravizio.Recurso.Pessoa e será exibido o cadastro da classe:

Cadastro de Classe

### 3. Selecione a aba Propriedades Customizadas e selecione EMAIL_ADICIONAL:

### Selecionar propriedade customizada

### 4. Selecione a aba Escopo e crie Novo escopo:

### Novo Escopo

### 5. Preencha os campos do novo escopo pelo filtro que deseja utilizar, no caso utilizaremos um filtro por Identificador Área com valor de comparação 4:

### Escopo

### 6. Salve e volte, agora apenas pessoas com a Área que possui o ID 4 podem visualizar o campo. Vamos verificar, entre em Recurso | Áreas:

### Áreas

### 7. Verifique qual Área possui o ID 4.

### Órgão com ID 4

### 8. Verifique agora no cadastro de pessoas em Recursos | Pessoas filtrando por Diretoria Financeira:

### Filtro por diretoria financeira

### 9. Certifique-se de que o campo E-mail Pessoal está disponível:

### Campo E-mail Pessoal

## Adicionando Escopo em campos de Ordens de Serviço

1. Vamos criar outro exemplo para um campo customizado de Ordem de Serviço. Voltando ao dicionário de classe, vamos filtrar dessa vez por Ordem Serviço para encontrar Venki.Supravizio.Processo.OrdemServico, Supravizio, em propriedades customizadas vamos criar um novo campo :

2. Na aba Escopo do nosso novo campo, vamos definir um novo escopo por Identificador Serviço com operador ln, com diversos valores de comparação (possibilitado pelo operador In):

Escopo com diversos valores de comparação

3. Salve as alterações e volte vamos verificar o resultado do escopo. Para saber os serviços que são associados, podemos verificar em Processo | Serviço | Serviços:

### Serviços escolhidos

4. Portanto foram associados os serviços de Telefonia fixa, Software, Servidores e Scanner. Vamos verificar se o novo campo está disponível com um simples processo no Portal e no workspace. Adicione no iniciador do subprocesso desejado uma operação de entrada de dados e adicione nela o campo para preenchimento criado:

### Propriedades do iniciador

5. Repare que a informação "Apenas 'Scanner' + Medidas Necessárias" é apresentada pelo fato de o subprocesso em que está sendo incluído o campo, só possui o Serviço "Scanner" do Escopo:

### Escopo por Scanner

6. Agora fazendo abertura de uma Ordem de serviço pelo Portal, repare que Selecionando o serviço scanner, o campo fica disponível já em outros serviços não:

### Serviço Scanner

### Campo Disponível

### Serviço Banco de Dados

### Campo Indisponível

7. Agora vamos verificar pelo Workspace iniciando duas diferentes Ordens de Serviço, uma com serviço de banco de dados e outra de Scanner:

### Inicio por serviço de Banco de Dados

### Inicio com serviço de Scanner
