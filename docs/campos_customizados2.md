# Campos Customizados

Caminho: Guia para Administradores > Configurando Processos > Editor de Processos > Campos Customizados

Neste tópico aprenderemos como criar campos customizados. Além disso, vamos aprender como armazenar novos campos em [Tabelas Customizadas](armazenando_dados_de_campos_cu).

O Supravizio possui um conjunto predefinidos de campos nativos. Alguns destes campos podem ser campos muito simples (campos do tipo texto, data, etc) ou campos com características muito específicas como, por exemplo, o campo **Data/hora entrega serviço** que registra o "fim" do tempo de um [Acordo de Nível de Serviço](acordo_de_nivel_servico), ou seu correspondente inverso o campo Data/hora solicitação, que registra o início da contabilização deste tempo. :

É possível reutilizar um campo nativo apenas redefinindo seu rótulo através da propriedade Rótulo do campo adicionado em um Data Object de Preenchimento de Campo:

Existem casos que estes campos nativos não atenderão a necessidades específicas. Para isso, o Supravizio permite a criação de campos do tipo Customizados. Os campos deste tipo obedecem as mesmas definições de Propriedades Customizadas em cadastros do sistema. Para mais informações sobre a criação de novas Propriedades Customizadas leia [Propriedades Customizadas](campos_customizados).

O Editor de Processos do Supravizio permite que você crie diretamente um novo campo ou mantenha campos existentes em Ordens de Serviço através do comando Campos:

Para criar um novo campo, você pode utilizar o comando Novo neste cadastro...

... ou através de um Data Object de Preenchimento de Campos, selecionando o valor Customizado na propriedade Nome:

Em seguida selecione a opção <Novo> na propriedade Campo Customizado:

Agora preencha os campos necessários para a criação do novo campo:

Para mais informações sobre as propriedades do cadastro de um Campo Customizado leia [Criação de Campos Customizados](criacao_de_campos_customizados).

Caso seja necessário alterar um campo existente, você pode fazer diretamente selecionando o campo na listagem de Campos no Editor de Processos, ou através de um Data Object de Preenchimento de Campos que contenha o campo, através da propriedade **Configuração global do campo**:

Após criado um campo, não é mais possível alterar seu Tipo, Nome, Nome Coluna e Nome Tabela:
