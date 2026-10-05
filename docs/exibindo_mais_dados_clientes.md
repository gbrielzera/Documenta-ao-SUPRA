# Exibindo mais dados sobre Clientes

Caminho: Guia para Solucionadores > Workspace  > Workspace Ordens de Serviço > Exibindo mais dados sobre Clientes

Para cada Tipo de Subprocesso é possível redefinir a exibição de dados do Cliente relacionado com a Ordem de Serviço ou informações quaisquer necessárias.

Esta configuração é feita no cadastro de Tipo de Subprocesso (Processo | Processos | Tipos de Subprocesso), na seção **Campos cliente**:

Para adicionar um novo campo, clique em Novo. Você pode definir a ordem de exibição através do campo Sequência e o Rótulo do campo. Seguida, você definirá a informação que quer exibir através de um script Ironpython no campo Fórmula:

Este script deve retornar sempre um valor Alfanumérico. Para isso, é importante convertê-lo para o tipo String do .Net. Um modo prático para isso, sem a necessidade de verificações sobre a existência ou se o objeto que será convertido para o tipo Alfanumérico (String) esteja nulo, basta utilizar a classe utilitária .Net Convert, utilizando o método ToString():

```
Convert.ToString(OrdemServico.Cliente.PerfilCliente)
```

Vejamos o caso do script acima. Queremos exibir o Perfil Cliente do cliente da solicitação:

Em muitos casos, este campo não é preenchido. Neste caso, caso seja necessário definir um valor "default", basta incluir uma cláusula condicional utilizando a sintaxe abaixo:

```
"Valor Default" if OrdemServico.Cliente.PerfilCliente == None else Convert.ToString(OrdemServico.Cliente.PerfilCliente)
```

Vamos incluir então o valor "Comum" caso não seja definido um perfil para o cliente:

No caso acima, do cliente Jorge Nascimento Andrade, será exibido com este valor padrão:

Como o atributo Fórmula é um script Ironpython, você pode acessar quaisquer tipos de informações. Você pode acessar um banco de dados utilizando o objeto utilitário DB, acessar um webservices utilizando o objeto utilitário Webservices e todos os outros objetos.
