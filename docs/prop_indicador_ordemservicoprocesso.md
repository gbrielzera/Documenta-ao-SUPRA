# OrdemServicoProcesso

Caminho: Customização > Modelo de objetos > Processo > Indicador > OrdemServicoProcesso

Seleciona Ordens de Serviço do Processo

**Exemplo 1: modificação da propriedade OrdemServicoProcesso**

```
# carrega objeto Indicador de identificador 78
indicador = Indicador.Carrega(78)
# modifica a propriedade OrdemServicoProcesso
indicador.OrdemServicoProcesso = Processo.Carrega(23);
# salva modificação da propriedade OrdemServicoProcesso
Indicador.Salva(indicador)
```
