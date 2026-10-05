# Cadastrando uma rotina de Importação

Caminho: Guia para Administradores > Roteiro de implantação > Importando Dados > Rotina de Importação de Dados de Recursos Humanos > Cadastrando uma rotina de Importação

Para inserir um novo registro basta clicar em **Novo. **Em seguida é exibida uma nova tela onde é possível preencher os campos de Importação de RH. Veja a figura abaixo:

Tela de parâmetros

**Preenchimento de Parâmetros:**

| **Fonte de Dados de Pessoas** | Fonte de dados para consulta em banco de dados relativo a Pessoas. O usuário poderá indicar a tabela ou view de banco de dados com os dados para importação de Pessoas (Clientes) e suas entidades associadas (Fornecedor, Unidade de Negócio, Prédio, Local). |
|---|---|
| **Fonte de Dados de Órgãos** | Fonte de dados para consulta em banco de dados relativo a Órgãos. O usuário poderá indicar a tabela ou view de banco de dados com os dados para importação de Áreas (ou Órgãos) e sua empresa associada. |
| **Fonte de Dados de Calendário** | Fonte de dados para consulta em banco de dados relativo a Calendário. o usuário poderá indicar a tabela ou view de banco de dados com os dados para importação de Calendários e os Feriados de cada Calendário. |
| **Desativa Pessoas ausentes na Fonte de Dados de Pessoas** | Realiza a desativação de uma Pessoa no cadastro de Pessoas do Supravizio caso o registro relacionado a esta Pessoa não exista na Fonte de Dados de Pessoas (definido a critério do cliente). |
| **Desativa Órgãos ausentes na Fonte de Dados de Órgãos** | Realiza a mesma operação definida para Pessoas, porém relacionando Órgãos no cadastro de Órgãos do Supravizio que não estejam na Fonte de Dados de Órgãos. |
| **Capitalizar nomes e cargos de pessoas** | Se esta opção for marcada todos os nomes de pessoas e respectivos cargos serão formatados com a primeira letra em maiúsculo e demais letras minúsculas. Exemplo: se a view possui o nome do funcionário como MARIA SILVA então a pessoa será cadastrada como Maria Silva. |
| **Capitalizar descritivo de Órgãos** | Se esta opção for marcada então todos os descritivos de órgãos serão formatados com a primeira letra em maiúsculo e demais letras minúsculas. |
| **Não limpar campo Telefone quando o valor do mesmo não estiver presente na fonte de dados** | Caso a opção esteja marcada e o campo retornado pela view não possui conteúdo, então o sistema preserva o conteúdo existente no cadastro da pessoa. O campo de Telefone do Portal esta diretamente relacionado com esse parâmetro, pois se a view utilizada para importação recuperar o preenchimento do campo no Portal quando o campo não for preenchido, o telefone da pessoa não será alterado porém, se for preenchido o telefone da pessoa será atualizado no cadastro de pessoas. |

Para cadastrar uma nova rotina de Importação de RH é necessário preencher os campos acima e é importante agendar as execuções com datas e horários, e registrar os endereços de e-mails para envio das notificações, na aba **Opções:**

Após realizar o agendamento e preencher os endereços de e-mail, clique em **OK **e será listado uma nova rotina de Importação de RH.
