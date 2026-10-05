# OrdemServicoFiltroFinalizadaNReal

Caminho: Customização > Modelo de objetos > Processo > Indicador > OrdemServicoFiltroFinalizadaNReal

Seleciona Ordens de Serviço Finalizadas como Não-realizada no Período de apuração do Indicador.

**Exemplo 1: modificação da propriedade OrdemServicoFiltroFinalizadaNReal**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade OrdemServicoFiltroFinalizadaNReal
indicador.OrdemServicoFiltroFinalizadaNReal = true;
# salva modificação da propriedade OrdemServicoFiltroFinalizadaNReal
Indicador.Salva(indicador)
```
