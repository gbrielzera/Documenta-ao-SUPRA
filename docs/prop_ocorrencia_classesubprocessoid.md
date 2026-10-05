# ClasseSubProcessoId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ClasseSubProcessoId

Identificador do tipo de Subprocesso da ocorrência. Este tipo se refere a um Subprocesso definido na versão de processo também associada a ocorrência e define os fluxos e responsabilidade de processo.

**Exemplo 1: modificação da propriedade ClasseSubProcessoId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade ClasseSubProcessoId
ocorrencia.ClasseSubProcessoId = 1;
# salva modificação da propriedade ClasseSubProcessoId
Ocorrencia.Salva(ocorrencia)
```
