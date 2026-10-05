# Descricao

Caminho: Customização > Modelo de objetos > Processo > QuestaoPesquisa > Descricao

Descrição do Indicador

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto QuestaoPesquisa de identificador 1
questaoPesquisa = QuestaoPesquisa.Carrega(1)
# modifica a propriedade Descricao
questaoPesquisa.Descricao = "Descrição";
# salva modificação da propriedade Descricao
QuestaoPesquisa.Salva(questaoPesquisa)
```
