# Codigo

Caminho: Customização > Modelo de objetos > Processo > Operacao > Codigo

Código da Operação

**Exemplo 1: modificação da propriedade Codigo**

```
# carrega objeto Operacao de identificador 1
operacao = Operacao.Carrega(1)
# modifica a propriedade Codigo
operacao.Codigo = "Código";
# salva modificação da propriedade Codigo
Operacao.Salva(operacao)
```
