# TiposAnexosMensagem

Caminho: Customização > Modelo de objetos > Processo > Atividade > TiposAnexosMensagem

Tipos de arquivos que serão anexados no comunicado gerado pelo evento

**Exemplo 1: percorrer objetos da propriedade TiposAnexosMensagem**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade TiposAnexosMensagem e para cada uma escreve conteúdo no log de mensagens
    for tipoAnexoMensagem in atividade.TiposAnexosMensagem:
        Utils.LogInformation(tipoAnexoMensagem.ToString())
```
