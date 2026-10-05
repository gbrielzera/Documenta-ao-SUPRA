# PerfilCliente

Caminho: Customização > Modelo de objetos > Recurso > Pessoa > PerfilCliente

Perfil especial concedido a um Cliente para atendimento diferenciado

**Exemplo 1: modificação da propriedade PerfilCliente**

```
# carrega objeto Pessoa de identificador 51
pessoa = Pessoa.Carrega(51)
# modifica a propriedade PerfilCliente
pessoa.PerfilCliente = PerfilCliente.Carrega(94);
# salva modificação da propriedade PerfilCliente
Pessoa.Salva(pessoa)
```
