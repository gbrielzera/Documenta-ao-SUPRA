# Descricao

Caminho: Customização > Modelo de objetos > Recurso > GrupoEmpresa > Descricao

Nome do Grupo Empresarial

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto GrupoEmpresa de identificador 1
grupoEmpresa = GrupoEmpresa.Carrega(1)
# modifica a propriedade Descricao
grupoEmpresa.Descricao = "Grupo Venki";
# salva modificação da propriedade Descricao
GrupoEmpresa.Salva(grupoEmpresa)
```
