# Automatizações em Listagem de Registros

Caminho: Guia para Administradores > Configurando Processos > Tópicos Avançados > Formulários Dinâmicos > Exemplos de criação de formulários > Automatizações em Listagem de Registros

Em Listagens de Registros, pode haver casos em que seja necessária automatização, como cálculo de valores ou validação de valores.

Vamos citar alguns exemplos de situações mais comuns:

## Exemplo 1: Listagem de itens

Neste exemplo, iremos configurar uma lista de itens para compras que pode ser utilizado, por exemplo no processo **Adquirir de Suprimentos**.

Fluxo do Processo

Configuramos o campo de seleção do produto para realizar uma consulta a outra base de dados:

Configuração do campo DESCRICAO

Para cálculo do valor total da Lista de Compras, utilizamos um campo calculado, que terá como valor o resultado da multiplicação entre os campos **PRECO** e **QUANTIDADE**:

Fórmula de cálculo

**Importante: **No caso de campos com Fórmula de Cálculo, o valor destes é calculado a cada alteração realizada. Sendo assim, os valores não são gravados no Banco de Dados.

Na configuração dos campos do grid, iremos preencher scripts em **Script Modificado **para que sejam executados a cada modificação de valor do respectivo campo:

Script Modificado na coluna do grid

Iremos introduzí-los scripts nas seguintes colunas:

**Local: Script Modificado**

**Coluna: Descrição**

```
#caso o campo descricao esteja preenchido ira buscar o peso e preco no banco de dados
if not String.IsNullOrEmpty(FormularioRegistro["DESCRICAO"].Valor):
    FormularioRegistro["PRECO"].Valor = DB.ExecuteScalar("SELECT VALOR FROM PRODUTOS WHERE CODIGO = '" + FormularioRegistro["DESCRICAO"].Valor + "'")
    FormularioRegistro["PESO"].Valor = DB.ExecuteScalar("SELECT PESO FROM PRODUTOS WHERE CODIGO = '" + FormularioRegistro["DESCRICAO"].Valor + "'")
    FormularioRegistro["TOTAL"].Valor = FormularioRegistro["PRECO"].Valor
#se a quantidade estiver preenchida calculara valor e peso total
if not String.IsNullOrEmpty(FormularioRegistro["DESCRICAO"].Valor) and FormularioRegistro["QUANTIDADE"].Valor > 0:
    FormularioRegistro["PESO"].Valor = FormularioRegistro["QUANTIDADE"].Valor * FormularioRegistro["PESO"].Valor
    FormularioRegistro["TOTAL"].Valor = FormularioRegistro["PRECO"].Valor * Convert.ToDecimal(FormularioRegistro["QUANTIDADE"].Valor)
```

**Local: Script Modificado**

**Coluna: Quantidade**

```
#caso o campo descricao e quantidade estejam preenchidos calcula peso e valor total
if not String.IsNullOrEmpty(FormularioRegistro["DESCRICAO"].Valor) and FormularioRegistro["QUANTIDADE"].Valor > 0:
    FormularioRegistro["TOTAL"].Valor = FormularioRegistro["PRECO"].Valor * Convert.ToDecimal(FormularioRegistro["QUANTIDADE"].Valor)
    if FormularioRegistro["PESO"].Valor > 0:
        FormularioRegistro["PESO"].Valor = FormularioRegistro["PESO"].Valor * Convert.ToDecimal(FormularioRegistro["QUANTIDADE"].Valor)
    else:
        FormularioRegistro["PESO"].Valor = DB.ExecuteScalar("SELECT PESO FROM PRODUTOS WHERE CODIGO = " + FormularioRegistro["DESCRICAO"].Valor.ToString(), "BASEPROD")
```

Também inserimos scripts a serem executados ao adicionar linhas:

```
Local do script
```

**Local: Script Adicionado**

**Campo: Itens para compra**

```
#inicia os valores para peso, preço e quantidade ao adicionar uma nova linha
NovoRegistro["PRECO"]= 0.0
NovoRegistro["QUANTIDADE"]= 0
NovoRegistro["TOTAL"] = 0.0
NovoRegistro["PESO"]= 0.0
```

Ao adicionar uma nova linha, os campos **Quantidade**, **Peso** e **Preço** estarão com valores iguais a zero e ao selecionar um item na **Descrição**, os outros campos serão carregados automaticamente de acordo com os valores obtidos durante consulta ao Banco de Dados.

Efeito das customizações no formulário

## Exemplo 2: Recuperação de dados de uma listagem

Ao utilizar a variável do campo, é retornado um objeto do tipo [DataTable](http://msdn.microsoft.com/pt-br/library/system.data.datatable.aspx) o qual pode ser percorrido através de suas linhas, do tipo [DataRows](http://msdn.microsoft.com/pt-br/library/system.data.datarow.aspx).

Abaixo, criamos uma tarefa onde é verificado o peso total dos itens. Para isso, teremos que percorrer o peso dos itens e inserir a soma destes em um campo a ser analisado pelo responsável.

Fluxo do Processo

Inserimos em **Script Formulário carregado**, para que este seja atualizado a cada momento em que o campo seja exibido. Note que aplicamos um laço de repetição para que seja percorrido o grid.

**Local: Script Formulário carregado**

**Tarefa: Verificar peso**

```
pesoTotal = 0
dt = OrdemServico.GetCustom("LISTA_ITENS")
for dr in dt.Rows:
    pesoTotal = pesoTotal + dr["PESO"]
Formulario["PESO_TOTAL"].Valor = pesoTotal
```

Ao entrar na tarefa e carregar o formulário, o script é executado e o valor já vem carregado de acordo com a soma do peso dos itens na listagem:

Tela de Edição
