# Montando Queries

Caminho: Guia para Administradores > Editor de Dashboard > Criando Dashboards > Montando Queries

Antes de iniciarmos a criação do Dashboard, é necessário possuirmos uma consulta SQL que será utilizada para a recuperação de dados.

Nesta consulta, pode ser usado o parâmetro **ID_PESSOA**, que irá recuperar o identificador da pessoa conectada. Para isso, basta utilizar o prefixo correspondente ao Banco de Dados utilizado ('**@**' para SQL Server e '**:**' para Oracle). Porém, em alguns casos, quando a publicação do dashboard for realizada de forma externa, não haverá usuário conectado. Nestas situações, o parâmetro retornará** -1**, devendo ser realizado um tratamento.

Os campos retornados estarão disponíveis ao lado esquerdo da tela de Edição de Dashboard:

Campos disponíveis para uso
