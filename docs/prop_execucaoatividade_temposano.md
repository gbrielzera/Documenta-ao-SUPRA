# TemposANO

Caminho: Customização > Modelo de objetos > Processo > ExecucaoAtividade > TemposANO

Log de tempos realizados pelos vários solucionadores envolvidos na execução da atividade.

**Exemplo 1: percorrer objetos da propriedade TemposANO**

```
# carrega objeto ExecucaoAtividade de identificador 78
execucaoAtividade = ExecucaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if execucaoAtividade != None:
    # percorre objetos da propriedade TemposANO e para cada uma escreve conteúdo no log de mensagens
    for temposANO in execucaoAtividade.TemposANO:
        Utils.LogInformation(temposANO.ToString())
```
