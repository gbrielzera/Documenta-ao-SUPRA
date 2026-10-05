# CampoDataHora1

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoDataHora1

Campo opcional do tipo Data/Hora de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoDataHora1**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoDataHora1
apontamento.CampoDataHora1 = DateTime;
# salva modificação da propriedade CampoDataHora1
Apontamento.Salva(apontamento)
```
