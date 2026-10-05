# SituacaoPesquisa

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > SituacaoPesquisa

Situação quanto ao Envio de Pesquisa de Satisfação

**Exemplo 1: modificação da propriedade SituacaoPesquisa**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade SituacaoPesquisa
ordemServico.SituacaoPesquisa = "PendenteEnvio";
# salva modificação da propriedade SituacaoPesquisa
OrdemServico.Salva(ordemServico)
```
