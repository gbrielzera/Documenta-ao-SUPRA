# Class

Caminho: Customização > Modelo de objetos > Utilitários > CustomClass > Class

Implementa um cadastro de todas as Classes de Negócio existentes no sistema. Este cadastro torna possível a customização do software permitindo: alteração de documentação, definição de novos campos e regras de negócio.

**Exemplo 1: modificação da propriedade Class**

```
# carrega objeto CustomClass de identificador 94
customClass = CustomClass.Carrega(94)
# modifica a propriedade Class
customClass.Class = Class.Carrega(57);
# salva modificação da propriedade Class
CustomClass.Salva(customClass)
```
