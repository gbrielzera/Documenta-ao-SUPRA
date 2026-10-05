# CampoString1

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoString1

Campo opcional do tipo String de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoString1**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoString1
apontamento.CampoString1 = "Campo string 1";
# salva modificação da propriedade CampoString1
Apontamento.Salva(apontamento)
```
