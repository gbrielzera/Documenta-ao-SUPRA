# GrupoTrabalhoInicialId

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > GrupoTrabalhoInicialId

Identificador do Grupo de Trabalho inicial

**Exemplo 1: modificação da propriedade GrupoTrabalhoInicialId**

```
# carrega objeto Ocorrencia de identificador 1
ocorrencia = Ocorrencia.Carrega(1)
# modifica a propriedade GrupoTrabalhoInicialId
ocorrencia.GrupoTrabalhoInicialId = 1;
# salva modificação da propriedade GrupoTrabalhoInicialId
Ocorrencia.Salva(ocorrencia)
```
