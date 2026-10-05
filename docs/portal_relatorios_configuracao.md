# Configurando o Módulo

Caminho: Guia para Administradores > Portal de Processos > Módulos > Módulo de Publicação de Relatórios > Configurando o Módulo

Para este módulo, podem ser configurados os seguintes parâmetros:

Configurador do módulo

Iremos realizar a publicação de um relatório para melhor exemplificar o uso desta tela.

Primeiramente, criamos um relatório do tipo "Fornecimento de voucher de taxi nos últimos 30 dias" e passamos o parâmetro CentroCusto como invisível.

A marcação da propriedade Exibir barra de ferramentas habilita a exibição da barra superior no relatório, conforme indica a figura abaixo:

Barra de Ferramentas no Relatório

A opção paginação indica se o relatório será dividido em páginas ou será contínuo.

Neste exemplo, deixamos as duas habilitadas.

Na aba script, inserimos um valor fixo para o parâmetro, a estrutura do script deve ser a seguinte:

```
Parametros["NomedoParametro"] = "Valor"
```

Exemplo de script para definição de parâmetro

Salvamos as alterações e fechamos a aba. Acessando a tela do relatório, notamos que o parâmetro Centro de Custo já não está mais visível e ao realizar a consulta, podemos ver que o parâmetro consulta é exatamente o mesmo que inserimos no script.

Relatório gerado com parâmetro pré-definido no script

## Recebendo parâmetros através do link da página

O módulo de Relatórios também permite receber parâmetros através da Query String da página, como por exemplo, em links recebidos em comunicados. Para isso, é necessário configurarmos o módulo para receber o valor como parâmetro para o relatório.

Script na configuração do módulo

Deste modo, o relatório poderá receber o valor presente no link como parâmetro.

Parâmetros recebidos através do Query String
