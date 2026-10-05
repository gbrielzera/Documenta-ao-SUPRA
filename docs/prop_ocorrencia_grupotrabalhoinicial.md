# GrupoTrabalhoInicial

Caminho: Customização > Modelo de objetos > Processo > Ocorrencia > GrupoTrabalhoInicial

Grupo de Trabalho que iniciou o atendimento da Ocorrência.

**Exemplo 1: modificação da propriedade GrupoTrabalhoInicial**

```
# carrega objeto Ocorrencia de identificador 78
ocorrencia = Ocorrencia.Carrega(78)
# modifica a propriedade GrupoTrabalhoInicial
ocorrencia.GrupoTrabalhoInicial = GrupoTrabalho.Carrega(23);
# salva modificação da propriedade GrupoTrabalhoInicial
Ocorrencia.Salva(ocorrencia)
```
