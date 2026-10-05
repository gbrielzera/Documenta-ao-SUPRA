# Id

Caminho: Customização > Modelo de objetos > Ativos > Modelo > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Modelo

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Modelo de identificador 1
modelo = Modelo.Carrega(1)
# modifica a propriedade Id
modelo.Id = 1;
# salva modificação da propriedade Id
Modelo.Salva(modelo)
```
