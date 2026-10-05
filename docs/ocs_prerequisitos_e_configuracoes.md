# Pré-requisitos e configurações

Caminho: Guia para Administradores > Inventário de Hardware e Software > Pré-requisitos e configurações

### Pré-requisitos

O OCS possui em seu pacote de instalação os pré-requisitos de software necessários para seu funcionamento contendo o os servidores e módulos Apache, MySQL, PHP e PERL e versões de agentes para sistemas operacionais diversos.

Para realizar o download dos pacotes de instalação acesse: [http://www.ocsinventory-ng.org/en/download/download-server.html](http://www.ocsinventory-ng.org/en/download/download-server.html)

Para a instalação do servidor OCS faça o download do OCSInventoryNG Server.

Para a instalação dos agentes que serão instalados nas estações de trabalho ou notebooks, faça o download do OCSInventoryNG Agent apropriado para cada sistema operacional.

### Conector ODBC MySQL

A integração entre o Supravizio e o OCS se dá através de conexão direta ao banco de dados do OCS. OCS, como dito anteriormente, utiliza o SGBD MySQL server. Geralmente a base de dados do OCS chama-se "ocsweb". O Supravizio dá ao usuário a possibilidade de criar conexões nativas com os SGBD's Sql Server e Oracle e conexões via ODBC e OleDB através do cadastro de Conexões de bancos de dados (Utilitários | Conexões de banco de dados). Para conexões com bancos de dados MySQL utilizaremos uma conexão usando um driver ODBC para MySQL.

No site [www.mysql.com](http://www.mysql.com) você encontrará diversos instaladores para os principais sistemas operacionais e arquiteturas. Faça o download do "MySQL Conector/ODBC" através do link: [http://www.mysql.com/downloads/connector/odbc/](http://www.mysql.com/downloads/connector/odbc/)

**Importante:** efetue o download da versão de arquitetura compatível com a instalação do Supravizio em seu servidor.

Após realizar a instalação do OCSInventoryNG Server e do conector MySQL ODBC acesse o cadastro de fontes de dados ODBC em Iniciar | Painel de Controle | Ferramentas Administrativas | Fontes de Dados (ODBC) e clique em Adicionar:

Selecione o conector MySQL ODBC:

Preencha os parâmetros para a conexão selecionando banco de dados "ocs"

Após preencher os dados de conexão clique em "Test". A mensagem esperada deve ser esta:

Configurando a Conexão com o banco de dados no Supravizio

Após instalar o OCS Inventory NG Server, instalar o conector MySQL e configurar a fonte de dados ODBC para o banco de dados do OCS, vamos agora cadastrar no Supravizio a conexão que será utilizada pela rotina de importação. Para isso, no menu principal acesse Utilitários | Conexões de banco de dados. Na tela de listagem clique em Novo. Preencha o cadastro conforme os campos abaixo. No campo String de conexão, clique no comando "Editar" preenchendo a string de conexão adequada, clicando em OK e em seguida clicando em Salvar:

String de conexão utilizada neste exemplo: **driver={mysql odbc 5.1 driver};server=localhost;database=ocsweb;user=root;password=venki;option=3;**

Caso tenha dúvidas quanto ao preenchimento de strings de conexão MySQL para ODBC consulte o site: [www.connectionstrings.com](http://www.connectionstrings.com)

Para testar a conexão basta clicar no comando "Testar" e a mensagem esperada deverá ser:

Feitas estas configurações agora é possível [criar rotinas de importação de hardwares e softwares](ocs_configurando_a_rotina_de_impor).
