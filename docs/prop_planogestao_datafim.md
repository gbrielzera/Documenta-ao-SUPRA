# DataFim

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao > DataFim

Data fim do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano.

**Exemplo 1: modificação da propriedade DataFim**

```
# carrega objeto PlanoGestao de identificador 1
planoGestao = PlanoGestao.Carrega(1)
# modifica a propriedade DataFim
planoGestao.DataFim = DateTime;
# salva modificação da propriedade DataFim
PlanoGestao.Salva(planoGestao)
```
