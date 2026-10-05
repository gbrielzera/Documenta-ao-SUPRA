# Id

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > Id

Número sequencial gerado automaticamente pelo sistema para identificar uma Pessoa.

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade Id
pessoa.Id = 1;
# salva modificação da propriedade Id
Pessoa.Salva(pessoa)
```
