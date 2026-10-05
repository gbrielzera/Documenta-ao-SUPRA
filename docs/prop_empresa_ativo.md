# Ativo

Caminho: Customização > Modelo de objetos > Recurso > Empresa > Ativo

Indica que a Empresa está ativa

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Empresa de identificador 1
empresa = Empresa.Carrega(1)
# modifica a propriedade Ativo
empresa.Ativo = true;
# salva modificação da propriedade Ativo
Empresa.Salva(empresa)
```
