# CriterioSelecao

Caminho: Customização > Modelo de objetos > Processo > TesteControle > CriterioSelecao

Critério de seleção utilizado na realização do Teste

**Exemplo 1: modificação da propriedade CriterioSelecao**

```
# carrega objeto TesteControle de identificador 1
testeControle = TesteControle.Carrega(1)
# modifica a propriedade CriterioSelecao
testeControle.CriterioSelecao = "Critério seleção";
# salva modificação da propriedade CriterioSelecao
TesteControle.Salva(testeControle)
```
