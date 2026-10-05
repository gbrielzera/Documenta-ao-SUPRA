# Criando um Dashboard com Mapa

Caminho: Guia para Administradores > Editor de Dashboard > Criando Dashboards > Criando um Dashboard com Mapa

Neste tópico vamos criar um mapa que representará a distribuição de pessoas por sua localização através do cadastro de Unidades de Negócio.

Inicialmente, é necessário criarmos dois campos no cadastro de Unidades de Negócio. Estes campos serão campos decimais que armazenarão a Latitude e Longitude do endereço da Unidade de Negócio. Para isso, acesse no menu principal Utilitários | Dicionário de Classes | Dicionário de Classes. Digite "unidade de negócio" no campo de busca e em seguida digite Enter. Ao exibir a listagem filtrada, dê um duplo clique no cadastro abaixo:

Ao exibir o cadastro, clique na aba Propriedades Customizadas e em seguida clique em Novo:

Preencha o cadastro do campo LATITUDE conforme cadastro abaixo:

Após preenchido o cadastro clique em Confirmar e Fechar. Vamos agora criar o campo LONGITUDE basicamente com as mesmas definições do campo LATITUDE. Para isso, ainda na listagem de Propriedades Customizadas do cadastro da classe Unidade de Negócio, mantenha o registro da propriedade LATITUDE selecionado e em seguida clique no comando indicado:

Altere os dados conforme cadastro abaixo, em seguida clique em Confirmar e Fechar:

Após criadas as duas propriedades (campos), clique no comando Salvar do cadastro da classe Unidade de Negócio.

Feito isso, acesse o cadastro de Unidades de Negócio para inserirmos as coordenadas. Acesse Recurso | Unidades de Negócio no menu principal.

Selecione o cadastro de cada uma das unidades, clicando em "Mais Campos" para incluir as coordenadas:

Uma forma fácil de se obter as coordenadas é utilizando o aplicativo Google Maps pelo endereço [http://maps.google.com](http://maps.google.com). Encontre o endereço da unidade e clique com o botão esquerdo do mouse por alguns segundos no ponto. Ele exibirá as coordenadas daquele ponto:

Preencha a Latitude e Longitude, clicando em OK e salvando o cadastro da unidade:

Observação: após salvar, quando recuperado novamente, o tipo de dado Decimal do Supravizio possui apenas 2 casas decimais. Caso necessite de mais precisão, crie os campos como Alfanuméricos e na consulta sql converta-os em Decimal (Sql Server) ou Number (Oracle), ou tipo de dado correspondente se outros SGBD's.

Vamos exibir agora a distribuição de colaboradores/clientes por Unidades de Negócio. No cadastro de Pessoas (menu Recurso | Pessoas), é importante preencher o campo Local de Trabalho para identificarmos a Unidade de Negócio do colaborador/cliente:

## Criando o Dashboard

Siga os passos abaixo:

| 1. | Selecione no menu principal o comando **Relatórios \| Editor de Dashboard**. |
|---|---|

| 2. | Será listada uma tela contendo os dashboards existentes. Neste caso, criaremos um novo, clicando no botão **Novo DashBoard**. |
|---|---|

| 3. | Abrirá uma nova tela solicitando um **Título do dashboard **a ser criado: |
|---|---|

Ao clicar para confirmar, o **Editor de Dashboard** será aberto.

| 4. | O primeiro passo é inserir uma **Fonte de Dados**, conforme explicamos anteriormente no tópico [Montando Queries](montando_queries). Para isso, clique no seguinte botão: |
|---|---|

Utilizamos a seguinte consulta para este exemplo:

```
select CP.LATITUDE, CP.LONGITUDE, U.DESCRICAO UNIDADE
from UNIDADE_NEGOCIO U
inner join CP_UNIDADE_NEGOCIO CP on CP.ID_UNIDADE_NEGOCIO = U.ID_UNIDADE_NEGOCIO
inner join PREDIO PR on PR.ID_UNIDADE_NEGOCIO = U.ID_UNIDADE_NEGOCIO
inner join LOCAL L on L.ID_PREDIO = PR.ID_PREDIO
inner join PESSOA P on P.ID_LOCAL = L.ID_LOCAL
```

5. Clique no comando abaixo:

6. Clique no comando abaixo:

7. Arraste as colunas para as seguintes Seções de Dados:

8. Em seguida, no mapa exibido, faça uma aproximação com os principais itens exibidos. Esta aproximação manterá o foco no mapa:

Você pode também converter a exibição ao invés de dados numéricos com balão, utilizar gráficos bolha que demonstrarão visualmente proporções. Para isso, clique com o botão direito do mouse no mapa e selecione a opção abaixo:

Após convertido:

Pronto, agora você pode publicar seu novo Dashboard. Para isso leia [Publicando Dashboards](publicando_dashboards).
