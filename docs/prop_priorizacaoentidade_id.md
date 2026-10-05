# Id

Caminho: Customização > Modelo de objetos > Processo > PriorizacaoEntidade > Id

Número sequencial gerado automaticamente pelo sistema para Identificar uma PriorizacaoEntidade

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto PriorizacaoEntidade de identificador 1
priorizacaoEntidade = PriorizacaoEntidade.Carrega(1)
# modifica a propriedade Id
priorizacaoEntidade.Id = 1;
# salva modificação da propriedade Id
PriorizacaoEntidade.Salva(priorizacaoEntidade)
```
