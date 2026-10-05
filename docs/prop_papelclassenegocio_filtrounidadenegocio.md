# FiltroUnidadeNegocio

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroUnidadeNegocio

Relação de Unidades de negócio onde estão localizadas as pessoas que serão recuperadas

**Exemplo 1: modificação da propriedade FiltroUnidadeNegocio**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroUnidadeNegocio
papelClasseNegocio.FiltroUnidadeNegocio = "Unidades de negócio";
# salva modificação da propriedade FiltroUnidadeNegocio
PapelClasseNegocio.Salva(papelClasseNegocio)
```
