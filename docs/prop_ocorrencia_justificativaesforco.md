# JustificativaEsforco

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > JustificativaEsforco

Justificativa para valor de Esforço estimado

**Exemplo 1: modificação da propriedade JustificativaEsforco**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade JustificativaEsforco
ocorrencia.JustificativaEsforco = "Justificativa esforço";
# salva modificação da propriedade JustificativaEsforco
Ocorrencia.Salva(ocorrencia)
```
