# ComentarioAvaliador

Caminho: Customização > Modelo de objetos > Processo > Pesquisa > ComentarioAvaliador

Comentário gravado pelo Avalidador no instante em que a Pesquisa é respondida

**Exemplo 1: modificação da propriedade ComentarioAvaliador**

```
# carrega objeto Pesquisa de identificador 1
pesquisa = Pesquisa.Carrega(1)
# modifica a propriedade ComentarioAvaliador
pesquisa.ComentarioAvaliador = "Comentário avaliador";
# salva modificação da propriedade ComentarioAvaliador
Pesquisa.Salva(pesquisa)
```
