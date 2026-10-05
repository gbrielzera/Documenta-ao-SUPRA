# Id

Caminho: Customização > Modelo de objetos > Utilitários > Global > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Global

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Global de identificador 1
global = Global.Carrega(1)
# modifica a propriedade Id
global.Id = 1;
# salva modificação da propriedade Id
Global.Salva(global)
```
