# PesquisaTipoApuracao

Caminho: Customização > Modelo de objetos > Processo > Indicador > PesquisaTipoApuracao

Tipo de Apuração para Pesquisas de Satisfação.

**Exemplo 1: modificação da propriedade PesquisaTipoApuracao**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade PesquisaTipoApuracao
indicador.PesquisaTipoApuracao = "Pesquisa";
# salva modificação da propriedade PesquisaTipoApuracao
Indicador.Salva(indicador)
```
