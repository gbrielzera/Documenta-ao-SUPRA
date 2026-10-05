# Descricao

Caminho: Customização > Modelo de objetos > Recurso > Empresa > Descricao

Nome da Empresa

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Empresa de identificador 1
empresa = Empresa.Carrega(1)
# modifica a propriedade Descricao
empresa.Descricao = "Venki Tecnologia";
# salva modificação da propriedade Descricao
Empresa.Salva(empresa)
```
