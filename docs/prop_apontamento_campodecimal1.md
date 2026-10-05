# CampoDecimal1

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoDecimal1

Campo opcional do tipo Decimal de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoDecimal1**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoDecimal1
apontamento.CampoDecimal1 = 0;
# salva modificação da propriedade CampoDecimal1
Apontamento.Salva(apontamento)
```
