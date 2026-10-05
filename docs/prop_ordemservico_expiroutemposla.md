# ExpirouTempoSLA

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ExpirouTempoSLA

Indica que o tempo determinado para entrega do serviço foi vencido. Todos os níveis tiveram o seu tempo vencido sem que ocorresse resolução do incidente ou atendimento.

**Exemplo 1: modificação da propriedade ExpirouTempoSLA**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ExpirouTempoSLA
ordemServico.ExpirouTempoSLA = true;
# salva modificação da propriedade ExpirouTempoSLA
OrdemServico.Salva(ordemServico)
```
