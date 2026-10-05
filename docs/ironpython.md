# IronPython

Caminho: Recursos Avançados > IronPython

A tecnologia IronPython é uma implementação da linguagem Python na plataforma Microsoft .NET. Isto significa que o IronPython disponibiliza um script em sintaxe Python e todos os recursos da plataforma Microsoft .NET.

Utilizando scripts Python o usuário analista de processos pode automatizar diversas tarefas do processo tais como:

- Manutenções no serviço de diretório Microsoft Active Directory tais como desbloqueio de conta, criação de usuários, inclusão ou remoção de usuários em grupos etc;
- Execução de procedimentos armazenados em banco de dados e comandos SQL
- Realizar chamadas webservices

Neste tópico apresentaremos alguns conceitos da linguagem Python necessários para construir os scripts utilizados nas atividades dos processos do Supravizio.

Para informações avançadas recomendados a leitura do material oficial da linguagem disponível no site [http://www.python.org/](http://www.python.org/).

Clique neste link para verificar exemplos de scripts criados com a a linguagem IronPython: [Utils](utils).

**Operadores Aritméticos**

Como na maioria das linguagens de programação, o IronPython possui vários operadores aritméticos. Descrevemos na tabela abaixo estes operadores aritméticos:

| **Operador** | **Significado** | **Exemplo** |
|---|---|---|
| + | Adição | a + b |
| - | Subtração | a – b |
| * | Multiplicação | a * b |
| / | Divisão | a / b |
| % | Resto da Divisão Inteira | a % b |
| - | Sinal negativo (- unário) | -a |
| + | Sinal Positivo (+ unário) | +a |

Os operadores aritméticos do IronPython, podem ser combinados para formar expressões onde deve ser observada a precedência (ordem convencional) de avaliação dos operadores.

O sinal ortográfico **parênteses ()** deve ser utilizados para determinar uma forma específica de avaliação de uma expressão.

**Operador de Atribuição**

Atribuição é a operação que permite definir o valor de uma variável através de uma constante ou através do resultado de uma expressão envolvendo operações diversas. Para isso basta escrever o nome da variável seguido o sinal aritmético **igual (=)** e do valor correspondente:

| **Exemplo 1** |
|---|
| Linha 1 | umNumeroQualquer **=** 12 |

Atenção: O número da linha a esquerda é apenas um estilo do texto que vamos utilizar para comentar o script, ele não deve ser escrito no editor.

**Variável, Objeto e Propriedade**

Variável é um espaço de memória que armazena algum valor, este espaço de memória deve ser rotulado com um nome e é por este nome que nos referimos nos scripts ao local da memória. O valor armazenado pode ser algo simples tal como um número ou algo complexo tal como um objeto complexo.

Por sua vez um objeto complexo possui variáveis e operações. Então quando temos uma variável que não é simples a variável é chamada de objeto, e as variáveis existentes dentro deste objeto são chamadas de propriedades.

Exemplo de uma variável com valor primitivo:

| **Exemplo 2** |
|---|
| Linha 2 | umNumeroQualquer **=** 12 |

No código acima estou criando uma variável chamada **umNumeroQualquer** que é simples, pois armazena um número que é considerado simples.

Abaixo apresentamos um exemplo de uma variável complexa:

| **Exemplo 3** |
|---|
| Linha 1 | ocorrencia = Ocorrencia.Carrega(1) |

No código acima, estamos criando uma variável chamada **ocorrencia** que é algo complexo, este objeto possui propriedades, um exemplo de propriedade para ocorrência é “Assunto”. Logo para acessar esta **propriedade** basta utilizar o sinal ortográfico **ponto (.)** e escrever o nome da propriedade, conforme o exemplo abaixo:

| **Exemplo 4** |
|---|
| Linha 1 | # carrega objeto Ocorrencia de identificador 1 |
| Linha 2 | ocorrencia = Ocorrencia.Carrega(1) |
| Linha 3 |  |
| Linha 4 | # modifica a propriedade Assunto |
| Linha 5 | ocorrencia.Assunto = "Assunto"; |

Na linha 5 estamos atribuindo a **propriedade** chamada **Assunto** existente no **objeto** chamado **ocorrencia**. Da mesma forma que podemos atribuir valores também podemos acessar valores.

O código acima traz a linha 1 e 4 marcadas com o símbolo **sustenido #** no inicio do texto, isso significa que esta linha é um comentário de script. Estes comentários não são processados e servem apenas para documentar o script. Documentar scripts é uma prática recomendada.

**Funcionalidades dos Objetos**

O comportamento dos objeto é definido por suas operações, toda operação é definida para tomada de uma ação podendo ou não retornar algum valor.

No exemplo 4 podemos observar na linha 2 do script uma funcionalidade sendo utilizada. Esta funcionalidade se chama** “Carregar"**, e esta tem como função carregar os objetos.

Ao construir uma operação, especificamos quais valores são esperados e especificamos também a sua saída, sendo que estas informações definem a assinatura da operação. Clique no link [Modelos de Objetos](modelo_de_objetos) para conhecer quais são as assinaturas das operações existentes nos objetos existentes no Supravizio.

Acessando o link [ApontamentoResponsavel](objetos_apontamentoresponsavel) podemos verificar no objeto ApontamentoResponsavel seis propriedades, e para estas propriedades encontramos o seu nome, sua descrição e o seu tipo. Encontramos também uma Operação, chamada **Carregar**. Segundo a descrição esta operação carrega um objeto baseado em informações existente na base de dados. **Carrega** recebe como parâmetros um nome de uma propriedade e um valor, e retorna um objeto **ApontamentoResponsavel**.

**Operadores Relacionais**

Além dos operadores aritméticos o IronPython possui operadores relacionais, isto é, operadores que permitem comparar valores literais, variáveis ou o resultado de expressões retornando um resultado do tipo lógico, isto é, um resultado falso ou verdadeiro. Os operadores relacionais disponíveis são:

| **Operador** | **Significado** | **Exemplo** |
|---|---|---|
| == | Igual | a == b |
| != | Diferente | a != b |
| > | Maior que | a > b |
| < | Menor que | a < b |
| >= | Maior ou igual a | a >= b |
| <= | Menor ou igual a | a <=b |

**Estruturas de Controle**

Estruturas de controle controlam o fluxo de execução dos scripts, a escolha do fluxo de operações executadas é controlada baseando-se em condições:

**Condição if...else**

O if...else é a estrutura de controle de fluxo mais simples e basea-se em uma condição. Se esta condição for satisfeita, executa um bloco de comandos, e podemos também definir um bloco de código se a condição não for satisfeita:

| **Template do comando if...else** |
|---|
| 1 | # x é um número inteiro |
| 2 | **if** uma condição aqui**:** |
| 3 | # Fazer algo aqui caso x seja menor que zero |
| 4 | **else:** |
| 5 | # Fazer algo aqui caso a condição não seja satisfeita |

**Atenção:** Repare que o bloco de código dentro da condição é alinhado à direita com **quatro espaços**, são estes espaços que definem o bloco de comandos:

**Quatro espaços definido as linhas do bloco de código**

Esta observação é válida para todas as estruturas de controle inclusive instruções dentro de instruções, conforme podemos verificar no exemplo abaixo:

| **Exemplo 5** |
|---|
| `linha 1` | `tipoPessoa = OrdemServico.Cliente.TipoColaborador` |
| `linha 2` | `cargo = OrdemServico.Cliente.Cargo` |
| `linha 3` |  |
| `linha 4` | `if tipoPessoa == "Empregado":` |
| `linha 5` | `if cargo == "Gerente":` |
| `linha 6` | `#  Preenche o campo DescricaoDetalhada da Ordem de Serviço` |
| `linha 7` | `OrdemServico.DescricaoDetalhada = "Conta de rede, email e internet"` |
| `linha 8` | `else:` |
| `linha 9` | `# Preenche o campo DescricaoDetalhada da Ordem de Serviço` |
| `linha 10` | `OrdemServico.DescricaoDetalhada = "Conta de rede e email"` |
| `linha 11` | `else:` |
| `linha 12` | `# Preenche o campo DescricaoDetalhada da Ordem de Serviço` |
| `linha 13` | `OrdemServico.DescricaoDetalhada = "Somente conta de rede"` |

De acordo com o script acima se o tipoPessoa for igual a** "Empregado"** e o cargo for igual a** "Gerente"** então é atribuído o texto** "Conta de rede, emal e internet"** para o campo **DescricaoDetalhada** do objeto Ordem de Serviço. Caso contrário se **tipoPessoa** for igual a "Empregado" com cargo diferente de "Gerente" então é atribuído o texto "Conta de rede e email" para a mesma variável, e e finalmente se tipoPessoa for diferente de "Empregado" (não importando o cargo) é atribuído o valor "Somente conta de rede".

**Operadores Lógicos**

O IronPython também possui operadores lógicos, isto é, operadores que permitem conectar logicamente o resultado de diferentes expressões aritméticas ou relacionais construindo assim uma expressão resultante composta de várias partes e portanto mais complexa:

| **Operador** | **Significado** | **Exemplo** |
|---|---|---|
| and | E lógico | a and b |
| or | Ou lógico | a or b |

**Estrutura de Repetição For**

Quando necessitamos repetir determinado número de vezes uma determinada sequencia de comandos utilizamos a estruturas de repetição FOR:

| **Exemplo 6** |
|---|
| `Linha 1` | `# carrega objeto OrdemServico de identificador 77` |
| `Linha 2` | `OrdemServico = OrdemServico.Carrega(77)` |
| `Linha 3` |  |
| `Linha 4` | `# verifica se o objeto foi recuperado com sucesso` |
| `Linha 5` | `if OrdemServico != None:` |
| `Linha 6` | `# percorre objetos da propriedade ItensAnexos` |
| `Linha 7` | `for anexo in OrdemServico.ItensAnexos:` |
| `Linha 8` | `# Podemos utilizar dados do item anexado na OS para executar uma tarefa` |
| `Linha 9` | `Utils.LogInformation("Item: " + anexo.ItemConfiguracao.ToString())` |

No script acima, podemos identificar que carregamos na linha 2 o objeto **OrdemServico** de identificador 77. Na linha 5 verificamos se o objeto foi recuperado com sucesso. Na linha 7 estamos realizando uma repetição utilizando a propriedade** ItensAnexos** do objeto **Ordemservico. **Para cada **ItensAnexo** temos uma interação nesta repetição. Na linha nove obtemos informações através do Utils.LogInformation, e estas informações servem para executar uma tarefa.
