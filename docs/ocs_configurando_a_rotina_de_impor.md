# Configurando a rotina de importação

Caminho: Guia para Administradores > Inventário de Hardware e Software > Configurando a rotina de importação

Após realizar a [configuração](ocs_prerequisitos_e_configuracoes) de todo o ambiente que compõe a solução OCS e do conector MySQL ODBC vamos configurar o Supravizio para obter os dados das descobertas através da rotina "Importação de Hardware e Software":

O Supravizio permite a configuração de uma ou mais rotinas de importação, possibilitando realizar importações específicas em intervalos de tempos variados e em contextos diferenciados. Inicialmente vamos criar uma rotina que realiza toda a importação a cada 6 horas. Para isso, na listagem do cadastro clique em Novo. Será exibida uma janela com os seguintes parâmetros:

Para cada tipo de ativo e componente temos de cadastrar um Tipo de Item de Configuração. Para realizar este cadastro leia [Tipo Item Configuração](classeconfiguracao_sub). Vamos precisar dos seguintes tipos:

| **Tipo de Item de Configuração** | **Super tipo** | **Campo correspondente** |
|---|---|---|
| Licença de Software | Software | Tipo de Item de Configuração utilizado para cadastrar um novo Software |
| Estação de Trabalho | Equipamento | Tipo de Item de Configuração utilizado para cadastrar um novo Hardware |
| Memória | Equipamento | Tipo de Item de Configuração para componentes do tipo Memória |
| Processador | Equipamento | Tipo de Item de Configuração para componentes do tipo Processador |
| Monitor | Equipamento | Tipo de Item de Configuração para componentes do tipo Monitor |
| Impressora | Equipamento | Tipo de Item de Configuração para componentes do tipo Impressora |
| Placa de vídeo | Equipamento | Tipo de Item de Configuração para componentes do tipo Placa de vídeo |
| Placa de som | Equipamento | Tipo de Item de Configuração para componentes do tipo Placa som |
| Placa de rede | Equipamento | Tipo de Item de Configuração para componentes do tipo Placa de rede |
| Placa controladora | Equipamento | Tipo de Item de Configuração para componentes do tipo Placa controladora |

Após cadastrar os Tipos de Itens de Configuração necessários, vamos agora preencher este cadastro. Preencha os campos conforme a tabela acima utilizada para a criação de cada tipo. No campo "Conexão do banco de dados do inventário" vamos utilizar a conexão que criamos no tópico "Pré-requisitos e Configurações":

Observe que temos no cadastro um campo chamado "Quantidade máxima de dias sem conexão do agente" este campo permite pré-definir um limite de dias para que a estação de trabalho atualize seus dados. Caso exceda este período, automaticamente. Vamos utilizar um prazo de 60 dias para este exemplo.

Para definirmos a periodicidade da execução desta rotina, clique na aba Opções preenchendo o campo "Executar novamente após

### Filtrando Registros do OCS

É possível também realizar um filtro excluindo ou incluindo registros importados. Podemos citar como exemplo, fazer com que hotfix de sistema operação não sejam importados. para isso, clique na aba "Filtro" da aba Principal:

Temos aqui a possibilidade de filtrar tanto softwares quanto equipamentos. Para filtrarmos softwares, basta adicionarmos no campo "Padrão de nomes de softwares que serão ignorados" palavras-chave ou trechos dos nomes, por exemplo, para hotfixes é comum o uso do termo "KB". É necessário consultar diretamente a base de dados do OCS para avaliar os registros que deverão ser excluídos no filtro:

Observe no exemplo acima que seriam importados muitos registros de hotfixes. Vamos usar o seguinte filtro para eliminarmos os hotfixes usando um comando "like":

Após isso, basta copiar o termo entre '% e %' e colá-lo no campo mencionado. Podem ser adicionados quantos forem necessário.

Para filtro de hardwares, utilizamos um sql que será incluído no filtro. Para este filtro podem ser utilizadas todas as colunas da tabela HARDWARE no banco de dados do OCS. Veja por exemplo, que no cadastro de hardwares abaixo encontramos 2 domínios (Dominio1 e Dominio2):

Queremos então que a rotina de importação colete apenas os hardwares do domínio Dominio1. Podemos filtrar os registros usando um comando select no browser de banco de dados para teste:

Feito o teste, basta copiar os termos após a cláusula "where" e colá-lo no campo "Cláusula SQL incluída no comando utilizado para recuperar computadores da tabela Hardware do banco de dados do inventário" e em seguida clique no comando "Testar Filtro":

**Importante:** pelo fato da Importação de Hardware e Software ser reversível, ou seja, uma vez importado a rotina não elimina um registro, recomenda-se realizar todos os filtros necessários para garantir a integridade dos dados. Caso seja importado algum registro indesejado este poderá ser filtrado e excluído manualmente.
