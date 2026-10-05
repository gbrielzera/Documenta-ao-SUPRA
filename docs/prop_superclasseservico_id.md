# Id

Caminho: Customização > Modelo de objetos > Processo > SuperClasseServico > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma ClasseServico

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto SuperClasseServico de identificador 1
superClasseServico = SuperClasseServico.Carrega(1)
# modifica a propriedade Id
superClasseServico.Id = 1;
# salva modificação da propriedade Id
SuperClasseServico.Salva(superClasseServico)
```
