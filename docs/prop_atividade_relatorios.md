# Relatorios

Caminho: Customização > Modelo de objetos > Processo > Atividade > Relatorios

Lista de relatórios que serão utilizados como apoio na execução de alguma tarefa ou como anexo em alguma mensagem gerada pela execução do processo. No caso de relatórios de apoio é possível a sua publicação na página de consultas do Autoatendimento.

**Exemplo 1: percorrer objetos da propriedade Relatorios**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade Relatorios e para cada uma escreve conteúdo no log de mensagens
    for relatorioAtividade in atividade.Relatorios:
        Utils.LogInformation(relatorioAtividade.ToString())
```
