# TipoCaixa

Caminho: Customização > Modelo de objetos > Processo > CaixaMensagem > TipoCaixa

Tipo de caixa de mensagem

**Exemplo 1: modificação da propriedade TipoCaixa**

```
# carrega objeto CaixaMensagem de identificador 1
caixaMensagem = CaixaMensagem.Carrega(1)
# modifica a propriedade TipoCaixa
caixaMensagem.TipoCaixa = "Email";
# salva modificação da propriedade TipoCaixa
CaixaMensagem.Salva(caixaMensagem)
```
