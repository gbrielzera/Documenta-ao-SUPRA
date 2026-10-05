# CampoBooleano2

Caminho: Customização > Modelo de objetos > Processo > Apontamento > CampoBooleano2

Campo opcional do tipo Booleano de índice 2. A semântica e descrição deste campo são definidas na Classe de Apontamento.

**Exemplo 1: modificação da propriedade CampoBooleano2**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade CampoBooleano2
apontamento.CampoBooleano2 = true;
# salva modificação da propriedade CampoBooleano2
Apontamento.Salva(apontamento)
```
