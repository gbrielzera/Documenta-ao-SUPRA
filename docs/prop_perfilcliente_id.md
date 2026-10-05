# Id

Caminho: Customização > Modelo de objetos > Recurso > PerfilCliente > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um Perfil de Cliente

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto PerfilCliente de identificador 1
perfilCliente = PerfilCliente.Carrega(1)
# modifica a propriedade Id
perfilCliente.Id = 1;
# salva modificação da propriedade Id
PerfilCliente.Salva(perfilCliente)
```
