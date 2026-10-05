# FavorecidoId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > FavorecidoId

Identificador do Favorecido

**Exemplo 1: modificação da propriedade FavorecidoId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade FavorecidoId
ordemServico.FavorecidoId = 1;
# salva modificação da propriedade FavorecidoId
OrdemServico.Salva(ordemServico)
```
