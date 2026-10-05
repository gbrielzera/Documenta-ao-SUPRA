# SintomaAnalisado

Caminho: Customização > Modelo de objetos > Processo > OrdemServico > SintomaAnalisado

Sintoma analisado por um Solucionador. Este texto é utilizado em Incidentes para associação de Incidentes pelo próprio Cliente no site de Autoatendimento.

**Exemplo 1: modificação da propriedade SintomaAnalisado**

```
# carrega objeto OrdemServico de identificador 1
ordemServico = OrdemServico.Carrega(1)
# modifica a propriedade SintomaAnalisado
ordemServico.SintomaAnalisado = "Sintoma analisado";
# salva modificação da propriedade SintomaAnalisado
OrdemServico.Salva(ordemServico)
```
