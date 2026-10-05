# Ativo

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > Ativo

Indica que a ClassePesquisaSatisfacao está ativa no Sistema. Quando inativo o registro não pode ser utilizado em outras telas do sistema.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 1
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(1)
# modifica a propriedade Ativo
classePesquisaSatisfacao.Ativo = true;
# salva modificação da propriedade Ativo
ClassePesquisaSatisfacao.Salva(classePesquisaSatisfacao)
```
