# OrdemServicoFiltroFinalizadaFalha

Caminho: Customização > Modelo de objetos > Processo > Indicador > OrdemServicoFiltroFinalizadaFalha

Seleciona Ordens de Serviço Finalizadas como Falha no Período de apuração do Indicador.

**Exemplo 1: modificação da propriedade OrdemServicoFiltroFinalizadaFalha**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade OrdemServicoFiltroFinalizadaFalha
indicador.OrdemServicoFiltroFinalizadaFalha = true;
# salva modificação da propriedade OrdemServicoFiltroFinalizadaFalha
Indicador.Salva(indicador)
```
