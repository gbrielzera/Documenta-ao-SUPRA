# GrupoEmpresas

Caminho: Customização > Modelo de objetos > Recurso > Empresa > GrupoEmpresas

Grupo Empresarial que controla a Empresa

**Exemplo 1: modificação da propriedade GrupoEmpresas**

```
# carrega objeto Empresa de identificador 51
empresa = Empresa.Carrega(51)
# modifica a propriedade GrupoEmpresas
empresa.GrupoEmpresas = GrupoEmpresa.Carrega(94);
# salva modificação da propriedade GrupoEmpresas
Empresa.Salva(empresa)
```
