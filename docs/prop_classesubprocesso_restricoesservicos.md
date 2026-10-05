# RestricoesServicos

Caminho: Customização > Modelo de objetos > Processo > ClasseSubProcesso > RestricoesServicos

Serviços que estarão disponíveis para o Subprocesso. Deve ser preenchido somente quando for necessário restringir os Serviços. Se não for preenchido então todos os Serviços estarão disponívies. Tomar como exemplo o passo 3 do Autoatendimento.

**Exemplo 1: percorrer objetos da propriedade RestricoesServicos**

```
# carrega objeto ClasseSubProcesso de identificador 78
classeSubProcesso = ClasseSubProcesso.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if classeSubProcesso != None:
    # percorre objetos da propriedade RestricoesServicos e para cada uma escreve conteúdo no log de mensagens
    for restricaoServico in classeSubProcesso.RestricoesServicos:
        Utils.LogInformation(restricaoServico.ToString())
```
