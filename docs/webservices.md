# Objeto Webservices

Caminho: Recursos Avançados > Objeto Webservices

Webservice é uma solução utilizada na integração de sistemas e na comunicação entre aplicações diferentes. Com esta tecnologia é possível que novas aplicações possam interagir com aquelas que já existem e que sistemas desenvolvidos em plataformas diferentes sejam compatíveis. Os Web services são componentes que permitem às aplicações enviar e receber dados em formato XML. Cada aplicação pode ter a sua própria "linguagem", que é traduzida para uma linguagem universal, o formato XML.

Para as empresas, os Webservices podem trazer agilidade para os processos e eficiência na comunicação entre cadeias de produção ou de logística. Toda e qualquer comunicação entre sistemas passa a ser dinâmica e principalmente segura, pois não há intervenção humana.

Essencialmente, o Web Service faz com que os recursos da aplicação do software estejam disponíveis sobre a rede de uma forma normalizada. Utilizando a tecnologia Webservice, uma aplicação pode invocar outra para efetuar tarefas simples ou complexas, independente se as duas aplicações estiverem em diferentes sistemas e escritas em linguagens diferenciadas. Por outras palavras, os Web Services fazem com que os seus recursos estejam disponíveis para que qualquer aplicação cliente possa operar e extrair os recursos fornecidos pelo Web Service.

Para mais detalhes sobre esta tecnologia recomendamos a leitura da página [http://pt.wikipedia.org/wiki/Web_service](http://pt.wikipedia.org/wiki/Web_service).

## Utilizando Webservices no Supravizio

O recurso de webservices está disponível no mecanismo de scripts do Supravizio por meio do utilitário Utils.LoadWebService. No exemplo seguinte implementamos uma consulta no evento Script Início de uma tarefa de processo.

```
ws = WebService.LoadWebService("http://localhost:1186/ExemploWebService/Service.asmx")

result = ws.UsuariosDesligados(1)

resumo = "Usuários que estão desligados: "

for f in result:

    resumo = resumo + "m " + f

Utils.LogInformation(resumo, "WebService")
```

Na linha 1 estamos criando um objeto WebService Client, que aponta para URL do usuário que está criando o objeto.

Na linha 2 estamos fazendo a chamada ao método remoto chamado UsuariosDesligados, este método foi implementado em um WebService e recebe como parâmetro o ID da área e retorna uma lista de usuários contendo apenas o ‘Usuário de Rede’ do desligado.

Da linha 3 a linha 5 criamos um pequeno texto, para exibir como exemplo, neste ponto o usuário pode definir sua lógica.

E na linha 6 estamos exibindo a informação.

O resultado desta execução foi:

Da mesma forma que consultamos, podemos executar qualquer rotina fora do Supravizio e retornar as informações de execução para a ferramenta, e para a Ordem de Serviço.
