# DataInicio

Caminho: Customização > Modelo de objetos > Processo > PlanoGestao > DataInicio

Data de início do plano. Quando modificado é atualizada a coleção de períodos de todos os Indicadores associados ao plano.

**Exemplo 1: modificação da propriedade DataInicio**

```
# carrega objeto PlanoGestao de identificador 1
planoGestao = PlanoGestao.Carrega(1)
# modifica a propriedade DataInicio
planoGestao.DataInicio = DateTime;
# salva modificação da propriedade DataInicio
PlanoGestao.Salva(planoGestao)
```
