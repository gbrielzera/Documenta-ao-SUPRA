# CampoInteiro1

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoInteiro1

Campo opcional do tipo Inteiro de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoInteiro1**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoInteiro1
apontamento.CampoInteiro1 = 1;
# salva modificação da propriedade CampoInteiro1
Apontamento.Salva(apontamento)
```
