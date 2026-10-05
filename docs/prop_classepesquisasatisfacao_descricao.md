# Descricao

Caminho: Customização > Modelo de objetos > Processo > ClassePesquisaSatisfacao > Descricao

Descrição detalhada da ClassePesquisaSatisfacao

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto ClassePesquisaSatisfacao de identificador 1
classePesquisaSatisfacao = ClassePesquisaSatisfacao.Carrega(1)
# modifica a propriedade Descricao
classePesquisaSatisfacao.Descricao = "Descrição";
# salva modificação da propriedade Descricao
ClassePesquisaSatisfacao.Salva(classePesquisaSatisfacao)
```
