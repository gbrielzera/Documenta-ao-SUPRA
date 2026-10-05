# PlanoGestaoId

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > PlanoGestaoId

Identificador do Plano de Gestao associado

**Exemplo 1: modificação da propriedade PlanoGestaoId**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade PlanoGestaoId
acordoNivelServico.PlanoGestaoId = 1;
# salva modificação da propriedade PlanoGestaoId
AcordoNivelServico.Salva(acordoNivelServico)
```
