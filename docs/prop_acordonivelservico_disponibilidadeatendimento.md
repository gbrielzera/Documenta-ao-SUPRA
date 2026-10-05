# DisponibilidadeAtendimento

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > DisponibilidadeAtendimento

Disponibilidade de atendimento (horário de início e horário de fim) nos dias da semana. A disponibilidae é levada em consideração no cálculo do tempo restante de atendimento.

**Exemplo 1: percorrer objetos da propriedade DisponibilidadeAtendimento**

```
# carrega objeto AcordoNivelServico de identificador 51
acordoNivelServico = AcordoNivelServico.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if acordoNivelServico != None:
    # percorre objetos da propriedade DisponibilidadeAtendimento e para cada uma escreve conteúdo no log de mensagens
    for disponibilidadeAtendimento in acordoNivelServico.DisponibilidadeAtendimento:
        Utils.LogInformation(disponibilidadeAtendimento.ToString())
```
