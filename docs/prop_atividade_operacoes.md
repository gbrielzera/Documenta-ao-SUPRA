# Operacoes

Caminho: Customização > Modelo de objetos > Processo > Atividade > Operacoes

Regras de negócio configuradas na atividade ou evento. Estas regras podem ser: preenchimento de um campo, aprovação etc.

**Exemplo 1: percorrer objetos da propriedade Operacoes**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade Operacoes e para cada uma escreve conteúdo no log de mensagens
    for operacaoAtividade in atividade.Operacoes:
        Utils.LogInformation(operacaoAtividade.ToString())
```
