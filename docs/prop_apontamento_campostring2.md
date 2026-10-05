# CampoString2

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoString2

Campo opcional do tipo String de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoString2**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoString2
apontamento.CampoString2 = "Campo string 2";
# salva modificação da propriedade CampoString2
Apontamento.Salva(apontamento)
```
