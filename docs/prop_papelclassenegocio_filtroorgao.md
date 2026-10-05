# FiltroOrgao

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroOrgao

Relação de órgãos onde estão lotadas as pessoas para recuperação

**Exemplo 1: modificação da propriedade FiltroOrgao**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroOrgao
papelClasseNegocio.FiltroOrgao = "Órgãos";
# salva modificação da propriedade FiltroOrgao
PapelClasseNegocio.Salva(papelClasseNegocio)
```
