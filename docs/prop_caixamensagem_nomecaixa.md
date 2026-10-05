# NomeCaixa

Caminho: Customização > Modelo de objetos > Processo > CaixaMensagem > NomeCaixa

Nome da caixa de mensagem que será monitorada pela máquina de processos. Não é permitido o uso da caixa utilizada pela rotina de envio de emails e redirecionamentos.

**Exemplo 1: modificação da propriedade NomeCaixa**

```
# carrega objeto CaixaMensagem de identificador 1
caixaMensagem = CaixaMensagem.Carrega(1)
# modifica a propriedade NomeCaixa
caixaMensagem.NomeCaixa = "Nome";
# salva modificação da propriedade NomeCaixa
CaixaMensagem.Salva(caixaMensagem)
```
