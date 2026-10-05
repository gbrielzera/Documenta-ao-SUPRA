# Id

Caminho: Customização > Modelo de objetos > Processo > MacroProcesso > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um MacroProcesso

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto MacroProcesso de identificador 1
macroProcesso = MacroProcesso.Carrega(1)
# modifica a propriedade Id
macroProcesso.Id = 1;
# salva modificação da propriedade Id
MacroProcesso.Salva(macroProcesso)
```
