# Class

Caminho: Customização > Modelo de objetos > Utilitários > ExceptionClass > Class

Classe de Negócio que implementa objeto de exceção para o erro. Esta classe mantém propriedades que podem ser utilizadas na formação de campos diversos da exceção: Mensagem, Causa, Efeito e Ação.

**Exemplo 1: modificação da propriedade Class**

```
# carrega objeto ExceptionClass de identificador 94
exceptionClass = ExceptionClass.Carrega(94)
# modifica a propriedade Class
exceptionClass.Class = Class.Carrega(57);
# salva modificação da propriedade Class
ExceptionClass.Salva(exceptionClass)
```
