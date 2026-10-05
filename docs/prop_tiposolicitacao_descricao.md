# Descricao

Caminho: Customização > Modelo de objetos > Processo > TipoSolicitacao > Descricao

Descrição detalhada do TipoSolicitacao

**Exemplo 1: modificação da propriedade Descricao**

```
# carrega objeto TipoSolicitacao de identificador 1
tipoSolicitacao = TipoSolicitacao.Carrega(1)
# modifica a propriedade Descricao
tipoSolicitacao.Descricao = "Descrição";
# salva modificação da propriedade Descricao
TipoSolicitacao.Salva(tipoSolicitacao)
```
