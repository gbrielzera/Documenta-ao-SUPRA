# ValorPrecoManutencao

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > ValorPrecoManutencao

Valor do Preço de manutenção do Item na ocasição da apuração de charge-back.

**Exemplo 1: modificação da propriedade ValorPrecoManutencao**

```
# carrega objeto HistoricoItem de identificador 1
historicoItem = HistoricoItem.Carrega(1)
# modifica a propriedade ValorPrecoManutencao
historicoItem.ValorPrecoManutencao = 0;
# salva modificação da propriedade ValorPrecoManutencao
HistoricoItem.Salva(historicoItem)
```
