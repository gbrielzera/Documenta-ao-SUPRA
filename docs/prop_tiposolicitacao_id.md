# Id

Caminho: Customização > Modelo de objetos > Processo > TipoSolicitacao > Id

Número sequencial gerado automaticamente pelo sistema para Identificar um TipoSolicitacao

**Exemplo 1: modificação da propriedade Id**

```
# carrega objeto TipoSolicitacao de identificador 1
tipoSolicitacao = TipoSolicitacao.Carrega(1)
# modifica a propriedade Id
tipoSolicitacao.Id = 1;
# salva modificação da propriedade Id
TipoSolicitacao.Salva(tipoSolicitacao)
```
