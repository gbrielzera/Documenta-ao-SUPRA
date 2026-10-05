# Categoria

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > Categoria

Classificação manual atribuída a Ordens de Serviço associadas com uma cor e com possibilidade de exibição na barra de rolagem de Ordens de Serviço. Para definição das cores é utilizado o modelo RGB que é baseado na teoria de visão colorida tricromática.

**Exemplo 1: modificação da propriedade Categoria**

```
# carrega objeto OrdemServico de identificador 78
ordemServico = OrdemServico.Carrega(78)
# modifica a propriedade Categoria
ordemServico.Categoria = Categoria.Carrega(23);
# salva modificação da propriedade Categoria
OrdemServico.Salva(ordemServico)
```
