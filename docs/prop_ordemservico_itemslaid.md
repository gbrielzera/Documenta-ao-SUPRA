# ItemSLAId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ItemSLAId

Identificador do critério de atendimento escolhido no Acordo de Nível de Serviço estabelecido com a área do Cliente

**Exemplo 1: modificação da propriedade ItemSLAId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ItemSLAId
ordemServico.ItemSLAId = 1;
# salva modificação da propriedade ItemSLAId
OrdemServico.Salva(ordemServico)
```
