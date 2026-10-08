# Propriedade Solicitacao

Caminho: Propriedade Solicitacao

Solicitação

**Exemplo 1: modificação da propriedade Solicitacao**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade Solicitacao
ordemServico.Solicitacao = "Solicitação";
# salva modificação da propriedade Solicitacao
OrdemServico.Salva(ordemServico)
```
