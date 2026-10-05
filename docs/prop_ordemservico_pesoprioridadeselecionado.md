# PesoPrioridadeSelecionado

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > PesoPrioridadeSelecionado

Peso prioridade selecionado

**Exemplo 1: modificação da propriedade PesoPrioridadeSelecionado**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade PesoPrioridadeSelecionado
ordemServico.PesoPrioridadeSelecionado = 1;
# salva modificação da propriedade PesoPrioridadeSelecionado
OrdemServico.Salva(ordemServico)
```
