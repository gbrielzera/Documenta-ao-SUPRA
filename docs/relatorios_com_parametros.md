# Relatórios com Parâmetros

Caminho: Guia para Administradores > Editor de Relatórios > Criando Relatórios > Relatórios com Parâmetros

Este tópico tem por objetivo dar uma visão geral sobre a utilização de parâmetros para filtros em relatórios. Este tem como pré-requisito a execução do tópico [Criando um Relatório Simples](criando_um_relatorio_simples).

1. Após executar o tópico indicado acima, na listagem de Relatórios da transação Editor de Relatórios, selecione o relatório criado e clique no comando **Novo > Copiar registro selecionado**.

2. Preencha o campo Descrição conforme figura abaixo:

3. Selecione a aba "Layout". Após isso, clique no comando **Configurar dados | Principal**.

4. Na área de edição da instrução SQL da consulta, faça a alteração para a parametrização da consulta.

Caso o Banco de Dados utilizado seja SQL Server, o parâmetro deverá ter o prefixo** @**(arroba)

```
Select OCORRENCIA.ASSUNTO, OCORRENCIA.NUMERO From OCORRENCIA Where OCORRENCIA.ID_CLASSE_SUB_PROC = @pSubprocesso
```

Caso seja Oracle, deverá ser precedido por :(dois pontos)

```
Select OCORRENCIA.ASSUNTO, OCORRENCIA.NUMERO From OCORRENCIA Where OCORRENCIA.ID_CLASSE_SUB_PROC = :pSubprocesso
```

Neste caso, nossa consulta listará apenas Ordens de Serviço de um Tipo de Subprocesso específico através do parâmetro **pSubprocesso**.

5. Clique em OK no Query Builder. Repare que o parâmetro pSubprocesso foi inserido automaticamente no nó Parâmetros da Lista de Campos:

6. Selecione a aba Parâmetros. Observe que o parâmetro pSubprocesso foi inserido automaticamente nesta listagem.

7. Vamos agora recuperar da tabela [CLASSE_SUB_PROCESSO](dados_classe_sub_processo) os Tipos de Subprocesso disponíveis para nosso filtro. Dê um duplo clique no registro do parâmetro pSubprocesso. Em seguida, com a janela de cadastro aberta, vamos inserir a seguinte instrução SQL para recuperação de itens:

SQL utilizado:** Select ID_CLASSE_SUB_PROCESSO, DESCRICAO From CLASSE_SUB_PROCESSO Order Bi DESCRICAO**

Clique em Fechar no formulário de Parâmetro de relatório. Em seguida, salve o relatório.

8. Na aba Layout, clique em Visualizar.

Observe que o novo parâmetro fica disponível para a consulta no lado esquerdo da janela de relatório:

Repare que os descritivos do parâmetro são os mesmos do campo DESCRICAO extraído da consulta SQL. O comportamento deste componente assume que o primeiro campo (ID_CLASSE_SUB_PROCESSO) armazena o** valor** do parâmetro. O segundo campo (DESCRICAO) indica a **representação textual** do registro.

É necessário neste ponto, a fim de uma melhor apresentação ao usuário final, realizarmos algumas formatações.

9. Feche a janela de visualização do relatório. Ainda na aba Layout, no quadro Lista de Campos, selecione o parâmetro pSubprocesso. Observe que exibirá as propriedades do parâmetro em região abaixo:

Isso fará com que o nome do parâmetro exibido na visualização do relatório tenha um descritivo mais adequado:

10. Vamos agora indicar um nome de descritivo mais adequado aos registros do controle de listagem. Na aba Parâmetros, dê novamente um duplo clique no registro do parâmetro pSubprocesso. Faça a seguinte alteração na instrução SQL:

SQL utilizado: **Select ID_CLASSE_SUB_PROCESSO, DESCRICAO as Descrição From CLASSE_SUB_PROCESSO Order By DESCRICAO**

11. Clique em Fechar no cadastro do parâmetro. Volte na aba Layout e clique no comando Visualizar. Repare que nosso relatório agora conta com descritivos amigáveis para o parâmetro pSubprocesso:

| **ANTES** | **DEPOIS** |
|---|---|

12. Salve o relatório.

Para publicar este relatório no menu principal, leia o tópico [Relatórios no Menu Principal](relatorios_no_menu_principal).

**Filtrando Valores Para os Parâmetros**

Podemos também utilizar os parâmetros sendo filtrados, caso não seja necessário exibir todos os campos de uma tabela no parâmetro para o relatório.

Para isso utilizamos a cláusula **WHERE **no final do SQL, antes do **ORDER BY**.

**Campos numéricos:**

O comando WHERE deve ser seguido com um campo da tabela sendo comparada com um outro valor.

Para esse exemplo temos um parâmetro chamado "person" com a seguinte query no "Itens para seleção":

ex: **SELECT nome FROM pessoa WHERE ID_PESSOA > 10**.

Neste caso, serão exibidos no parâmetro, apenas os nomes das pessoas na qual o identificador for maior que 10:

Podemos também determinar intervalos, como por exemplo: **SELECT nome FROM pessoa WHERE ID_PESSOA BETWEEN 10 AND 20**.

Neste caso serão listados apenas os nomes das pessoas com o identificados entre 10 e 20.

**Campos alfanuméricos:**

Para fazermos a comparação com campos alfanuméricos, como por exemplo o nome da pessoa, utilizamos o comando **LIKE.**

O comando LIKE deve ser seguido por aspas simples (') e algum coringa como o %, que determina qualquer quantidade e qualquer letra, e sendo ter por uma aspas simples, por ser um valor alfanumérico.

Para este exemplo, utilizamos o mesmo campo "person", porém, agora selecionaremos apenas as pessoas que tenham a primeira letra do nome com F.

ex: **SELECT nome FROM pessoa WHERE nome LIKE 'F%'**.

Podemos observar que foram exibidos somente nome das pessoas que o nome começa com F, independe das letras ou nomes posteriores:

Podemos também utilizar o coringa no final do valor comparado, para selecionar apenas as pessoas que tenham o sobrenome "Silva".

ex: **SELECT nome FROM pessoa WHERE nome LIKE '%Silva'**.

Podemos observar que foram listados apenas as pessoas cujo o nome terminam com Silva, independente da quantidade de letras ou nomes anteriores.
