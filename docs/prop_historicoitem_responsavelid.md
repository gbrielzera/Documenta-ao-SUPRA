# ResponsavelId

Caminho: Customização > Modelo de objetos > Recurso > HistoricoItem > ResponsavelId

Identificador do Responsável pelo Ativo na ocasião da apuração do Charge-back.

**Exemplo 1: modificação da propriedade ResponsavelId**

```
# carrega objeto HistoricoItem de identificador 1
historicoItem = HistoricoItem.Carrega(1)
# modifica a propriedade ResponsavelId
historicoItem.ResponsavelId = 1;
# salva modificação da propriedade ResponsavelId
HistoricoItem.Salva(historicoItem)
```
