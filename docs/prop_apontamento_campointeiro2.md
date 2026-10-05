# CampoInteiro2

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoInteiro2

Campo opcional do tipo Inteiro de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoInteiro2**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoInteiro2
apontamento.CampoInteiro2 = 1;
# salva modificação da propriedade CampoInteiro2
Apontamento.Salva(apontamento)
```
