# NivelSLAId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > NivelSLAId

Identificador da NivelSLA associada

**Exemplo 1: modificação da propriedade NivelSLAId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade NivelSLAId
ordemServico.NivelSLAId = 1;
# salva modificação da propriedade NivelSLAId
OrdemServico.Salva(ordemServico)
```
