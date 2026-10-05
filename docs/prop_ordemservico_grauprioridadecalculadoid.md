# GrauPrioridadeCalculadoId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > GrauPrioridadeCalculadoId

Identificador do Grau da Prioridade inicialmente definido para a Ordem de Serviço.

**Exemplo 1: modificação da propriedade GrauPrioridadeCalculadoId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade GrauPrioridadeCalculadoId
ordemServico.GrauPrioridadeCalculadoId = 1;
# salva modificação da propriedade GrauPrioridadeCalculadoId
OrdemServico.Salva(ordemServico)
```
