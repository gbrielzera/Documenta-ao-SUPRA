# Prenchimento customizado de campos

Caminho: Guia para Administradores > Configurando Processos > Tópicos Avançados > Formulários Dinâmicos > Exemplos de criação de formulários > Prenchimento customizado de campos

Podem haver casos em que não seja desejado exibir determinados campos ou que a exibição seja condicional a uma situação específica.

Vamos citar alguns exemplos de situações mais comuns:

## Exemplo 1: Campos em cascata

Neste exemplo, haverão três campos: "Seleção da Empresa", "Seleção de Órgão" e "Seleção de Pessoa". Com a utilização do script, o segundo campo só será exibido assim que selecionado o primeiro e respectivamente, ocorrendo o mesmo com o terceiro campo.

Estes campos recuperarão apenas os registros condizentes com a opção selecionada acima.

Para isso, inserimos a Entrada de Dados na respectiva tarefa. A fim de facilitar a leitura, utilizamos os nomes "**SELEC_EMPRESA**", "**SELEC_ORGAO**" e "**SELEC_PESSOA**", respectivamente, nos campos customizados.

Fluxo utilizado no Processo

Durante a criação dos campos customizados, inserimos os seguintes códigos no campo **Script para recuperação de opções**.

Tela de criação de campo customizado

**Local: Script para recuperação de opções**

**Campo: Seleção da Empresa**

```
Itens = Utils.ExecuteDataTable("select ID_EMPRESA, DESCRICAO from EMPRESA")
```

**Local: Script para recuperação de opções**

**Campo: Seleção do Órgão**

```
if OrdemServico.GetCustom("SELEC_EMPRESA") != None:
    Itens = Utils.ExecuteDataTable("select ID_ORGAO, DESCRICAO from ORGAO where ID_EMPRESA = " + OrdemServico.GetCustom("SELEC_EMPRESA").ToString())
```

**Local: Script para recuperação de opções**

**Campo: Seleção de Pessoa**

```
if OrdemServico.GetCustom("SELEC_ORGAO") != None:
    Itens = Utils.ExecuteDataTable("select ID_PESSOA, NOME from PESSOA where ID_ORGAO = " + OrdemServico.GetCustom("SELEC_ORGAO").ToString())
```

Em seguida, inserimos os seguintes códigos em **Script Modificado** de cada campo:

**Local: Script Modificado**

**Campo: Seleção da Empresa**

### SELEC_EMPRESA:

```
if Formulario["SELEC_EMPRESA"].Valor != None:
    Formulario["SELEC_ORGAO"].Itens = Utils.ExecuteDataTable("select ID_ORGAO, DESCRICAO from ORGAO where ID_EMPRESA = " + Controle.Valor.ToString())
    Formulario["SELEC_ORGAO"].Visivel = True
else:
    Formulario["SELEC_ORGAO"].Visivel = False
    Formulario["SELEC_PESSOA"].Visivel = False
Formulario["SELEC_ORGAO"].Valor = None
```

**Local: Script Modificado**

**Campo: Seleção de Órgão**

### SELEC_ORGAO:

```
if Formulario["SELEC_ORGAO"].Valor != None:
    Formulario["SELEC_PESSOA"].Itens = Utils.ExecuteDataTable("select ID_PESSOA, NOME from PESSOA where ID_ORGAO = " + Controle.Valor.ToString())
    Formulario["SELEC_PESSOA"].Visivel = True
else:
    Formulario["SELEC_PESSOA"].Visivel = False
Formulario["SELEC_PESSOA"].Valor = None
```

E em **Script Formulário carregado**, o seguinte código:

**Local: Script Formulário carregado**

**Tarefa: Seleção Pessoa**

```
Formulario["SELEC_ORGAO"].Visivel = Formulario["SELEC_EMPRESA"].Valor != None
Formulario["SELEC_PESSOA"].Visivel = Formulario["SELEC_ORGAO"].Valor != None
```

Ao abrir uma Ordem de Serviço, inicialmente será exibido apenas "Seleção da Empresa", tornando visível o próximo campo assim que o anterior seja selecionado.

Campos na Ordem de Serviço

## Exemplo 2: Recuperação de dados de cadastro

Neste exemplo, iremos realizar a recuperação de dados de um usuário, de acordo com o preenchimento de um campo (aqui utilizamos o campo login).

Fluxo utilizado no Processo

Na tarefa "Preencher Login", preenchemos **Script Formulário carregado** com o seguinte script:

**Local: Script Formulário carregado**

**Tarefa: Preencher Login**

```
Formulario["NOME_USUARIO"].Habilitado = False
Formulario["EMAIL_CONTATO"].Habilitado = False
Formulario["NOME_USUARIO"].Valor = Utils.ExecuteScalar("select NOME from Pessoa where USUARIO_REDE = " + "'" + OrdemServico.GetCustom("USUARIO_REDE")+ "'")
Formulario["EMAIL_CONTATO"].Valor = Utils.ExecuteScalar("select EMAIL from Pessoa where USUARIO_REDE = " + "'" + OrdemServico.GetCustom("USUARIO_REDE")+ "'")
```

Ao abrir uma Ordem de Serviço, digitamos o Login do Usuário:

Exibição do campo na Ordem de Serviço

Ao avançar a tarefa, o script será executado e serão exibidos os dados deste usuário:

Recuperação dos dados do usuário

## Exemplo 3: Visibilidade de campo condicional

Este script pode ser utilizado em situações onde seja necessário ou não o preenchimento de um campo, de acordo com o valor de outro.

Assim que for selecionada a opção, será exibido o próximo campo, onde o usuário poderá digitar as especificações.

Fluxo utilizado no Processo

Criamos os campos "POSSUI_DESPESAS" e "DESPESAS" e inserimos o seguinte código em **Script Modificado **do primeiro campo:

**Local: Script Modificado**

**Campo: Possui despesas?**

```
if Controle.Valor  == True:
    Formulario["DESPESAS"].Visivel = True
else:
    Formulario["DESPESAS"].Visivel = False
```

E após, inserimos o seguinte código em **Script Formulário carregado**:

**Local: Script Formulário carregado**

**Tarefa: Lançar despesas de viagem**

```
Formulario["DESPESAS"].Visivel = Formulario["POSSUI_DESPESAS"].Valor == True
```

Assim que selecionada a opção Sim, o campo **Despesas** se tornará visível e habilitado para preenchimento por parte do usuário.

Exibição do campo na Ordem de Serviço

A seguir, vamos dar outro exemplo em que o campo "Possui despesas?" é preenchido em outra atividade:

Fluxo do processo

Como o campo está em outra tarefa, devemos utilizar o método **OrdemServico.GetCustom() **para acessar o valor. E sendo o campo não obrigatório, pode acontecer casos em que este não tenha sido preenchido. Para estes casos, vamos exibir uma mensagem informando.

Também vale ressaltar que o campo é do tipo **Lógico**, ou seja, seu valor padrão será False. Portanto, devemos passar um valor padrão no método.

Sendo assim, inserimos o seguinte script em **Script Formulario Carregado**:

**Local: Script Formulário carregado**

**Tarefa: Lançar despesas de viagem**

```
if OrdemServico.GetCustom("POSSUI_DESPESAS") == "Sim":
    Formulario["DESPESAS"].Visivel = True
elif OrdemServico.GetCustom("POSSUI_DESPESAS", "None") == "None":
    Formulario.ExibeMensagem("O campo 'Possui Despesas?' não foi preenchido")
else:
    Formulario["DESPESAS"].Visivel = False
```
