# Id

Caminho: Customização > Modelo de objetos > Recurso > Contrato > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Contrato

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade Id
contrato.Id = 1;
# salva modificação da propriedade Id
Contrato.Salva(contrato)
```
