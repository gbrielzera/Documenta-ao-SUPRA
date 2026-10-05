# Criando um Dashboard

Caminho: Guia para Administradores > Editor de Dashboard > Criando Dashboards > Criando um Dashboard

Através deste exemplo demostraremos a criação e utilização de um dashboard que exibirá de forma gráfica o percentual de satisfação de clientes nas pesquisas enviadas aos mesmos.

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
SELECT PESSOA.NOME, EQ.ROTULO AS RESPOSTA, COUNT(EQ.VALOR) TOTAL, P.DATA_HORA_RESPOSTA
FROM CLASSE_PESQ_SATISF CLPS, PESQUISA P, ITEM_PESQUISA IP, QUESTAO_PESQUISA QP, GRUPO_QUESTAO GQ, ESCORE_QUESTAO EQ, OCORRENCIA O, PESSOA WHERE QP.ID_GRUPO_QUESTAO = GQ.ID_GRUPO_QUESTAO AND O.ID_OCORRENCIA = P.OS AND PESSOA.ID_PESSOA = O.ID_FINALIZADOR AND CLPS.ID_CLASSE_PESQ_SATISF = P.ID_CLASSE_PESQ_SATISF AND QP.ID_QUESTAO = IP.ID_QUESTAO AND P.ID_PESQUISA = IP.ID_PESQUISA AND GQ.ID_GRUPO_QUESTAO = EQ.ID_GRUPO_QUESTAO AND IP.ESCORE = EQ.VALOR AND (IP.ESCORE IS NOT NULL) AND (P.SITUACAO = 'Concluida') GROUP BY PESSOA.NOME, EQ.ROTULO, EQ.VALOR, P.DATA_HORA_RESPOSTA ORDER BY 1
```

| 5. | Criada a fonte de dados, o próximo passo é escolher uma forma de representação. Neste exemplo, utilizaremos o **Pies **ou também conhecido como gráfico de pizza. Para isso, basta clicar no botão indicado: |
|---|---|

| 6. | Ao clicar neste botão, será possível a edição do gráfico, assim como a inserção de dados no mesmo. Para inserir os campos retornados na consulta, arraste-o para o local desejado na seção **Data Items**. |
|---|---|

Aqui, definimos os campos na seguinte forma:

| 7. | Montado o painel, clique no botão **Salvar **para guardar o Dashboard que acabou de ser criado: |
|---|---|

**Importante**: Para que este se torne visível aos solucionadores no Supravizio Web, temos que realizar a publicação do Dashboard. Explicaremos mais sobre este procedimento no tópico [Publicando Dashboards](publicando_dashboards).
