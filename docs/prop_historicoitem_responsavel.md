# Responsavel

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > Responsavel

Responsável pelo Ativo

**Exemplo 1: modificação da propriedade Responsavel**

```
# carrega objeto HistoricoItem de identificador 51
historicoItem = HistoricoItem.Carrega(51)
# modifica a propriedade Responsavel
historicoItem.Responsavel = Pessoa.Carrega(94);
# salva modificação da propriedade Responsavel
HistoricoItem.Salva(historicoItem)
```
