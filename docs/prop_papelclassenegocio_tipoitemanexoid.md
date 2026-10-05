# TipoItemAnexoId

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > TipoItemAnexoId

Identificador do Tipo de Item de Configuração

**Exemplo 1: modificação da propriedade TipoItemAnexoId**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade TipoItemAnexoId
papelClasseNegocio.TipoItemAnexoId = 1;
# salva modificação da propriedade TipoItemAnexoId
PapelClasseNegocio.Salva(papelClasseNegocio)
```
