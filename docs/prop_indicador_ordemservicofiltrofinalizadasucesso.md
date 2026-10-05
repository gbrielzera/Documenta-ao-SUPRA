# OrdemServicoFiltroFinalizadaSucesso

Caminho: Customização > Modelo de objetos > Processo > Indicador > OrdemServicoFiltroFinalizadaSucesso

Seleciona Ordens de Serviço Finalizadas como Sucesso no Período de apuração do Indicador. Para determinar a finalização no período é utilizada a Data/hora de Execução de Mudança.

**Exemplo 1: modificação da propriedade OrdemServicoFiltroFinalizadaSucesso**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade OrdemServicoFiltroFinalizadaSucesso
indicador.OrdemServicoFiltroFinalizadaSucesso = true;
# salva modificação da propriedade OrdemServicoFiltroFinalizadaSucesso
Indicador.Salva(indicador)
```
