# Jobs Customizados

Caminho: Recursos Avançados > Jobs Customizados

O Supravizio permite que sejam programadas rotinas implementadas em IronPhyton para diversas finalidades. Estas rotinas são chamadas de **Jobs Customizados**.

Esta opção se encontra disponível no menu, na opção **Utilitários**.

Localização da opção Jobs Customizados

Para demonstrar a sua funcionalidade, iremos criar uma rotina que desativa pessoas que possuem previsão de finalização de contrato e também a desativa no Active Directory.

Para isso, inicialmente, devemos criar uma **Propriedade Customizada** para inclusão desta data de previsão.

Entre em **Utilitários - Dicionário de Classes - Dicionário de Classes **e procure por "**Pessoa**", a fim de localizar a classe "**Venki.Supravizio.Recurso.Pessoa, Supravizio", **dando um duplo clique nela em seguida.

Tela do Dicionário de Classes

Na tela do cadastro da classe, entre na aba **Propriedades Customizadas**, e após em Novo.

Será exibida a seguinte tela:

Nova Propriedade Customizada

Nela preencha conforme a imagem acima, e depois confirme e salve estas alterações.

Criada a **Propriedade Customizada**, entre no cadastro de alguma **Pessoa** ativa (neste exemplo, utilizamos Maria Tereza), através do caminho **Recurso - Pessoas**.

No cadastro desta **Pessoa**, clique em **Mais Campos**, onde deverá constar a Propriedade que acabamos de criar.

Nela, inclua uma **Data para término de contrato**.

Tela de Cadastro de Pessoas

Agora, iremos criar uma nova rotina em **Jobs Customizados**. Para isso, siga o caminho** Utilitários - Jobs Customizados**.

Na tela que irá abrir, clique em **Novo**:

Tela Jobs Customizados

Em seguida, serão exibidos dois campos:

Descrição: deve ser preenchido com uma descrição da rotina a ser criada, este campo pode ser alterado pelo usuário

Script para execução: campo de edição do script em IronPhyton a ser executado

Preencha-os com o seguinte conteúdo:

Campos a serem preenchidos

Segue script abaixo:

```
finalizados = Utils.ExecuteDataTable("select CP.ID_PESSOA from PESSOA P, CP_PESSOA CP where P.ID_PESSOA = CP.ID_PESSOA and P.ATIVO = 'Sim' and CP.DATA_TERMINO_CONTRATO IS NOT NULL and CP.DATA_TERMINO_CONTRATO <= GetDate()")
if finalizados != None:
    for row in finalizados.Rows:
        pessoa = Pessoa.Carrega(row["ID_PESSOA"])
        if pessoa != None:
            Utils.ADDisableUser(pessoa.UsuarioRede)
            pessoa.Ativo = False
            Pessoa.Salva(pessoa)
```

**IMPORTANTE**: a função GetDate() é uma função nativa em SGBD SQL Server. Para a execução em SGBD Oracle, utilize SYSDATE.

Na aba **Opções**, programe uma data e horário de agendamento de execução.

Aba Opções

Confirme as alterações e salve a nova rotina.

Criação da nova rotina

Caso deseje alterá-la, basta dar um duplo clique em seu cadastro.

Também pode ser obtido um **Relatório de Execução**, selecionando a rotina e pressionando **Relatório Execução**.

Além dos horários agendados, também podemos executar esta rotina aleatoriamente, selecionando-a e clicando no botão **Repetir**.
