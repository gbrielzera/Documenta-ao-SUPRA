# TempoSLA

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > TempoSLA

Tempo em minutos para ANS.

**Exemplo 1: modificação da propriedade TempoSLA**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade TempoSLA
ordemServico.TempoSLA = 1;
# salva modificação da propriedade TempoSLA
OrdemServico.Salva(ordemServico)
```
