# ControleId

Caminho: Customização > Modelo de objetos > Processo > TesteControle > ControleId

Identificador do(a) Controle associado(a)

**Exemplo 1: modificação da propriedade ControleId**

```
# carrega objeto TesteControle de identificador 1
testeControle = TesteControle.Carrega(1)
# modifica a propriedade ControleId
testeControle.ControleId = 1;
# salva modificação da propriedade ControleId
TesteControle.Salva(testeControle)
```
