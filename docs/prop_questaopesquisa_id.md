# Id

Caminho: Customização > Modelo de objetos > Processo > QuestaoPesquisa > Id

Identificador

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto QuestaoPesquisa de identificador 1
questaoPesquisa = QuestaoPesquisa.Carrega(1)
# modifica a propriedade Id
questaoPesquisa.Id = 1;
# salva modificação da propriedade Id
QuestaoPesquisa.Salva(questaoPesquisa)
```
