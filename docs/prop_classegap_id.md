# Id

Caminho: Customização > Modelo de objetos > Processo > ClasseGap > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um ClasseGAP

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ClasseGap de identificador 1
classeGap = ClasseGap.Carrega(1)
# modifica a propriedade Id
classeGap.Id = 1;
# salva modificação da propriedade Id
ClasseGap.Salva(classeGap)
```
