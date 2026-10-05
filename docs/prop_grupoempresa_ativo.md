# Ativo

Caminho: Customização > Modelo de objetos > Recurso > GrupoEmpresa > Ativo

Indica que o Grupo Empresarial está Ativo.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto GrupoEmpresa de identificador 1
grupoEmpresa = GrupoEmpresa.Carrega(1)
# modifica a propriedade Ativo
grupoEmpresa.Ativo = true;
# salva modificação da propriedade Ativo
GrupoEmpresa.Salva(grupoEmpresa)
```
