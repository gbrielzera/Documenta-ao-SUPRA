# Responsavel

Caminho: Customização > Modelo de objetos > Processo > Apontamento > Responsavel

Responsável pelo Apontamento

**Exemplo 1: modificação da propriedade Responsavel**

```
# carrega objeto Apontamento de identificador 94
apontamento = Apontamento.Carrega(94)
# modifica a propriedade Responsavel
apontamento.Responsavel = Pessoa.Carrega(82);
# salva modificação da propriedade Responsavel
Apontamento.Salva(apontamento)
```
