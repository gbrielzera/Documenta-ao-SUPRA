# Descricao

Caminho: Customização > Modelo de objetos > Processo > ClasseApontamento > Descricao

Descrição detalhada do ClasseApontamento

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ClasseApontamento de identificador 1
classeApontamento = ClasseApontamento.Carrega(1)
# modifica a propriedade Descricao
classeApontamento.Descricao = "Descrição";
# salva modificação da propriedade Descricao
ClasseApontamento.Salva(classeApontamento)
```
