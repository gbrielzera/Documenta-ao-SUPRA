# Id

Caminho: Customização > Modelo de objetos > Processo > Apontamento > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Apontamento

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade Id
apontamento.Id = 1;
# salva modificação da propriedade Id
Apontamento.Salva(apontamento)
```
