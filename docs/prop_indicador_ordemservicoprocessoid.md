# OrdemServicoProcessoId

Caminho: Customização > Modelo de objetos > Processo > Indicador > OrdemServicoProcessoId

Identificador do Processo associado

**Exemplo 1: modificação da propriedade OrdemServicoProcessoId**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade OrdemServicoProcessoId
indicador.OrdemServicoProcessoId = 1;
# salva modificação da propriedade OrdemServicoProcessoId
Indicador.Salva(indicador)
```
