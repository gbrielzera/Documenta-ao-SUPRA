# Unidade Negocio

Caminho: Janelas > Recurso > Unidade Negocio

A Unidade de Negócio define uma localização (site, filial etc) onde estão localizados os Clientes e Ativos. Para uma Unidade de Negócio é possível cadastrar Prédios e respectivos andares, salas e locais.

## Acessando o cadastro

Para acessar este cadastro utilize as opções de menu **Recurso | Unidades de Negócio**. Veja na figura abaixo que será apresentada uma tela contendo diversos registros do cadastro. Para detalhes sobre os comandos disponíveis nesta tela veja [Telas de cadastros](telas_de_cadastros).

Tela iniciado do cadastro

Para editar um registro específico utilize um duplo clique na linha do grid ou clique no botão Visualizar:

Tela de edição do cadastro

## Campos do cadastro

| **Descrição** | Texto que descreve claramente a localização ou finalidade da Unidade de Negócio Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna DESCRICAO da tabela [UNIDADE_NEGOCIO](dados_unidade_negocio). |
|---|---|
| **Sigla** | Nome resumido (código) utilizado para identificar uma Unidade de Negócio Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório - Todos os caracteres preenchidos são convertidos automaticamente para minúsculo - Não é permitida duplicidade de valores Este campo é mantido na coluna SIGLA da tabela [UNIDADE_NEGOCIO](dados_unidade_negocio). |
| **Ativo** | Indica que a Unidade de Negócio está ativa Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna ATIVO da tabela [UNIDADE_NEGOCIO](dados_unidade_negocio). |
| **Localização** | Endereço, Cidade, Estado ou qualquer outra referência de Localização da Unidade de Negócio. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório Este campo é mantido na coluna LOCALIZACAO da tabela [UNIDADE_NEGOCIO](dados_unidade_negocio). |
| **Empresa** | Empresa para a qual a Unidade pertence. Este campo é utilizado como critério de filtro para os locais exibidos na abertura de Ordens de Serviço do Autoatendimento. Se o usuário conectado estiver associado a uma empresa pertencente a um grupo de empresas, então são exibidas todas as unidades do grupo. Se sua empresa não estiver associada a um grupo então são exibidas as unidades da empresa. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |
| **Calendário** | Um Acordo de Nível de Serviço define prazos de atendimento para solicitações de um cliente. Além de prazos o acordo define condições tais como períodos de disponibilidade, possibilidades de suspensão do tempo, cobertura por processos e remuneração por serviços. O Acordo de Nível de Serviço é atribuído automaticamente pelo sistema no instante em que abrimos uma Ordem de Serviço ou modificamos campos chave: Cliente, Itens de Configuração, Prioridades, Subprocessos, Data/hora de solicitação entre outros. A data/hora de solicitação é considerada o marco inicial da contagem de tempo e a data/hora de fim é o marco final. A data/hora de fim pode ser sobrescrita pela data/hora de entrega de serviço, que pode ser preenchida durante a execução da Ordem de Serviço. Utilizando um clique no rótulo do campo podemos acessar o cadastro do registro selecionado no controle. Se o usuário conectado possui acesso ao cadastro deste registro então é possível sua edição. Para este campo existem as seguintes regras: - Este campo possui preenchimento obrigatório |

| **Prédios** | Prédios contidos na Unidade de Negócio Todos os registros desta coleção de dados são mantidos na tabela [PREDIO](dados_predio). |
|---|---|

## Inserindo registros

Para incluir um novo registro neste cadastro clique no botão Novo da tela iniciado do cadastro conforme a figura abaixo:

Comando para cadastrar um novo registro

Após clicar no botão Novo será exibido o diálogo de edição para preenchimento do novo registro. Assim que finalizada a edição clique no botão Salvar para gravar os dados em banco de dados.

Também é possível criar um(a) novo(a) Unidade Negocio a partir de outra existente. Neste caso o novo registro será uma cópia completa do registro original exceto os campos de identificação e descritivo.

Para criar uma cópia de registro existente basta acessar novamente a tela de listagem do cadastro e executar o comando **Copiar registro selecionado** conforme figura abaixo. Repare que para acessar este comando é necessário um clique no ícone contido no botão de novo registro. Na figura abaixo podemos observar o comando para criação cópias de registro:

Comando para cópia de registro

Executando o comando acima é apresentada a tela de edição do registro onde é possível complementar ou modificar os campos do registro. Para concluir a inserção basta clicar em Salvar conforme instruções deste tópico.

## Removendo registros

Para remover um registro acesse a tela inicial, selecione um ou mais registros e clique no botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de listagem

A remoção pode também ser executada na tela de edição do registro utilizando o botão **Apagar** conforme a figura abaixo:

Comando Apagar na tela de edição

Para mais informações sobre remoção de registros em cadastros veja [Remoção de registros em cadastros](remocao_registros_cadastros).
