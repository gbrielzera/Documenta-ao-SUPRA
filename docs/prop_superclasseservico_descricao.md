# Descricao

Caminho: Customização > Modelo de objetos > Processo > SuperClasseServico > Descricao

Descrição detalhada da ClasseServico

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto SuperClasseServico de identificador 1
superClasseServico = SuperClasseServico.Carrega(1)
# modifica a propriedade Descricao
superClasseServico.Descricao = "Descrição";
# salva modificação da propriedade Descricao
SuperClasseServico.Salva(superClasseServico)
```
