# PerfilClienteId

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > PerfilClienteId

Identificador do(a) PerfilCliente associado(a)

**Exemplo 1: modificação da propriedade PerfilClienteId**

```
# carrega objeto Pessoa de identificador 1
pessoa = Pessoa.Carrega(1)
# modifica a propriedade PerfilClienteId
pessoa.PerfilClienteId = 1;
# salva modificação da propriedade PerfilClienteId
Pessoa.Salva(pessoa)
```
