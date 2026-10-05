# Descricao

Caminho: Customização > Modelo de objetos > Processo > AfirmacaoFinanceira > Descricao

Descrição detalhada do AfirmacaoFinanceira

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto AfirmacaoFinanceira de identificador 1
afirmacaoFinanceira = AfirmacaoFinanceira.Carrega(1)
# modifica a propriedade Descricao
afirmacaoFinanceira.Descricao = "Descrição";
# salva modificação da propriedade Descricao
AfirmacaoFinanceira.Salva(afirmacaoFinanceira)
```
