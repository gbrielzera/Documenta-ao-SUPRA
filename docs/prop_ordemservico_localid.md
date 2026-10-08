# Propriedade LocalId

Caminho: Propriedade LocalId

Identificador do Local de Atendimento do Cliente

**Exemplo 1: modificação da propriedade LocalId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade LocalId
ordemServico.LocalId = 1;
# salva modificação da propriedade LocalId
OrdemServico.Salva(ordemServico)
```
