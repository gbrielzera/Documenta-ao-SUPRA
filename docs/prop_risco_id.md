# Id

Caminho: Customização > Modelo de objetos > Processo > Risco > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Risco

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Risco de identificador 1
risco = Risco.Carrega(1)
# modifica a propriedade Id
risco.Id = 1;
# salva modificação da propriedade Id
Risco.Salva(risco)
```
