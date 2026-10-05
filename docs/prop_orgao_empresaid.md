# EmpresaId

Caminho: Customização > Modelo de objetos > Recurso > Orgao > EmpresaId

Identificador da Empresa dona do Órgão.

**Exemplo 1: modificação da propriedade EmpresaId**

```
# carrega objeto Orgao de identificador 1
orgao = Orgao.Carrega(1)
# modifica a propriedade EmpresaId
orgao.EmpresaId = 1;
# salva modificação da propriedade EmpresaId
Orgao.Salva(orgao)
```
