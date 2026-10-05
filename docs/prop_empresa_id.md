# Id

Caminho: Customização > Modelo de objetos > Recurso > Empresa > Id

Número sequencial gerado por sistema para identificar uma Empresa

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Empresa de identificador 1
empresa = Empresa.Carrega(1)
# modifica a propriedade Id
empresa.Id = 1;
# salva modificação da propriedade Id
Empresa.Salva(empresa)
```
