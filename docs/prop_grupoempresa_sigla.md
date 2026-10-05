# Sigla

Caminho: Customização > Modelo de objetos > Recurso > GrupoEmpresa > Sigla

Nome resumido utilizado para identificar um Grupo Empresarial.

**Exemplo 1: modificação da propriedade Sigla**

```
# carrega objeto GrupoEmpresa de identificador 1
grupoEmpresa = GrupoEmpresa.Carrega(1)
# modifica a propriedade Sigla
grupoEmpresa.Sigla = "VENKI";
# salva modificação da propriedade Sigla
GrupoEmpresa.Salva(grupoEmpresa)
```
