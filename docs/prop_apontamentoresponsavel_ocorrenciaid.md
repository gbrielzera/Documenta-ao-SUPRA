# OcorrenciaId

Caminho: Customização > Modelo de objetos > Processo > ApontamentoResponsavel > OcorrenciaId

Número sequencial gerado automaticamente pelo sistema para Identificar uma Ocorrência

**Exemplo 1: modificação da propriedade OcorrenciaId**

```
# carrega objeto ApontamentoResponsavel de identificador 1
apontamentoResponsavel = ApontamentoResponsavel.Carrega(1)
# modifica a propriedade OcorrenciaId
apontamentoResponsavel.OcorrenciaId = 1;
# salva modificação da propriedade OcorrenciaId
ApontamentoResponsavel.Salva(apontamentoResponsavel)
```
