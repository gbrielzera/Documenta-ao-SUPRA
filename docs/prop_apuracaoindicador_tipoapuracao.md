# TipoApuracao

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > TipoApuracao

Tipo de dado Apurado.

**Exemplo 1: modificação da propriedade TipoApuracao**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade TipoApuracao
apuracaoIndicador.TipoApuracao = "TotalFinalizado";
# salva modificação da propriedade TipoApuracao
ApuracaoIndicador.Salva(apuracaoIndicador)
```
