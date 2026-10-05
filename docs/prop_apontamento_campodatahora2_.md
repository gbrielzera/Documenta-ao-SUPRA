# CampoDataHora2

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoDataHora2

Campo opcional do tipo Data/Hora de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoDataHora2**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoDataHora2
apontamento.CampoDataHora2 = DateTime;
# salva modificação da propriedade CampoDataHora2
Apontamento.Salva(apontamento)
```
