# Id

Caminho: Customização > Modelo de objetos > Processo > AfirmacaoFinanceira > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um AfirmacaoFinanceira

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto AfirmacaoFinanceira de identificador 1
afirmacaoFinanceira = AfirmacaoFinanceira.Carrega(1)
# modifica a propriedade Id
afirmacaoFinanceira.Id = 1;
# salva modificação da propriedade Id
AfirmacaoFinanceira.Salva(afirmacaoFinanceira)
```
