# DataHoraExecucao

Caminho: Customização > Modelo de objetos > Processo > ExecucaoTimer > DataHoraExecucao

Data e hora que o Timer foi executado com sucesso

**Exemplo 1: modificação da propriedade DataHoraExecucao**

```
# carrega objeto ExecucaoTimer de identificador 1
execucaoTimer = ExecucaoTimer.Carrega(1)
# modifica a propriedade DataHoraExecucao
execucaoTimer.DataHoraExecucao = DateTime;
# salva modificação da propriedade DataHoraExecucao
ExecucaoTimer.Salva(execucaoTimer)
```
