# CampoDecimal2

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoDecimal2

Campo opcional do tipo Decimal de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoDecimal2**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoDecimal2
apontamento.CampoDecimal2 = 0;
# salva modificação da propriedade CampoDecimal2
Apontamento.Salva(apontamento)
```
