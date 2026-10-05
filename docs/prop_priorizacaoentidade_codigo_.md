# Codigo

Caminho: Customização > Modelo de objetos > Processo > PriorizacaoEntidade > Codigo

Código para recuperação de objetos reconhecidos pelo fabricante do software.

**Exemplo 1: modificação da propriedade Codigo**

```
# carrega objeto PriorizacaoEntidade de identificador 1
priorizacaoEntidade = PriorizacaoEntidade.Carrega(1)
# modifica a propriedade Codigo
priorizacaoEntidade.Codigo = "Código";
# salva modificação da propriedade Codigo
PriorizacaoEntidade.Salva(priorizacaoEntidade)
```
