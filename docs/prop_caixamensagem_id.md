# Id

Caminho: Customização > Modelo de objetos > Processo > CaixaMensagem > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um CaixaEmail

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto CaixaMensagem de identificador 1
caixaMensagem = CaixaMensagem.Carrega(1)
# modifica a propriedade Id
caixaMensagem.Id = 1;
# salva modificação da propriedade Id
CaixaMensagem.Salva(caixaMensagem)
```
