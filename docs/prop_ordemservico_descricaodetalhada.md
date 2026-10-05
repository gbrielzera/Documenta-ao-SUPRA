# DescricaoDetalhada

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > DescricaoDetalhada

Descrição detalhada da solicitação do Cliente

**Exemplo 1: modificação da propriedade DescricaoDetalhada**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade DescricaoDetalhada
ordemServico.DescricaoDetalhada = "Descrição detalhada";
# salva modificação da propriedade DescricaoDetalhada
OrdemServico.Salva(ordemServico)
```
