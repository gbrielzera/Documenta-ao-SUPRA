# PesquisaFiltroConcluida

Caminho: Customização > Modelo de objetos > Processo > Indicador > PesquisaFiltroConcluida

Seleciona Pesquisas de Satisfação respondidas por Clientes

**Exemplo 1: modificação da propriedade PesquisaFiltroConcluida**

```
# carrega objeto Indicador de identificador 1
indicador = Indicador.Carrega(1)
# modifica a propriedade PesquisaFiltroConcluida
indicador.PesquisaFiltroConcluida = true;
# salva modificação da propriedade PesquisaFiltroConcluida
Indicador.Salva(indicador)
```
