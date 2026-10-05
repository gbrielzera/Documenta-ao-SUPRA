# PesquisaFiltroAndamento

Caminho: Customização > Modelo de objetos > Processo > Indicador > PesquisaFiltroAndamento

Seleciona Pesquisas de Satisfação não respondidas

**Exemplo 1: modificação da propriedade PesquisaFiltroAndamento**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade PesquisaFiltroAndamento
indicador.PesquisaFiltroAndamento = true;
# salva modificação da propriedade PesquisaFiltroAndamento
Indicador.Salva(indicador)
```
