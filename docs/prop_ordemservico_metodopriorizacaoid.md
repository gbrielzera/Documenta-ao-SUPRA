# MetodoPriorizacaoId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > MetodoPriorizacaoId

Identificador do MetodoPriorizacao associado

**Exemplo 1: modificação da propriedade MetodoPriorizacaoId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade MetodoPriorizacaoId
ordemServico.MetodoPriorizacaoId = 1;
# salva modificação da propriedade MetodoPriorizacaoId
OrdemServico.Salva(ordemServico)
```
