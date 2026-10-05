# CampoBooleano1

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoBooleano1

Campo opcional do tipo Booleano de índice 1. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoBooleano1**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoBooleano1
apontamento.CampoBooleano1 = true;
# salva modificação da propriedade CampoBooleano1
Apontamento.Salva(apontamento)
```
