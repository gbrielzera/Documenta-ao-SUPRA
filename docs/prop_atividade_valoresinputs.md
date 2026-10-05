# ValoresInputs

Caminho: Customização > Modelo de objetos > Processo > Atividade > ValoresInputs

Definição de valores para parâmetros de entrada do Subprocesso alvo. Estes parâmetros são declarados no Subprocesso alvo (Modificar Subprocesso) e depois copiados para esta propriedade quando definimos o Subprocesso alvo.

**Exemplo 1: percorrer objetos da propriedade ValoresInputs**

```
# carrega objeto Atividade de identificador 78
atividade = Atividade.Carrega(78)
# verifica se o objeto foi recuperado com sucesso
if atividade != None:
    # percorre objetos da propriedade ValoresInputs e para cada uma escreve conteúdo no log de mensagens
    for valorInput in atividade.ValoresInputs:
        Utils.LogInformation(valorInput.ToString())
```
