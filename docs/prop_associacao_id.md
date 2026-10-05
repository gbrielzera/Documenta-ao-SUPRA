# Id

Caminho: Customização > Modelo de objetos > Processo > Associacao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma Associacao

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade Id
associacao.Id = 1;
# salva modificação da propriedade Id
Associacao.Salva(associacao)
```
