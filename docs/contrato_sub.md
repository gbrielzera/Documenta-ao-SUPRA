# Contrato

Caminho: Janelas > Recurso > Contrato

Um Contrato relaciona recursos (pessoas), Itens de configuração e regras para apontamento de horas trabalhadas. Além destas informações o contrato possui uma vigência, um fornecedor e um contratante. Um contrato pode ser informado em uma Ordem de Serviço por meio de um campo nativo denominado Contrato. Este campo é editado em um controle do tipo DropDownList contendo os contratos vigentes do Cliente da Ordem de Serviço. O Contrato é visível para seu gestor na aplicação de Autoatendimento, onde é possível acompanhar os apontamentos associados.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Recurso | Contratos**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Descrição detalhada do Contrato Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [CONTRATO](dados_contrato). |
|---|---|
| **Data início validade** | Data início de Validade do Contrato Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_INICIO_VALIDADE da tabela [CONTRATO](dados_contrato). |
| **Data fim validade** | Data de fim de Validade do Contrato Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DATA_FIM_VALIDADE da tabela [CONTRATO](dados_contrato). |
| **Empresa Contratante** | Empresa Contratante Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Fornecedor** | Um Fornecedor é uma tipo especial de Empresa habilitada como prestador de serviços para a área. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Código referência** | Código do contrato gerado pela área de suprimentos. |
| **Responsável Contrato** | Pessoa que é responsável pela manutenção de dados do Contrato. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Responsável Fornecedor** | Nome da pessoa responsável pelo Contrato pelo Fornecedor contratado. |
| **Meio contato Fornecedor** | Telefone ou email de contato com Responsável pelo Contrato pelo Fornecedor. |
| **Plano de Gestão** | Indicadores de Desempenho para Gestão do Contrato Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. |
| **Forma de Apontamento** | Forma de definição de apontamentos, se por total de horas ou por período Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna FORMA_APONTAMENTO da tabela [CONTRATO](dados_contrato). |
| **Publicar vigência no Autoatendimento** | Publicar a vigência do contrato (data de início e fim de validade) na página de contratos do Autoatendimento Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna PUBLICA_VIGENCIA_AA da tabela [CONTRATO](dados_contrato). |

| **Recursos Aplicados** | Grupos de solucionadores previstos na prestação de Serviço. Todos os registros desta coleção de dados são mantidos na tabela [RECURSO_APLICADO](dados_recurso_aplicado). |
|---|---|

| **Apontamentos** | Tipos de Apontamentos previstos no Contrato Todos os registros desta coleção de dados são mantidos na tabela [TIPO_APONT_CONT](dados_tipo_apont_cont). |
|---|---|

| **Itens de Configuração** | Itens de Configuração mantidos pelo Contrato Todos os registros desta coleção de dados são mantidos na tabela [CONTRATO_ITEM](dados_contrato_item). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Contrato a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).
