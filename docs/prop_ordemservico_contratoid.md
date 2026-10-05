# ContratoId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ContratoId

Identificador do Contrato associado

**Exemplo 1: modificação da propriedade ContratoId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ContratoId
ordemServico.ContratoId = 1;
# salva modificação da propriedade ContratoId
OrdemServico.Salva(ordemServico)
```
