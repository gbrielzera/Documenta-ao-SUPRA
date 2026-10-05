# Senha

Caminho: Customização > Modelo de objetos > Processo > CaixaMensagem > Senha

Senha da caixa de mensagem monitorada. Esta senha é necessária para acessar a caixa.

**Exemplo 1: modificação da propriedade Senha**

```
# carrega objeto CaixaMensagem de identificador 1
caixaMensagem = CaixaMensagem.Carrega(1)
# modifica a propriedade Senha
caixaMensagem.Senha = "Senha";
# salva modificação da propriedade Senha
CaixaMensagem.Salva(caixaMensagem)
```
