# EmpresaId

Caminho: Customização > Modelo de objetos > Recurso > UnidadeNegocio > EmpresaId

Identificador da Empresa associada

**Exemplo 1: modificação da propriedade EmpresaId**

```
# carrega objeto UnidadeNegocio de identificador 1
unidadeNegocio = UnidadeNegocio.Carrega(1)
# modifica a propriedade EmpresaId
unidadeNegocio.EmpresaId = 1;
# salva modificação da propriedade EmpresaId
UnidadeNegocio.Salva(unidadeNegocio)
```
