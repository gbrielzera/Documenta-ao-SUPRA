# Descricao

Caminho: Customização > Modelo de objetos > Processo > MetodoPriorizacao > Descricao

Descrição detalhada da ClasseSeveridade

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto MetodoPriorizacao de identificador 1
metodoPriorizacao = MetodoPriorizacao.Carrega(1)
# modifica a propriedade Descricao
metodoPriorizacao.Descricao = "Priorização ITIL";
# salva modificação da propriedade Descricao
MetodoPriorizacao.Salva(metodoPriorizacao)
```
