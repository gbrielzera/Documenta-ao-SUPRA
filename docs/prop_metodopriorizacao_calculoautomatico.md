# CalculoAutomatico

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > CalculoAutomatico

Indica que o cálculo é automático sempre que ocorrer modificação no campos Cliente, Serviço ou quando for adicionado ou removido um Item de Configuração.

**Exemplo 1: modificação da propriedade CalculoAutomatico**

```
# carrega objeto MetodoPriorizacao de identificador 1
metodoPriorizacao = MetodoPriorizacao.Carrega(1)
# modifica a propriedade CalculoAutomatico
metodoPriorizacao.CalculoAutomatico = true;
# salva modificação da propriedade CalculoAutomatico
MetodoPriorizacao.Salva(metodoPriorizacao)
```
