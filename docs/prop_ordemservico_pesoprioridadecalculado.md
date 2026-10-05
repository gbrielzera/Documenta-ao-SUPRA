# PesoPrioridadeCalculado

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > PesoPrioridadeCalculado

Peso prioridade calculado

**Exemplo 1: modificação da propriedade PesoPrioridadeCalculado**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade PesoPrioridadeCalculado
ordemServico.PesoPrioridadeCalculado = 1;
# salva modificação da propriedade PesoPrioridadeCalculado
OrdemServico.Salva(ordemServico)
```
