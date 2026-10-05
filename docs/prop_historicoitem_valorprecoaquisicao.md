# ValorPrecoAquisicao

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > ValorPrecoAquisicao

Valor do Preço de aquisição do Item na ocasição da apuração de charge-back.

**Exemplo 1: modificação da propriedade ValorPrecoAquisicao**

```
# carrega objeto HistoricoItem de identificador 1
historicoItem = HistoricoItem.Carrega(1)
# modifica a propriedade ValorPrecoAquisicao
historicoItem.ValorPrecoAquisicao = 0;
# salva modificação da propriedade ValorPrecoAquisicao
HistoricoItem.Salva(historicoItem)
```
