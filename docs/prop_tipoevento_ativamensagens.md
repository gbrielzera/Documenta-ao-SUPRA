# AtivaMensagens

Caminho: Customização > Modelo de objetos > Processo > TipoEvento > AtivaMensagens

Ativa ou desativa o Envio de Mensagens na ocorrência de eventos deste Tipo

**Exemplo 1: modificação da propriedade AtivaMensagens**

```
# carrega objeto TipoEvento de identificador 1
tipoEvento = TipoEvento.Carrega(1)
# modifica a propriedade AtivaMensagens
tipoEvento.AtivaMensagens = true;
# salva modificação da propriedade AtivaMensagens
TipoEvento.Salva(tipoEvento)
```
