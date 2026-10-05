# ItemSLA

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ItemSLA

Critério de atendimento escolhido no Acordo de Nível de Serviço estabelecido com a área do Cliente

**Exemplo 1: modificação da propriedade ItemSLA**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade ItemSLA
ordemServico.ItemSLA = ItemSLA.Carrega(23);
# salva modificação da propriedade ItemSLA
OrdemServico.Salva(ordemServico)
```
