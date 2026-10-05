# Id

Caminho: Customização > Modelo de objetos > Recurso > GrupoEmpresa > Id

Número sequencial gerado por sistema para Identificar um Grupo Empresarial

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto GrupoEmpresa de identificador 1
grupoEmpresa = GrupoEmpresa.Carrega(1)
# modifica a propriedade Id
grupoEmpresa.Id = 1;
# salva modificação da propriedade Id
GrupoEmpresa.Salva(grupoEmpresa)
```
