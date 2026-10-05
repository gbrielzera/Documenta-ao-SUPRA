# FiltroCustomizados

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > FiltroCustomizados

Relação de campos customizados do cadastro de Pessoas utilizados como filtro para recuperação

**Exemplo 1: modificação da propriedade FiltroCustomizados**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade FiltroCustomizados
papelClasseNegocio.FiltroCustomizados = "Campos customizados";
# salva modificação da propriedade FiltroCustomizados
PapelClasseNegocio.Salva(papelClasseNegocio)
```
