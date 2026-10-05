# CulturaClienteId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > CulturaClienteId

Identificador da Cultura preferencial do Cliente

**Exemplo 1: modificação da propriedade CulturaClienteId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade CulturaClienteId
pessoa.CulturaClienteId = 1;
# salva modificação da propriedade CulturaClienteId
Pessoa.Salva(pessoa)
```
