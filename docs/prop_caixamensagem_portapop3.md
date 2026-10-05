# PortaPOP3

Caminho: Customização > Modelo de objetos > Processo > CaixaMensagem > PortaPOP3

Porta do protocolo TCP/IP utilizada para acesso ao servidor de email via POP3. Se não for preenchida então será utilizada o padrão 110.

**Exemplo 1: modificação da propriedade PortaPOP3**

```
# carrega objeto CaixaMensagem de identificador 1
caixaMensagem = CaixaMensagem.Carrega(1)
# modifica a propriedade PortaPOP3
caixaMensagem.PortaPOP3 = 1;
# salva modificação da propriedade PortaPOP3
CaixaMensagem.Salva(caixaMensagem)
```
