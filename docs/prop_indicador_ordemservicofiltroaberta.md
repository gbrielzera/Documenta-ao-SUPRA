# OrdemServicoFiltroAberta

Caminho: Customização > Modelo de objetos > Processo > Indicador > OrdemServicoFiltroAberta

Seleciona Ordens de Serviço Abertas no Período de apuração do Indicador

**Exemplo 1: modificação da propriedade OrdemServicoFiltroAberta**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade OrdemServicoFiltroAberta
indicador.OrdemServicoFiltroAberta = true;
# salva modificação da propriedade OrdemServicoFiltroAberta
Indicador.Salva(indicador)
```
