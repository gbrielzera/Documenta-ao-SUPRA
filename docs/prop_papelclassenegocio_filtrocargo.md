# FiltroCargo

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroCargo

Permite a recuperação pelo preenchimento do campo Cargo.

**Exemplo 1: modificação da propriedade FiltroCargo**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroCargo
papelClasseNegocio.FiltroCargo = "Cargo";
# salva modificação da propriedade FiltroCargo
PapelClasseNegocio.Salva(papelClasseNegocio)
```
