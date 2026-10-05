# MacroProcessoId

Caminho: Customização > Modelo de objetos > Processo > Processo > MacroProcessoId

Identificador do MacroProcesso associado

**Exemplo 1: modificação da propriedade MacroProcessoId**

```
# carrega objeto Processo de identificador 1
processo = Processo.Carrega(1)
# modifica a propriedade MacroProcessoId
processo.MacroProcessoId = 1;
# salva modificação da propriedade MacroProcessoId
Processo.Salva(processo)
```
