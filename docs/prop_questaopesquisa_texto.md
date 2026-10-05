# Texto

Caminho: Customização > Modelo de objetos > Processo > QuestaoPesquisa > Texto

Texto apresentado para o Cliente no momento de aplicação da Pesquisa de Satisfação

**Exemplo 1: modificação da propriedade Texto**

```
# carrega objeto QuestaoPesquisa de identificador 1
questaoPesquisa = QuestaoPesquisa.Carrega(1)
# modifica a propriedade Texto
questaoPesquisa.Texto = "Texto";
# salva modificação da propriedade Texto
QuestaoPesquisa.Salva(questaoPesquisa)
```
