# PesquisaClassePesquisa

Caminho: Customização > Modelo de objetos > Processo > Indicador > PesquisaClassePesquisa

Tipo de pesquisa de satisfação que será considerada no cálculo do indicador.

**Exemplo 1: modificação da propriedade PesquisaClassePesquisa**

```
# carrega objeto Indicador de identificador 78
indicador = Indicador.Carrega(78)
# modifica a propriedade PesquisaClassePesquisa
indicador.PesquisaClassePesquisa = ClassePesquisaSatisfacao.Carrega(23);
# salva modificação da propriedade PesquisaClassePesquisa
Indicador.Salva(indicador)
```
