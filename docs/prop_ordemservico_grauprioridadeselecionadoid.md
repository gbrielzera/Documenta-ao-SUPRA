# GrauPrioridadeSelecionadoId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > GrauPrioridadeSelecionadoId

Identificador do Grau de Prioridade selecionado

**Exemplo 1: modificação da propriedade GrauPrioridadeSelecionadoId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade GrauPrioridadeSelecionadoId
ordemServico.GrauPrioridadeSelecionadoId = 1;
# salva modificação da propriedade GrauPrioridadeSelecionadoId
OrdemServico.Salva(ordemServico)
```
