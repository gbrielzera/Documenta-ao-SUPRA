# MacroProcesso

Caminho: Customização > Modelo de objetos > Processo > Processo > MacroProcesso

Agrupamento de processos endereçados a uma área de negócio

**Exemplo 1: modificação da propriedade MacroProcesso**

```
# carrega objeto Processo de identificador 78
processo = Processo.Carrega(78)
# modifica a propriedade MacroProcesso
processo.MacroProcesso = MacroProcesso.Carrega(23);
# salva modificação da propriedade MacroProcesso
Processo.Salva(processo)
```
