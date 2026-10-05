# DataHoraInicio

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > DataHoraInicio

Data e hora de início para o período no qual o Solucionador foi responsável

**Exemplo 1: modificação da propriedade DataHoraInicio**

```
# carrega objeto ApontamentoResponsavel de identificador 1
apontamentoResponsavel = ApontamentoResponsavel.Carrega(1)
# modifica a propriedade DataHoraInicio
apontamentoResponsavel.DataHoraInicio = DateTime;
# salva modificação da propriedade DataHoraInicio
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
