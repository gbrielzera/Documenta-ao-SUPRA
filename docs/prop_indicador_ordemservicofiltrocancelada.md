# OrdemServicoFiltroCancelada

Caminho: Customização > Modelo de objetos > Processo > Indicador > OrdemServicoFiltroCancelada

Seleciona Ordens de Serviço Canceladas no Período de apuração do Indicador

**Exemplo 1: modificação da propriedade OrdemServicoFiltroCancelada**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade OrdemServicoFiltroCancelada
indicador.OrdemServicoFiltroCancelada = true;
# salva modificação da propriedade OrdemServicoFiltroCancelada
Indicador.Salva(indicador)
```
