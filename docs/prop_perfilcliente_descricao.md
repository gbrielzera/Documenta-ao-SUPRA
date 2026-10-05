# Descricao

Caminho: Customização > Modelo de objetos > Recurso > PerfilCliente > Descricao

Texto que descreve claramente a utilização de um Perfil de Cliente. Este texto é utilizado na tela de Cadastro de Clientes para associação de Perfil com Cliente e também na tela de Ordem de Serviço para informar ao Solucionador o privilégio conferido.

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto PerfilCliente de identificador 1
perfilCliente = PerfilCliente.Carrega(1)
# modifica a propriedade Descricao
perfilCliente.Descricao = "Descrição";
# salva modificação da propriedade Descricao
PerfilCliente.Salva(perfilCliente)
```
