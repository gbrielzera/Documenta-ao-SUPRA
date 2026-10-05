# PlanoGestaoId

Caminho: Customização > Modelo de objetos > Processo > ApuracaoIndicador > PlanoGestaoId

Identificador do Plano de Gestão proprietário da apuração

**Exemplo 1: modificação da propriedade PlanoGestaoId**

```
# carrega objeto ApuracaoIndicador de identificador 1
apuracaoIndicador = ApuracaoIndicador.Carrega(1)
# modifica a propriedade PlanoGestaoId
apuracaoIndicador.PlanoGestaoId = 1;
# salva modificação da propriedade PlanoGestaoId
ApuracaoIndicador.Salva(apuracaoIndicador)
```
