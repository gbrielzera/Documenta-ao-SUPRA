# PlanoGestaoId

Caminho: Customização > Modelo de objetos > Recurso > Contrato > PlanoGestaoId

Identificador do Plano de Gestão

**Exemplo 1: modificação da propriedade PlanoGestaoId**

```
# carrega objeto Contrato de identificador 1
contrato = Contrato.Carrega(1)
# modifica a propriedade PlanoGestaoId
contrato.PlanoGestaoId = 1;
# salva modificação da propriedade PlanoGestaoId
Contrato.Salva(contrato)
```
