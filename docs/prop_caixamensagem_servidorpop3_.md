# ServidorPOP3

Caminho: Customização > Modelo de objetos > Processo > CaixaMensagem > ServidorPOP3

Servidor POP3 onde está localizada a caixa de email configurada.

**Exemplo 1: modificação da propriedade ServidorPOP3**

```
# carrega objeto CaixaMensagem de identificador 1
caixaMensagem = CaixaMensagem.Carrega(1)
# modifica a propriedade ServidorPOP3
caixaMensagem.ServidorPOP3 = "Servidor POP3";
# salva modificação da propriedade ServidorPOP3
CaixaMensagem.Salva(caixaMensagem)
```
