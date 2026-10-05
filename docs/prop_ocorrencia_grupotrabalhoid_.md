# GrupoTrabalhoId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > GrupoTrabalhoId

Identificador do GrupoTrabalho responsável pela ocorrência. Assim como o campo Responsável o Grupo de trabalho é mantido pelo sistema quando executada a função de encaminhamento ou segundo papel definido em atividades do processo.

**Exemplo 1: modificação da propriedade GrupoTrabalhoId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade GrupoTrabalhoId
ocorrencia.GrupoTrabalhoId = 1;
# salva modificação da propriedade GrupoTrabalhoId
Ocorrencia.Salva(ocorrencia)
```
