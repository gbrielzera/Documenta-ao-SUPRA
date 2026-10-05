# TemporalityClass

Caminho: Customização > Modelo de objetos > Utilitários > Message > TemporalityClass

Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio.

**Exemplo 1: modificação da propriedade TemporalityClass**

```
# carrega objeto Message de identificador 94
message = Message.Carrega(94)
# modifica a propriedade TemporalityClass
message.TemporalityClass = Class.Carrega(57);
# salva modificação da propriedade TemporalityClass
Message.Salva(message)
```
