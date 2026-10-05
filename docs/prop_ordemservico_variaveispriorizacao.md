# VariaveisPriorizacao

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > VariaveisPriorizacao

Valores utilizados nas variáveis de Priorização.

**Exemplo 1: modificação da propriedade VariaveisPriorizacao**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade VariaveisPriorizacao
ordemServico.VariaveisPriorizacao = "Valores variáveis priorização";
# salva modificação da propriedade VariaveisPriorizacao
OrdemServico.Salva(ordemServico)
```
