# Conexões de Usuários

Caminho: Relatórios > Conexões de Usuários

O relatório de Conexões de Usuário tem por objetivo apresentar informações de conexões realizadas por usuários a aplicação.

## Parâmetros

Na figura abaixo podemos observar a tela de parâmetros para este relatório:

Parâmetros do relatório

| **Início** | Data de início para recuperação de dados de conexões. Este parâmetro recupera os valores cuja data de referência seja maior ou igual ao valor informado. |
|---|---|
| **Fim** | Data limite fim para recuperação de dados de conexões. Este parâmetro recupera os valores cuja data de referência seja menor ou igual ao valor informado. |
| **Usuário** | Este parâmetro filtra os registros de acordo com o usuário do sistema selecionado na listagem. Se não for informado então este critério é desconsiderado na recuperação. |
| **Grupo de Trabalho** | Filtra registros de acordo com o Grupo de Trabalho dos usuários. Se não for informado então este critério é desconsiderado na recuperação. |
| **Tipo de Acesso** | Realiza o filtro pela forma no qual foi realizado o acesso, para caso tenha sido um Solucionador ou Web Service. Caso a opção Todos seja selecionada, serão exibidos os registros de ambas as opções. |

## Saídas

Após informar os parâmetros de recuperação clique no botão Consultar para visualizar o conteúdo do relatório.

Inicialmente, é apresentado um gráfico com a quantidade de acessos de acordo com o horário.

O eixo horizontal representa o horário em que foram realizados os acessos, enquanto o eixo vertical representa a quantidade de acessos. Neste gráfico, há duas barras, onde a verde indica a quantidade de acessos realizados com sucesso, enquanto a vermelha indica os acessos bloqueados por exceder o limite de usuários licenciados.

Acessos realizados de acordo com horário

No segundo gráfico, podemos observar a evolução da quantidade de acessos realizados diariamente:

Evolução da quantidade de acessos

Ao final do relatório, é exibida uma listagem de todos os acessos realizados detalhadamente, de acordo com o filtro selecionado nos parâmetros. Note que nesta listagem também são exibidos os acessos que foram bloqueados.

Listagem de acessos realizados
