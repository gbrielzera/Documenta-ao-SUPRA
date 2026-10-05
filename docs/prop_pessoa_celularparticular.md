# CelularParticular

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > CelularParticular

Telefone Celular particular da Pessoa

**Exemplo 1: modificação da propriedade CelularParticular**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade CelularParticular
pessoa.CelularParticular = "9991-9393";
# salva modificação da propriedade CelularParticular
Pessoa.Salva(pessoa)
```
