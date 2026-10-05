# Id

Caminho: Customização > Modelo de objetos > Processo > ModeloComunicado > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um ModeloComunicado

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto ModeloComunicado de identificador 1
modeloComunicado = ModeloComunicado.Carrega(1)
# modifica a propriedade Id
modeloComunicado.Id = 1;
# salva modificação da propriedade Id
ModeloComunicado.Salva(modeloComunicado)
```
