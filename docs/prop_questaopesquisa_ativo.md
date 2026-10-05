# Ativo

Caminho: Customização > Modelo de objetos > Processo > QuestaoPesquisa > Ativo

Indica que o Indicador está ativo. Somente Indicadores ativos são exibidos na Pesquisa de Satisfação

**Exemplo 1: modificação da propriedade Ativo**

```
# carrega objeto QuestaoPesquisa de identificador 1
questaoPesquisa = QuestaoPesquisa.Carrega(1)
# modifica a propriedade Ativo
questaoPesquisa.Ativo = true;
# salva modificação da propriedade Ativo
QuestaoPesquisa.Salva(questaoPesquisa)
```
