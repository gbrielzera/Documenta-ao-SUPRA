# Id

Caminho: Customização > Modelo de objetos > Processo > Indicador > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Indicador. Este número não pode ser modificado pelo usuário.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade Id
indicador.Id = 1;
# salva modificação da propriedade Id
Indicador.Salva(indicador)
```
