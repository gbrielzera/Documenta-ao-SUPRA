# ClasseSubProcessoInicialId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > ClasseSubProcessoInicialId

Identificador do Tipo de Subprocesso inicialmente atribuído a Ocorrência.

**Exemplo 1: modificação da propriedade ClasseSubProcessoInicialId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade ClasseSubProcessoInicialId
ocorrencia.ClasseSubProcessoInicialId = 1;
# salva modificação da propriedade ClasseSubProcessoInicialId
Ocorrencia.Salva(ocorrencia)
```
