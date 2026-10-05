# AcoesExecutadasEmAcordos

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > AcoesExecutadasEmAcordos

Ações configuradas em Acordos de Nível Operacional que foram executadas pela Ocorrência

**Exemplo 1: percorrer objetos da propriedade AcoesExecutadasEmAcordos**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if ocorrencia != None:
    # percorre objetos da propriedade AcoesExecutadasEmAcordos e para cada uma escreve conteúdo no log de mensagens
    for execucaoAcaoAcordo in ocorrencia.AcoesExecutadasEmAcordos:
        Utils.LogInformation(execucaoAcaoAcordo.ToString())
```
