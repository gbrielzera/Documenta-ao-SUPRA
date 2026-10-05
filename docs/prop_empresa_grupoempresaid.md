# GrupoEmpresaId

Caminho: Customização > Modelo de objetos > Recurso > Empresa > GrupoEmpresaId

Identificador do Grupo de Empresas ao qual pertence a Empresa

**Exemplo 1: modificação da propriedade GrupoEmpresaId**

```
# carrega objeto Empresa de identificador 1
empresa = Empresa.Carrega(1)
# modifica a propriedade GrupoEmpresaId
empresa.GrupoEmpresaId = 1;
# salva modificação da propriedade GrupoEmpresaId
Empresa.Salva(empresa)
```
