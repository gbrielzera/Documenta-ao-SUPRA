# Descricao

Caminho: Customização > Modelo de objetos > Processo > PriorizacaoEntidade > Descricao

Descrição detalhada da PriorizacaoEntidade

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto PriorizacaoEntidade de identificador 1
priorizacaoEntidade = PriorizacaoEntidade.Carrega(1)
# modifica a propriedade Descricao
priorizacaoEntidade.Descricao = "Descrição";
# salva modificação da propriedade Descricao
PriorizacaoEntidade.Salva(priorizacaoEntidade)
```
