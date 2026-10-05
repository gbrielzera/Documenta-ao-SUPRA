# ComentarioContato

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > ComentarioContato

Comentários gerais sobre contatos com o Cliente

**Exemplo 1: modificação da propriedade ComentarioContato**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade ComentarioContato
ordemServico.ComentarioContato = "Comentário contato";
# salva modificação da propriedade ComentarioContato
OrdemServico.Salva(ordemServico)
```
