# Situacao

Caminho: Customização > Modelo de objetos > Processo > Apontamento > Situacao

Situação do Apontamento

**Exemplo 1: modificação da propriedade Situacao**

```
# carrega objeto Apontamento de identificador 1
apontamento = Apontamento.Carrega(1)
# modifica a propriedade Situacao
apontamento.Situacao = "Cancelado";
# salva modificação da propriedade Situacao
Apontamento.Salva(apontamento)
```
