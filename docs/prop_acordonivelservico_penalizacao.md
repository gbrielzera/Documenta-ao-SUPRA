# Penalizacao

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > Penalizacao

Penalização aplicada no valor de Charge-back caso existam Ordens de Serviço em que não foi cumprido o Acordo de Nível de Serviço. Esta regra é válida somente para as opções de Charge-back 'Ocorrencia' e 'Hora'.

**Exemplo 1: modificação da propriedade Penalizacao**

```
# carrega objeto AcordoNivelServico de identificador 1
acordoNivelServico = AcordoNivelServico.Carrega(1)
# modifica a propriedade Penalizacao
acordoNivelServico.Penalizacao = 1;
# salva modificação da propriedade Penalizacao
AcordoNivelServico.Salva(acordoNivelServico)
```
