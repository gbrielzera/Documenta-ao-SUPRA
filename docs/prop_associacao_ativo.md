# Ativo

Caminho: Customização > Modelo de objetos > Processo > Associacao > Ativo

Indica que a Associacao está ativa no Sistema. Se estiver inativa então não é possível a criação de novas associações desta natureza.

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto Associacao de identificador 1
associacao = Associacao.Carrega(1)
# modifica a propriedade Ativo
associacao.Ativo = true;
# salva modificação da propriedade Ativo
Associacao.Salva(associacao)
```
