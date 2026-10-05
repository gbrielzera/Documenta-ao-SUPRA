# CategoriaId

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > CategoriaId

Identificador da Categoria atribuída manualmente a Ordem de Serviço.

**Exemplo 1: modificação da propriedade CategoriaId**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade CategoriaId
ordemServico.CategoriaId = 1;
# salva modificação da propriedade CategoriaId
OrdemServico.Salva(ordemServico)
```
