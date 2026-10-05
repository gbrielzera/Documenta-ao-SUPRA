# Descricao

Caminho: Customização > Modelo de objetos > Processo > MacroProcesso > Descricao

Descrição detalhada do MacroProcesso

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto MacroProcesso de identificador 1
macroProcesso = MacroProcesso.Carrega(1)
# modifica a propriedade Descricao
macroProcesso.Descricao = "Descrição";
# salva modificação da propriedade Descricao
MacroProcesso.Salva(macroProcesso)
```
