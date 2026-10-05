# SearchList

Caminho: Guia para Administradores > Roteiro de implantação > Propriedades Customizadas > Criação de Campos Customizados > Tipos de Controle > SearchList

Exibe um controle com dois campos de busca. Digitando o número identificador no primeiro campo obtém-se o registro, digitando um texto no segundo campo, obtém-se os registros resultantes da pesquisa, selecionando o primeiro. Este controle é utilizado apenas se o campo Classe referência for preenchido. Para este controle, é possível utilizar valores dos tipos Alfanumérico, Listagem de Objetos, Inteiro.

Exemplo de controle SearchList

Para obter os registros nesta listagem, é necessário que seja informada uma fonte de dados, que pode ser realizada de duas formas:

Através da opção **Cadastro associado**, listando registros do Supravizio, como por exemplo, Pessoas ou Áreas cadastradas.

Cadastro associado

Caso o campo criado possua o tipo Alfanumérico ou Inteiro, além de um **Cadastro associado**, também será possível customizar a fonte de dados utilizando um script, inserido no campo **Script para recuperação de opções**.

No caso de controles **SearchList**, além da variável Itens que receberá os valores, estarão disponíveis mais três variáveis para que possa ser implementado filtro para o controle:

• **ValorCorrente** - Retorna o valor selecionado pelo usuário.

• **EntradaUsuario** - Armazena o conteúdo digitado pelo usuário no filtro.

• **FiltroAdicional** - Possibilita implementar um complemento ao filtro digitado pelo usuário no controle.

Configuração com script para filtro

**Exemplo de script para recuperação de opções**

```
sqlValor = "SELECT P.ID_PESSOA, P.NOME FROM PESSOA P WHERE P.ID_PESSOA = " + ValorCorrente
sqlEntrada = "SELECT P.ID_PESSOA, P.NOME FROM Pessoa P WHERE UPPER(P.NOME) like UPPER('%" + EntradaUsuario +"%')"
sqlOrder = " ORDER BY 2"
if not String.IsNullOrEmpty(ValorCorrente) and not String.IsNullOrEmpty(EntradaUsuario):
    Itens = DB.ExecuteDataTable("(" + sqlValor + ") UNION (" + sqlEntrada + " ) " + sqlOrder)
elif String.IsNullOrEmpty(EntradaUsuario) and String.IsNullOrEmpty(ValorCorrente):
    Itens = None
elif String.IsNullOrEmpty(EntradaUsuario):
    Itens = DB.ExecuteDataTable( sqlValor + sqlOrder)
else:
    Itens = DB.ExecuteDataTable( sqlEntrada + sqlOrder)
```

Assim, quando visualizamos o controle, é possível realizar um filtro a partir do Nome da Pessoa:

Filtro
