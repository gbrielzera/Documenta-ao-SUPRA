# Relatorios

Caminho: Customização > Modelo de objetos > Processo > OperacaoAtividade > Relatorios

Relação de relatórios envolvidos em uma solicitação de aprovação ou programados para geração de arquivos anexados na ocorrência. Estes relatórios são disponibilizados como um link na página de aprovações do AA. Na configuração destes relatórios é necessário definir todos os eventuais parâmetros.

**Exemplo 1: percorrer objetos da propriedade Relatorios**

```
# carrega objeto OperacaoAtividade de identificador 78
operacaoAtividade = OperacaoAtividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if operacaoAtividade != None:
    # percorre objetos da propriedade Relatorios e para cada uma escreve conteúdo no log de mensagens
    for relatorioOperacao in operacaoAtividade.Relatorios:
        Utils.LogInformation(relatorioOperacao.ToString())
```
