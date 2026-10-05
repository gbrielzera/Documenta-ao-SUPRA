# FiltroEmpresa

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroEmpresa

Relação de empresas onde estão lotadas as pessoas que serão recuperadas

**Exemplo 1: modificação da propriedade FiltroEmpresa**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroEmpresa
papelClasseNegocio.FiltroEmpresa = "Empresas";
# salva modificação da propriedade FiltroEmpresa
PapelClasseNegocio.Salva(papelClasseNegocio)
```
