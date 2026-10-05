# Id

Caminho: Customização > Modelo de objetos > Processo > Operacao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma Operacao

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Operacao de identificador 1
operacao = Operacao.Carrega(1)
# modifica a propriedade Id
operacao.Id = 1;
# salva modificação da propriedade Id
Operacao.Salva(operacao)
```
