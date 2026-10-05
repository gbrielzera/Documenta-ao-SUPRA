# ScriptSelecaoAtores

Caminho: Customização > Modelo de objetos > Processo > PapelClasseNegocio > ScriptSelecaoAtores

Script para seleção de Atores de um Papel de Processo

**Exemplo 1: modificação da propriedade ScriptSelecaoAtores**

```
# carrega objeto PapelClasseNegocio de identificador 1
papelClasseNegocio = PapelClasseNegocio.Carrega(1)
# modifica a propriedade ScriptSelecaoAtores
papelClasseNegocio.ScriptSelecaoAtores = "Script Seleção Atores";
# salva modificação da propriedade ScriptSelecaoAtores
PapelClasseNegocio.Salva(papelClasseNegocio)
```
