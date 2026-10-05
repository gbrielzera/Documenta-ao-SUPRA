# Descricao

Caminho: Customização > Modelo de objetos > Processo > Operacao > Descricao

Descrição detalhada da Operacao

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto Operacao de identificador 1
operacao = Operacao.Carrega(1)
# modifica a propriedade Descricao
operacao.Descricao = "Descrição";
# salva modificação da propriedade Descricao
Operacao.Salva(operacao)
```
