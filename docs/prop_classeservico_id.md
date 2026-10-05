# Id

Caminho: Customização > Modelo de objetos > Processo > ClasseServico > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma Classe de Servico

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ClasseServico de identificador 1
classeServico = ClasseServico.Carrega(1)
# modifica a propriedade Id
classeServico.Id = 1;
# salva modificação da propriedade Id
ClasseServico.Salva(classeServico)
```
