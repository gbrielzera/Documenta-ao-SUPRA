# InterrupcoesAcordadas

Caminho: Customização > Modelo de objetos > Recurso > AcordoNivelServico > InterrupcoesAcordadas

Interrupções acordadas na cronometragem do tempo total de atendimento.

**Exemplo 1: percorrer objetos da propriedade InterrupcoesAcordadas**

```
# carrega objeto AcordoNivelServico de identificador 51
acordoNivelServico = AcordoNivelServico.Carrega(51)
# verifica se o objeto foi recuperado com sucesso
if acordoNivelServico != None:
    # percorre objetos da propriedade InterrupcoesAcordadas e para cada uma escreve conteúdo no log de mensagens
    for acordoInterrupcaoSLA in acordoNivelServico.InterrupcoesAcordadas:
        Utils.LogInformation(acordoInterrupcaoSLA.ToString())
```
