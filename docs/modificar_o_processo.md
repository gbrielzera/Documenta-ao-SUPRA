# Customização do número das Ordens de Serviço

Caminho: Customização do número das Ordens de Serviço

O Supravizio permite realizar a customização da sequência numérica das Ordens de Serviço. É possível realizá-la tanto por uma fórmula específica ou por um script durante o fluxo do processo.

## Customização Por Fórmulas

Na tela de cadastro do Processo, é possível incluir uma fórmula que altera o número exibido para a Ordem de Serviço.

A seguir, iremos mostrar o passo-a-passo de como realizá-la:

### Passo 1: Clique com o botão direito sobre o Processo que deseja alterar e em seguida, em Modificar o Processo.

**Modificar o Processo**

### Passo 2: Adicione uma Fórmula para numeração, de acordo com o formato desejado.

Campo para a fórmula

Para melhor entendimento, vamos citar alguns exemplos que podem ser utilizados para tal customização.

### Exemplo 1: Adicionando um Identificador Fixo

Neste exemplo, iremos adicionar um identificador na frente do número, como por exemplo, a **IN** referenciando ao processo **Incidente**.

Para isso, utilizaremos a seguinte fórmula:

```
"IN" + OrdemServico.NumeroSequencial
```

Ao abrir uma nova Ordem de Serviço, o número ficará com o seguinte formato:

Número Customizado

### Exemplo 2: Adicionando o Ano Corrente

Neste, além de padronizar o número da Ordem de Serviço e adicionar o Ano Corrente ao final do número identificador.

Para isso, utilizaremos a seguinte fórmula:

```
NumeroSistema.PadLeft(3, '0').ToString() + "/" + DateTime.Now.Year.ToString()
```

Ao abrir uma nova Ordem de Serviço, o número ficará com o seguinte formato:

Número Customizado

### Exemplo 3: Utilizando uma sequência numérica de acordo com o Subprocesso

Também é possível gerar uma sequência numérica avulsa ao número gerado inicialmente pelo Sistema.

Neste exemplo, adicionaremos a sigla do respectivo Subprocesso e faremos com que haja uma sequência independente para cada Tipo de Subprocesso.

Para isso, utilizaremos a seguinte fórmula:

```
OrdemServico.ClasseSubProcesso.Sigla.ToString()+Utils.NewSequenceValue(OrdemServico.ClasseSubProcesso.ToString()).ToString().PadLeft(3, '0')
```

Ao abrir uma nova Ordem de Serviço, o número ficará com o seguinte formato:

Número Customizado

## Customização por Script

Também é possível realizar esta customização através de scripts inseridos durante o Fluxo do Processo.

A vantagem de utilizar este tipo de customização é que podem ser utilizados campos preenchidos na própria Ordem de Serviço.

Vamos utilizar neste exemplo o fluxo Solicitação de Compra:

l

Fluxo do Processo

Note que logo no início é definido o Identificador da Compra, o qual utilizaremos como identificador da Ordem de Serviço.

Inserimos o seguinte script no Evento Inicial:

```
OrdemServico.Numero = OrdemServico.GetCustom("ID_COMPRA").ToString() + OrdemServico.Numero.ToString().PadLeft(3, '0')
```

Local onde o script foi inserido

Ao abrir uma Ordem de Serviço, o número permanecerá o mesmo até o script ser executado (ao fim do Evento Inicial):

Abertura de Ordem de Serviço

Quando o script for executado, o número será alterado de acordo com o identificador da compra. No caso, utilizamos **SUP** referenciando **Suprimentos**.

Número Customizado na Ordem de Serviço

Ordens de Serviço Associadas Para auxiliar na identificação das Ordens de Serviço associadas, o Supravizio permite a customização do número destas. Esta funcionalidade pode ser utilizada, por exemplo, para facilitar a identificação da associação entre a Ordem de Serviço chamadora e a invocada.

Pode ser realizada de duas formas, conforme vamos mostrar nos exemplos abaixo.

### Exemplo 1: Utilizando parãmetro no cadastro da associação

No cadastro de [Associações](associacao_sub), há o parâmetro **Separador para numeração relativa**, o qual define um caracter a ser utilizado para a montagem de uma numeração relativa entre a Ordem de Serviço chamadora e a invocada.

Para acessar a transação, utilize o caminho **Processo | Processos | Associações**:

Caminho para a transação

Para este exemplo, faremos com que a Ordem de Serviço referente a um **Problema** seja enumerada de acordo com a de **Incidente** que a gerou. Para isso, acessamos o cadastro da associação e preenchemos o campo **Separador para numeração relativa** o valor '**.**' e após, salvamos as alterações.

Cadastro da associação

Ao abrirmos uma Ordem de Serviço associada, a nova terá uma numeração contendo o número da Ordem de Serviço chamadora, seguida de um número sequencial.

Ordem de Serviço associada

### Exemplo 2: Customizando por script

O número das Ordens de Serviço associadas também podem ser customizadas através de scripts nas tarefas. Para isso, podem ser utilizadas as seguintes funções:

Neste exemplo, iremos inserir um identificador para a Ordem de Serviço de **Problema**, gerada por um **Incidente** a fim de identificar que qual foi a origem da mesma. Para isso, adicionamos o seguinte script no Script Início da atividade:

Script inserido

Quando for gerada uma Ordem de Serviço referente a um **Problema**, esta terá a numeração conforme montamos no script, um identificador "PROB." seguido do número do **Incidente** que a gerou.

Número da Ordem de Serviço gerada
