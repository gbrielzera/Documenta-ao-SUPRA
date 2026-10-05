# Id

Caminho: Customização > Modelo de objetos > Processo > Apropriacao > Id

Identificador da Apropriação

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto Apropriacao de identificador 1
apropriacao = Apropriacao.Carrega(1)
# modifica a propriedade Id
apropriacao.Id = 1;
# salva modificação da propriedade Id
Apropriacao.Salva(apropriacao)
```
